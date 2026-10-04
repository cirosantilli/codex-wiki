"""Original oriented tangles; Python 3.14 and root matplotlib dependencies.
Write only the PNG basename to CWD; respect the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path as MP
from matplotlib.patches import PathPatch

def line(ax,p,color='#172b4d',lw=1.8):
    ax.plot(*zip(*p),color=color,lw=lw,solid_capstyle='round')
def arrow(ax,p,q):
    ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':'#172b4d','lw':1.1,'mutation_scale':11})
def arc(ax,a,b,y,z):
    ax.add_patch(PathPatch(MP([(a,y),(a,z),(b,z),(b,y)],[MP.MOVETO,MP.CURVE4,MP.CURVE4,MP.CURVE4]),facecolor='none',edgecolor='#172b4d',lw=1.8))
def cross(ax,a,b,y,z,plus=True):
    p=[(a,y),(b,z)];q=[(b,y),(a,z)]
    under,over=(q,p) if plus else (p,q)
    line(ax,under);line(ax,over,'white',6);line(ax,over)
def setup(ax,n,title):
    for y in [0,1]:ax.axhline(y,color='#bbbbbb',lw=.7,ls=':')
    ax.set(xlim=(-.5,n-.5),ylim=(-.18,1.2),title=title);ax.axis('off')
def main():
    fig,axes=plt.subplots(1,3,figsize=(14,4.8),layout='constrained',facecolor='white')
    ax=axes[0];setup(ax,8,'Q6(b): horizontal tensor product')
    for x,up in [(0,True),(3,False)]:
        line(ax,[(x,1),(x,0)]);arrow(ax,(x,.4 if up else .65),(x,.65 if up else .4))
    for x in [1,2]:line(ax,[(x,1),(x,.78)])
    arc(ax,1,2,.78,.2);arrow(ax,(1,.8),(1,.98));arrow(ax,(2,.98),(2,.8))
    for x in [4,5]:line(ax,[(x,0),(x,.22)])
    arc(ax,4,5,.22,.8);arrow(ax,(4,.2),(4,.02));arrow(ax,(5,.02),(5,.2))
    cross(ax,6,7,1,0,False);arrow(ax,(6.1,.9),(6.27,.73));arrow(ax,(6.9,.9),(6.73,.73))
    ax.text(1.5,.08,'evaluation',ha='center',fontsize=8)
    ax.text(4.5,.9,'reversed coevaluation',ha='center',fontsize=8)
    ax.text(6.5,-.12,'negative crossing',ha='center',fontsize=8)
    ax=axes[1];setup(ax,4,'Q6(b): composable two-cap repair')
    cross(ax,0,1,1,.73,True)
    for x in [2,3]:line(ax,[(x,1),(x,.73)])
    for x in [1,2]:line(ax,[(x,.73),(x,.6)])
    arc(ax,1,2,.6,.32)
    for x in [0,3]:line(ax,[(x,.73),(x,.3)])
    arc(ax,0,3,.3,-.04)
    arrow(ax,(.12,.96),(.36,.90));arrow(ax,(.88,.96),(.64,.9))
    arrow(ax,(2,.8),(2,.98));arrow(ax,(3,.8),(3,.98))
    ax.text(1.5,.47,'middle evaluation',ha='center',fontsize=8)
    ax.text(1.5,.02,'outer evaluation',ha='center',fontsize=8)
    ax=axes[2];setup(ax,3,'Q6(c): elementary-tangle slices')
    line(ax,[(0,1),(0,.78)]);cross(ax,1,2,1,.78,True)
    cross(ax,0,1,.78,.4,True);line(ax,[(2,.78),(2,.4)])
    line(ax,[(0,.4),(0,0)])
    for x in [1,2]:line(ax,[(x,.4),(x,.25)])
    arc(ax,1,2,.25,-.04)
    arrow(ax,(0,.98),(0,.82));arrow(ax,(1.72,.84),(1.5,.89))
    arrow(ax,(1.88,.974),(1.67,.93));arrow(ax,(2,.65),(2,.77))
    arrow(ax,(.3,.67),(.47,.61));arrow(ax,(.75,.685),(.58,.6204))
    arrow(ax,(0,.27),(0,.12))
    ax.text(1.5,.04,'reversed evaluation',ha='center',fontsize=8)
    ax.text(2.15,.88,'upper crossing',fontsize=8,rotation=90,va='center')
    ax.text(2.15,.57,'lower crossing',fontsize=8,rotation=90,va='center')
    fig.suptitle('Read top to bottom; crossing gaps mark underpasses',fontsize=12)
    fig.savefig(Path('paper-2-tangles.png'),dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
