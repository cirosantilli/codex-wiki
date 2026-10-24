"""Draw the reduced BDDs in Oxford CAFV 2015 Q1(d,e); output to cwd.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch


def draw(ax, positions, labels, arrows, title):
    for source, target, bit, curve in arrows:
        ax.add_patch(FancyArrowPatch(positions[source], positions[target], arrowstyle='-|>',
            mutation_scale=14, linewidth=1.6, linestyle='--' if bit == 0 else '-',
            connectionstyle=f'arc3,rad={curve}', shrinkA=15, shrinkB=15, color='#222222'))
    for name, (x, y) in positions.items():
        if name in ('zero', 'one'):
            ax.add_patch(Rectangle((x - .18, y - .18), .36, .36, facecolor='white', edgecolor='black', lw=1.5, zorder=3))
        else:
            ax.add_patch(Circle((x, y), .19, facecolor='white', edgecolor='black', lw=1.5, zorder=3))
        ax.text(x, y, labels[name], ha='center', va='center', fontsize=16, zorder=4)
    ax.set_title(title, fontsize=16, pad=15)
    ax.set_xlim(-1.65, 1.65)
    ax.set_ylim(-.4, 3.8)
    ax.set_aspect('equal')
    ax.axis('off')


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 5.6), dpi=100, facecolor='white')
    draw(axes[0], {'r':(0,3.4),'u':(-1,2.3),'v':(1,2.3),'w':(.5,1.2),'zero':(-1,0),'one':(1,0)},
        {'r':'z','u':'y','v':'y','w':'x','zero':'0','one':'1'},
        [('r','u',0,0),('r','v',1,0),('u','zero',0,0),('u','one',1,.22),
         ('v','w',0,0),('v','one',1,0),('w','zero',0,0),('w','one',1,0)],
        'z < y < x: 4 decision nodes')
    draw(axes[1], {'r':(0,3.4),'u':(-.65,2.3),'v':(-.65,1.2),'zero':(-1,0),'one':(1,0)},
        {'r':'y','u':'x','v':'z','zero':'0','one':'1'},
        [('r','u',0,0),('r','one',1,0),('u','zero',0,.25),('u','v',1,0),
         ('v','zero',0,0),('v','one',1,0)],
        'y < x < z: 3 decision nodes')
    fig.text(.5,.04,'Dashed edge = 0       Solid edge = 1', ha='center', fontsize=13)
    fig.tight_layout(rect=(0,.07,1,1), pad=1.5)
    fig.savefig(Path('formal-verification-2015-decision-diagrams.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
