"""Draw all eight rows of an original CNF formula, using opaque white output.

Tested with Python 3.14 and matplotlib 3.10.7. Run from _media.
"""
from itertools import product
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size': 14, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(10, 6.3), dpi=100, facecolor='white')
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.02, top=0.98)
    ax.axis('off')
    ink = '#172c40'
    ax.text(0.5, 0.97, 'All eight assignments: exactly two models', transform=ax.transAxes, ha='center', fontsize=20, weight='bold', color=ink)
    ax.text(0.5, 0.895, r'$C_1=x\vee y\qquad C_2=\neg x\vee z\qquad C_3=\neg y\vee\neg z$', transform=ax.transAxes, ha='center', fontsize=17, color=ink)
    headers = ['$x$', '$y$', '$z$', '$C_1$', '$C_2$', '$C_3$', '$F$', 'Result']
    rows, models = [], []
    for x, y, z in product((0, 1), repeat=3):
        values = (int(bool(x or y)), int(bool((not x) or z)), int(bool((not y) or (not z))))
        accepted = all(values)
        rows.append([x, y, z, *values, int(accepted), 'model' if accepted else 'fails'])
        models.append(accepted)
    assert [tuple(row[:3]) for row, ok in zip(rows, models) if ok] == [(0, 1, 0), (1, 0, 1)]
    table = ax.table(cellText=rows, colLabels=headers, cellLoc='center', bbox=(0.025, 0.14, 0.95, 0.68), colWidths=[.09]*3+[.125]*3+[.09, .16])
    table.auto_set_font_size(False)
    table.set_fontsize(17)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor('#aabac6')
        cell.set_linewidth(0.8)
        cell.get_text().set_color(ink)
        if r == 0:
            cell.set_facecolor('#e5eef5')
            cell.get_text().set_weight('bold')
        elif models[r-1]:
            cell.set_facecolor('#e0f3e9')
            cell.get_text().set_color('#17613e')
            cell.get_text().set_weight('bold')
        else:
            cell.set_facecolor('white' if r % 2 else '#f5f7f9')
            if c in (3, 4, 5, 6) and rows[r-1][c] == 0:
                cell.get_text().set_color('#aa3434')
    ax.text(0.5, 0.075, r'$F=C_1\wedge C_2\wedge C_3$: all three clause values must be 1.', transform=ax.transAxes, ha='center', fontsize=16, color=ink)
    ax.text(0.5, 0.015, '0 = false    1 = true    Green rows are the satisfying assignments.', transform=ax.transAxes, ha='center', fontsize=14, color=ink)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
