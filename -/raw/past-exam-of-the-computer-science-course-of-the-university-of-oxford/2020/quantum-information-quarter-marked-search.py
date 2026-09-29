"""Original exact-search amplitude illustration for Oxford Quantum Information 2020.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7, pinned in the root pyproject.
Run anywhere: writes the same-basename white opaque PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    size=8
    marked=np.zeros(size,dtype=bool)
    marked[[1,6]]=True
    uniform=np.ones(size)/np.sqrt(size)
    oracle=np.where(marked,-1.0,1.0)*uniform
    mean=oracle.mean()
    reflection=2*np.outer(uniform,uniform)-np.eye(size)
    final=reflection@oracle
    assert np.allclose(final[~marked],0)
    assert np.allclose(final[marked],2/np.sqrt(size))
    probabilities=abs(final)**2
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10,3.9),dpi=100,gridspec_kw={'width_ratios':[1.35,1]})
    fig.patch.set_facecolor('white')
    x=np.arange(size)
    ax.bar(x-.17,oracle,width=.34,color='#8d9ba4',label='After phase oracle')
    ax.bar(x+.17,final,width=.34,color='#21618c',label='After reflection')
    ax.axhline(0,color='#222222',linewidth=.8)
    ax.axhline(mean,color='#a86528',linestyle='--',linewidth=1,label='Oracle-state mean')
    ax.set(xlabel='Computational-basis label',ylabel='Real probability amplitude',xticks=x,ylim=(-.44,.86),title='Invert signed amplitudes about their mean')
    ax.legend(fontsize=8,loc='upper left')
    bx.bar(x,probabilities,color=['#21618c' if v else '#eeeeee' for v in marked],width=.65)
    bx.set(xlabel='Measured label',ylabel='Final Born probability',xticks=x,ylim=(0,.64),title='Uniform over the marked labels')
    for label in [1,6]:
        bx.text(label,.52,'1/2',ha='center',fontsize=10)
    fig.suptitle('One exact Grover iteration: 2 marked inputs out of 8 (illustrative labels 1 and 6)',fontsize=11)
    fig.tight_layout(rect=(0,0,1,.93))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,
                metadata={'Software':'NumPy/Matplotlib; original Oxford 2020 quantum-information solution'})
    plt.close(fig)


if __name__=='__main__':main()
