"""Original distillation schematic. Python 3.14, matplotlib 3.10; run in _media."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch, Arc


def main():
    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=140, facecolor='white')
    ax.set(xlim=(0, 12.6), ylim=(0, 7.5), aspect='equal')
    ax.axis('off')
    glass, blue, orange, green = '#34536b', '#d7edf7', '#c66a25', '#21795b'
    ax.text(.25, 7.14, 'Distillation: from pot to collected condensate', fontsize=19, weight='bold')
    ax.text(.25, 6.75, 'Original schematic • not to scale • no measured temperatures', fontsize=11, color='#555555')
    # A continuous internal vapor route: pot, packed column, head, sloping condenser.
    ax.add_patch(Circle((2.3, 1.85), .78, facecolor='#fffaf0', edgecolor=glass, lw=2))
    ax.add_patch(Polygon([(1.61, 1.50), (2.99, 1.50), (2.83, 1.28), (1.77, 1.28)], closed=True,
                         facecolor='#f5cf85', edgecolor='none'))
    ax.plot([2.05, 2.05, 2.05], [2.59, 3.0, 5.9], color=glass, lw=2)
    ax.plot([2.55, 2.55, 2.55], [2.59, 3.0, 5.9], color=glass, lw=2)
    # Column packing: conceptual contacting surfaces, not individual equilibrium stages.
    for y in [3.15, 3.50, 3.85, 4.20, 4.55]:
        ax.add_patch(Arc((2.3, y), .31, .22, theta1=0, theta2=320, color='#899aa7', lw=1.6))
    # Side arm top and bottom; bulb top exactly at midpoint of opening (y=5.30).
    ax.plot([2.55, 3.20, 9.65, 9.85], [5.45, 5.45, 3.25, 2.75], color=glass, lw=2)
    ax.plot([2.55, 3.14, 9.45, 9.63], [5.15, 5.15, 3.00, 2.52], color=glass, lw=2)
    ax.add_patch(Rectangle((2.00, 5.85), .60, .16, facecolor='#b4c1ca', edgecolor=glass))
    ax.plot([2.30, 2.30], [6.20, 5.12], color='#ae3434', lw=3)
    ax.add_patch(Circle((2.30, 5.16), .14, facecolor='#ae3434', edgecolor='white', lw=.5))
    # Jacket around inclined vapor tube. Water-flow direction deliberately unspecified.
    ax.add_patch(Polygon([(4.24, 5.39), (8.90, 3.80), (8.63, 3.01), (3.97, 4.60)],
                         facecolor=blue, edgecolor=glass, lw=1.6, zorder=0))
    ax.plot([4.64, 4.52], [5.25, 5.60], color=glass, lw=5, solid_capstyle='butt')
    ax.plot([8.22, 8.10], [3.14, 2.79], color=glass, lw=5, solid_capstyle='butt')
    # Open graduated receiver, with distillate at bottom and adapter inside its mouth.
    ax.plot([9.25, 9.25, 10.24, 10.24], [2.65, .85, .85, 2.65], color=glass, lw=2)
    ax.add_patch(Rectangle((9.28, .89), .93, .52, facecolor='#f5cf85', edgecolor='none'))
    for y in [1.1, 1.4, 1.7, 2.0, 2.3]:
        ax.plot([9.25, 9.46], [y, y], color=glass, lw=1)
    ax.plot([9.1, 10.4], [.75, .75], color=glass, lw=2)
    # Source-observed ring under a heating mantle; the stand is schematic.
    ax.add_patch(Arc((2.3, 1.55), 2.05, 1.45, theta1=180, theta2=360, lw=14, color='#ded6cd'))
    ax.add_patch(Arc((2.3, 1.55), 2.05, 1.45, theta1=180, theta2=360, lw=1.6, color='#887466'))
    ax.plot([.65, .65], [.43, 3.15], lw=4, color='#818b93')
    ax.plot([.30, 1.05], [.40, .40], lw=5, color='#818b93')
    ax.plot([.65, 1.35], [.73, .73], lw=3, color='#818b93')
    ax.add_patch(Arc((2.3, .73), 2.05, .16, theta1=0, theta2=360, lw=3, color='#818b93'))
    ax.add_patch(FancyArrowPatch((2.3, .18), (2.3, .78), arrowstyle='-|>', mutation_scale=18, color=orange, lw=2))
    ax.text(2.8, .18, 'controlled heating', color=orange, fontsize=11)
    # Vapor up; returning condensate down. Arrows are explanatory, not flow measurements.
    for xpos, direction, color in [(2.16, (3.1, 4.65), orange), (2.46, (4.65, 3.1), green)]:
        ax.add_patch(FancyArrowPatch((xpos, direction[0]), (xpos, direction[1]), arrowstyle='-|>',
                                    mutation_scale=12, lw=1.6, color=color))
    ax.add_patch(FancyArrowPatch((5.2, 4.60), (6.6, 4.12), arrowstyle='-|>', mutation_scale=16, lw=2, color=orange))

    def label(text, xy, target, color=glass, ha='left'):
        ax.annotate(text, xy=target, xytext=xy, fontsize=11, color=color, ha=ha,
                    arrowprops={'arrowstyle': '-', 'color': color, 'lw': 1.1}, va='center')
    label('Thermometer bulb:\ntop midway in side-arm opening', (3.45, 6.1), (2.40, 5.28))
    label('Packed column\nvapor rises\nliquid returns', (.10, 4.65), (2.03, 4.05))
    label('Pot: liquid mixture', (.22, 2.64), (1.69, 2.10))
    label('Heating mantle\non ring support', (.12, 1.30), (1.39, .87))
    label('Condenser\nwater-cooled jacket', (7.60, 5.55), (7.0, 4.05))
    label('Open receiver\ndistillate', (10.45, 2.22), (10.18, 1.48))
    ax.text(4.0, 1.7, 'Simple distillation: omit the packed column.\nFractional distillation: add repeated vapor–liquid contact.',
            fontsize=11, linespacing=1.7, color='#38444d')
    fig.subplots_adjust(left=.02, right=.99, bottom=.02, top=.99)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', dpi=140)
    plt.close(fig)


if __name__ == '__main__':
    main()
