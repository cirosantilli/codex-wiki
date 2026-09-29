"""Original Gaussian-plane versus radial-density diagram; output PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10.8,4.9),layout='constrained')
    grid=np.linspace(-3,3,321)
    xx,yy=np.meshgrid(grid,grid)
    joint=np.exp(-(xx*xx+yy*yy)/2)/(2*np.pi)
    im=ax.pcolormesh(xx,yy,joint,shading='auto',cmap='Blues',rasterized=True)
    fig.colorbar(im,ax=ax,shrink=.78,pad=.02,label='Density per unit area')
    ax.add_patch(Wedge((0,0),1.1,0,360,width=.2,fc='#ef9d27',ec='#af660d',alpha=.8))
    ax.scatter([0],[0],s=40,color='#16385c',zorder=5)
    ax.annotate('Planar density peaks at (0, 0)',(0,0),xytext=(-2.85,2.45),fontsize=10,
                arrowprops={'arrowstyle':'->','color':'#16385c'})
    ax.annotate(r'Ring: $0.9<R<1.1$',(.7,-.7),xytext=(-2.85,-2.5),fontsize=11,
                arrowprops={'arrowstyle':'->','color':'#874908'},color='#874908')
    ax.set(xlabel=r'$X$',ylabel=r'$Y$',xlim=(-3,3),ylim=(-3,3),aspect='equal',title='Independent Gaussian coordinates')
    r=np.linspace(0,3.7,601);density=r*np.exp(-r*r/2)
    bx.plot(r,density,color='#245988',lw=2.7,label=r'$f_R(r)=r e^{-r^2/2}$')
    ring=np.linspace(.9,1.1,101)
    bx.fill_between(ring,0,ring*np.exp(-ring*ring/2),color='#ef9d27',alpha=.85)
    bx.axvline(1,color='#7a5b92',ls='--',lw=1.5)
    bx.scatter([1],[np.exp(-.5)],color='#7a5b92',zorder=5)
    bx.annotate(r'Radial mode: $r=1$',(1,np.exp(-.5)),xytext=(1.65,.60),
                arrowprops={'arrowstyle':'->','color':'#7a5b92'},fontsize=11)
    probability=np.exp(-.9**2/2)-np.exp(-1.1**2/2)
    bx.text(1.45,.14,f'Shaded probability = {probability:.4f}\nSame ring, two ways to count',fontsize=11,bbox={'fc':'white','ec':'none','alpha':.94,'pad':3})
    bx.set(xlim=(0,3.7),ylim=(0,.75),xlabel=r'Radius $r$',ylabel='Density per unit radius',
           title='Radial density includes circumference')
    bx.grid(alpha=.17);bx.legend(loc='upper right',fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
