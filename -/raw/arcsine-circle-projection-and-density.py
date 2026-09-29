"""Original uniform-circle projection and arcsine density; output PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.9),layout='constrained')
    theta=np.linspace(0,2*np.pi,601)
    ax.plot(np.cos(theta),np.sin(theta),color='#597a96',lw=1.7)
    phase=2*np.pi*(np.arange(24)+.5)/24
    x,y=np.cos(phase),np.sin(phase)
    for xx,yy in zip(x,y):ax.plot([xx,xx],[yy,0],color='#6b8eac',lw=.8,alpha=.42)
    ax.scatter(x,y,s=30,color='#315e80',zorder=4)
    ax.scatter(x,np.zeros_like(x),s=30,color='#bd6d17',zorder=5)
    ax.plot([-1,1],[0,0],color='#734a22',lw=2)
    ax.axvline(0,color='#a3abb0',lw=.7)
    chosen=5;xx,yy=x[chosen],y[chosen]
    ax.annotate('Horizontal projection',(xx,0),xytext=(-1.16,-1.20),fontsize=11,
                arrowprops={'arrowstyle':'->','color':'#8b521d'},color='#8b521d')
    ax.text(-1.13,1.12,'Equal angle steps; unequal horizontal steps',fontsize=10)
    ax.set(xlim=(-1.28,1.28),ylim=(-1.35,1.35),aspect='equal',xlabel=r'$Y=\cos\Phi$',ylabel='Vertical circle coordinate',
           title='Uniform angle on a unit circle')
    z=np.linspace(-.999,.999,1001)
    density=1/(np.pi*np.sqrt(1-z*z))
    bx.plot(z,density,color='#74549b',lw=2.6)
    bx.axvline(-.5,color='#ae7e3f',ls='--',lw=1.1);bx.axvline(.5,color='#ae7e3f',ls='--',lw=1.1)
    bx.fill_between(z,0,density,where=np.abs(z)>.5,color='#e3b66e',alpha=.42)
    bx.text(-.93,1.58,r'$f_Y(y)=1/(\pi\sqrt{1-y^2})$',fontsize=14)
    bx.text(-.84,.88,'Outside [-1/2, 1/2]:\n2/3 of the probability',fontsize=11,
            bbox={'fc':'white','ec':'none','alpha':.9,'pad':3})
    for end in [-1,1]:
        bx.annotate('',xy=(end,1.88),xytext=(end,1.67),arrowprops={'arrowstyle':'->','color':'#74549b','lw':1.5})
    bx.set(xlim=(-1.05,1.05),ylim=(0,2.0),xlabel='Projected position y',ylabel='Probability density per unit y',
           title='More probability near the two ends')
    bx.grid(alpha=.16)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
