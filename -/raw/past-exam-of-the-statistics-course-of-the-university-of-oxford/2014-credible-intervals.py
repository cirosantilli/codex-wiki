"""Python 3.14; numpy, matplotlib. Write an opaque PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
alpha=.05
lo=-np.log(1-alpha/2); hi=-np.log(alpha/2); hpd=-np.log(alpha)
x=np.linspace(0,4.5,1000)
fig,axes=plt.subplots(1,2,figsize=(8.8,3.5),sharey=True,layout='constrained',facecolor='white')
for ax,(a,b,title) in zip(axes,[(lo,hi,'Equal tails: 2.5% in each tail'),(0,hpd,'Highest density: 5% upper tail')]):
 ax.plot(x,np.exp(-x),color='#244870',lw=2)
 mask=(x>=a)&(x<=b)
 ax.fill_between(x,np.exp(-x),where=mask,color='#82b9d8',alpha=.65)
 ax.axvline(b,color='#9b3b32',ls='--',lw=1.1)
 if a>0:ax.axvline(a,color='#9b3b32',ls='--',lw=1.1)
 ax.set(xlabel=r'$\theta$',title=title,xlim=(0,4.5),ylim=(0,1.08))
 ax.text(.48,.83,f'95% interval\n[{a:.3f}, {b:.3f}]',transform=ax.transAxes)
 ax.spines[['top','right']].set_visible(False)
axes[0].set_ylabel(r'Posterior density $e^{-\theta}$')
fig.savefig(Path.cwd()/'2014-credible-intervals.png',dpi=140,facecolor='white')
