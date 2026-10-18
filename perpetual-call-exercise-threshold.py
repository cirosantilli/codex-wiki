"""Perpetual-call exercise policies in a p=2 model; output PNG to cwd.

Tested with Python 3.14.4 and the NumPy/Matplotlib versions in pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':11,'savefig.facecolor':'white'})
    fig,axes=plt.subplots(1,2,figsize=(10.4,4.1),layout='constrained')
    s=np.linspace(0,3.7,1200)
    intrinsic=np.maximum(s-1,0)
    axes[0].plot(s,intrinsic,'--',color='#777777',lw=1.7,label='Immediate exercise')
    for threshold,color,label in [(2,'#1565a7','Optimal threshold 2'),(1.4,'#218859','Early threshold 1.4'),(3.2,'#c65522','Late threshold 3.2')]:
        value=np.where(s<threshold,(threshold-1)*(s/threshold)**2,s-1)
        axes[0].plot(s,value,color=color,lw=2.1,label=label)
        axes[0].scatter([threshold],[threshold-1],color=color,s=22,zorder=5)
    axes[0].set(xlabel='Current stock price / strike',ylabel='Value / strike',xlim=(0,3.7),ylim=(-.03,2.8),title='A fixed policy can lose exercise value')
    axes[0].legend(loc='upper left',fontsize=9,frameon=False)
    b=np.linspace(1,4,1000);factor=(b-1)/b**2
    axes[1].plot(b,factor,color='#1565a7',lw=2.3)
    for threshold,color in [(1.4,'#218859'),(2,'#1565a7'),(3.2,'#c65522')]:
        val=(threshold-1)/threshold**2
        axes[1].scatter([threshold],[val],color=color,zorder=5,s=28)
        axes[1].annotate(f'{threshold:g}',(threshold,val),xytext=(0,9),textcoords='offset points',ha='center',color=color)
    axes[1].set(xlabel='Exercise threshold / strike',ylabel=r'Continuation value divided by $S^2$',xlim=(1,4),ylim=(-.006,.285),title=r'The threshold factor $(B-1)/B^2$ peaks at 2')
    for ax in axes:
        ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
    fig.savefig(Path.cwd()/'perpetual-call-exercise-threshold.png',dpi=100,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
