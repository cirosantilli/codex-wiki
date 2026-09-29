"""Draw conserved whole-species inventories; Python 3.14/matplotlib 3.10, no measured data."""
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15})
    fig, ax = plt.subplots(figsize=(9, 5.8), dpi=120, facecolor='white')
    ax.axis('off')
    ink = '#213342'
    ax.text(.5, .97, 'Redox: conserved counts', ha='center', va='top', fontsize=23, weight='bold', color=ink, transform=ax.transAxes)
    ax.text(.5, .87, r'$\mathrm{Zn}+\mathrm{Cu}^{2+}\;\longrightarrow\;\mathrm{Zn}^{2+}+\mathrm{Cu}$', ha='center', fontsize=25, color=ink, transform=ax.transAxes)
    labels = ['Inventory', 'Reactants\nZn + Cu²⁺', 'Products\nZn²⁺ + Cu']
    data = [['Zinc atoms', '1', '1'], ['Copper atoms', '1', '1'], ['Net charge / e', '0 + 2 = +2', '2 + 0 = +2'], ['All electrons', '30 + 27 = 57', '28 + 29 = 57']]
    table = ax.table(cellText=data, colLabels=labels, cellLoc='center', colWidths=[.30, .35, .35], bbox=[.04, .28, .92, .48])
    table.auto_set_font_size(False)
    table.set_fontsize(16)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#bac8d3')
        cell.set_linewidth(1.1)
        cell.set_facecolor('#edf4f8' if row == 0 else ('#e9f5ed' if row == 4 else 'white'))
        if row == 0:
            cell.set_text_props(weight='bold', color=ink)
    ax.text(.5, .18, 'All 57 electrons remain: their distribution changes', ha='center', fontsize=18, weight='bold', color='#267245', transform=ax.transAxes)
    ax.text(.5, .10, 'Atomic numbers: Zn = 30; Cu = 29.  A 2+ ion has two fewer electrons.', ha='center', fontsize=13, transform=ax.transAxes)
    ax.text(.5, .035, 'Exact reacting-species counts • compensating solution anions omitted', ha='center', fontsize=12, transform=ax.transAxes)
    fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
