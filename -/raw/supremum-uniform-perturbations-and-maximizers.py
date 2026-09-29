"""Original polynomial examples: uniform error bounds values, not optimizer locations."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
    fig,(ax,right)=plt.subplots(1,2,figsize=(12,6),layout='constrained',facecolor='white')
    x=np.unique(np.r_[np.linspace(-1,1,501),0,.1]);f=-x*x;g=f+.2*x
    ax.fill_between(x,f-.2,f+.2,color='#dce8f4',label=r'Uniform band $f\pm0.2$')
    ax.plot(x,f,c='#2465aa',lw=2.4,label=r'$f(x)=-x^2$')
    ax.plot(x,g,c='#c16127',lw=2.4,label=r'$g(x)=-x^2+0.2x$')
    ax.scatter([0],[0],s=90,marker='*',c='#2465aa',zorder=5)
    ax.scatter([.1],[.01],s=90,marker='*',c='#c16127',zorder=5)
    ax.set(xlim=(-1,1),ylim=(-1.25,.4),xlabel=r'$x$',ylabel='Objective value',title='Value change 0.01 is below error bound 0.2')
    ax.legend(loc='upper left',fontsize=10,framealpha=1)
    inset=ax.inset_axes([.28,.08,.64,.32]);u=np.linspace(-.2,.3,201)
    inset.plot(u,-u*u,c='#2465aa',lw=1.7);inset.plot(u,-u*u+.2*u,c='#c16127',lw=1.7)
    inset.scatter([0,.1],[0,.01],c=['#2465aa','#c16127'],s=35,marker='*')
    inset.set(xlim=(-.2,.3),ylim=(-.055,.025));inset.set_xticks([0,.1]);inset.set_yticks([0,.01]);inset.tick_params(labelsize=9)
    inset.set_title('Zoom at the maxima',fontsize=10);inset.set_facecolor('white')
    for eps,style in [(.1,'-'),(.02,'--')]:
        right.plot(x,eps*x,c='#2465aa',ls=style,lw=2.2,label=rf'$+\varepsilon x$, $\varepsilon={eps}$')
        right.plot(x,-eps*x,c='#c16127',ls=style,lw=2.2,label=rf'$-\varepsilon x$, $\varepsilon={eps}$')
        right.scatter([1],[eps],c='#2465aa',marker='*',s=100,clip_on=False,zorder=5)
        right.scatter([-1],[eps],c='#c16127',marker='*',s=100,clip_on=False,zorder=5)
    right.annotate('',xy=(1,-.08),xytext=(-1,-.08),arrowprops={'arrowstyle':'<->','lw':1.5,'color':'#555555'})
    right.text(0,-.095,'Maximizing inputs stay two units apart',ha='center',va='top',fontsize=10)
    right.set(xlim=(-1.07,1.07),ylim=(-.13,.15),xlabel=r'$x$',ylabel='Objective value',title='Small function changes can move the maximizer')
    right.legend(loc='upper center',fontsize=9,ncol=2,framealpha=1)
    fig.suptitle('A supremum is stable under uniform error; the maximizing input need not be',fontsize=16)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=110,facecolor='white');plt.close(fig)


if __name__=='__main__':main()
