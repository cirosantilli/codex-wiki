"""Original oriented contour; Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.

The only output is Path.cwd()/Path(__file__).with_suffix('.png').name.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,ax=plt.subplots(figsize=(5.5,5),dpi=120,facecolor='white');ax.set_facecolor('white')
    x=np.linspace(-1,1,500)
    ax.fill_between(x,x*x-1,np.sqrt(np.maximum(0,1-x*x)),color='#e6f0f7')
    t=np.linspace(0,np.pi,400)
    ax.plot(np.cos(t),np.sin(t),color='#256a9a',lw=2)
    ax.plot(x,x*x-1,color='#a65c2b',lw=2)
    for a,b in [(.65,.85),(2.15,2.35)]:
        ax.annotate('',xy=(np.cos(b),np.sin(b)),xytext=(np.cos(a),np.sin(a)),arrowprops={'arrowstyle':'-|>','lw':1.8,'color':'#256a9a','mutation_scale':15})
    for a,b in [(-.65,-.45),(.35,.55)]:
        ax.annotate('',xy=(b,b*b-1),xytext=(a,a*a-1),arrowprops={'arrowstyle':'-|>','lw':1.8,'color':'#a65c2b','mutation_scale':15})
    ax.scatter([-1,1],[0,0],s=25,color='#344f62',zorder=4)
    ax.axhline(0,color='#7e8a94',lw=.8);ax.axvline(0,color='#7e8a94',lw=.8)
    ax.text(0,1.14,r'$y=\sqrt{1-x^2}$',ha='center',color='#256a9a',fontsize=12)
    ax.text(0,-1.2,r'$y=x^2-1$',ha='center',color='#a65c2b',fontsize=12)
    ax.text(.1,.22,'D',fontsize=15,color='#344f62')
    ax.text(-1.08,.05,'(−1, 0)',ha='right',fontsize=9,color='#344f62')
    ax.text(1.08,.05,'(1, 0)',ha='left',fontsize=9,color='#344f62')
    ax.set(xlim=(-1.55,1.55),ylim=(-1.4,1.45),aspect='equal',xticks=[-1,0,1],yticks=[-1,0,1])
    ax.set_xlabel('x');ax.set_ylabel('y')
    ax.set_title('Counterclockwise semicircle–parabola contour',fontsize=12,pad=12)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(length=0,colors='#566e7c')
    fig.tight_layout(pad=1.2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'codex-wiki semicircle parabola contour'})
    plt.close(fig)


if __name__=='__main__':
    main()
