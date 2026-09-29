"""Draw exact electron cancellation; run from _media with Python 3.14/matplotlib 3.10."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 14})
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=120, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 6.2))
    ax.axis('off')
    orange, blue, ink = '#a84413', '#126591', '#213342'
    ax.text(5, 5.9, 'Electron bookkeeping: coupled half-reactions', ha='center', fontsize=21, weight='bold', color=ink)
    ax.text(5, 5.52, 'One zinc oxidized pairs with one copper(II) ion reduced', ha='center', fontsize=14)
    for y, color, title, eq, charge in [
        (4.30, orange, 'OXIDATION  •  zinc loses 2 electrons', r'$\mathrm{Zn}\;\longrightarrow\;\mathrm{Zn}^{2+}+2e^{-}$', 'Charge / e:   0 = +2 − 2'),
        (2.85, blue, 'REDUCTION  •  copper(II) gains 2 electrons', r'$\mathrm{Cu}^{2+}+2e^{-}\;\longrightarrow\;\mathrm{Cu}$', 'Charge / e:   +2 − 2 = 0'),
    ]:
        ax.add_patch(FancyBboxPatch((0.5, y - .60), 9, 1.25, boxstyle='round,pad=0.05', ec=color, fc='white', lw=1.7))
        ax.text(.8, y + .34, title, color=color, fontsize=14, weight='bold')
        ax.text(.9, y - .19, eq, color=color, fontsize=23)
        ax.text(9.2, y - .15, charge, ha='right', fontsize=13)
    ax.text(5, 1.82, 'ADD: the same 2e⁻ appears on both sides → cancel equal terms', ha='center', fontsize=14, color=ink)
    ax.text(5, 1.22, r'$\mathrm{Zn}+\mathrm{Cu}^{2+}\;\longrightarrow\;\mathrm{Zn}^{2+}+\mathrm{Cu}$', ha='center', fontsize=25, color=ink)
    ax.text(5, .68, 'Net free-electron coefficient:  +2 − 2 = 0', ha='center', fontsize=16, weight='bold')
    ax.text(5, .20, 'Algebraic coupling • no electron trajectory, cell geometry or terminal sign', ha='center', fontsize=12)
    fig.subplots_adjust(left=.015, right=.985, bottom=.015, top=.985)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
