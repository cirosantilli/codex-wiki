"""Draw the two-coroutine FIFO trace; output is always in the current directory.
Tested with Python 3.14.4 and matplotlib 3.10.7 (repository dependencies).
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, ax = plt.subplots(figsize=(9.6, 4.6), dpi=120, facecolor='white')
    ax.set(xlim=(0, 1), ylim=(0, 1)); ax.axis('off')
    fig.subplots_adjust(left=0.025, right=0.985, top=0.94, bottom=0.04)
    ax.text(0.5, 0.97, 'Two coroutines, one FIFO continuation queue',
            ha='center', va='center', fontsize=15, weight='bold', color='#172b4d')
    xp, xc = 0.25, 0.58
    ax.text(xp, 0.875, 'Parent P', ha='center', weight='bold', color='#225d99')
    ax.text(xc, 0.875, 'Child C', ha='center', weight='bold', color='#a04e13')
    ax.text(0.86, 0.875, 'Ready after transfer', ha='center', fontsize=10)
    for x in [xp, xc]:
        ax.plot([x, x], [0.19, 0.84], color='#b7c3d0', lw=1.4, ls=(0, (3, 3)), zorder=0)
    rows = [
        (0.77, xp, xc, 'fork', 'P'),
        (0.64, xc, xp, 'write 1; yield', 'C'),
        (0.51, xp, xc, 'write 3; yield', 'P'),
        (0.38, xc, xp, 'write 2; finish', 'empty'),
    ]
    for y, source, dest, label, queue in rows:
        color = '#225d99' if source == xp else '#a04e13'
        ax.text(source, y+0.045, label, ha='center', va='center', fontsize=10, color=color,
                bbox={'boxstyle': 'round,pad=0.25', 'fc': 'white', 'ec': color, 'lw': 1})
        ax.annotate('', xy=(dest,y-0.008), xytext=(source,y-0.008),
                    arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 1.8, 'mutation_scale': 12})
        ax.add_patch(FancyBboxPatch((0.80,y-0.032),0.12,0.055,
                     boxstyle='round,pad=0.009',edgecolor='#b7c3d0',facecolor='#f3f6f9'))
        ax.text(0.86,y-0.005,queue,ha='center',va='center',fontsize=10)
    ax.text(xp, 0.235, 'write 4; finish', ha='center', color='#225d99', fontsize=10,
            bbox={'boxstyle':'round,pad=0.25','fc':'white','ec':'#225d99'})
    ax.text(0.86, 0.235, 'scheduler exits', ha='center', fontsize=10, color='#52657a')
    ax.text(0.5, 0.08, 'Writes: 1, 3, 2, 4     →     prepended list: [4, 2, 3, 1]',
            ha='center', va='center', fontsize=12, color='#172b4d',
            bbox={'boxstyle':'round,pad=0.5','fc':'#edf5f1','ec':'#9cbaad'})
    target=Path.cwd()/'programming-languages-2015-coroutine-schedule.png'
    fig.savefig(target,facecolor='white',transparent=False,
                metadata={'Software':'codex-wiki matplotlib generator'})
    plt.close(fig)


if __name__ == '__main__':
    main()
