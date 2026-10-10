"""Enumerate all five six-step Dyck paths and their parenthesis encodings."""
from itertools import combinations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def paths(n):
    for up in combinations(range(2*n), n):
        steps=np.full(2*n,-1,dtype=int)
        steps[list(up)]=1
        heights=np.r_[0,np.cumsum(steps)]
        if heights.min()>=0:
            yield steps,heights


def main():
    examples=list(paths(3))
    assert len(examples)==5
    fig,axes=plt.subplots(2,3,figsize=(11.4,6.5),dpi=100,facecolor='white')
    fig.suptitle('Five paths, five balanced parenthesis strings',fontsize=18,y=.97)
    for ax,(steps,h) in zip(axes.flat,examples):
        code=''.join('(' if s==1 else ')' for s in steps)
        ax.plot(range(7),h,color='#246c99',lw=2.8,marker='o',ms=5)
        ax.fill_between(range(7),0,h,color='#246c99',alpha=.08)
        ax.axhline(0,color='#555',lw=1)
        ax.set(xlim=(-.2,6.2),ylim=(-.15,3.5),xticks=range(7),yticks=range(4))
        ax.set_title(code,fontfamily='monospace',fontsize=18,pad=10)
        ax.set_xlabel('Step count');ax.set_ylabel('Unmatched openings')
        ax.grid(alpha=.15)
        ax.spines[['top','right']].set_visible(False)
    axes.flat[-1].axis('off')
    axes.flat[-1].text(.5,.65,'3 up steps + 3 down steps\nEvery prefix stays at height ≥ 0',ha='center',va='center',fontsize=12,transform=axes.flat[-1].transAxes)
    axes.flat[-1].text(.5,.31,'C₃ = 5',ha='center',va='center',fontsize=23,color='#246c99',transform=axes.flat[-1].transAxes)
    fig.subplots_adjust(left=.07,right=.97,bottom=.1,top=.85,wspace=.32,hspace=.57)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white')
    plt.close(fig)


if __name__=='__main__':main()
