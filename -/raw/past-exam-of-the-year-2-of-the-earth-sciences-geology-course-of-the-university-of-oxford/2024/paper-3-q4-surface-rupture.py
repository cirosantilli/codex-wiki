"""Original surface-rupture cartoons; opaque basename PNG to CWD.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size':9})
    fig,axes=plt.subplots(1,3,figsize=(11.6,4.3),layout='constrained')
    for j,ax in enumerate(axes):
        ax.fill_between([-3,3],[-.7,-.7],-2,color='#d7d9d7')
        ax.plot([.2,1.2],[-.7,-2],color='#a42f21',lw=2.2)
        ax.text(-2.8,-1.65,'Footwall');ax.text(1.1,-1.65,'Hanging\nwall ↓')
        ax.set(xlim=(-3,3),ylim=(-2.2,1.6),title=['Exposed competent rock','Thin loose cover','Thick weak cover; rupture may die out'][j]);ax.axis('off')
    ax=axes[0]
    ax.fill_between([-3,0,.2,3],[.6,.6,-.7,-.7],[-.7]*4,color='#d7d9d7')
    ax.plot([-3,0,.2,3],[.6,.6,-.7,-.7],'k',lw=2)
    ax.plot([0,.2],[.6,-.7],color='#a42f21',lw=2)
    ax.text(-2.7,1,'Sharp free face / fresh fault plane')
    ax=axes[1]
    x=[-3,-.6,-.4,-.15,.15,.45,.65,3];y=[.7,.7,.5,.5,-.05,-.05,.15,.15]
    ax.fill_between(x,y,-.7,color='#e9cc9f');ax.plot(x,y,'k',lw=2)
    for a,b in [((.2,-.7),(-.4,.5)),((.2,-.7),(.15,-.05)),((.2,-.7),(.65,.15))]:ax.plot([a[0],b[0]],[a[1],b[1]],color='#a42f21',lw=1.5)
    ax.text(-2.7,1,'Fissures, splays, small graben, slumping')
    ax=axes[2];x=np.linspace(-3,3,401);y=.45-.4*np.tanh(x)
    ax.fill_between(x,y,-.7,color='#e9cc9f');ax.plot(x,y,'k',lw=2)
    ax.plot([.2,.05],[-.7,-.15],color='#a42f21',lw=2)
    for xx in (-.65,-.1,.55):
        yy=.45-.4*np.tanh(xx);ax.plot([xx-.08,xx,xx+.08],[yy,yy-.27,yy],color='#a42f21')
    ax.text(-2.7,1.2,'Broad flexure / distributed extension')
    ax.text(-2.7,-.5,'No discrete through-going break required',fontsize=8)
    fig.suptitle('Extension across a normal fault: surficial cover controls how slip reaches the surface\nSchematic cross sections; all blocks and cover deform together')
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
