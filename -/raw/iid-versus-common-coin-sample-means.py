"""Exact sample-mean probability masses, iid fair draws versus a common fair coin."""
from math import comb
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig,axes=plt.subplots(2,2,figsize=(11.5,7),dpi=100,facecolor='white',sharex=True,sharey=True)
    fig.suptitle('Averaging fresh draws concentrates; copying one draw does not',fontsize=17,y=.97)
    for n,ax in zip([1,4,16,64],axes.flat):
        x=np.arange(n+1)/n;p=np.array([comb(n,k)/2**n for k in range(n+1)])
        assert abs(p.sum()-1)<1e-14
        ax.vlines(x,0,p,color='#216c9b',lw=2.0 if n<64 else 1.3,label='IID: exact binomial masses')
        ax.plot(x,p,'o',ms=4 if n<64 else 2.7,color='#216c9b')
        ax.vlines([0,1],0,[.5,.5],color='#cc7728',lw=2.1,linestyles='--',label='Common coin: two masses of ½')
        ax.plot([0,1],[.5,.5],'s',ms=6,color='#cc7728',mfc='white')
        ax.axvline(.5,color='#777',ls=':',lw=1)
        ax.set_title(f'n = {n}  ·  IID variance = 1/{4*n}',fontsize=13,pad=10)
        ax.set(xlim=(-.055,1.055),ylim=(0,.565),xticks=[0,.25,.5,.75,1],yticks=[0,.1,.2,.3,.4,.5])
        ax.grid(axis='y',alpha=.15);ax.spines[['top','right']].set_visible(False)
    for ax in axes[-1,:]:ax.set_xlabel('Sample mean')
    for ax in axes[:,0]:ax.set_ylabel('Probability mass at this value')
    handles,labels=axes.flat[0].get_legend_handles_labels();fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.5,.008),ncol=2,frameon=False,fontsize=11)
    fig.subplots_adjust(left=.08,right=.97,bottom=.16,top=.85,hspace=.38,wspace=.15)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)


if __name__=='__main__':main()
