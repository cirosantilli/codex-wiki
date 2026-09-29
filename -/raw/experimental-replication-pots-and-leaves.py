"""Draw a constructed treatment-unit hierarchy; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon


def main():
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=110, facecolor='white')
    ax.set(xlim=(0, 10), ylim=(0, 5.6))
    ax.axis('off')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.text(5, 5.28, 'Eight treatment units, twenty-four measurements',
            ha='center', va='center', fontsize=18, weight='bold', color='#233341')
    ax.text(5, 4.90, 'Constructed design: one plant per pot, three leaves measured per plant',
            ha='center', fontsize=11.5, color='#465461')
    colors = ['#17628c', '#a3421d']
    for row, (group, color) in enumerate(zip(['A', 'B'], colors)):
        y = 3.65 - row * 1.8
        ax.text(.2, y+.42, f'Treatment {group}', color=color, fontsize=13,
                rotation=90, ha='center', va='center', weight='bold')
        for i in range(4):
            x = 1.0 + i * 2.25
            ax.add_patch(FancyBboxPatch((x-.05, y-.7), 1.87, 1.43,
                         boxstyle='round,pad=0.08', ec=color, fc='white', lw=2))
            ax.text(x+.89, y-.49, f'Pot {group}{i+1}: one unit', ha='center',
                    color=color, fontsize=11)
            ax.add_patch(Polygon([(x+.52,y-.26), (x+1.25,y-.26),
                                  (x+1.15,y-.02), (x+.63,y-.02)],
                                 ec='#6d5134', fc='#dfc7a5', lw=1.2))
            ax.plot([x+.89,x+.89], [y-.02,y+.48], color='#39733b', lw=2)
            for k, (dx, dy, angle) in enumerate([(-.23,.16,25),(.24,.27,-25),(-.17,.43,25)]):
                cx, cy = x+.89+dx, y+dy
                ax.add_patch(Ellipse((cx,cy), .47, .23, angle=angle,
                             ec='#39733b', fc='#dcead7', lw=1.4))
                ax.text(cx,cy,str(k+1),ha='center',va='center',fontsize=9,color='#233341')
    ax.text(5,.47, 'Count pots for treatment replication; count leaves for recorded measurements.',
            ha='center', fontsize=12, color='#233341')
    fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
