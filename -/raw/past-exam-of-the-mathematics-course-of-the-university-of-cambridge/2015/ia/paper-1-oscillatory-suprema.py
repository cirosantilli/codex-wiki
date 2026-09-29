"""Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Write one opaque PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4.3),dpi=100,facecolor='white')
    t=np.linspace(1,90,20000)
    a=np.arcsin(1/t)
    for ax,(left,right) in zip(axes,[(0,np.pi),(np.pi,1.5*np.pi)]):
        x=np.linspace(left,right,600)
        ax.plot(x,np.sqrt(x),color='#b45309',ls='--',lw=1.4,label=r'envelope $\sqrt{x}$')
        ax.plot(x,-np.sqrt(x),color='#b45309',ls='--',lw=1.2)
        ax.axhline(0,color='0.65',lw=.8)
        ax.axhline(np.sqrt(np.pi),color='#7c3aed',ls=':',lw=1.4,label=r'$\sqrt{\pi}$')
        ax.set(xlim=(left-.025,right+.025),ylim=(-2.3,2.5),xlabel='$x$',ylabel='$g(x)$')
        ax.grid(alpha=.16)
        ax.plot([np.pi],[0],'o',color='black',ms=5,zorder=6)
    for x in [a,np.pi-a]:
        ix=np.argsort(x)
        axes[0].plot(x[ix],(np.sqrt(x)*np.sin(t))[ix],color='#2563eb',lw=.8)
    axes[0].plot([0],[0],'o',color='black',ms=5)
    axes[0].plot([np.pi],[np.sqrt(np.pi)],'o',mfc='white',mec='#7c3aed',ms=7,zorder=6)
    axes[0].set_title('Left: supremum approached, never attained')
    axes[0].set_xticks([0,np.pi/2,np.pi],['0',r'$\pi/2$',r'$\pi$'])
    x=np.pi+a;ix=np.argsort(x)
    axes[1].plot(x[ix],(-np.sqrt(x)*np.sin(t))[ix],color='#2563eb',lw=.8)
    x0=np.pi+np.arcsin(2/(3*np.pi))
    axes[1].plot([x0],[np.sqrt(x0)],'o',color='#dc2626',ms=6,zorder=6)
    axes[1].annotate(r'$g(x_0)>\sqrt{\pi}$',(x0,np.sqrt(x0)),xytext=(x0+.3,2.28),arrowprops={'arrowstyle':'->','color':'#dc2626'},color='#dc2626')
    axes[1].set_title('Right: an interior value beats the endpoint')
    axes[1].set_xticks([np.pi,1.25*np.pi,1.5*np.pi],[r'$\pi$',r'$5\pi/4$',r'$3\pi/2$'])
    axes[0].legend(loc='lower center',fontsize=8)
    fig.text(.5,.025,'Oscillations nearest multiples of pi are truncated for readability; black dots are defined endpoint values.',ha='center',fontsize=9)
    fig.subplots_adjust(left=.065,right=.985,bottom=.16,top=.88,wspace=.25)
    fig.savefig(Path.cwd()/'paper-1-oscillatory-suprema.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
