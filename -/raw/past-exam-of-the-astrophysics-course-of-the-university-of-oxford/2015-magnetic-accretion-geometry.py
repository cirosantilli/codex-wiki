"""Original explanatory figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The only output is a same-basename PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

from matplotlib.patches import Circle,Rectangle
fig,ax=plt.subplots(figsize=(9,5),layout='constrained')
ax.add_patch(Circle((0,0),.46,facecolor='#d7e2e8',edgecolor='#126782',lw=2,zorder=3))
for sign in [-1,1]:ax.add_patch(Rectangle((sign*2.4 if sign>0 else -5.2,-.12),2.8,.24,facecolor='#b9a99a',edgecolor='#77675a',zorder=2))
for l in [2.4,3.2,4.0]:
 th0=np.arcsin(np.sqrt(.46/l));th=np.linspace(th0,np.pi-th0,500);r=l*np.sin(th)**2
 for sign in [-1,1]:ax.plot(sign*r*np.sin(th),r*np.cos(th),color='#126782',lw=1.2,alpha=.8)
for sign in [-1,1]:
 ax.annotate('',xy=(sign*.25,.36),xytext=(sign*.65,1.0),arrowprops={'arrowstyle':'-|>','lw':2.2,'color':'#bb5d22'})
 ax.annotate('',xy=(sign*2.5,.0),xytext=(sign*4.5,.0),arrowprops={'arrowstyle':'-|>','lw':2.4,'color':'#bb5d22'})
ax.text(0,-.77,'Neutron star',ha='center',color='#126782',bbox={'facecolor':'white','edgecolor':'none','pad':1.5});ax.text(3.8,-.48,'Outer accretion disk',ha='center')
ax.annotate('Polar columns and X-rays',xy=(.20,.42),xytext=(.8,2.0),arrowprops={'arrowstyle':'->','color':'#bb5d22'},color='#bb5d22')
ax.annotate('Magnetic field guides inflow',xy=(-1.25,1.4),xytext=(-5.0,2.1),arrowprops={'arrowstyle':'->','color':'#126782'},color='#126782')
ax.annotate('',xy=(2.4,-1.25),xytext=(0,-1.25),arrowprops={'arrowstyle':'<->','color':'#555555'})
ax.text(1.2,-1.61,r'Truncation $r_{\rm Alf}$',ha='center')
ax.text(0,-2.18,r'Accretion: $R_*\lesssim r_{\rm Alf}\lesssim r_{\rm co}$; beyond corotation, propeller inhibition is possible',ha='center',fontsize=11)
ax.set(aspect='equal',xlim=(-5.5,5.5),ylim=(-2.4,2.5));ax.axis('off')
ax.set_title('Magnetic neutron-star accretion: schematic, not to scale\n'+r'$r_{\rm co}=2.07\times10^6$ m for the supplied 1.37-s spin')

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
