"""Complete B_n vector and tensor-square crystals. Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Optional --rank N (default 3). Output basename to CWD;
preserves supplied MPLCONFIGDIR.
"""
import argparse
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.gettempdir()+'/codex-wiki-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from collections import deque


def crystal(n):
    labels=[str(i) for i in range(1,n+1)]+['0']+[r'\overline{'+str(i)+'}' for i in range(n,0,-1)]
    colors=list(range(1,n))+[n,n]+list(range(n-1,0,-1))
    N=len(labels)
    def counts(b,i):
        e=f=0
        while b-e>0 and colors[b-e-1]==i:e+=1
        while b+f<N-1 and colors[b+f]==i:f+=1
        return e,f
    edges=[]
    for a in range(N):
        for b in range(N):
            for i in range(1,n+1):
                _,phi=counts(a,i);eps,_=counts(b,i)
                if phi>eps:
                    target=(a+1,b) if a<N-1 and colors[a]==i else None
                else:
                    target=(a,b+1) if b<N-1 and colors[b]==i else None
                if target is not None:edges.append(((a,b),target,i))
    neighbors={(a,b):[] for a in range(N) for b in range(N)}
    for source,target,i in edges:
        neighbors[source].append(target);neighbors[target].append(source)
    heads=[(0,0),(0,1),(0,N-1)]
    component={};sizes=[]
    for j,head in enumerate(heads):
        todo=deque([head]);component[head]=j;size=0
        while todo:
            node=todo.popleft();size+=1
            for adjacent in neighbors[node]:
                if adjacent not in component:component[adjacent]=j;todo.append(adjacent)
        sizes.append(size)
    expected=[n*(2*n+3),n*(2*n+1),1]
    assert sizes==expected and len(component)==N*N
    return labels,colors,counts,edges,component,sizes


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--rank',type=int,default=3)
    n=parser.parse_args().rank
    if n<1:raise ValueError('rank must be positive')
    labels,colors,counts,edges,components,sizes=crystal(n);N=len(labels)
    palette=['#2878aa','#d16628','#7b4994','#158357','#b0265e','#86751f']
    fills=['#dceef7','#fae8dc','#d9d9d9']
    fig=plt.figure(figsize=(9,10),constrained_layout=True)
    grid=fig.add_gridspec(2,1,height_ratios=[1,7]);top=fig.add_subplot(grid[0]);ax=fig.add_subplot(grid[1])
    for b,label in enumerate(labels):
        top.text(b,0,'$'+label+'$',ha='center',va='center',fontsize=15)
        if b<N-1:
            color=palette[(colors[b]-1)%len(palette)]
            top.annotate('',(b+.78,0),(b+.22,0),arrowprops=dict(arrowstyle='->',color=color,lw=1.8))
            top.text(b+.5,.17,str(colors[b]),ha='center',color=color,fontsize=11)
    top.set(xlim=(-.5,N-.5),ylim=(-.5,.7));top.axis('off');top.set_title(f'Vector crystal for B{n}: colors label simple roots',fontsize=13)
    for (a,b),(c,d),i in edges:
        x0,y0=b,N-1-a;x1,y1=d,N-1-c
        dx,dy=x1-x0,y1-y0
        ax.annotate('',(x1-.24*dx,y1-.24*dy),(x0+.24*dx,y0+.24*dy),arrowprops=dict(arrowstyle='->',lw=1.7,color=palette[(i-1)%len(palette)]),zorder=1)
    for a in range(N):
        for b in range(N):
            ax.scatter(b,N-1-a,s=950,facecolor=fills[components[(a,b)]],edgecolor='#777777',lw=.5,zorder=2)
            ax.text(b,N-1-a,'$'+labels[a]+r'\otimes'+labels[b]+'$',ha='center',va='center',fontsize=10,zorder=3)
    handles=[Patch(facecolor=fills[j],label=f'{name}: {sizes[j]} vertices') for j,name in enumerate(['Traceless symmetric square','Exterior square','Trivial component'])]
    handles += [Line2D([0],[0],color=palette[(i-1)%len(palette)],lw=2,label=f'root color {i}') for i in range(1,n+1)]
    ax.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,-.12),ncol=3,fontsize=9)
    ax.set(xlim=(-.6,N-.4),ylim=(-.6,N-.4));ax.set_aspect('equal');ax.axis('off')
    ax.set_title(f'Entire tensor-square crystal: {(2*n+1)**2} vertices; first factor changes downward, second rightward',fontsize=12)
    fig.savefig('paper-4-crystals.png',dpi=135,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
