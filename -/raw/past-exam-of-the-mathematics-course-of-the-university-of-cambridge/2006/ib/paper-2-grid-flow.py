"""Original feasible-flow diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write opaque PNG basename to caller CWD; preserve supplied MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/paper-2-grid-flow-mplconfig')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

PATHS = [[[0, 3], [0, 2], [0, 1], [0, 0], [1, 0], [2, 0], [3, 0]], [[0, 3], [0, 2], [0, 1], [1, 1], [1, 0], [2, 0], [3, 0]], [[0, 3], [0, 2], [1, 2], [1, 1], [2, 1], [2, 0], [3, 0]], [[0, 3], [1, 3], [1, 2], [2, 2], [2, 1], [3, 1], [3, 0]], [[0, 3], [1, 3], [2, 3], [2, 2], [3, 2], [3, 1], [3, 0]], [[0, 3], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1], [3, 0]], [[0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [3, 3], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0]], [[0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0]]]

def main():
    flow=Counter()
    for path in PATHS:
        for u,v in zip(path,path[1:]):
            flow[(tuple(u),tuple(v))]+=1
    fig,ax=plt.subplots(figsize=(6.7,6.7),dpi=140,facecolor='white')
    ax.set_facecolor('white')
    ax.fill([-.25,-.25,4.25],[-.25,4.25,4.25],color='#edf4fb',zorder=0)
    for i in range(5):
        for j in range(5):
            if i<4:ax.plot([i,i+1],[j,j],color='#d7d7d7',lw=1,zorder=1)
            if j<4:ax.plot([i,i],[j,j+1],color='#d7d7d7',lw=1,zorder=1)
    ax.plot([-.1,4.1],[-.1,4.1],color='#d07c15',lw=1.5,ls='--',zorder=1)
    for (u,v),amount in flow.items():
        capacity=max(abs(u[0]-u[1]),abs(v[0]-v[1]))
        assert amount<=capacity
        dx=v[0]-u[0];dy=v[1]-u[1]
        ax.annotate('',xy=(v[0]-.17*dx,v[1]-.17*dy),xytext=(u[0]+.17*dx,u[1]+.17*dy),arrowprops={'arrowstyle':'->','lw':1.1+.55*amount,'color':'#1764ab'},zorder=2)
        x=(u[0]+v[0])/2;y=(u[1]+v[1])/2
        ax.text(x+(.12 if dy else 0),y+(.12 if dx else 0),f'{amount}/{capacity}',ha='center',va='center',fontsize=9,color='#173a58',bbox={'facecolor':'white','edgecolor':'none','pad':.5},zorder=3)
    for i in range(5):
        for j in range(5):
            color='#1764ab' if (i,j)==(0,3) else '#b44627' if (i,j)==(3,0) else '#ffffff'
            ax.scatter([i],[j],s=370,color=color,edgecolor='#444444',zorder=4)
            ax.text(i,j,f'{i}{j}',ha='center',va='center',fontsize=8,color='white' if color!='#ffffff' else '#222222',zorder=5)
    ax.text(.45,3.65,'Source side: i₁ < i₂',fontsize=10)
    ax.text(3.2,.6,'Sink side',fontsize=10)
    ax.set(xlim=(-.4,4.4),ylim=(-.4,4.4),aspect='equal',xlabel='First coordinate i₁',ylabel='Second coordinate i₂',title='Maximum flow = 8; edge labels are flow / capacity')
    ax.set_xticks(range(5));ax.set_yticks(range(5))
    fig.tight_layout()
    fig.savefig('paper-2-grid-flow.png',facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':
    main()
