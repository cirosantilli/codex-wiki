"""Six-vertex graph-state measurement pattern; opaque PNG to cwd only.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; respects MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(10,4.8),dpi=100)
    pos={'u0':(0,1),'u1':(1,1),'u2':(2,1),'v0':(0,0),'v1':(1,0),'v2':(2,0)}
    edges=[('u0','u1'),('u1','u2'),('v0','v1'),('v1','v2'),('u2','v1')]
    for u,v in edges:
        x,y=pos[u];X,Y=pos[v];ax.plot([x,X],[y,Y],color='0.35',lw=2,zorder=1)
    for name,(x,y) in pos.items():
        ax.scatter([x],[y],s=1100,facecolor='white',edgecolor='#0077a8',linewidth=2,zorder=2)
        ax.text(x,y,rf'${name[0]}_{name[1]}$',ha='center',va='center',zorder=3)
    ax.text(0,1.36,r'$X$ basis; outcome $s_0$',ha='center')
    ax.text(1,1.36,r'$(-1)^{s_0}\alpha$; outcome $s_1$',ha='center')
    ax.text(2,1.36,'Unmeasured / discard',ha='center')
    ax.text(0,-.36,r'$X$ basis; outcome $t_0$',ha='center')
    ax.text(1,-.36,r'$(-1)^{t_0}\beta$; outcome $t_1$',ha='center')
    ax.text(2,-.36,r'$Z$ basis; outcome $m$',ha='center')
    ax.text(.5,.55,'Input initialization',ha='center',fontsize=10,color='0.35')
    ax.text(1.7,.56,'CZ interaction',ha='center',fontsize=10,color='0.35',rotation=40)
    ax.set_title('Graph-state pattern for two J gates and a controlled-Z interaction',pad=22)
    ax.text(1,-.74,r'Returned circuit bit: $b_2=m\oplus s_1\oplus t_1$',ha='center',fontsize=14)
    ax.text(1,-1.0,r'All vertices start in $|+\rangle$; every edge is CZ. Measure $u_0,v_0$ before $u_1,v_1$.',ha='center',fontsize=10)
    ax.set_xlim(-.6,2.6);ax.set_ylim(-1.12,1.7);ax.axis('off')
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-61-measurement-pattern.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
