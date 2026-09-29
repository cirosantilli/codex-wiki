"""Write the opaque domain sketch to cwd; Make alone owns media placement.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(6.4,4.2),dpi=100,facecolor='white')
fig.subplots_adjust(left=.11,right=.96,bottom=.15,top=.89)
r=np.linspace(1,2,250)
ax.fill_between(r,.25,r**-2,color='#dcebf6')
ax.plot(r,r**-2,color='#285b8f',lw=2.4,label=r'$z=\rho^{-2}$')
ax.plot([1,1],[.25,1],color='#b66212',lw=2.2,label='Unit cylinder')
ax.plot([1,2],[.25,.25],color='#278067',lw=2.2,label=r'$z=1/4$')
ax.axhline(1,color='gray',lw=1,ls=':')
ax.axvline(0,color='#333333',lw=1.5)
ax.scatter([1,2],[1,.25],color='#285b8f',s=25,zorder=5)
ax.text(1.17,.37,'Section of V',fontsize=12)
ax.annotate('Revolve about z axis',xy=(0,.5),xytext=(.15,.68),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlim=(-.06,2.2),ylim=(.10,1.14),xlabel=r'Distance from axis, $\rho$',ylabel='z',title='Annular volume: meridional section')
ax.set_xticks([0,1,2]);ax.set_yticks([.25,1],['1/4','1'])
ax.spines[['top','right']].set_visible(False);ax.legend(frameon=True,facecolor='white',edgecolor='white',framealpha=1,loc='upper right',fontsize=10)
fig.savefig(Path.cwd()/'paper-3-domain.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
