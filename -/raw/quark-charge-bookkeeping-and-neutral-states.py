"""Original constituent arithmetic and orthogonal neutral-flavor examples."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def neutral_vectors():
    return np.array([1., -1., 0.]) / np.sqrt(2), np.array([1., 1., -2.]) / np.sqrt(6)


def main():
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.7, 5.0), gridspec_kw={'width_ratios': [1.22, 1]}, constrained_layout=True)
    ax.axis('off')
    ax.set_title('Add the constituent quantum numbers', fontsize=14, pad=22)
    table = ax.table(cellText=[
        ['Proton', r'$uud$', '+1', '1', '0'],
        ['Neutron', r'$udd$', '0', '1', '0'],
        [r'$K^+$', r'$u\bar s$', '+1', '0', '+1'],
        [r'$\Omega^-$', r'$sss$', '-1', '1', '-3'],
    ], colLabels=['Hadron', 'Valence', 'Q', 'B', 'S'], loc='center', cellLoc='center', colWidths=[.27, .25, .16, .16, .16])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2.8)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor('#c7d0d7')
        cell.set_facecolor('#e6eff5' if r == 0 else ('#f6f8fa' if r % 2 else 'white'))
    ax.text(.5, .08, r'$Q_p=2/3+2/3-1/3=1$', ha='center', transform=ax.transAxes, fontsize=14)
    v, w = neutral_vectors()
    x = np.arange(3)
    bx.bar(x-.18, v, width=.34, color='#176f9c', label=r'$\pi^0$ flavor direction')
    bx.bar(x+.18, w, width=.34, color='#b26010', label=r'$\eta_8$ flavor direction')
    bx.axhline(0, color='#414a54', lw=.9)
    bx.set_xticks(x, [r'$u\bar u$', r'$d\bar d$', r'$s\bar s$'])
    bx.set(xlim=(-.6, 2.6), ylim=(-1.0, 1.22), ylabel='Real flavor amplitude', title='Neutral does not mean identical')
    bx.legend(loc='upper right', fontsize=10, frameon=False)
    bx.text(.5, -.18, r'$\langle\pi^0|\eta_8\rangle=(1-1+0)/\sqrt{12}=0$', ha='center', transform=bx.transAxes, fontsize=12)
    bx.spines[['top', 'right']].set_visible(False)
    bx.grid(axis='y', alpha=.15)
    fig.suptitle('Constituent labels and quantum states answer different questions', fontsize=16)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
