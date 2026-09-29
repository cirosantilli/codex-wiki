"""Python 3.14 / matplotlib 3.10: opaque PNG basename to caller CWD.
Caller MPLCONFIGDIR is preserved.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def draw(ax,x,y,labels,longs,bonds):
    for i,label in enumerate(labels):
        if label=='...': ax.text(x+i,y,r'$\cdots$',ha='center',va='center',fontsize=18)
        else:
            ax.add_patch(Circle((x+i,y),.115,facecolor='white',edgecolor='#17212d',lw=1.7,zorder=4))
            ax.text(x+i,y+.23,label,ha='center',va='bottom',fontsize=12)
            ax.text(x+i,y-.23,'long' if i in longs else 'short',ha='center',va='top',fontsize=8,color='#596579')
    for i,double,direction in bonds:
        for shift in ((-.043,.043) if double else (0,)):
            ax.plot([x+i+.15,x+i+.85],[y+shift,y+shift],color='#17212d',lw=1.4)
        if direction:
            mid=x+i+.5
            ax.annotate('',xy=(mid+.19*direction,y),xytext=(mid-.19*direction,y),arrowprops=dict(arrowstyle='->',lw=1.8,color='#17212d'))


def main():
    fig,ax=plt.subplots(figsize=(10,6.4),dpi=130,facecolor='white')
    ax.set(xlim=(-1,10),ylim=(-.75,5.8)); ax.axis('off')
    ax.text(4.4,5.58,'Symplectic Dynkin diagrams',ha='center',fontsize=16)
    ax.text(1.3,5.14,'Finite',ha='center',fontsize=12)
    ax.text(7,5.14,r'Extended: add $\alpha_0=-\theta$',ha='center',fontsize=12)
    ax.text(-.9,4.45,r'$n\geq4$',fontsize=12)
    draw(ax,0,4.4,[r'$\alpha_1$',r'$\alpha_2$','...',r'$\alpha_{n-1}$',r'$\alpha_n$'],{4},[(0,False,0),(1,False,0),(2,False,0),(3,True,-1)])
    draw(ax,5.1,4.4,[r'$\alpha_0$',r'$\alpha_1$','...',r'$\alpha_{n-1}$',r'$\alpha_n$'],{0,4},[(0,True,1),(1,False,0),(2,False,0),(3,True,-1)])
    ax.text(-.9,2.95,r'$n=3$',fontsize=12)
    draw(ax,.4,2.9,[r'$\alpha_1$',r'$\alpha_2$',r'$\alpha_3$'],{2},[(0,False,0),(1,True,-1)])
    draw(ax,5.6,2.9,[r'$\alpha_0$',r'$\alpha_1$',r'$\alpha_2$',r'$\alpha_3$'],{0,3},[(0,True,1),(1,False,0),(2,True,-1)])
    ax.text(-.9,1.45,r'$n=2$',fontsize=12)
    draw(ax,.8,1.4,[r'$\alpha_1$',r'$\alpha_2$'],{1},[(0,True,-1)])
    draw(ax,6.1,1.4,[r'$\alpha_0$',r'$\alpha_1$',r'$\alpha_2$'],{0,2},[(0,True,1),(1,True,-1)])
    ax.text(-.9,-.05,r'$n=1$',fontsize=12)
    draw(ax,1.3,-.1,[r'$\alpha_1$'],{0},[])
    draw(ax,6.6,-.1,[r'$\alpha_0$',r'$\alpha_1$'],{0,1},[(0,True,0)])
    fig.tight_layout(pad=.4)
    fig.savefig(Path('paper-6-cn-diagrams.png'),facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__': main()
