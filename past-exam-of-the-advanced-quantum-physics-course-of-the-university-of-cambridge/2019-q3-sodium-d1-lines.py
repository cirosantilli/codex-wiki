"""Original weak-field electronic D1 line positions; Python 3.14/matplotlib 3.10.7.

Run from mirrored _media directory. Hyperfine structure and line broadening omitted.
Equal heights illustrate unpolarized lower-state populations and a weak probe.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig,axes=plt.subplots(2,1,figsize=(7.3,4.8),sharex=True,layout='constrained')
    configs=[([-2/3,2/3],'#236bc0',r'Parallel: $\mathbf{E}\parallel\mathbf{B}$', [r'$+1/2\to+1/2$',r'$-1/2\to-1/2$']),([-4/3,4/3],'#c26712',r'Perpendicular: $\mathbf{E}\perp\mathbf{B}$',[r'$\sigma^-,\ \Delta m=-1$',r'$\sigma^+,\ \Delta m=+1$'])]
    for ax,(positions,color,title,labels) in zip(axes,configs):
        ax.axhline(0,color='0.4',lw=.8)
        ax.axvline(0,color='0.7',ls=':',lw=1)
        for x,label in zip(positions,labels):
            ax.plot([x,x],[0,1],color=color,lw=2.5)
            ax.scatter([x],[1],s=32,color=color)
            ax.text(x,1.08,label,ha='center',fontsize=10,color=color)
        ax.set(ylim=(-.05,1.4),title=title,ylabel='Relative absorption')
        ax.set_yticks([0,1])
    axes[-1].set(xlim=(-1.8,1.8),xlabel=r'Frequency offset $(\nu-\nu_0)/(\mu_B B_z/h)$')
    axes[-1].set_xticks([-4/3,-2/3,0,2/3,4/3],labels=[r'$-4/3$',r'$-2/3$','0',r'$2/3$',r'$4/3$'])
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
