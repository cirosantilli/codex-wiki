"""Collapse an additive six-element group to its three cosets and operation."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    cosets=[{r,(r+3)%6} for r in range(3)]
    assert set.union(*cosets)==set(range(6))
    assert all(cosets[a].isdisjoint(cosets[b]) for a in range(3) for b in range(a))
    for a in range(6):
        for b in range(6):
            assert ((a+b)%6)%3 == (a%3+b%3)%3
    for a in range(3):
        for b in range(3):
            result={(x+y)%6 for x in cosets[a] for y in cosets[b]}
            assert result==cosets[(a+b)%3]
    colors=['#f0d6ca','#d5e5f1','#d8e9d7']
    names=[r'$N$',r'$1+N$',r'$2+N$']
    fig,axes=plt.subplots(1,3,figsize=(11.8,5.2),dpi=120,facecolor='white',
                          gridspec_kw={'width_ratios':[1,1,1.05]})
    for ax in axes[:2]:
        ax.set(xlim=(-1.6,1.6),ylim=(-1.65,1.55),aspect='equal')
        ax.axis('off')
    for g in range(6):
        angle=np.pi/2-2*np.pi*g/6
        x,y=np.cos(angle),np.sin(angle)
        axes[0].add_patch(Circle((x,y),.25,facecolor=colors[g%3],edgecolor='#657b8b',lw=1.4))
        axes[0].text(x,y,str(g),ha='center',va='center',fontsize=16)
    axes[0].text(0,-1.53,r'$N=\{0,3\}$',ha='center',fontsize=14)
    axes[0].set_title('G: six residues',fontsize=15,pad=18)
    for r in range(3):
        angle=np.pi/2-2*np.pi*r/3
        x,y=np.cos(angle),np.sin(angle)
        axes[1].add_patch(Circle((x,y),.39,facecolor=colors[r],edgecolor='#657b8b',lw=1.4))
        axes[1].text(x,y+.1,names[r],ha='center',va='center',fontsize=14)
        axes[1].text(x,y-.15,rf'$\{{{r},{r+3}\}}$',ha='center',va='center',fontsize=12)
    axes[1].text(0,-1.53,'Each coset is one group element',ha='center',fontsize=11)
    axes[1].set_title('G/N: three cosets',fontsize=15,pad=18)
    axes[2].axis('off')
    axes[2].set_title('Addition in G/N',fontsize=15,pad=18)
    rows=[[names[(a+b)%3] for b in range(3)] for a in range(3)]
    table=axes[2].table(cellText=rows,rowLabels=names,colLabels=names,
                        cellLoc='center',rowLoc='center',loc='center',bbox=[.14,.28,.84,.42])
    table.auto_set_font_size(False);table.set_fontsize(14)
    for (a,b),cell in table.get_celld().items():
        cell.set_edgecolor('white');cell.set_linewidth(2)
        if a>0 and b>=0:cell.set_facecolor(colors[((a-1)+b)%3])
        else:cell.set_facecolor('#eeeeee')
    axes[2].text(.5,.16,r'$(2+N)+(2+N)=1+N$',ha='center',transform=axes[2].transAxes,fontsize=13)
    fig.text(.348,.52,'→',ha='center',fontsize=38,color='#637c8b')
    fig.suptitle('Forget differences of three, preserve addition',fontsize=18,y=.975)
    fig.text(.5,.045,r'$(\mathbb{Z}/6\mathbb{Z})/\{0,3\}\cong\mathbb{Z}/3\mathbb{Z}$',
             ha='center',fontsize=17)
    fig.subplots_adjust(left=.035,right=.975,bottom=.14,top=.79,wspace=.23)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
