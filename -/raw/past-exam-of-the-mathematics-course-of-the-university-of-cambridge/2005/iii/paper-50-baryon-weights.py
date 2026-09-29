"""Original flavour-weight diagrams; Python 3.14.4, matplotlib 3.10.7.

Write the opaque PNG basename to the caller's CWD. Matplotlib respects the
caller's MPLCONFIGDIR; this generator does not select a cache directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.8), dpi=120)
    fig.patch.set_facecolor('white')
    for ax in axes:
        ax.set_facecolor('white')
        ax.set_xlim(-1.9, 1.9)
        ax.set_ylim(-1.22, .85)
        ax.set_xticks([-1.5, -1, -.5, 0, .5, 1, 1.5])
        ax.set_yticks([-1, -.5, 0, .5])
        ax.set_yticklabels(['−1', '−1/2', '0', '1/2'])
        ax.axhline(0, color='#cccccc', linewidth=.8, zorder=0)
        ax.axvline(0, color='#cccccc', linewidth=.8, zorder=0)
        ax.set_xlabel(r'$I_3$', fontsize=12)
        ax.set_ylabel(r'$Y=(B+S)/2$', fontsize=11)
        ax.grid(True, alpha=.12)
        ax.tick_params(labelsize=8)
    def points(ax, entries, color):
        for x, y, label in entries:
            ax.scatter([x], [y], s=32, color=color, zorder=3)
            ax.annotate(label, (x, y), xytext=(0, 9), textcoords='offset points',
                        ha='center', va='bottom', fontsize=11)
    axes[0].set_title(r'Flavour singlet: $\mathbf{1}$', fontsize=12)
    points(axes[0], [(0, 0, r'$\Lambda_1$')], '#555555')
    axes[0].text(.5, .07, 'Algebraic qqq state; absent from\nthe spatially symmetric ground multiplet',
                 transform=axes[0].transAxes, ha='center', va='bottom', fontsize=8)
    axes[1].set_title(r'Octet: $\mathbf{8}$ (two abstract copies)', fontsize=12)
    octet=[(-.5,.5,r'$n$'),(.5,.5,r'$p$'),(-1,0,r'$\Sigma^-$'),
           (0,0,r'$\Sigma^0,\Lambda^0$'),(1,0,r'$\Sigma^+$'),
           (-.5,-.5,r'$\Xi^-$'),(.5,-.5,r'$\Xi^0$')]
    hull=[(-.5,.5),(.5,.5),(1,0),(.5,-.5),(-.5,-.5),(-1,0),(-.5,.5)]
    axes[1].plot([x for x,y in hull],[y for x,y in hull],color='#bbccdd',linewidth=1,zorder=0)
    points(axes[1],octet,'#236192')
    axes[1].text(.5,.07,'The origin has multiplicity two',transform=axes[1].transAxes,
                 ha='center',va='bottom',fontsize=8)
    axes[2].set_title(r'Symmetric decuplet: $\mathbf{10}$',fontsize=12)
    decuplet=[(-1.5,.5,r'$\Delta^-$'),(-.5,.5,r'$\Delta^0$'),(.5,.5,r'$\Delta^+$'),
             (1.5,.5,r'$\Delta^{++}$'),(-1,0,r'$\Sigma^{*-}$'),(0,0,r'$\Sigma^{*0}$'),
             (1,0,r'$\Sigma^{*+}$'),(-.5,-.5,r'$\Xi^{*-}$'),(.5,-.5,r'$\Xi^{*0}$'),
             (0,-1,r'$\Omega^-$')]
    axes[2].plot([-1.5,1.5,0,-1.5],[.5,.5,-1,.5],color='#dbb9ac',linewidth=1,zorder=0)
    points(axes[2],decuplet,'#a34722')
    fig.suptitle(r'Baryon flavour weights in the convention $Q=I_3+Y$',fontsize=14,y=.98)
    fig.tight_layout(rect=(0,0,1,.93),w_pad=1.3)
    output=Path(Path(__file__).with_suffix('.png').name)
    fig.savefig(output,facecolor='white',transparent=False)
    plt.close(fig)
    print(output)

if __name__=='__main__':
    main()
