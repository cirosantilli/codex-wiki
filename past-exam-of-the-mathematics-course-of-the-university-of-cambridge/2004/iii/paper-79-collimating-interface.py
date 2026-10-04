"""Original ray/front plot; tested Python 3.14 with root NumPy/Matplotlib pins.
Only output is a same-basename opaque PNG in caller CWD. Preserves MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def geometry(radius):
    # z0=1, alpha=3, alpha_f=1; solid rho=2, beta=1.5; fluid rho=1.
    alpha, alpha_f, z0 = 3.0, 1.0, 1.0
    s = z0 * (alpha - alpha_f)
    d2 = alpha ** 2 - alpha_f ** 2
    D = np.sqrt(s ** 2 + d2 * np.asarray(radius) ** 2)
    Z = (alpha * s + alpha_f * D) / d2
    r = (alpha * D + alpha_f * s) / d2
    return Z, r, D


def displacement_coefficient(radius):
    alpha, alpha_f, beta, rho, rho_f = 3.0, 1.0, 1.5, 2.0, 1.0
    _, r, D = geometry(radius)
    denom_angle = np.sqrt(4 + alpha ** 2 * radius ** 2)
    sinP = alpha * radius / denom_angle
    cosP = 2 / denom_angle
    sinS = beta / alpha * sinP
    cosS = np.sqrt(1 - sinS ** 2)
    cosF = D / denom_angle
    C = 1 - 2 * sinS ** 2
    E = C ** 2 + (beta / alpha) ** 2 * (2 * sinP * cosP) * (2 * sinS * cosS)
    T = 2 * rho * alpha_f * C * cosP / (rho_f * alpha_f * cosP + rho * alpha * E * cosF)
    return T / (alpha_f * r)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.5), layout='constrained', facecolor='white')
    x = np.linspace(-4, 4, 701)
    Z, _, _ = geometry(np.abs(x))
    ax = axes[0]
    ax.fill_between(x, 0, Z, color='C1', alpha=0.08)
    ax.fill_between(x, Z, 3.55, color='C0', alpha=0.06)
    ax.plot(x, Z, color='black', label='Solid–fluid interface')
    for hit in [-3.5, -2, -0.8, 0, 0.8, 2, 3.5]:
        height, _, _ = geometry(abs(hit))
        ax.plot([0, hit], [0, height], color='C1', linewidth=1)
        ax.plot([hit, hit], [height, 3.45], color='C0', linewidth=1)
        ax.annotate('', xy=(hit, 3.35), xytext=(hit, 3.05),
                    arrowprops={'arrowstyle': '->', 'color': 'C0'})
    ax.scatter([0], [0], color='black', zorder=4)
    ax.axhline(3.0, linestyle='--', color='0.45', label='Equal arrival time')
    ax.text(-3.7, 0.85, 'Solid', fontsize=10)
    ax.text(-3.7, 3.3, 'Fluid', fontsize=10)
    ax.set(xlabel=r'Meridional coordinate / $z_0$', ylabel=r'Height / $z_0$',
           title='Spherical incidence, parallel transmitted rays', xlim=(-4, 4), ylim=(-0.12, 3.55))
    ax.legend(loc='lower left', fontsize=8)
    R = np.geomspace(0.02, 1000, 1000)
    ax = axes[1]
    ax.loglog(R, displacement_coefficient(R), label='Exact leading-front transfer')
    far = R[R >= 3]
    ax.loglog(far, 8 / (9 * far ** 2), '--', label=r'Large-$R$ coefficient $8/(9R^2)$')
    ax.hlines(4 / 7, 0.02, 0.25, color='0.5', linestyle=':', label=r'$A_u(0)=4/7$')
    ax.set(xlabel=r'$R/z_0$', ylabel=r'Displacement coefficient $A_u$',
           title=r'$\alpha=3,\ \beta=1.5,\ \alpha_f=1,\ \rho/\rho_f=2$', xlim=(0.02, 1000))
    ax.grid(alpha=0.2, which='both')
    ax.legend(fontsize=8, loc='lower left')
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
