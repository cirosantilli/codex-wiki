"""Original count-derived blocking comparisons for Oxford Statistics Core 2018.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject).
Writes the same-basename opaque white PNG to CWD. No individual records or
third-party image inputs are used.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    tables=np.array([[[9,70,19],[13,132,55]],[[11,56,7],[15,139,63]],[[16,85,10],[9,174,45]],[[12,53,9],[20,174,28]],[[6,79,5],[16,272,27]]])
    pooled=tables.sum(0)
    assert np.array_equal(pooled,[[54,343,50],[73,891,218]])
    rates=tables[:,:,2]/tables.sum(2)
    difference=100*(rates[:,1]-rates[:,0])
    weights=tables.sum((1,2))/tables.sum()
    standardized=weights@rates
    adjusted=100*(standardized[1]-standardized[0])
    crude=100*(218/1182-50/447)
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.3),dpi=100,gridspec_kw={'width_ratios':[1.2,1]})
    fig.patch.set_facecolor('white');x=np.arange(5);labels=['18–24','25–34','35–44','45–54','55+']
    ax.bar(x-.17,100*rates[:,0],width=.34,color='#7e96a9',label='Not populist')
    ax.bar(x+.17,100*rates[:,1],width=.34,color='#b15c27',label='Populist')
    ax.set(xticks=x,xticklabels=labels,xlabel='Age group',ylabel='Reported Yes (%)',ylim=(0,35),title='Within-group blocking reports')
    ax.legend(loc='upper right',fontsize=9)
    bx.plot(difference,x,'o',color='#244b67',markersize=6)
    bx.hlines(x,0,difference,color='#8da4b4',linewidth=2)
    bx.axvline(crude,color='#555555',linestyle='--',linewidth=1,label=f'Crude: {crude:.2f} pp')
    bx.axvline(adjusted,color='#b15c27',linestyle=':',linewidth=1.4,label=f'Common-age weights: {adjusted:.2f} pp')
    bx.set(yticks=x,yticklabels=labels,xlabel='Populist minus not-populist (pp)',title='Descriptive contrasts',xlim=(-1,23))
    bx.invert_yaxis();bx.legend(fontsize=8,loc='lower right')
    fig.suptitle('Reported blocking by populism and age: 1,629 complete cases',fontsize=12)
    fig.text(.5,.012,'Not know remains a valid non-Yes response. Points show empirical contrasts, without uncertainty intervals.',ha='center',fontsize=8)
    fig.tight_layout(rect=(0,.045,1,.92))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,metadata={'Software':'Original derived plot; NumPy/Matplotlib'})
    plt.close(fig)


if __name__=='__main__':
    main()
