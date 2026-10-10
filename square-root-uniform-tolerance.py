"""Draw common square-root tolerances and unbounded amplification; no external data."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'axes.titlesize': 13, 'axes.labelsize': 12})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 4.8), layout='constrained')
    fig.set_facecolor('white')
    fig.suptitle(r'$g(x)=\sqrt{x}$: uniform continuity allows more than a linear error bound', fontsize=15)
    colors = ['#1764a0', '#bb5a13', '#7254a3']
    eps, delta = 0.4, 0.16
    left.axvspan(-delta, delta, color=colors[0], alpha=0.09)
    for s in [-1, 1]:
        left.axhline(s*eps, color='#555555', lw=1.4, ls='--')
        left.axvline(s*delta, color='#777777', lw=1, ls=':')
    for a, color in zip([0, 1, 4], colors):
        h = np.linspace(max(-a, -0.24), 0.24, 600)
        left.plot(h, np.sqrt(a+h)-np.sqrt(a), color=color, lw=2.5, label=rf'Base point $a={a}$')
    left.set(xlim=(-0.24, 0.24), ylim=(-0.53, 0.59), xlabel=r'Input change $h$ (with $a+h\geq0$)', ylabel=r'Output change $g(a+h)-g(a)$', title=r'Common window: $|h|<0.16$')
    left.text(-0.225, 0.44, r'$\varepsilon=0.4$', fontsize=11)
    left.text(-0.225, -0.49, r'$|g(a+h)-g(a)|\leq\sqrt{|h|}$', fontsize=11)
    left.legend(loc='upper left', bbox_to_anchor=(0.015, 0.81), fontsize=10)
    left.axhline(0, lw=0.7, color='#444444')
    right.set_xscale('log')
    right.set_yscale('log')
    h = np.geomspace(1e-6, 1, 400)
    right.plot(h, 1/np.sqrt(h), color=colors[0], lw=2.5)
    samples = np.array([1, 1/4, 1/16, 1/64])
    right.scatter(samples, 1/np.sqrt(samples), color=colors[1], s=38, zorder=3)
    right.set(xlim=(1e-6, 1), ylim=(0.85, 1600), xlabel=r'Input distance $h$ from zero (log scale)', ylabel='Output / input distance (log scale)', title='No finite Lipschitz bound at zero')
    right.text(2e-6, 2.2, r'$\dfrac{|g(h)-g(0)|}{h}=\dfrac{1}{\sqrt{h}}$', fontsize=14)
    right.annotate('Smaller inputs,\nlarger amplification', (2e-6, 1/np.sqrt(2e-6)), xytext=(4e-4, 140), fontsize=11, arrowprops={'arrowstyle': '->', 'color': colors[0]})
    right.text(0.008, 1.3, 'Exact ratios: 1, 2, 4, 8', fontsize=10)
    for ax in [left, right]:
        ax.set_facecolor('white')
        ax.grid(alpha=0.17)
        ax.spines[['top', 'right']].set_visible(False)
    fig.savefig(Path(__file__).stem+'.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
