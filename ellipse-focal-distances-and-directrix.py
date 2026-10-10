"""Original metric ellipse example: focal sum and focus/directrix ratio."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.5), facecolor='white')
    t = np.linspace(0, 2*np.pi, 801)
    p = np.array([3., 12/5])
    left = np.array([-4., 0.])
    right = np.array([4., 0.])
    foot = np.array([25/4, 12/5])
    for ax in axes:
        ax.plot(5*np.cos(t), 3*np.sin(t), color='#236f97', lw=2.1)
        ax.axhline(0, color='#c4ccd2', lw=.9)
        ax.axvline(0, color='#c4ccd2', lw=.9)
        ax.scatter(*p, color='#222f3d', s=40, zorder=6)
        ax.text(.7, 3.48, r'$P=(3,12/5)$', fontsize=11)
        ax.scatter([-4, 4], [0, 0], color='#aa4c29', s=35, zorder=6)
        ax.text(-4.42, -.52, r'$F_-$', fontsize=12)
        ax.text(3.9, -.52, r'$F_+$', fontsize=12)
        ax.set_aspect('equal')
        ax.set_xlim(-5.7, 7.0)
        ax.set_ylim(-4.15, 4.05)
        ax.set_xticks([-4, 0, 4])
        ax.set_yticks([-3, 0, 3])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.spines[['top', 'right']].set_visible(False)
        ax.set_facecolor('white')
    ax = axes[0]
    ax.plot([left[0], p[0], right[0], left[0]], [left[1], p[1], right[1], left[1]],
            color='#b84d25', lw=1.8)
    ax.text(-1.38, 1.62, r'$37/5$', fontsize=13, color='#a24120')
    ax.text(3.98, 1.35, r'$13/5$', fontsize=13, color='#a24120')
    ax.text(-.2, -.46, '8', fontsize=12, color='#a24120')
    ax.set_title('Fixed sum of focal distances', fontsize=14, weight='bold')
    ax.text(.5, -.24, r'$37/5+13/5=10=2a$'+'\nClosed string loop: 10 + 8 = 18',
            transform=ax.transAxes, ha='center', fontsize=12)
    ax = axes[1]
    ax.axvline(25/4, color='#23836d', lw=1.8)
    ax.plot([p[0], right[0]], [p[1], right[1]], color='#b84d25', lw=2)
    ax.plot([p[0], foot[0]], [p[1], foot[1]], color='#23836d', lw=2)
    ax.plot([foot[0]-.18, foot[0]-.18, foot[0]],
            [foot[1], foot[1]-.18, foot[1]-.18], color='#23836d', lw=1.2)
    ax.text(4.1, 1.3, r'$13/5$', color='#a24120', fontsize=13)
    ax.text(4.57, 2.69, r'$13/4$', color='#23836d', fontsize=13)
    ax.text(6.36, -3.0, r'$x=25/4$', color='#23836d', fontsize=11, rotation=90)
    ax.set_title('Fixed focus-directrix ratio', fontsize=14, weight='bold')
    ax.text(.5, -.24, r'$e=(13/5)/(13/4)=4/5$'+'\nOne focus is paired with this directrix.',
            transform=ax.transAxes, ha='center', fontsize=12)
    fig.suptitle(r'One ellipse: $x^2/25+y^2/9=1$,  $a=5$, $b=3$, $c=4$',
                 fontsize=17, weight='bold', y=.965)
    fig.subplots_adjust(left=.06, right=.98, top=.83, bottom=.24, wspace=.20)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
