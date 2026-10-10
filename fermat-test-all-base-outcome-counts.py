"""Exhaustive arithmetic outcomes of Fermat tests, not sampled measurements."""
from pathlib import Path
from math import gcd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    ns=[341,561,1105,563]
    counts=[]
    for n in ns:
        units=[a for a in range(1,n) if gcd(a,n)==1]
        passed=sum(pow(a,n-1,n)==1 for a in units)
        counts.append((passed,len(units)-passed,n-1-len(units),len(units)))
    fig,ax=plt.subplots(figsize=(11.3,5.8),facecolor='white')
    colors=['#25836b','#cf733a','#9faeba']
    labels=['Coprime base passes','Coprime exponent witness','Nonunit: gcd reveals a factor']
    for row,n in enumerate(ns):
        start=0
        for k,value in enumerate(counts[row][:3]):
            if value:
                ax.barh(row,value,left=start,height=.53,color=colors[k],
                        label=labels[k] if row==0 else None)
                ax.text(start+value/2,row,str(value),va='center',ha='center',
                        color='white' if k<2 else '#17324a',fontsize=12,weight='bold')
            start+=value
        passed,_,_,units=counts[row]
        ax.text(1130,row,f'{passed}/{units}',va='center',ha='left',fontsize=12)
    ax.set_yticks(np.arange(4),labels=[r'$341=11\cdot31$'+'\nComposite, not Carmichael',
         r'$561=3\cdot11\cdot17$'+'\nCarmichael',r'$1105=5\cdot13\cdot17$'+'\nCarmichael',
         '563\nPrime (independent trial division)'])
    ax.invert_yaxis();ax.set_xlim(0,1270);ax.set_xticks([0,200,400,600,800,1000])
    ax.set_xlabel('Number of nonzero bases: every a from 1 through n−1 is checked',fontsize=11)
    ax.text(1130,-.69,'Coprime pass\nfraction',fontsize=11,weight='bold')
    ax.spines[['top','right']].set_visible(False)
    ax.set_axisbelow(True);ax.grid(axis='x',color='#dce3e7',lw=.65)
    ax.legend(loc='upper left',bbox_to_anchor=(0,-.18),ncol=1,frameon=False,fontsize=11)
    fig.suptitle('Passing every coprime Fermat test does not establish primality',
                 fontsize=17,weight='bold',y=.96)
    fig.text(.5,.018,'Exact finite enumeration. Uniform sampling among coprime bases is a separate assumption.',
             ha='center',fontsize=10.5,color='#40546a')
    fig.subplots_adjust(left=.25,right=.96,top=.83,bottom=.28)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
