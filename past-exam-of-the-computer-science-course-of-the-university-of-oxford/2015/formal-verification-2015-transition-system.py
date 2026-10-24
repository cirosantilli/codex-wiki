"""Plot the synthesized four-state relation in Oxford CAFV 2015 Q1(f).

Output in cwd. Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    fig, ax = plt.subplots(figsize=(7.6, 6.3), dpi=100, facecolor='white')
    positions = {'00':(-1.25,1.1), '01':(1.25,1.1), '10':(-1.25,-1.1), '11':(1.25,-1.1)}
    for s in positions:
        for t in positions:
            if not (t[0] == '1' or (s[1] == '1' and t[1] == '1')):
                continue
            p, q = positions[s], positions[t]
            if s == t:
                x, y = p
                direction = -1 if x < 0 else 1
                start = (x + direction * .20, y + .20)
                end = (x + direction * .20, y - .20)
                path = f'arc3,rad={-1.8 * direction}'
                shrink = 0
            else:
                start, end = p, q
                path = 'arc3,rad=0.17' if (s, t) in [('01','11'),('11','01'),('10','11'),('11','10')] else 'arc3,rad=0'
                shrink = 24
            ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,
                linewidth=1.6,connectionstyle=path,shrinkA=shrink,shrinkB=shrink,color='#222222',zorder=1))
    for name, (x, y) in positions.items():
        ax.add_patch(Circle((x,y),.27,facecolor='white',edgecolor='black',lw=1.5,zorder=3))
        ax.text(x,y,f'$q_{{{name}}}$',ha='center',va='center',fontsize=18,zorder=4)
    ax.text(0,-1.95,'Current state: (u, x)     Next state: (y, z)',ha='center',fontsize=13)
    ax.set_title('Transition relation: y or (x and z)', fontsize=17, pad=18)
    ax.set_xlim(-2.35,2.35)
    ax.set_ylim(-2.2,1.9)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.tight_layout(pad=1.3)
    fig.savefig(Path('formal-verification-2015-transition-system.png'),facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
