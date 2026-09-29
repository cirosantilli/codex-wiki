"""Display equal-value lines and the kernel of a scalar linear measurement."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def functional(v):
    return np.array([2.,-1.]) @ np.asarray(v)


def main():
    v,w=np.array([3.,1.]),np.array([1.,2.])
    assert functional(v)==5 and functional(w)==0
    assert functional(v+w)==functional(v)+functional(w)==5
    for a,b in [(2,3),(-1,4),(.25,-.5),(0,0)]:
        assert np.isclose(functional(a*v+b*w),a*functional(v)+b*functional(w))
    x=np.linspace(-.4,4.4,200)
    fig,ax=plt.subplots(figsize=(8.4,6),dpi=120,facecolor='white')
    for c,pos in [(-2,(.7,3.5)),(2,(2.3,2.6)),(4,(3.15,2.3)),(6,(3.8,1.6))]:
        ax.plot(x,2*x-c,color='#c5ced6',lw=1.4)
        ax.text(*pos,rf'$\varphi={c}$',fontsize=12,color='#687b8a',
                bbox={'facecolor':'white','edgecolor':'none','pad':1})
    ax.plot(x,2*x,color='#287549',lw=2.1,label=r'Kernel: $\varphi=0$')
    ax.plot(x,2*x-5,color='#286da0',lw=2.1,ls='--',label=r'Equal-value line: $\varphi=5$')
    for point,color in [(v,'#286da0'),(w,'#287549')]:
        ax.annotate('',xy=point,xytext=(0,0),
                    arrowprops={'arrowstyle':'->','color':color,'lw':2.5})
        ax.scatter(*point,s=65,color=color,zorder=4)
    ax.scatter(*(v+w),s=65,color='#286da0',zorder=4)
    ax.annotate('',xy=v+w,xytext=v,
                arrowprops={'arrowstyle':'->','color':'#b56c27','lw':2.4})
    ax.annotate(r'$v=(3,1)$'+'\n'+r'$\varphi(v)=5$',xy=v,xytext=(3.02,.1),
                fontsize=12,color='#286da0',
                bbox={'facecolor':'white','edgecolor':'none','pad':2})
    ax.annotate(r'$w=(1,2)$'+'\n'+r'$\varphi(w)=0$',xy=w,xytext=(.03,2.6),
                fontsize=12,color='#287549',
                arrowprops={'arrowstyle':'->','color':'#287549'})
    ax.text(3.32,3.23,r'$v+w=(4,3)$'+'\n'+r'$\varphi(v+w)=5$',fontsize=12,color='#286da0',
            bbox={'facecolor':'white','edgecolor':'none','pad':3})
    ax.text(2.57,2.02,r'Add $w$',color='#995c24',fontsize=11,
            bbox={'facecolor':'white','edgecolor':'none','pad':2})
    ax.axhline(0,color='#9aa7b1',lw=.7)
    ax.axvline(0,color='#9aa7b1',lw=.7)
    ax.set(xlim=(-.4,4.4),ylim=(-.4,4.4),aspect='equal',xlabel='x',ylabel='y')
    ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='upper left',frameon=True,fontsize=11)
    fig.suptitle(r'$\varphi(x,y)=2x-y$: move along a level line without changing the reading',
                 fontsize=15,y=.97)
    fig.text(.5,.025,'Adding a vector from the kernel leaves the measured value unchanged.',
             ha='center',fontsize=12)
    fig.subplots_adjust(left=.1,right=.95,bottom=.13,top=.88)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,
                facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
