"""Draw the joint XOR law and the dependence revealed by conditioning.

Uses only matplotlib and numpy from the root pyproject.toml; saves PNG to cwd.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def draw_joint(ax, matrix, title, subtitle):
    ax.imshow(matrix, cmap='Blues', vmin=0, vmax=0.5)
    for x in range(2):
        for y in range(2):
            probability = matrix[x, y]
            label = {0: '0', 0.25: '1/4', 0.5: '1/2'}[probability]
            ax.text(y, x, label, ha='center', va='center', fontsize=19,
                    color='white' if probability > 0.3 else '#213547')
    ax.set(xticks=[0, 1], yticks=[0, 1], xlabel='Y', ylabel='X')
    ax.set_title(title, fontsize=12)
    ax.set_xticks(np.arange(-0.5, 2, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 2, 1), minor=True)
    ax.grid(which='minor', color='white', linewidth=2)
    ax.tick_params(which='minor', bottom=False, left=False)
    ax.text(0.5, -0.29, subtitle, ha='center', va='top', transform=ax.transAxes,
            fontsize=11)


def main():
    joint = np.zeros((2, 2, 2))
    states = []
    for x in (0, 1):
        for y in (0, 1):
            z = x ^ y
            joint[x, y, z] = 0.25
            states.append([str(x), str(y), str(z), '1/4'])
    marginal = joint.sum(axis=2)
    conditional = [joint[:, :, z] / joint[:, :, z].sum() for z in (0, 1)]
    assert np.allclose(marginal, 0.25)
    assert all(np.allclose(m.sum(axis=0), [0.5, 0.5]) for m in conditional)
    assert all(np.allclose(m.sum(axis=1), [0.5, 0.5]) for m in conditional)

    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(10, 7.5), layout='constrained', facecolor='white')
    grid = fig.add_gridspec(2, 6, height_ratios=[1, 1.28])
    graph = fig.add_subplot(grid[0, :3])
    graph.set(xlim=(-1.5, 1.5), ylim=(-0.2, 1.7))
    graph.axis('off')
    graph.set_title('Independent fair X, Y; Z is their XOR', fontsize=12, pad=12)
    positions = {'X': (-0.9, 1.05), 'Y': (0.9, 1.05), 'Z': (0, 0.10)}
    for name, (x, y) in positions.items():
        graph.add_patch(FancyBboxPatch((x - 0.19, y - 0.16), 0.38, 0.32,
                                      boxstyle='round,pad=0.035',
                                      facecolor='#edf2f7', edgecolor='#41576b'))
        graph.text(x, y, name, ha='center', va='center', fontsize=16, weight='bold')
    for x in (-0.9, 0.9):
        graph.add_patch(FancyArrowPatch((x * 0.83, 0.88), (x * 0.18, 0.31),
                                       arrowstyle='-|>', mutation_scale=18,
                                       linewidth=2, color='#425e79'))
    graph.text(0, 1.42, 'No dependence between the inputs', ha='center', fontsize=10)
    graph.text(0, 0.59, r'$Z=X\oplus Y$', ha='center', fontsize=16)
    table_ax = fig.add_subplot(grid[0, 3:])
    table_ax.axis('off')
    table_ax.set_title('All four possible joint states', fontsize=12, pad=12)
    table = table_ax.table(cellText=states, colLabels=['X', 'Y', 'Z', 'P(X,Y,Z)'],
                          cellLoc='center', bbox=[0.03, 0.02, 0.94, 0.90],
                          colWidths=[0.15, 0.15, 0.15, 0.35])
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#c2cbd4')
        cell.set_facecolor('#e7eef5' if row == 0 else 'white')
        if row == 0:
            cell.set_text_props(weight='bold')
    matrices = [marginal, *conditional]
    titles = ['Before observing Z', 'Given Z = 0\nP(Z = 0) = 1/2',
              'Given Z = 1\nP(Z = 1) = 1/2']
    subtitles = ['P(X,Y)\nIndependent: I(X;Y) = 0',
                 'P(X,Y | Z = 0)\nY = X: one bit of dependence',
                 'P(X,Y | Z = 1)\nY = 1 - X: one bit of dependence']
    for index, (matrix, title, subtitle) in enumerate(zip(matrices, titles, subtitles)):
        ax = fig.add_subplot(grid[1, 2*index:2*index+2])
        draw_joint(ax, matrix, title, subtitle)
    fig.suptitle('Conditioning can reveal dependence: I(X;Y | Z) = 1 bit',
                 fontsize=16, weight='bold')
    fig.savefig(Path.cwd() / 'conditional-information-xor.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
