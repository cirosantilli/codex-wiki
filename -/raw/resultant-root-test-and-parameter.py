"""Original real common-root example; write PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.8),layout='constrained')
    x=np.linspace(-1.65,1.65,500)
    ax.plot(x,x*x-1,color='#176ea0',lw=2.5,label=r'$f(x)=x^2-1$')
    ax.axhline(0,color='#6c7880',lw=1)
    ax.scatter([-1,1],[0,0],s=65,color='#176ea0',zorder=4,label=r'Roots of $f$')
    ax.axvline(.5,color='#da7a25',ls='--',lw=2,label=r'Root of $g_{1/2}(x)=x-1/2$')
    ax.scatter([.5],[-.75],color='#da7a25',s=55,zorder=5)
    ax.annotate(r'$f(1/2)=-3/4$',(.5,-.75),xytext=(-1.5,-1.3),
                arrowprops={'arrowstyle':'->','color':'#7f6550'},fontsize=12)
    ax.text(.57,.20,r'$t=1/2$',color='#a95c16')
    ax.set(xlim=(-1.65,1.65),ylim=(-1.55,1.9),xlabel=r'Root coordinate $x$',ylabel=r'$f(x)$',
           title='Does the moving root also make f zero?')
    ax.legend(loc='upper left',fontsize=9);ax.grid(alpha=.15)
    bx.plot(x,x*x-1,color='#7654a5',lw=2.5,label=r'$R(t)=\det S(f,g_t)=t^2-1$')
    bx.axhline(0,color='#6c7880',lw=1)
    bx.scatter([-1,1],[0,0],s=65,color='#276e4a',zorder=4)
    bx.annotate('Common root',(-1,0),xytext=(-1.58,.75),
                arrowprops={'arrowstyle':'->','color':'#276e4a'},color='#276e4a')
    bx.annotate('Common root',(1,0),xytext=(.5,.75),
                arrowprops={'arrowstyle':'->','color':'#276e4a'},color='#276e4a')
    bx.scatter([.5],[-.75],color='#da7a25',s=55,zorder=5)
    bx.annotate('No common root',(.5,-.75),xytext=(-1.50,-1.3),
                arrowprops={'arrowstyle':'->','color':'#a95c16'},color='#a95c16')
    bx.set(xlim=(-1.65,1.65),ylim=(-1.55,1.9),xlabel=r'Parameter $t$',ylabel=r'Resultant $R(t)$',
           title='The determinant tests all parameter values')
    bx.legend(loc='upper center',fontsize=10);bx.grid(alpha=.15)
    fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
