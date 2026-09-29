"""Triangular jet and unstable phase speeds. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Writes paper-82-jet-semicircle.png to caller CWD.
Preserves caller MPLCONFIGDIR.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.gettempdir() + '/codex-wiki-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def speed(k):
    q = np.exp(-2 * k)
    discriminant = (2*k - 3)**2 - 2*(2*k + 5)*q + q*q
    return (2*k + q - 1) / (4*k), np.sqrt(np.maximum(-discriminant, 0)) / (4*k)


def main():
    lo, hi = 1.0, 3.0
    for _ in range(60):
        k = (lo + hi) / 2
        if 2*k - 3 - np.exp(-2*k) - 4*np.exp(-k) > 0:
            hi = k
        else:
            lo = k
    cutoff = (lo + hi) / 2
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), constrained_layout=True)
    y = np.linspace(-2, 2, 401)
    axes[0].plot(y, np.maximum(1 - np.abs(y), 0), lw=2.5)
    axes[0].set(xlabel='y', ylabel='U(y)', title='Triangular velocity profile', ylim=(-.05, 1.12))
    theta = np.linspace(0, np.pi, 400)
    cr = .5 + .5*np.cos(theta)
    ci = .5*np.sin(theta)
    axes[1].fill_between(cr, ci, 0, color='#e2edf7')
    axes[1].plot(cr, ci, 'k--', label="Howard semicircle")
    k = np.linspace(.002, cutoff, 700)
    cr, ci = speed(k)
    axes[1].plot(cr, ci, color='#a22544', lw=2.4, label='Unstable sinuous branch')
    for sample in (.2, .8, 1.5):
        r, i = speed(sample)
        axes[1].scatter(r, i, color='#a22544', s=20)
        axes[1].annotate(f'k = {sample}', (r, i), xytext=(5, 8), textcoords='offset points', fontsize=9)
    r, i = speed(cutoff)
    axes[1].scatter(r, i, color='#a22544', s=25)
    axes[1].annotate(f'cutoff k = {cutoff:.4f}', (r, i), xytext=(12, 16), textcoords='offset points', fontsize=9)
    axes[1].axhline(0, color='gray', lw=.8)
    axes[1].set(xlabel=r'$c_r$', ylabel=r'$c_i$', title='Growing modes in the complex speed plane', xlim=(-.04, 1.04), ylim=(-.035, .55))
    axes[1].set_aspect('equal', adjustable='box')
    axes[1].legend(loc='upper right', fontsize=8)
    for ax in axes:
        ax.grid(alpha=.2)
    fig.savefig('paper-82-jet-semicircle.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
