"""Original circular-versus-linear digest and plasmid-selection diagram.

Python 3.14; matplotlib 3.10.7, numpy 2.3.5. Run from _media to emit the matching PNG.
All positions and candidate constructs are hypothetical, not experimental observations.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

LENGTH = 6000
CUTS = (1000, 2500, 4500)
COLORS = ('#f3c484', '#83b7df', '#a7cfba', '#f3c484')


def circular_fragments(length, cuts):
    ordered = sorted(cuts)
    return [b-a for a, b in zip(ordered, ordered[1:])] + [length-ordered[-1]+ordered[0]]


def linear_fragments(length, cuts):
    ends = [0, *sorted(cuts), length]
    return [b-a for a, b in zip(ends, ends[1:])]


def box(ax, xy, width, height, text, color='#f8fafc', border='#cbd5e1', fontsize=11):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle='round,pad=0.012',
                               facecolor=color, edgecolor=border, linewidth=1.2))
    ax.text(xy[0]+width/2, xy[1]+height/2, text, ha='center', va='center', fontsize=fontsize, linespacing=1.4)


def arrow(ax, a, b):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=15, lw=1.4, color='#475569'))


def main():
    assert circular_fragments(LENGTH, CUTS) == [1500, 2000, 2500]
    assert linear_fragments(LENGTH, CUTS) == [1000, 1500, 2000, 1500]
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig = plt.figure(figsize=(11, 7.2), dpi=130, facecolor='white')
    fig.text(.04, .95, 'Count fragments first; confirm selected candidates separately', fontsize=17, weight='bold')
    fig.text(.04, .908, 'Original 6000 bp example • complete A + B cutting at 1000, 2500 and 4500', color='#475569')
    ax = fig.add_axes([.04, .53, .92, .32])
    ax.set(xlim=(-600, 7900), ylim=(-.7, 2.0)); ax.axis('off')
    ax.text(-540, 1.65, 'Circular DNA: follow cuts around the ring, then unfold each interval', weight='bold', fontsize=11)
    starts = [0, 1500, 3500]
    for x, length, color in zip(starts, circular_fragments(LENGTH, CUTS), COLORS):
        ax.add_patch(Rectangle((x, .9), length, .32, facecolor=color, edgecolor='white', linewidth=2))
        ax.text(x+length/2, 1.06, f'{length} bp', ha='center', va='center', fontsize=11)
    for x, label in zip((0, 1500, 3500, 6000), ('A 1000', 'B 2500', 'B 4500', 'A 1000')):
        ax.text(x, 1.32, label, ha='center', fontsize=9)
    ax.text(6450, 1.06, '3 fragments\nSum: 6000 bp', va='center', fontsize=11)
    ax.text(4750, .65, '2500 bp crosses zero', ha='center', color='#475569', fontsize=9)
    ax.text(-540, .27, 'Linear DNA: physical ends already exist at 0 and 6000', weight='bold', fontsize=11)
    ends = (0, *CUTS, LENGTH)
    for x, length, color in zip(ends[:-1], linear_fragments(LENGTH, CUTS), COLORS):
        ax.add_patch(Rectangle((x, -.35), length, .32, facecolor=color, edgecolor='white', linewidth=2))
        ax.text(x+length/2, -.19, f'{length}', ha='center', va='center', fontsize=11)
    for x, label in zip(ends, ('end 0', 'A 1000', 'B 2500', 'B 4500', 'end 6000')):
        ax.text(x, -.52, label, ha='center', fontsize=9)
    ax.text(6450, -.19, '4 fragments\nSum: 6000 bp', va='center', fontsize=11)
    flow = fig.add_axes([.04, .105, .92, .37]); flow.set(xlim=(0, 1), ylim=(0, 1)); flow.axis('off')
    flow.text(0, .97, 'A growth marker identifies candidates, not the insert', fontsize=13, weight='bold')
    box(flow, (.015, .55), .26, .23, 'Intended construct\n6000 bp, marker + insert', color='#fff3e6', border='#d77722')
    box(flow, (.015, .15), .26, .23, 'Empty carrier\n4500 bp, marker retained', color='#edf6f1', border='#27845b')
    box(flow, (.405, .35), .21, .23, 'Both can grow\nunder marker selection', color='#eff6ff', border='#2475b0')
    box(flow, (.735, .35), .24, .23, 'Recover candidate DNA\nDigest + sequence joins', fontsize=11)
    arrow(flow, (.29, .66), (.395, .50)); arrow(flow, (.29, .27), (.395, .42))
    arrow(flow, (.63, .465), (.725, .465))
    flow.text(.405, .16, 'Selection ≠ insert confirmation', fontsize=11, color='#475569')
    fig.text(.04, .045, 'No measured bands or colony counts. Equal-sized linear fragments can share a gel band.\nThe empty carrier assumes precise insert removal and joining without other DNA loss.', fontsize=10, color='#475569', linespacing=1.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
