"""Original first-return path and independent Catalan recurrence contributions."""
from pathlib import Path
from math import comb
import matplotlib.pyplot as plt
import numpy as np


def main():
    steps=np.array([1,1,1,-1,-1,-1,1,-1])
    h=np.r_[0,np.cumsum(steps)]
    assert np.flatnonzero(h[1:]==0)[0]+1==6
    fig,(pathax,countax)=plt.subplots(1,2,figsize=(12,5.5),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1.25,1]})
    fig.suptitle('A first return splits one Dyck path into two smaller ones',fontsize=17,y=.97)
    colors=['#744da0']+['#246c99']*4+['#744da0']+['#d07d24']*2
    for i,color in enumerate(colors):pathax.plot([i,i+1],h[i:i+2],color=color,lw=3.4)
    pathax.scatter(range(9),h,color='#333',s=23,zorder=3)
    pathax.axhline(0,color='#555',lw=1);pathax.axhline(1,color='#246c99',lw=1,ls=':',alpha=.5)
    pathax.annotate('First return',(6,0),(4.8,1.85),arrowprops={'arrowstyle':'->','color':'#444'},fontsize=11)
    pathax.text(.45,1.27,'U',fontsize=14,color=colors[0]);pathax.text(3,3.36,'P: 2 up/down pairs',ha='center',fontsize=11,color='#246c99')
    pathax.text(5.5,.74,'D',fontsize=14,color=colors[5]);pathax.text(7.05,1.28,'Q: 1 pair',ha='center',fontsize=11,color='#d07d24')
    pathax.set(xlim=(-.3,8.3),ylim=(-.15,3.9),xticks=range(9),yticks=range(4),xlabel='Step count',ylabel='Height')
    pathax.set_title('U P D Q: n = 4, k = 2',fontsize=13,pad=13)
    pathax.grid(alpha=.15);pathax.spines[['top','right']].set_visible(False)
    catalan=lambda n:comb(2*n,n)//(n+1)
    k=np.arange(4);values=[catalan(int(i))*catalan(3-int(i)) for i in k]
    assert values==[5,2,2,5] and sum(values)==14
    countax.bar(k,values,color=['#a8c7d9','#a8c7d9','#246c99','#a8c7d9'],width=.65)
    for i,value in enumerate(values):countax.text(i,value+.13,f'{catalan(i)} × {catalan(3-i)} = {value}',ha='center',fontsize=11)
    countax.set(xticks=k,ylim=(0,6.1),yticks=range(7),xlabel='Semilength k of the inside path P',ylabel='Number of paths in this group')
    countax.set_title('C₄ = 5 + 2 + 2 + 5 = 14',fontsize=13,pad=13)
    countax.grid(axis='y',alpha=.15);countax.set_axisbelow(True);countax.spines[['top','right']].set_visible(False)
    fig.subplots_adjust(left=.06,right=.98,bottom=.18,top=.78,wspace=.32)
    fig.text(.5,.055,'P is shifted one level upward; Q starts after the first return to zero. Original enumeration.',ha='center',fontsize=11)
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)


if __name__=='__main__':main()
