"""Original clocked-detector trace; Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Writes its opaque PNG to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    a=np.array([0,1,1,0,1,1,1,0,0,1,0,1,1,0],dtype=int)
    z=np.zeros_like(a);z[2:]=a[:-2]*a[1:-1]*(1-a[2:])
    fig,axes=plt.subplots(2,1,figsize=(7,3.1),dpi=110,sharex=True)
    fig.patch.set_facecolor('white')
    for ax,values,label in zip(axes,[a,z],['Sampled a[k]','Registered z[k]']):
        ax.step(np.arange(len(a)+1),np.r_[values,values[-1]],where='post',lw=2,color='#17628b')
        ax.scatter(np.arange(len(a)),values,s=14,color='#172735',zorder=3)
        for k in range(len(a)):ax.axvline(k,color='#ddd',lw=.6,zorder=0)
        for k in np.flatnonzero(z):ax.axvspan(k,k+1,color='#bfe7c5',alpha=.5,zorder=0)
        ax.set(ylim=(-.18,1.25),yticks=[0,1],ylabel=label,xlim=(-.2,len(a)))
        ax.spines[['top','right']].set_visible(False)
    axes[-1].set_xticks(np.arange(len(a)))
    axes[-1].set_xlabel('Active clock edge k; values shown after that edge')
    fig.suptitle('One registered pulse after two or more high samples',fontsize=12)
    fig.tight_layout(rect=(0,0,1,.93))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
