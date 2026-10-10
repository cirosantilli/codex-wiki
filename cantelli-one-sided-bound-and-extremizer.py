"""Variance-only upper-tail bounds and an exact two-point extremizer.

Original mathematical examples, not data. Opaque white PNG in CWD.
Dependency and Python versions are documented in pyproject.toml.
"""
from pathlib import Path
from math import erfc,sqrt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(10.6,4.8),dpi=120,facecolor='white')
for ax in axes:
    ax.set_facecolor('white');ax.grid(alpha=0.17)
a=np.linspace(0.15,4,400)
normal=np.array([0.5*erfc(float(x)/sqrt(2)) for x in a])
axes[0].plot(a,np.minimum(1,1/a**2),color='#b97840',lw=2,label='Chebyshev upper bound (capped)')
axes[0].plot(a,1/(1+a**2),color='#286f99',lw=2,label='Cantelli: 1/(1+a²)')
axes[0].plot(a,normal,color='#368565',lw=2,label='Actual standard-normal upper tail')
axes[0].scatter([2],[0.2],color='#286f99',s=32,zorder=5)
axes[0].annotate('a = 2: bound 1/5', (2,0.2),xytext=(1.9,0.48),fontsize=10,
                 arrowprops={'arrowstyle':'->','color':'#286f99'})
axes[0].set(xlim=(0,4),ylim=(0,1.05),xlabel='Deviation a, with variance 1',ylabel='Probability or valid upper bound',
            title='One specified tail retains more information')
axes[0].legend(loc='upper right',fontsize=8.4,framealpha=0.96)
axes[1].axvspan(2,2.7,color='#dcebf1',zorder=0)
axes[1].axvline(2,color='#657b86',ls=':',lw=1.3)
axes[1].vlines([-0.5,2],0,[0.8,0.2],colors=['#657b86','#286f99'],lw=4)
axes[1].scatter([-0.5,2],[0.8,0.2],s=55,color=['#657b86','#286f99'],zorder=4)
axes[1].text(-0.5,0.84,'P = 4/5',ha='center',fontsize=11)
axes[1].text(2,0.24,'P = 1/5',ha='center',fontsize=11)
axes[1].text(0.5,0.6,'Mean = 0\nVariance = 1\nP(X ≥ 2) = 1/5',ha='center',fontsize=11)
axes[1].set(xlim=(-1.25,2.7),ylim=(0,1.02),xticks=[-0.5,0,1,2],xlabel='Value of X',ylabel='Probability mass',
            title='An exact extremizer includes the threshold')
fig.text(0.5,0.025,'Only mean and variance are fixed; the extremal distribution generally changes when the threshold changes.',
         ha='center',fontsize=9.5)
fig.subplots_adjust(left=0.065,right=0.98,top=0.9,bottom=0.17,wspace=0.28)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white');plt.close(fig)
