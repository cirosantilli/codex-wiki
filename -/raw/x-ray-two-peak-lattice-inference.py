"""Original selected-reflection simulation; run from _media (Python 3.14).

Uses only the repository's NumPy/Matplotlib dependencies. No experimental data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, wavelength = 0.400, 0.200  # nm, chosen model parameters
    n = np.array([1, 2])
    theta = np.arcsin(wavelength * np.sqrt(n) / (2 * a))
    angles = np.degrees(2 * theta)
    inferred = wavelength * np.sqrt(n) / (2 * np.sin(theta))
    assert np.allclose(inferred, a, rtol=0, atol=1e-14)
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120)
    colors = ['#176998', '#b2590b']
    for angle, label, color in zip(angles, ['(100)', '(110)'], colors):
        ax.vlines(angle, 0, 1, color=color, lw=3)
        ax.text(angle, 1.045, label + f'\n{angle:.4f}°', ha='center', color=color)
    ax.set(xlim=(20, 50), ylim=(0, 1.35), yticks=[],
           xlabel=r'Detector deflection $2\theta$ (degrees)',
           title='Selected positions only')
    ax.set_ylabel('Stick height has no intensity meaning')
    xs = np.linspace(0, 2.3, 100)
    bx.plot(xs, xs / 16, color='#505050', lw=1.8)
    for ni, y, label, color in zip(n, np.sin(theta)**2, ['(100)', '(110)'], colors):
        bx.scatter(ni, y, s=70, color=color, zorder=3)
        bx.annotate(label, (ni, y), xytext=(-8, 11),
                    textcoords='offset points', ha='right', color=color)
    bx.text(.15, .129, r'Slope $=1/16$'+'\n'+r'$a=\lambda/(2\sqrt{\mathrm{slope}})$'+'\n'+r'$=0.400\ \mathrm{nm}$', va='top', fontsize=12)
    bx.set(xlim=(0, 2.4), ylim=(0, .16), xticks=[0, 1, 2],
           yticks=[0, .0625, .125], xlabel=r'Index sum $N=h^2+k^2+l^2$',
           ylabel=r'$\sin^2\theta$', title='Recover the repeat length')
    bx.grid(alpha=.18)
    fig.suptitle('Simulated cubic model: two indexed peaks, one length', fontsize=15)
    fig.text(.5, .035, r'Chosen $a=0.400$ nm, $\lambda=0.200$ nm. No powder trace or measured NaCl data.', ha='center', fontsize=11)
    fig.subplots_adjust(left=.08, right=.97, top=.80, bottom=.20, wspace=.38)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
