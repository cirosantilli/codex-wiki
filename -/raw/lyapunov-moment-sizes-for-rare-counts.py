"""Absolute moment sizes for toy counts and a constant-magnitude variable.

Matching opaque PNG goes into CWD. See pyproject.toml for versions.
"""
from pathlib import Path
from math import comb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

r=np.linspace(0.5,6,300);k=np.arange(1,11)
pmf=np.array([comb(10,int(j))*0.1**int(j)*0.9**(10-int(j)) for j in k])
independent=np.array([np.dot(pmf,k**float(t))**(1/float(t)) for t in r])
shared=10*0.1**(1/r)
fig,axes=plt.subplots(1,2,figsize=(10.6,4.8),dpi=120,facecolor='white')
for ax in axes:
    ax.set_facecolor('white');ax.grid(alpha=0.17)
axes[0].plot(r,shared,lw=2.2,color='#286f99',label='Shared count: 10(0.1)¹/ʳ')
axes[0].plot(r,independent,lw=2.2,color='#368565',label='Independent binomial count')
axes[0].scatter([1,2,2],[1,np.sqrt(10),np.sqrt(1.9)],color=['#657b86','#286f99','#368565'],s=33,zorder=5)
axes[0].annotate('Same first size: 1',(1,1),xytext=(2.4,0.4),fontsize=9.5,
                 arrowprops={'arrowstyle':'->','color':'#657b86'})
axes[0].annotate('Second sizes:\n√10 ≈ 3.162\n√1.9 ≈ 1.378',(2,np.sqrt(10)),xytext=(3.9,3),fontsize=9.5,
                 arrowprops={'arrowstyle':'->','color':'#286f99'})
axes[0].set(xlim=(0.4,6),ylim=(0,7.5),xlabel='Positive exponent r',ylabel='Absolute moment size (E|N|ʳ)¹/ʳ',
            title='Higher moments emphasize rare large counts')
axes[0].legend(loc='upper left',fontsize=9,framealpha=0.96)
axes[1].vlines([-2,2],0,[0.5,0.5],color='#657b86',lw=3)
axes[1].scatter([-2,2],[0.5,0.5],s=50,color='#286f99',zorder=5)
axes[1].text(-2,0.55,'P = 1/2',ha='center',fontsize=11)
axes[1].text(2,0.55,'P = 1/2',ha='center',fontsize=11)
axes[1].text(0,0.82,'|Z| = 2 on every outcome\n(E|Z|ʳ)¹/ʳ = 2 for every r > 0',ha='center',fontsize=11)
axes[1].set(xlim=(-3,3),ylim=(0,1.05),xticks=[-2,0,2],xlabel='Value of Z',ylabel='Probability mass',
            title='Signs can vary while equality holds')
fig.text(0.5,0.025,'These are original finite-support models on probability spaces of total mass one.',ha='center',fontsize=10)
fig.subplots_adjust(left=0.065,right=0.98,top=0.9,bottom=0.17,wspace=0.28)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)
