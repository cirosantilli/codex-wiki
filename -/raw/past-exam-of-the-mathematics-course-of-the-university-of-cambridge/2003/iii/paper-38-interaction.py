"""Generate the interaction-plot coordinates calculated from the software input.
Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-38-interaction.png to the caller's CWD; honors MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    # The software vector uses 33 at the disputed entry, reproducing its fit.
    values = np.array([
        [39,37,38,36,42], [33,33,30,30,31],
        [24,26,24,27,27], [13,14,15,17,18],
        [19,18,19,20,22], [13,13,14,16,16],
        [8,10,12,13,14], [4,5,5,8,7],
    ], dtype=float).reshape(2,4,5)
    means = values.mean(axis=2)
    fig, ax = plt.subplots(figsize=(7.2,4.5), dpi=130, facecolor='white')
    ax.set_facecolor('white')
    for vals, label, style, color in zip(means, ['Men','Women'], ['-','--'], ['#235b92','#a3453b']):
        ax.plot(np.arange(4), vals, style, marker='o', color=color, label=label, linewidth=2)
        for k, v in enumerate(vals):
            ax.annotate(f'{v:.1f}', (k,v), xytext=(0,8), textcoords='offset points', ha='center', fontsize=10)
    ax.set_xticks(np.arange(4), ['18–24','25–44','45–64','65+'])
    ax.set_xlabel('Age group')
    ax.set_ylabel('Mean of yearly percentages')
    ax.set_ylim(0,44)
    ax.set_title('Sex-by-age interaction averaged over years')
    ax.legend(frameon=False)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y', alpha=0.2)
    fig.text(0.5,0.015,'Uses the printed software input; the disputed entry is 33.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,0.035,1,1))
    fig.savefig('paper-38-interaction.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
