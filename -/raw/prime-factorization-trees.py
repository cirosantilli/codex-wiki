"""Draw two binary splits with the same multiset of prime leaves."""

from collections import Counter
from math import isqrt, prod
from pathlib import Path

import matplotlib.pyplot as plt


def prime(n):
    return n > 1 and all(n % d for d in range(2,isqrt(n)+1))


def validate(tree):
    if isinstance(tree,int):
        assert prime(tree)
        return tree,[tree]
    value,left,right = tree
    lv,ll = validate(left)
    rv,rl = validate(right)
    assert value == lv*rv and value > lv > 1 and value > rv > 1
    return value,ll+rl


def layout(tree,lo=0,hi=1,depth=0,nodes=None,edges=None):
    if nodes is None:
        nodes,edges = [],[]
    x=(lo+hi)/2
    leaf=isinstance(tree,int)
    value=tree if leaf else tree[0]
    nodes.append((x,depth,value,leaf))
    if not leaf:
        mid=(lo+hi)/2
        for child,a,b in [(tree[1],lo,mid),(tree[2],mid,hi)]:
            cx=(a+b)/2
            edges.append((x,depth,cx,depth+1))
            layout(child,a,b,depth+1,nodes,edges)
    return nodes,edges


def main():
    trees=[(360,(36,(6,2,3),(6,2,3)),(10,2,5)),
           (360,(8,2,(4,2,2)),(45,5,(9,3,3)))]
    for t in trees:
        value,leaves=validate(t)
        assert value == prod(leaves) == 360
        assert Counter(leaves) == Counter({2:3,3:2,5:1})
    fig,axes=plt.subplots(1,2,figsize=(11.5,5.8),dpi=120,facecolor='white')
    for ax,tree,title in zip(axes,trees,['Start with 36 × 10','Start with 8 × 45']):
        nodes,edges=layout(tree)
        for x,y,cx,cy in edges:
            ax.plot([x,cx],[y,cy],color='#afbac3',lw=2,zorder=1)
        for x,y,value,leaf in nodes:
            ax.text(x,y,str(value),ha='center',va='center',fontsize=13,zorder=3,
                    bbox={'boxstyle':'round,pad=.4','facecolor':'#d6ecd7' if leaf else '#deebf4',
                          'edgecolor':'#2e7440' if leaf else '#3c7099','linewidth':1.5})
        ax.set(xlim=(-.04,1.04),ylim=(3.45,-.4))
        ax.axis('off')
        ax.set_title(title,fontsize=15,pad=15)
    fig.suptitle('Different splits, identical prime factors',fontsize=18,y=.97)
    fig.text(.5,.09,r'$360=2^3\cdot3^2\cdot5$',ha='center',fontsize=20)
    fig.text(.5,.025,'Blue nodes can be split; green leaves are prime.',ha='center',fontsize=12)
    fig.subplots_adjust(left=.03,right=.97,bottom=.2,top=.82,wspace=.13)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
