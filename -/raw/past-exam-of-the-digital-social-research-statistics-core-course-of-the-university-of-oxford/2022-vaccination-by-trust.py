"""Original count-based plot. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7+dfsg1. Output: basename PNG in process CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist


def wilson(k, n):
    p = k / n
    z = NormalDist().inv_cdf(0.975)
    denom = 1 + z*z/n
    center = (p + z*z/(2*n))/denom
    half = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))/denom
    return center-half, center+half


def main():
    tables = [
        np.array([[14, 8], [8, 6], [19, 15], [22, 104], [13, 112]]),
        np.array([[3, 3], [5, 8], [4, 18], [9, 104], [8, 108]]),
        np.array([[1, 2], [2, 5], [3, 10], [3, 52], [7, 72]]),
    ]
    labels = ['Below £20,000', '£20,000–£40,000', '£40,000 and above']
    colors = ['#176b8c', '#936000', '#843c92']
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.6), dpi=110, sharey=True)
    fig.patch.set_facecolor('white')
    for ax, tab, label, color in zip(axes, tables, labels, colors):
        n = tab.sum(axis=1)
        k = tab[:, 1]
        p = k/n
        lo, hi = wilson(k, n)
        assert np.all((lo >= 0) & (hi <= 1) & (lo <= p) & (p <= hi))
        x = np.arange(5)
        ax.errorbar(x, 100*p, yerr=100*np.array([p-lo, hi-p]),
                    fmt='o-', capsize=3, color=color, lw=1.5, markersize=5)
        for i, (yi, ni) in enumerate(zip(p, n)):
            ax.annotate(f'n={ni}', (i, 100*yi), xytext=(0, 9),
                        textcoords='offset points', ha='center', fontsize=8)
        ax.set_title(f'{label}\nTotal n={int(n.sum())}', fontsize=10)
        ax.set_xticks(x, ['1', '2', '3', '4', '5'])
        ax.set_xlabel('NHS trust category (low → high)', fontsize=9)
        ax.set_ylim(0, 108)
        ax.set_yticks(np.arange(0, 101, 20))
        ax.grid(axis='y', color='#dedede', lw=0.6)
        ax.set_facecolor('white')
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].set_ylabel('Vaccinated respondents (%)')
    fig.suptitle('Recorded vaccination and NHS trust within income groups', fontsize=12)
    fig.text(0.5, 0.018, 'Original plot from reported counts; pointwise 95% Wilson intervals. Lines connect ordered categories, not equal trust increments.',
             ha='center', fontsize=8)
    fig.tight_layout(rect=[0, 0.065, 1, 0.94])
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
