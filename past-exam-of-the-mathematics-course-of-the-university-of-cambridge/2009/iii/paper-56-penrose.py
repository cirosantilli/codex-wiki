"""Penrose diagram of the single-horizon charged geometry.

Python 3.14 / matplotlib 3.10; write the PNG basename to the caller's CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(figsize=(9, 6), layout='constrained', facecolor='white')
    for side in (-1, 1):
        ax.plot([side, 2*side, side], [1, 0, -1], color='#222222', lw=1.7)
        ax.plot([side, 0, side], [1, 0, -1], color='#246aa2', lw=1.7)
        ax.text(1.62*side, .58, '$\\mathscr{I}^{+}$', fontsize=17, ha='center')
        ax.text(1.62*side, -.58, '$\\mathscr{I}^{-}$', fontsize=17, ha='center')
        ax.text(2.12*side, 0, '$i^0$', fontsize=14, ha='center', va='center')
        ax.text(1.12*side, 1.08, '$i^+$', fontsize=14, ha='center')
        ax.text(1.12*side, -1.2, '$i^-$', fontsize=14, ha='center')
        ax.text(.60*side, .48, '$\\mathcal{H}^+$', color='#246aa2', fontsize=13, ha='center')
        ax.text(.60*side, -.58, '$\\mathcal{H}^-$', color='#246aa2', fontsize=13, ha='center')
    ax.plot([-1, 1], [1, 1], color='#9b302f', lw=3)
    ax.plot([-1, 1], [-1, -1], color='#9b302f', lw=3)
    ax.text(0, 1.15, '$r=0$: future spacelike singularity', fontsize=13, ha='center')
    ax.text(0, -1.32, '$r=0$: past spacelike singularity', fontsize=13, ha='center')
    ax.text(0, .67, 'II\nBlack hole', fontsize=14, ha='center', va='center')
    ax.text(0, -.67, 'IV\nWhite hole', fontsize=14, ha='center', va='center')
    ax.text(1.15, 0, 'I\nExterior', fontsize=14, ha='center', va='center')
    ax.text(-1.15, 0, 'III\nExterior', fontsize=14, ha='center', va='center')
    ax.scatter([0], [0], color='#246aa2', s=32, zorder=3)
    ax.annotate('Bifurcation sphere', (0, 0), xytext=(0, .25), ha='center', fontsize=11,
                arrowprops={'arrowstyle':'-', 'color':'#555555'})
    ax.text(0, -1.6, 'Blue null boundaries: $r=2m$; each interior point represents a two-sphere.',
            ha='center', fontsize=11)
    ax.set_aspect('equal')
    ax.set_xlim(-2.45, 2.45)
    ax.set_ylim(-1.75, 1.48)
    ax.axis('off')
    fig.savefig('paper-56-penrose.png', dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
