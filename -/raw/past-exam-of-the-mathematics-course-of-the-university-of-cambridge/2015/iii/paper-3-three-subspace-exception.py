"""Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5. One opaque PNG in cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,(ax,bx)=plt.subplots(1,2,figsize=(9,3.6),dpi=100,facecolor='white')
    sources=[(-1,1.2),(-1,0),(-1,-1.2)];sink=(1,0)
    colors=['#2563eb','#dc2626','#16a34a']
    labels=[r'$1\mapsto e_1$',r'$1\mapsto e_2$',r'$1\mapsto e_1+e_2$']
    for (x,y),color,label in zip(sources,colors,labels):
        ax.plot(x,y,'o',color=color,ms=8)
        ax.text(x-.3,y,'$k$',va='center',fontsize=14)
        ax.annotate('',sink,(x+.05,y),arrowprops={'arrowstyle':'->','color':color,'lw':2,'shrinkB':10})
        ax.text(0,y*.55+.1,label,fontsize=11,color=color,ha='center')
    ax.plot(*sink,'o',color='#111827',ms=10)
    ax.text(sink[0]+.16,sink[1],'$k^2$',va='center',fontsize=15)
    ax.set(xlim=(-1.6,1.8),ylim=(-1.8,1.8),title='One indecomposable with a two-dimensional sink')
    ax.axis('off')
    t=np.linspace(-1.1,1.1,100)
    bx.plot(t,t*0,color=colors[0],lw=2,label=r'$k e_1$')
    bx.plot(t*0,t,color=colors[1],lw=2,label=r'$k e_2$')
    bx.plot(t,t,color=colors[2],lw=2,label=r'$k(e_1+e_2)$')
    bx.scatter([1,0,1],[0,1,1],color=colors,s=32,zorder=4)
    bx.text(1,-.14,'$e_1$',ha='center');bx.text(-.16,1,'$e_2$',va='center',ha='right')
    bx.text(.95,.81,'$e_1+e_2$',ha='right')
    bx.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),title='Coordinate model of the three image lines',aspect='equal')
    bx.set_xticks([]);bx.set_yticks([]);bx.legend(loc='lower left',fontsize=9)
    for spine in bx.spines.values():spine.set_color('.8')
    fig.text(.5,.04,'Preserving all three lines forces a sink endomorphism to be scalar.',ha='center',fontsize=11)
    fig.subplots_adjust(left=.025,right=.98,bottom=.16,top=.88,wspace=.12)
    fig.savefig(Path.cwd()/'paper-3-three-subspace-exception.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
