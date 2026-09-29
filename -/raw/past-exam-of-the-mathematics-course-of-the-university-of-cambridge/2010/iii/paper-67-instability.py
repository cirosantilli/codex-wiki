"""Draw the analytic instability domain; tested with Python 3.14.

Uses root-pinned NumPy/Matplotlib, preserves caller MPLCONFIGDIR, and writes
paper-67-instability.png to the caller's current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    threshold = 3 + 2*np.sqrt(2)
    b = np.linspace(.025, 1, 1200)
    d = threshold/b
    fig, ax = plt.subplots(figsize=(7, 4.1), dpi=120, facecolor='white',
                           constrained_layout=True)
    ax.set_facecolor('white')
    ax.fill_between(b, d, 35, where=d<35, color='#b9dcd2', alpha=1)
    ax.plot(b, d, color='#176b55', linewidth=2,
            label=r'Neutral boundary: $d=(3+2\sqrt{2})/b$')
    ax.axvline(1, linestyle='--', color='#555555', linewidth=1.3)
    ax.text(.58, 24, 'Diffusion-driven\ninstability', ha='center',
            va='center', fontsize=12, color='#124f3f')
    ax.text(.56, 3, 'No diffusion-driven instability', ha='center', fontsize=9)
    ax.text(1.055, 18, 'Homogeneous\nkinetics not stable', fontsize=9,
            rotation=90, ha='center', va='center')
    ax.annotate(r'$d\to\infty$ as $b\to0^+$', xy=(.18,32.4),
                xytext=(.32,32), arrowprops={'arrowstyle':'->'}, fontsize=9)
    ax.scatter([1],[threshold], facecolors='white', edgecolors='#176b55', zorder=4)
    ax.set(xlim=(0,1.16), ylim=(0,35), xlabel='Reaction parameter b',
           ylabel='Inhibitor / activator diffusivity ratio d',
           title='Diffusion-driven instability: 0 < b < 1 and db > 3 + 2√2')
    ax.grid(alpha=.22)
    ax.legend(loc='upper right', fontsize=8)
    fig.savefig('paper-67-instability.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
