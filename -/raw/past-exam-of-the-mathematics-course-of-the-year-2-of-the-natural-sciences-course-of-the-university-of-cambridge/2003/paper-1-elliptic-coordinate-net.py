"""Original planar cross-section of elliptic cylindrical coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,ax=plt.subplots(figsize=(7.1,5.6),dpi=120,layout='constrained')
    angle=np.linspace(0,2*np.pi,1600)
    for i,u in enumerate([.3,.65,1.0,1.3,1.55]):
        ax.plot(np.cosh(u)*np.cos(angle),np.sinh(u)*np.sin(angle),color='#227ca6',lw=1.6,label=r'Constant $u$ (ellipses)' if i==0 else None)
    u=np.linspace(0,1.9,800)
    for i,v in enumerate(np.arange(1,12)*np.pi/6):
        ax.plot(np.cosh(u)*np.cos(v),np.sinh(u)*np.sin(v),color='#bc682a',lw=1.25,label=r'Constant $v$ (half-branches)' if i==0 else None)
    ax.plot([-1,1],[0,0],color='0.35',lw=3,label=r'Degenerate $u=0$ segment')
    ax.scatter([-1,1],[0,0],color='#842b58',s=35,zorder=5)
    ax.annotate('Focus',xy=(-1,0),xytext=(-1.62,-.54),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
    ax.annotate('Focus',xy=(1,0),xytext=(1.15,-.54),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
    ax.set(xlim=(-2.9,2.9),ylim=(-2.55,2.55),xlabel='x/a',ylabel='y/a',title='An orthogonal confocal coordinate net')
    ax.set_aspect('equal')
    ax.axhline(0,color='0.7',lw=.7,zorder=0)
    ax.axvline(0,color='0.7',lw=.7,zorder=0)
    ax.legend(loc='upper center',fontsize=9,ncol=1)
    ax.grid(alpha=.13)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
