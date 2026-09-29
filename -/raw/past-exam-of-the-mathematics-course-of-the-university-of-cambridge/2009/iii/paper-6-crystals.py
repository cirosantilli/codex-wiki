"""Python 3.14 / matplotlib 3.10: opaque PNG basename to caller CWD.
Preserve caller MPLCONFIGDIR. --rank N draws entire rank-N graph (default 3).
"""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def crystal_edges(n):
    colors=list(range(1,n))+[n]+list(range(n-1,0,-1))
    edges=[]
    def phi(a,i): return a<2*n-1 and colors[a]==i
    def eps(a,i): return a>0 and colors[a-1]==i
    for a in range(2*n):
        for b in range(2*n):
            for i in range(1,n+1):
                if phi(a,i)>eps(b,i):
                    if phi(a,i): edges.append(((a,b),(a+1,b),i))
                elif phi(b,i): edges.append(((a,b),(a,b+1),i))
    return edges


def components(n,edges):
    adj={(a,b):set() for a in range(2*n) for b in range(2*n)}
    for a,b,_ in edges: adj[a].add(b); adj[b].add(a)
    remaining=set(adj); out=[]
    while remaining:
        start=min(remaining); found={start}; todo=[start]
        while todo:
            for b in adj[todo.pop()]-found: found.add(b); todo.append(b)
        remaining-=found; out.append(found)
    return out


def letter(a,n): return str(a+1) if a<n else r'\bar{'+str(2*n-a)+'}'


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--rank',type=int,default=3)
    n=parser.parse_args().rank
    if n<1: parser.error('rank must be positive')
    colors=list(range(1,n))+[n]+list(range(n-1,0,-1))
    palette=['#276fbf','#cf4e12','#27823e','#8245a4','#80662f','#bd3980']
    edges=crystal_edges(n); comps=components(n,edges); fill=['#d9eafa','#ffead3','#dedede']
    component={v:k for k,c in enumerate(comps) for v in c}
    fig,(top,ax)=plt.subplots(2,1,figsize=(8,9),dpi=140,facecolor='white',gridspec_kw={'height_ratios':[1,6]})
    top.set(xlim=(-.65,2*n-.35),ylim=(-.7,.9)); top.axis('off')
    top.text((2*n-1)/2,.7,f'Defining C{n} crystal',ha='center',fontsize=16)
    for a in range(2*n):
        top.text(a,-.04,'$'+letter(a,n)+'$',ha='center',va='center',fontsize=15,bbox=dict(boxstyle='circle,pad=.22',facecolor='white',edgecolor='#17212d'))
        if a<2*n-1:
            col=palette[(colors[a]-1)%len(palette)]
            top.annotate('',xy=(a+.82,-.04),xytext=(a+.18,-.04),arrowprops=dict(arrowstyle='->',color=col,lw=1.6))
            top.text(a+.5,.17,str(colors[a]),ha='center',color=col,fontsize=11)
    ax.set(xlim=(-.65,2*n-.35),ylim=(-2*n+.3,.65),aspect='equal'); ax.axis('off')
    ax.set_title(f'Complete tensor-square crystal, rank {n}',fontsize=15,pad=15)
    highest={(0,0),(0,2*n-1)}|({(0,1)} if n>1 else set())
    for a in range(2*n):
        for b in range(2*n):
            ax.add_patch(Circle((b,-a),.26,facecolor=fill[component[(a,b)]],edgecolor='#17212d',lw=2 if (a,b) in highest else .7,zorder=3))
            ax.text(b,-a,'$'+letter(a,n)+r'\!\otimes\!'+letter(b,n)+'$',ha='center',va='center',fontsize=11,zorder=4)
    for (a,b),(c,d),i in edges:
        dx=d-b;dy=a-c; col=palette[(i-1)%len(palette)]
        ax.annotate('',xy=(d-.28*dx,-c-.28*dy),xytext=(b+.28*dx,-a+.28*dy),arrowprops=dict(arrowstyle='->',color=col,lw=1.6),zorder=2)
        ax.text((b+d)/2+(.10 if dx==0 else 0),-(a+c)/2+(.10 if dx!=0 else 0),str(i),ha='center',va='center',color=col,fontsize=10,bbox=dict(facecolor='white',edgecolor='none',pad=.3),zorder=2)
    legend=r'$L(2\omega_1)$: '+str(len(comps[0]))+' vertices'
    if n>1: legend+='     '+r'$L(\omega_2)$: '+str(len(comps[1]))+' vertices'
    legend+='     '+r'$L(0)$: 1 vertex'
    fig.text(.5,.028,legend,ha='center',fontsize=11)
    fig.text(.5,.009,'Heavy outlines mark highest vertices; arrow labels are simple-root colors.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.05,1,1),pad=.8)
    fig.savefig(Path('paper-6-crystals.png'),facecolor='white',transparent=False); plt.close(fig)

if __name__=='__main__': main()
