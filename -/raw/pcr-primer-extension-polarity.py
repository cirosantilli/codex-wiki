"""Draw primer-directed copying; tested with Python 3.14 / matplotlib 3.10.7.

Run from _media; writes pcr-primer-extension-polarity.png in the CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.5), dpi=120)
    fig.patch.set_facecolor('white')
    gray, blue, green, orange = '#344054', '#2166ac', '#16704a', '#b65a0b'
    panels = [
        ('Upper template: new strand grows leftward', 'AGTCCCTG', 'TCAGGGAC', "5′", "3′", "3′", "5′", 4, 8, green, 4, 0),
        ('Lower template: new strand grows rightward', 'TCAGGGAC', 'AGTCCCTG', "3′", "5′", "5′", "3′", 0, 4, blue, 4, 8),
    ]
    for ax, (title, template, product, tl, tr, pl, pr, begin, end, color, start, finish) in zip(axes, panels):
        ax.set(xlim=(-1.6, 9.6), ylim=(-1.1, 2.15))
        ax.axis('off')
        ax.set_title(title, loc='left', fontsize=14, weight='bold', pad=8)
        ax.plot([0, 8], [1.25, 1.25], color=gray, lw=3)
        ax.text(-0.65, 1.25, tl, ha='center', va='center', color=gray, fontsize=14)
        ax.text(8.65, 1.25, tr, ha='center', va='center', color=gray, fontsize=14)
        ax.text(9.1, 1.25, 'template', ha='left', va='center', color=gray, fontsize=11)
        ax.plot([0, 8], [0.35, 0.35], color=orange, lw=5, solid_capstyle='butt')
        ax.plot([begin, end], [0.35, 0.35], color=color, lw=7, solid_capstyle='butt')
        for x, (a, b) in enumerate(zip(template, product)):
            ax.text(x + 0.5, 1.5, a, ha='center', va='center', fontsize=17, family='DejaVu Sans Mono', color=gray)
            ax.text(x + 0.5, 0.66, b, ha='center', va='center', fontsize=17, family='DejaVu Sans Mono', color=color if begin <= x < end else orange)
            ax.plot([x + 0.5, x + 0.5], [0.8, 1.05], color='#a0a7b4', lw=1.2, ls=':')
        ax.text(-0.65, 0.35, pl, ha='center', va='center', color=orange if start > finish else color, fontsize=14)
        ax.text(8.65, 0.35, pr, ha='center', va='center', color=color if start > finish else orange, fontsize=14)
        ax.text((begin + end)/2, -0.02, 'paired primer', color=color, ha='center', va='center', fontsize=11)
        ax.text(2 if start > finish else 6, -0.02, 'added nucleotides', color=orange, ha='center', va='center', fontsize=11)
        ax.add_patch(FancyArrowPatch((start, -0.45), (finish, -0.45), arrowstyle='-|>', mutation_scale=20, lw=2.2, color=orange))
        ax.text(start, -0.72, 'original paired 3′ end', ha='center', va='center', fontsize=10)
        ax.text(2 if start > finish else 6, -0.95, '5′ → 3′ synthesis', ha='center', va='center', fontsize=11, color=orange)
    fig.suptitle('PCR extension: chemical direction is independent of page direction', fontsize=16, weight='bold', y=0.98)
    fig.text(0.5, 0.025, 'Original 8-position schematic • Four-base primers illustrate polarity only • No flanking DNA shown', ha='center', fontsize=10, color=gray)
    fig.subplots_adjust(left=0.06, right=0.88, top=0.89, bottom=0.12, hspace=0.45)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
