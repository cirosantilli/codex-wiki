"""Original functional MWPC diagram. Python 3.14; matplotlib 3.10.7.

Run from _media; emits the matching opaque white PNG in the working directory.
Geometry and waveforms are illustrative, not measurements or a field solution.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


def main():
    fig = plt.figure(figsize=(10.8, 6.6), facecolor='white')
    ax = fig.add_axes((0.02, 0.03, 0.96, 0.87))
    ax.set(xlim=(0, 12), ylim=(0, 7.2))
    ax.axis('off')
    blue, orange, green = '#166ca3', '#c96213', '#24764b'
    fig.suptitle('Gas ionization → avalanche → wire address', fontsize=18, y=0.96)
    ax.text(0.4, 6.8, 'Cross-section: wires point toward the viewer', fontsize=11)
    ax.add_patch(Rectangle((0.45, 2.45), 6.6, 3.7, facecolor='#f7fafc', edgecolor='#d6dce0'))
    for y in (2.6, 6.0):
        ax.plot((0.55, 6.95), (y, y), color=green, lw=5)
    ax.text(6.9, 6.16, 'cathode', color=green, ha='right', fontsize=11)
    ax.text(6.9, 2.22, 'cathode', color=green, ha='right', fontsize=11)
    wires = (1.2, 2.5, 3.8, 5.1, 6.4)
    for k, x in enumerate(wires):
        ax.add_patch(Circle((x, 4.3), 0.075, color=orange, zorder=6))
        ax.text(x, 3.80, str(k), ha='center', fontsize=10)
        # Wire routing schematic exits the section; only channel 2 is highlighted.
        ax.plot((x, x, 7.75), (4.22, 1.95 - k * .16, 1.95 - k * .16),
                color=orange if k == 2 else '#c1c8cc', lw=1.5 if k == 2 else .7,
                zorder=0)
    ax.text(0.65, 3.3, 'anode wires', color=orange, fontsize=11)
    ax.add_patch(FancyArrowPatch((3.05, 6.45), (4.6, 2.20), arrowstyle='-|>', mutation_scale=15,
                                color='#4c485d', lw=2))
    ax.text(1.4, 6.35, 'charged particle', color='#4c485d', fontsize=11)
    for x, y in ((3.35, 5.6), (3.55, 5.05), (4.1, 3.65)):
        ax.plot(x, y, 'o', color=blue, ms=4)
        ax.add_patch(FancyArrowPatch((x, y), (3.78, 4.39 if y > 4.3 else 4.2),
                                    arrowstyle='->', mutation_scale=11, color=blue, lw=1.3,
                                    connectionstyle='arc3,rad=0.12'))
    ax.text(4.15, 5.32, 'electrons drift', color=blue, fontsize=11)
    for r in (.16, .25, .34):
        ax.add_patch(Circle((3.8, 4.3), r, fill=False, edgecolor=orange, alpha=.7, lw=1))
    ax.annotate('local avalanche', xy=(3.98, 4.48), xytext=(4.6, 4.85), fontsize=11,
                color=orange, arrowprops={'arrowstyle': '->', 'color': orange})
    ax.text(.55, 2.92, 'gas', fontsize=11)
    ax.text(.6, .58, 'Illustrative geometry and pulses; no scale or measured timing.', fontsize=10, color='#555555')
    # A field-direction cue; electrons have negative charge and drift opposite E.
    ax.annotate('E', xy=(2.5, 5.7), xytext=(2.5, 4.75), ha='center', color=green,
                arrowprops={'arrowstyle': '->', 'color': green, 'lw': 1.5}, fontsize=12)
    ax.text(7.65, 6.35, 'One electronic channel per wire', fontsize=12, weight='bold')
    boxes = [(7.9, 4.7, 'amplify'), (7.9, 3.45, 'threshold'), (7.9, 2.2, 'latch address')]
    for x, y, label in boxes:
        ax.add_patch(Rectangle((x, y), 3.25, .7, facecolor='white', edgecolor=blue, lw=1.6))
        ax.text(x + 1.625, y + .35, label, va='center', ha='center', fontsize=12)
    for top, bottom in ((4.7, 4.15), (3.45, 2.9)):
        ax.add_patch(FancyArrowPatch((9.52, top), (9.52, bottom), arrowstyle='-|>',
                                    mutation_scale=13, color=blue, lw=1.3))
    ax.annotate('', xy=(7.9, 5.05), xytext=(7.3, 5.05),
                arrowprops={'arrowstyle': '->', 'color': orange, 'lw': 1.8})
    ax.text(7.28, 5.38, 'pulse', fontsize=10, color=orange)
    ax.plot((7.25, 7.35, 7.41, 7.5, 7.7), (5.06, 5.06, 4.76, 4.98, 5.06), color=orange, lw=1.6)
    ax.text(7.95, 1.63, 'selected interval: wire 2 fired', fontsize=11, color=blue)
    ax.text(7.95, 1.19, 'addresses → track reconstruction', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
