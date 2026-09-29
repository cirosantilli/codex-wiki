"""Original explanatory schematic. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(figsize=(8,4.3),layout='constrained')
ax.axvspan(-5,0,color='#dceaf4');ax.axvspan(0,5,color='#f8e8da');ax.axvline(0,color='k',lw=2)
ax.plot([-5,5],[0,0],color='k');ax.scatter([-3.8,3.8],[0,0],marker='v',s=100,color='k',zorder=4)
ax.scatter([0],[-2.4],marker='*',s=180,color='#c53432',zorder=5,label='true source')
ax.scatter([-1.7],[-2.4],marker='*',s=180,color='#6a509a',zorder=5,label='apparent source')
ax.plot([-3.8,0,3.8],[0,-2.4,0],color='#c53432',lw=1.8)
ax.annotate('',xy=(-1.6,-2.4),xytext=(-.2,-2.4),arrowprops={'arrowstyle':'->','lw':2,'color':'#6a509a'})
ax.text(-2.5,-.6,'southwest\nfaster block',ha='center');ax.text(2.5,-.6,'northeast\nslower block',ha='center')
ax.text(.12,-1.6,'vertical fault',rotation=90,va='center');ax.text(-3.8,.18,'SW station',ha='center');ax.text(3.8,.18,'NE station',ha='center')
ax.text(0,-3.25,'Uniform-speed fit shifts the source toward the early-arrival side.\nSchematic straight paths within each block; no distance scale implied.',ha='center',fontsize=10)
ax.set(xlim=(-5,5),ylim=(-3.6,.65),title='Velocity-model error can survive a dense station network');ax.axis('off');ax.legend(loc='lower right',bbox_to_anchor=(1,.16),frameon=False)

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
