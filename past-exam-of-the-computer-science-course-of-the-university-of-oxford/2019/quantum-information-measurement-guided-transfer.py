"""Original rotating-measurement probability figure for Oxford Quantum Information 2019.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7, as documented in root pyproject.
Writes a same-basename opaque white PNG to CWD; no external inputs.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    n=np.arange(1,13)
    target=(1+np.cos(np.pi/n)**n)/2
    uninterrupted=np.cos(np.pi/(2*n))**(2*n)
    assert np.isclose(target[2],9/16) and np.isclose(uninterrupted[2],27/64)
    fig,(ax,bx)=plt.subplots(1,2,figsize=(9.8,4.0),dpi=100)
    fig.patch.set_facecolor('white')
    ax.plot(n,target,'o-',color='#245b88',label='Final label 0: all histories',markersize=4)
    ax.plot(n,uninterrupted,'s--',color='#b1632e',label='Label 0 at every step',markersize=4)
    ax.set(xlabel='Number of measurements n',ylabel='Probability',title='Final return includes earlier switches',xticks=[1,2,3,4,6,8,10,12],ylim=(-.03,1.03))
    ax.legend(fontsize=8,loc='lower right')
    large=np.unique(np.geomspace(10,10000,160).astype(int))
    error=(1-np.cos(np.pi/large)**large)/2
    bx.loglog(large,error,color='#245b88',label='Total final error')
    bx.loglog(large,np.pi**2/(4*large),'--',color='#b1632e',label=r'Leading term $\pi^2/(4n)$')
    bx.set(xlabel='Number of measurements n',ylabel='Probability of missing the target',title='Target becomes |1⟩ with certainty')
    bx.legend(fontsize=8)
    for axis in [ax,bx]:axis.grid(alpha=.18)
    fig.suptitle('Measurement-guided transfer: outcome 0 in the final basis is physical state |1⟩',fontsize=11)
    fig.tight_layout(rect=(0,0,1,.92))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,metadata={'Software':'Original analytic figure; NumPy/Matplotlib'})
    plt.close(fig)


if __name__=='__main__':
    main()
