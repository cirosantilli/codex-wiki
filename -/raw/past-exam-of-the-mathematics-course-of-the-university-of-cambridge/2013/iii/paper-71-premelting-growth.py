"""Exact reduced frost-heave growth and its asymptotes.
Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5. Honor MPLCONFIGDIR.
Output only paper-71-premelting-growth.png in cwd.
"""
import os,tempfile
def main():
    cache=None
    if 'MPLCONFIGDIR' not in os.environ:
        cache=tempfile.TemporaryDirectory(prefix='paper-71-mpl-')
        os.environ['MPLCONFIGDIR']=cache.name
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    t=np.linspace(0,4,700);eta=(-np.expm1(-7*t/4))**(4/7)
    fig,ax=plt.subplots(figsize=(8.4,5.4),dpi=100,facecolor='white')
    ax.plot(t,eta,color='#2786a8',lw=2.5,label='exact, $\\eta(0)=0$')
    small=np.linspace(0,.21,100);ax.plot(small,(7*small/4)**(4/7),color='#b44b35',ls=':',lw=2,label='small $\\tau$: $(7\\tau/4)^{4/7}$')
    late=np.linspace(1,4,200);ax.plot(late,1-4/7*np.exp(-7*late/4),color='#825b9c',ls='--',lw=1.5,label='large $\\tau$: $1-(4/7)e^{-7\\tau/4}$')
    ax.axhline(1,color='#666',ls=':',lw=1);ax.text(3.10,1.035,'equilibrium $\\eta=1$',fontsize=10)
    ax.annotate('monotone and concave down',xy=(.5,float((-np.expm1(-7*.5/4))**(4/7))),xytext=(1.3,.5),arrowprops=dict(arrowstyle='->'),fontsize=10)
    ax.set(xlim=(0,4),ylim=(0,1.14),xlabel='Time $\\tau=t/t_*$',ylabel='Ice thickness $\\eta=h/h_*$',title='Flow-limited premelting growth approaches a gravity-limited thickness')
    ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=10)
    fig.text(.5,.035,'The zero-thickness start is a formal reduced-model limit; a finite initial film requires an initial microscopic regime.',ha='center',fontsize=9)
    fig.subplots_adjust(left=.11,right=.96,bottom=.17,top=.89)
    fig.savefig('paper-71-premelting-growth.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
    if cache:cache.cleanup()
if __name__=='__main__':main()
