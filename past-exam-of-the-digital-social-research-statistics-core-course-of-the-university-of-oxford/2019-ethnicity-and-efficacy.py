"""Original empirical-probability plot from the held Oxford Statistics Core 2019 counts.

Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject dependencies).
Writes its same-basename white opaque PNG to the current working directory.
No individual records are reconstructed; only printed contingency counts are used.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    counts={
        'Asian (N=77)':np.array([[15,2,2],[5,6,10],[3,10,3],[4,12,5]]),
        'Black (N=57)':np.array([[0,5,1],[8,10,6],[2,10,3],[7,4,1]]),
        'White (N=2332)':np.array([[151,94,66],[378,349,150],[147,213,99],[188,257,240]])}
    pooled=sum(counts.values())
    assert np.array_equal(pooled,np.array([[166,101,69],[391,365,166],[152,233,105],[199,273,246]]))
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(9.8,4.4),dpi=100,sharey=True)
    fig.patch.set_facecolor('white')
    x=np.arange(4)
    styles=[('#c46313','o'),('#247b6c','s'),('#345f9d','^')]
    for ax,col,title in zip(axes,[0,2],['High efficacy','Low efficacy']):
        for (label,a),(color,marker) in zip(counts.items(),styles):
            ax.plot(x,100*a[:,col]/a.sum(1),label=label,color=color,marker=marker,linewidth=1.6,markersize=5)
        ax.plot(x,100*pooled[:,col]/pooled.sum(1),label='Pooled (N=2466)',color='#555555',linestyle='--',linewidth=1.3)
        ax.set(xticks=x,xticklabels=['Strongly\ndisagree','Disagree','Neutral','Agree'],title=title,ylim=(-3,85),yticks=np.arange(0,81,20),xlabel='Response to the technology-distrust statement')
        ax.grid(axis='y',alpha=.2)
        ax.set_axisbelow(True)
    axes[0].set_ylabel('Within-row percentage of respondents')
    handles,labels=axes[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='upper center',bbox_to_anchor=(.51,.93),ncol=4,frameon=False,fontsize=9)
    fig.suptitle('More agreement means more technology distrust',fontsize=12,y=.99)
    fig.text(.5,.015,'Empirical percentages only; connecting lines do not imply equal category spacing or show uncertainty.',ha='center',fontsize=8)
    fig.tight_layout(rect=(0,.055,1,.86))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,metadata={'Software':'Original count-derived figure, NumPy/Matplotlib'})
    plt.close(fig)


if __name__=='__main__':
    main()
