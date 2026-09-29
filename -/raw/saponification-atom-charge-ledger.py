"""Draw an original ester hydrolysis ledger; Python 3.14, matplotlib 3.10."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig = plt.figure(figsize=(10, 6.2), dpi=100, facecolor='white')
    ax = fig.add_axes([0.03, 0.02, 0.94, 0.96])
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis('off')
    ax.text(5, 5.96, 'One ester + one hydroxide → one carboxylate + one alcohol',
            ha='center', va='top', fontsize=17, weight='bold')
    ax.text(5, 5.37,
            r'$\mathrm{CH_3COOC_2H_5 + OH^- \longrightarrow CH_3COO^- + C_2H_5OH}$',
            ha='center', va='center', fontsize=19)
    cols = [0.4, 4.0, 5.25, 6.5, 7.75, 9.0]
    headers = ['Species / side', 'C atoms', 'H atoms', 'O atoms', 'Charge', 'Role']
    rows = [
        ['Ethyl acetate', '4', '8', '2', '0', 'ester'],
        ['Hydroxide', '0', '1', '1', '−1', 'base'],
        ['Reactant total', '4', '9', '3', '−1', ''],
        ['Acetate', '2', '3', '2', '−1', 'anion'],
        ['Ethanol', '2', '6', '1', '0', 'alcohol'],
        ['Product total', '4', '9', '3', '−1', ''],
    ]
    for x, label in zip(cols, headers):
        ax.text(x, 4.60, label, ha='left' if x == cols[0] else 'center',
                va='center', weight='bold', fontsize=12)
    for j, row in enumerate(rows):
        y = 4.06 - j * 0.49
        total = j in (2, 5)
        if total:
            ax.add_patch(FancyBboxPatch((0.18, y - 0.20), 9.64, 0.40,
                         boxstyle='round,pad=0.03', facecolor='#e7f2f8', edgecolor='none'))
        for i, (x, label) in enumerate(zip(cols, row)):
            ax.text(x, y, label, ha='left' if i == 0 else 'center', va='center',
                    weight='bold' if total else 'normal', color='#17344a')
        if j == 2:
            ax.plot([0.18, 9.82], [y - 0.26, y - 0.26], color='#96a7b2', linewidth=1)
    ax.text(5, 0.98, 'Atoms balance separately; the negative charge remains on acetate.',
            ha='center', fontsize=13, weight='bold')
    ax.text(5, 0.49, 'Hydroxide is consumed. Sodium, if present, is a spectator ion.',
            ha='center', fontsize=12)
    ax.text(5, 0.14, 'Formula accounting, not a molecular collision or kinetic trace.',
            ha='center', fontsize=11, color='#53616a')
    fig.savefig(Path(__file__).stem + '.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
