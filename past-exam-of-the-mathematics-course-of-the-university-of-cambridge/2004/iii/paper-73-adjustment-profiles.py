"""Balanced ramp adjustment. Python 3.14; root NumPy/Matplotlib dependencies.
Write the opaque PNG basename to the caller's working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def profile(x, alpha):
    inside = np.abs(x) <= 1
    eta = np.where(inside, x-np.exp(-alpha)*np.sinh(alpha*x)/alpha,
                   np.sign(x)*(1-np.sinh(alpha)*np.exp(-alpha*np.abs(x))/alpha))
    v = np.where(inside, 1-np.exp(-alpha)*np.cosh(alpha*x),
                 np.sinh(alpha)*np.exp(-alpha*np.abs(x)))
    return eta, v


def main():
    fig, axes = plt.subplots(3, 2, figsize=(10, 8), sharex='col')
    for col, alpha in enumerate([0.08, 8.0]):
        extent = 4.5/alpha if alpha < 1 else 2.2
        x = np.linspace(-extent, extent, 3001)
        eta, v = profile(x, alpha)
        axes[0, col].plot(x, eta, color='#17649b', lw=2, label='balanced height')
        axes[0, col].plot(x, np.clip(x, -1, 1), '--', color='#888888', lw=1, label='initial height')
        axes[0, col].set_ylim(-1.15, 1.15)
        axes[0, col].set_title(rf'$\alpha={alpha:g}$: '+('narrow ramp' if alpha < 1 else 'wide ramp'))
        axes[1, col].plot(x, v, color='#a74422', lw=2)
        axes[1, col].set_ylim(-0.03*(1-np.exp(-alpha)), 1.15*(1-np.exp(-alpha)))
        axes[2, col].plot(x, np.zeros_like(x), color='#40683e', lw=2)
        axes[2, col].set_ylim(-0.12, 0.12)
        axes[2, col].set_yticks([0])
        axes[2, col].set_xlabel(r'$x/L$')
        for ax in axes[:, col]:
            ax.axvline(-1, color='#bbbbbb', lw=.8, linestyle=':')
            ax.axvline(1, color='#bbbbbb', lw=.8, linestyle=':')
            ax.grid(alpha=.18)
            ax.set_xlim(-extent, extent)
    axes[0, 0].set_ylabel(r'$\eta_s/h$')
    axes[1, 0].set_ylabel(r'$v_s\, /\, [gh/(fL)]$')
    axes[2, 0].set_ylabel(r'$u_s\, /\, [gh/(fL)]$')
    axes[0, 0].legend(loc='lower right', fontsize=8)
    fig.suptitle('Geostrophic adjustment: height spreads over the deformation radius', fontsize=13)
    fig.text(.5, .02, r'$f>0$, $h>0$; dotted lines mark ramp endpoints. Narrow-ramp peak velocity is $gh\alpha/(fL)$.', ha='center', fontsize=9)
    fig.tight_layout(rect=(0, .05, 1, .95))
    fig.savefig(Path.cwd()/'paper-73-adjustment-profiles.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
