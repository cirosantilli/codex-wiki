"""Compare zero- and positive-measure Cantor-type constructions; output to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def stages(q, levels=5):
    current=[(0.0,1.0)]
    yield current
    for level in range(1,levels+1):
        width=q(level)/2**level
        current=[child for left,right in current for child in [(left,left+width),(right-width,right)]]
        yield current


def main():
    plt.rcParams.update({'font.size':11,'savefig.facecolor':'white'})
    fig,axes=plt.subplots(1,2,figsize=(10.2,4.6),layout='constrained')
    examples=[(lambda n:(2/3)**n,r'$q_n=(2/3)^n$: limiting measure $0$','#1565a7'),(lambda n:.5+2**(-n-1),r'$q_n=1/2+2^{-n-1}$: limiting measure $1/2$','#238354')]
    for ax,(q,title,color) in zip(axes,examples):
        for level,intervals in enumerate(stages(q)):
            for left,right in intervals:
                ax.add_patch(Rectangle((left,level-.13),right-left,.26,facecolor=color,edgecolor=color,linewidth=.4))
            ax.text(1.03,level,f'{q(level):.3f}',va='center',fontsize=10)
        ax.set(xlim=(-.02,1.18),ylim=(5.5,-.6),yticks=range(6),xticks=[0,.25,.5,.75,1],xlabel='$x$',ylabel='Stage $n$',title=title)
        ax.text(1.03,-.42,'Measure',fontsize=9,ha='left')
        ax.grid(axis='x',alpha=.16)
        ax.spines[['top','right']].set_visible(False)
    fig.savefig(Path.cwd()/'generalized-cantor-retained-measure.png',dpi=100,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
