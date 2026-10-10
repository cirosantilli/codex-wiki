"""Check S3 composition and compare normal and nonnormal coset behavior."""

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def compose(p,q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    return tuple(p.index(i) for i in range(3))


def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))


def left(g,H):
    return {compose(g,h) for h in H}


def right(H,g):
    return {compose(h,g) for h in H}


def panel(ax,title,groups,notes):
    ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
    ax.set_title(title,fontsize=16,pad=18)
    for j,(label,entries,color) in enumerate(groups):
        y=.73-j*.30
        ax.add_patch(FancyBboxPatch((.035,y-.1),.93,.22,boxstyle='round,pad=.015',
                                    facecolor=color,edgecolor='#8c9eac',lw=1))
        ax.text(.08,y+.055,label,fontsize=14,va='center')
        ax.text(.08,y-.04,entries,fontsize=15,va='center')
    ax.text(.5,.09,notes,fontsize=12,ha='center',va='center',linespacing=1.6)


def main():
    e=(0,1,2);t12=(1,0,2);g=(1,2,0);t13=(2,1,0);t23=(0,2,1)
    G=set(permutations(range(3)));N={p for p in G if parity(p)==1};H={e,t12}
    assert len(N)==3 and len(H)==2
    for a in G:
        for b in G:assert parity(compose(a,b))==parity(a)*parity(b)
        assert left(a,N)==right(N,a)
        assert {compose(compose(a,n),inverse(a)) for n in N}==N
    assert left(g,H)=={g,t13}
    assert right(H,g)=={g,t23}
    assert compose(compose(g,t12),inverse(g))==t23 and t23 not in H
    assert left(t12,N)=={t12,t13,t23}==right(N,t12)
    fig,axes=plt.subplots(1,2,figsize=(11.6,5.1),dpi=120,facecolor='white')
    panel(axes[0],r'$N=A_3$: normal',
          [(r'Even coset $N$',r'$\{e,(123),(132)\}$','#d8e9d7'),
           (r'Odd coset $(12)N=N(12)$',r'$\{(12),(13),(23)\}$','#d5e5f1')],
          'Left and right cosets match.\nParity gives a two-element quotient.')
    panel(axes[1],r'$H=\{e,(12)\}$: not normal',
          [(r'Left coset $gH$',r'$\{(123),(13)\}$','#f0ddc8'),
           (r'Right coset $Hg$',r'$\{(123),(23)\}$','#efdbde')],
          r'$g=(123)$; the two cosets differ.'+'\n'+r'$g(12)g^{-1}=(23)\notin H$')
    fig.suptitle('In S₃, normality is stronger than being a subgroup',fontsize=18,y=.97)
    fig.text(.5,.028,'Permutation products act rightmost first; e is the identity permutation.',
             fontsize=12,ha='center')
    fig.subplots_adjust(left=.04,right=.96,bottom=.14,top=.8,wspace=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
