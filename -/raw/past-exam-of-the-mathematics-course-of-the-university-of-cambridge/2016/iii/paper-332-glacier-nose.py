"""Generate the basal-drag nose plot in cwd; Make alone places media.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(8.2,4.8),dpi=100,facecolor='white')
fig.subplots_adjust(left=.10,right=.97,bottom=.14,top=.90)
h=np.linspace(0,4,500); s=h**3/3+h**2/2
ax.plot(s,h,lw=2.6,color='#285b8f',label='Combined shear + basal slip')
x=np.linspace(0,s[-1],500)
ax.plot(x,np.sqrt(2*x),'--',color='#b66212',label=r'Thin limit: $\mathcal{H}\sim(2cS)^{1/2}$')
ax.plot(x,np.cbrt(3*x),':',lw=2,color='#278067',label=r'Thick limit: $\mathcal{H}\sim(3cS)^{1/3}$')
ax.scatter([5/6],[1],color='#a32b29',zorder=5)
ax.annotate('equal mobilities',xy=(5/6,1),xytext=(4,1.2),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlim=(0,29.5),ylim=(0,4.2),xlabel=r'Speed × distance behind nose, $cS$',ylabel=r'Dimensionless thickness, $\mathcal{H}$',title='A translating glacier nose with linear basal drag')
ax.legend(loc='lower right',frameon=False,fontsize=10)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'paper-332-glacier-nose.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
