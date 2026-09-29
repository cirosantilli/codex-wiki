"""RSC Pauling values and calculated ground-state Mulliken values; Python 3.14.

Run from _media; writes its own basename to the current working directory.
Source: https://periodic-table.rsc.org/element/{1/hydrogen,17/chlorine}
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

PAULING = np.array([2.20, 3.16])
IONIZATION = np.array([1312.05, 1251.186])  # kJ/mol
AFFINITY = np.array([72.769, 348.575])  # positive energy released, kJ/mol
EV_TO_KJ_MOL = 1.602176634e-19 * 6.02214076e23 / 1000
MULLIKEN = (IONIZATION + AFFINITY) / 2 / EV_TO_KJ_MOL


def main():
    assert np.isclose(PAULING[1] - PAULING[0], 0.96)
    np.testing.assert_allclose(MULLIKEN, [7.176325, 8.290178], atol=0.00001)
    plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.25), layout='constrained')
    for ax, vals, title, label, xmax in zip(axes, [PAULING, MULLIKEN],
            ['Pauling: tabulated', 'Mulliken: calculated'],
            ['Relative electronegativity (dimensionless)', 'Ground-state average (eV per atom)'], [4, 10]):
        ax.barh([1, 0], vals, color=['#2679ab', '#c36922'], height=.45)
        ax.set(yticks=[1, 0], yticklabels=['Hydrogen', 'Chlorine'], xlim=(0, xmax), ylim=(-.65, 1.65), xlabel=label, title=title)
        for y, val in zip([1, 0], vals):
            ax.text(val + .07, y, f'{val:.2f}' if xmax == 4 else f'{val:.3f}', va='center', fontsize=13)
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(axis='x', alpha=.18)
        ax.set_axisbelow(True)
    fig.suptitle('Same ordering, different scales and units', fontsize=17)
    fig.text(.5, -.035, r'Mulliken inputs: $I$ = removal cost; $A$ = attachment energy released; $\chi_M=(I+A)/2$.', ha='center', fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white', bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
