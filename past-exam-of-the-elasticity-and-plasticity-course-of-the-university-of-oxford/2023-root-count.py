"""Plot rigid-backed elastic-layer roots. Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7.

Run from the desired output directory; writes 2023-root-count.png there.
"""

from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def intersections(A, epsilon):
    roots = []
    n = 1
    while (n - 0.5) * np.pi < A - 1e-12:
        lo = (n - 0.5) * np.pi + 1e-9
        hi = min(n * np.pi, A) - 1e-9
        for _ in range(80):
            mid = (lo + hi) / 2
            residual = np.tan(mid) + epsilon * mid / np.sqrt(A * A - mid * mid)
            if residual > 0:
                hi = mid
            else:
                lo = mid
        roots.append((lo + hi) / 2)
        n += 1
    return np.array(roots)


def main():
    epsilon = 0.18
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.2), layout='constrained', facecolor='white')
    for ax, A, subtitle in zip(
        axes,
        [2.6 * np.pi, 2.5 * np.pi],
        ['3 trapped modes', '2 trapped modes; cutoff excluded'],
        strict=True,
    ):
        theta = np.linspace(0, A - 1e-5, 2200)
        rhs = -epsilon * theta / np.sqrt(A * A - theta * theta)
        ax.plot(theta / np.pi, rhs, color='#c44728', lw=2.2,
                label=r'$-\epsilon\theta/\sqrt{A^2-\theta^2}$')
        # Draw each branch separately so no line crosses a tangent pole.
        for n in range(4):
            left = max(0, (n - 0.5) * np.pi) + 1e-5
            right = min(A, (n + 0.5) * np.pi) - 1e-5
            if left < right:
                t = np.linspace(left, right, 800)
                ax.plot(t / np.pi, np.tan(t), color='#14659c', lw=1.6,
                        label=r'$\tan\theta$' if n == 0 else None)
        roots = intersections(A, epsilon)
        ax.scatter(roots / np.pi, np.tan(roots), color='#222222', s=25, zorder=5,
                   label='trapped mode')
        ax.axvline(A / np.pi, color='#7a478b', ls='--', lw=1.3, label=r'endpoint $A$')
        ax.axhline(0, color='0.5', lw=0.7)
        ax.set(xlim=(0, 2.8), ylim=(-6, 0.8), xlabel=r'$\theta/\pi$',
               title=rf'$A={A / np.pi:.1f}\pi$, $\epsilon={epsilon}$' + '\n' + subtitle)
        ax.set_xticks(np.arange(0, 3, 0.5))
        ax.grid(alpha=0.18)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].set_ylabel('value of each side')
    handles, labels = axes[0].get_legend_handles_labels()
    axes[1].legend(handles, labels, loc='lower left', fontsize=9, framealpha=0.95)
    fig.savefig(Path.cwd() / '2023-root-count.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
