"""Three-scale sketch; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
The PNG basename is written to cwd only; caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def approximate_solution(x,epsilon):
    a,b,d=epsilon/2,2.,1/epsilon
    return np.exp(-a*x)/((b-a)*(d-a))-np.exp(-b*x)/((b-a)*(d-b))+np.exp(-d*x)/((d-a)*(d-b))

def main():
    epsilon=.02
    plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,axs=plt.subplots(1,3,figsize=(12.5,4.2),dpi=100)
    fast=np.linspace(0,8,500);ordinary=np.linspace(0,8,700)
    slow=np.unique(np.r_[np.linspace(0,.4,500),np.linspace(.4,8,700)])
    axs[0].plot(fast,approximate_solution(epsilon*fast,epsilon)/epsilon**2,label='Three-root approximation')
    axs[0].plot(fast,fast-1+np.exp(-fast),'--',label='Leading initial-layer shape')
    axs[0].set(xlabel=r'$x/\varepsilon$',ylabel=r'$y/\varepsilon^2$',title='Fast layer: quadratic start')
    axs[1].plot(ordinary,approximate_solution(ordinary,epsilon)/epsilon)
    axs[1].plot(ordinary,.5*(np.exp(-epsilon*ordinary/2)-np.exp(-2*ordinary)),'--')
    peak=np.log(4/epsilon)/(2-epsilon/2)
    axs[1].annotate('Broad maximum',xy=(peak,float(approximate_solution(peak,epsilon)/epsilon)),xytext=(4,.3),arrowprops={'arrowstyle':'->','color':'0.4'})
    axs[1].set(xlabel=r'$x$',ylabel=r'$y/\varepsilon$',title='Ordinary scale: rise to plateau')
    axs[2].plot(slow,approximate_solution(slow/epsilon,epsilon)/epsilon)
    axs[2].plot(slow,.5*np.exp(-slow/2),'--',label='Leading slow decay')
    axs[2].set(xlabel=r'$\varepsilon x$',ylabel=r'$y/\varepsilon$',title='Slow scale: decay to zero')
    for ax in axs:
        ax.grid(alpha=.25);ax.set_ylim(bottom=0)
    axs[0].legend(fontsize=8,loc='upper left')
    axs[2].legend(fontsize=8)
    fig.suptitle(r'Singular initial-value solution for $\varepsilon=0.02$: three distinct spatial scales',fontsize=14)
    fig.tight_layout(rect=(0,0,1,.92))
    fig.savefig(Path.cwd()/'paper-74-three-scales.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)
if __name__=='__main__':main()
