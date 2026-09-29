"""Original counterexample, not participant data. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.array([3.,1.,3.,1.])
y=np.array([3.,3.,1.,1.])
assert x.mean()==y.mean()==2
assert np.dot(x-x.mean(),y-y.mean())==0
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axs=plt.subplots(1,2,figsize=(7.6,3.6),dpi=100,facecolor='white')
fig.subplots_adjust(left=.08,right=.98,top=.79,bottom=.24,wspace=.3)
colors=['#377eac','#bc5e32']
for ax,v,name,color in zip(axs,[x,y],['Condition A','Condition B'],colors):
    ax.bar(np.arange(1,5),v,color=color,width=.65)
    ax.axhline(2,color='#303a42',ls='--',lw=1.2)
    ax.text(4.45,2.13,'Mean = 2',ha='right',fontsize=10)
    ax.set(ylim=(0,4),xlim=(.45,4.55),xticks=[1,2,3,4],xlabel='Measured location')
    ax.set_title(name,pad=12)
    ax.spines[['top','right']].set_visible(False)
axs[0].set_ylabel('Response (arbitrary units)')
fig.suptitle('Same regional mean; different spatial patterns',fontsize=14,y=.98)
fig.text(.5,.065,'Centered patterns: (1, −1, 1, −1) and (1, 1, −1, −1)\nDot product = 0. Illustrative values, not experimental data.',ha='center',va='center',fontsize=10)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
