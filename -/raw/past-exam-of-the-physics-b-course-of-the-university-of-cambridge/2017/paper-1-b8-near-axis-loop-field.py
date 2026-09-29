"""Original leading near-axis loop-field geometry; Python 3.14, numpy, matplotlib.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(7,4.1),layout='constrained',facecolor='white')
ax.set_facecolor('white')
z=np.linspace(.7,2.4,350)
zref=1.3
# In units a=1, integrate dx/dz=B_x/B_z=3zx/[2(1+z^2)].
for seed in [-.12,-.08,-.04,0,.04,.08,.12]:
    x=seed*((1+z*z)/(1+zref*zref))**.75
    ax.plot(z,x,color='#165b99',lw=1.35)
    for position in [.95,1.65,2.15]:
        ix=np.searchsorted(z,position)
        ax.annotate('',xy=(z[ix+10],x[ix+10]),xytext=(z[ix-10],x[ix-10]),arrowprops={'arrowstyle':'->','color':'#165b99','lw':1.35})
ax.scatter([zref],[0],color='black',s=20,zorder=4)
ax.text(zref+.025,-.025,r'$P$',fontsize=12)
ax.annotate('',xy=(1.9,.14),xytext=(1.6,.14),arrowprops={'arrowstyle':'->','color':'#cc7a1d','lw':2})
ax.text(1.75,.16,r'$B_z>0$',color='#a45d10',ha='center')
ax.annotate('',xy=(1.6,.205),xytext=(1.6,.14),arrowprops={'arrowstyle':'->','color':'#cc7a1d','lw':2})
ax.text(1.58,.22,r'$B_\rho>0$',color='#a45d10',ha='center')
ax.set(xlim=(.7,2.4),ylim=(-.27,.27),xlabel=r'$z/a$',ylabel=r'Signed transverse position $x/a$',title='Local field geometry beyond a current loop')
ax.text(.02,.025,r'Near axis: $B_\rho=-\rho B_0^{\prime}/2$; loop lies at $z=0$',transform=ax.transAxes,fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
