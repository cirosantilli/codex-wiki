"""Illustrative conditional-probability geometry, not experimental observations.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; existing pyproject dependencies.
Outputs the matching opaque PNG into the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 301)
X, Y = np.meshgrid(x, x)
D = X-Y
assert np.allclose(np.diag(D), 0)
assert D.min() == -1 and D.max() == 1
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig, ax = plt.subplots(figsize=(6.4, 4.8),dpi=100,facecolor='white')
fig.subplots_adjust(left=.13,right=.87,bottom=.17,top=.88)
im = ax.imshow(D,origin='lower',extent=(0,1,0,1),vmin=-1,vmax=1,cmap='RdBu',aspect='equal',interpolation='nearest')
ax.plot([0,1],[0,1],color='#333333',lw=1.4,ls='--')
ax.text(.09,.76,'Negative\ncontingency',ha='left',va='center',color='#202020',
    bbox={'facecolor':'white','edgecolor':'none','alpha':.9,'pad':3})
ax.text(.68,.16,'Positive\ncontingency',ha='center',va='center',color='#202020',
    bbox={'facecolor':'white','edgecolor':'none','alpha':.9,'pad':3})
for y,marker in [(.8,'o'),(.2,'s')]:
    ax.scatter([.8],[y],s=75,marker=marker,c='white',edgecolors='black',linewidth=1.3,zorder=5)
ax.annotate(r'$\Delta P=0$',xy=(.8,.8),xytext=(.40,.91),ha='center',
    arrowprops={'arrowstyle':'->','color':'black'},bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.annotate(r'$\Delta P=0.6$',xy=(.8,.2),xytext=(.37,.39),ha='center',
    arrowprops={'arrowstyle':'->','color':'black'},bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.set(xlabel=r'$P(\mathrm{relief}\mid\mathrm{act})$',ylabel=r'$P(\mathrm{relief}\mid\mathrm{do\ not\ act})$',xlim=(0,1),ylim=(0,1))
ax.set_xticks(np.linspace(0,1,6)); ax.set_yticks(np.linspace(0,1,6))
cb=fig.colorbar(im,ax=ax,fraction=.047,pad=.05,ticks=[-1,-.5,0,.5,1])
cb.set_label(r'$\Delta P=P(O\mid A)-P(O\mid\neg A)$')
fig.suptitle('Outcome frequency is different from control',fontsize=13,y=.965)
fig.text(.5,.035,'Calculated illustration only; conditional association needs causal controls.',ha='center',fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False,
    metadata={'Software':'Matplotlib','Description':'Original conditional-probability contingency illustration'})
plt.close(fig)
