"""Original factor tree highlights the earlier cases used by a strong-induction step."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({'font.size':12})
    fig = plt.figure(figsize=(12,6.4), layout='constrained', facecolor='white')
    gs=fig.add_gridspec(2,1,height_ratios=[3,1.25]);ax=fig.add_subplot(gs[0]);lower=fig.add_subplot(gs[1])
    nodes={'r':(0,2.4,84),'a':(-2,1.25,6),'b':(2,1.25,14),'c':(-3,0,2),'d':(-1,0,3),'e':(1,0,2),'f':(3,0,7)}
    for p,c in [('r','a'),('r','b'),('a','c'),('a','d'),('b','e'),('b','f')]:
        px,py,_=nodes[p];cx,cy,_=nodes[c]
        ax.annotate('',xy=(cx,cy+.23),xytext=(px,py-.23),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#566573'})
    for key,(x,y,n) in nodes.items():
        prime=key in 'cdef';color='#287e59' if prime else '#2465aa'
        ax.add_patch(Circle((x,y),.25,fc='#ffffff',ec=color,lw=2.3));ax.text(x,y,str(n),ha='center',va='center',fontsize=17,color=color)
    ax.text(-3.8,2.4,r'Prove $P(84)$',ha='left',va='center',fontsize=15)
    ax.text(2.8,2.4,'Each child is smaller\nthan its parent',ha='left',va='center',fontsize=11)
    ax.text(-2.9,-.65,r'Prime leaves: $2,3,2,7$',color='#287e59',fontsize=13)
    ax.text(.6,-.65,r'$84=2^2\cdot3\cdot7$',fontsize=15)
    ax.set(xlim=(-4,4.8),ylim=(-1,2.9),title='The recursive construction uses smaller divisors, not just 83');ax.axis('off')
    lower.axvspan(2,83,color='#e7eef7',ymin=.22,ymax=.7)
    lower.scatter(list(range(2,84)),[0]*82,s=12,color='#a3b6cf')
    lower.scatter([6,14],[0,0],s=110,color='#2465aa',zorder=5)
    lower.scatter([84],[0],s=100,facecolors='white',edgecolors='#b44c43',linewidths=2,zorder=5)
    for n in [2,6,14,83]:lower.text(n,-.24,str(n),ha='center',va='top',fontsize=10 if n<83 else 9)
    lower.text(44,.4,r'Hypothesis: $P(2),P(3),\ldots,P(83)$ are available',ha='center',fontsize=13)
    lower.annotate('Use 6 and 14',xy=(10,.03),xytext=(22,.9),arrowprops={'arrowstyle':'->'},fontsize=11)
    lower.text(85.7,0,r'$P(84)$'+'\nis the goal',color='#a44038',va='center',fontsize=10)
    lower.set(xlim=(0,94),ylim=(-.6,1.2));lower.axis('off')
    fig.suptitle('Strong induction follows the dependencies of factorization',fontsize=17)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white');plt.close(fig)


if __name__=='__main__':main()
