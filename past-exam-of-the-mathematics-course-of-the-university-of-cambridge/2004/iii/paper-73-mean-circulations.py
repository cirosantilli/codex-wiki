"""Step density-flux circulation for zero momentum-flux divergence.
Python 3.14; root NumPy/Matplotlib. Opaque PNG output to caller CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def fields(Y, Z, residual=False):
    if residual:
        chi = np.where(Z < 0, .5*np.exp(Z), -.5*np.exp(-Z))
    else:
        chi = np.where(Z < 0, -(1-.5*np.exp(Z)), -.5*np.exp(-Z))
    # In coordinates Y=l*y, Z=kappa*z, both velocities share l*kappa*A0.
    vy = -.5*np.exp(-np.abs(Z))*np.sin(Y)
    wz = chi*np.cos(Y)
    return np.sin(Y)*chi, vy, wz


def draw(ax, residual):
    y = np.linspace(0, np.pi, 151)
    regions = [np.linspace(-3.6, -.025, 130), np.linspace(.025, 3.6, 130)] if residual else [np.linspace(-3.6, 3.6, 261)]
    for z in regions:
        Y, Z = np.meshgrid(y, z)
        X, V, W = fields(Y, Z, residual)
        levels = np.linspace(.05, .45, 5) if residual and z[-1] < 0 else np.linspace(-.9, -.05, 10)
        if residual and z[0] > 0:
            levels = np.linspace(-.45, -.05, 5)
        ax.contour(Y, Z, X, levels=levels, colors='#7597b1', linewidths=.8)
        ax.streamplot(y, z, V, W, density=.7, color='#174f78', linewidth=1, arrowsize=1.1)
    ax.axhline(0, color='#aa4c2b', linestyle='--', lw=1)
    if residual:
        for start in [.25, 1.2, 2.15]:
            ax.annotate('', xy=(start+.55, 0), xytext=(start, 0), arrowprops={'arrowstyle':'->','color':'#aa4c2b','lw':2})
        ax.text(np.pi/2, .22, 'positive meridional sheet transport', ha='center', fontsize=8, color='#98401e')
        ax.text(np.pi/2, -3.28, r'$\mathcal{X}^*\to0$ at both vertical infinities', ha='center', fontsize=9)
    else:
        ax.text(np.pi/2, -3.28, 'persistent lower-region vertical circulation', ha='center', fontsize=8)
    ax.set_xlim(0, np.pi)
    ax.set_ylim(-3.6, 3.6)
    ax.set_xticks([0, np.pi/2, np.pi], ['0', r'$\pi/2$', r'$\pi$'])
    ax.set_xlabel(r'$ly$ ($l=\pi/L$)')
    ax.set_title('Residual mean' if residual else 'Eulerian mean')
    for x in [0, np.pi]:
        ax.axvline(x, color='#333333', lw=1.8)
    ax.grid(alpha=.1)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.5), sharey=True)
    draw(axes[0], False)
    draw(axes[1], True)
    axes[0].set_ylabel(r'$\kappa z$ ($\kappa=N_0l/|f_0|$)')
    fig.suptitle('Wave-flux termination: Eulerian and residual circulations', fontsize=13)
    fig.text(.5, .015, 'Contours are streamfunctions; arrows follow computed velocities. Residual contours are split at the flux jump.', ha='center', fontsize=8)
    fig.tight_layout(rect=(0, .045, 1, .94))
    fig.savefig(Path.cwd()/'paper-73-mean-circulations.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
