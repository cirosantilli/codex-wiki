"""Original interaction plot. Tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Source: Chinn and Rona (2001), Table 2, English boys, age-specific
published percentages: https://pmc.ncbi.nlm.nih.gov/articles/PMC26603/
These are published descriptive values, not the missing examination fit.
Respect the caller's MPLCONFIGDIR; emit only the PNG basename to caller CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

years=np.array([1974,1984,1994])
percent=np.array([[6.8,4.6,5.4],[6.2,5.7,9.0],[6.2,5.8,12.7]])
labels=['Ages 4–6','Ages 7–8','Ages 9–11']
fig,axes=plt.subplots(1,2,figsize=(9.4,3.7),layout='constrained',facecolor='white')
for ax in axes:ax.set_facecolor('white')
for values,label in zip(percent,labels):
 axes[0].plot(years,values,marker='o',linewidth=2,label=label)
 p=values/100
 axes[1].plot(years,np.log(p/(1-p)),marker='o',linewidth=2,label=label)
for ax in axes:
 ax.set_xticks(years);ax.set_xlabel('Survey year');ax.grid(alpha=.22)
axes[0].set_ylabel('Overweight prevalence (%)');axes[0].set_title('Published proportions')
axes[1].set_ylabel('Log odds of overweight');axes[1].set_title('Interaction on the logit scale')
axes[0].legend(frameon=False,fontsize=9)
fig.suptitle('English boys: age differences widen after 1984',fontsize=12)
fig.savefig('paper-28-overweight.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
