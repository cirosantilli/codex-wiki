"""Qualitative solar-composition M–R sketch, NOT an evolutionary model grid.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes an opaque 800 x 500 PNG into the current working directory.
Historical example coordinates are approximate; see the adjacent exam solution.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mknots=np.array([.1,.3,1,3,10,13,30,70,78,100,200,300])
rknots=np.array([.65,.95,1.05,1.08,1.,.98,.90,.82,.88,1.12,2.15,3.0])
mass=np.geomspace(.1,300,600)
radius=np.interp(np.log10(mass),np.log10(mknots),rknots)
fig,ax=plt.subplots(figsize=(8,5),dpi=100,facecolor='white')
fig.subplots_adjust(left=.1,right=.98,bottom=.14,top=.87)
ax.axvspan(.1,13,color='#ecf3fa')
ax.axvspan(13,78,color='#f8f1e5')
ax.axvspan(78,300,color='#edf6eb')
ax.semilogx(mass,radius,color='#233b63',linewidth=3,label='Qualitative mature sequence')
for m in [13,78]: ax.axvline(m,color='#888888',linestyle=':',linewidth=1)
ax.text(1.1,2.85,'Gas giants',ha='center',fontsize=11)
ax.text(31,2.85,'Brown dwarfs',ha='center',fontsize=11)
ax.text(156,2.85,'Low-mass\nstars',ha='center',fontsize=11)
ax.annotate('Deuterium-burning\nclassification scale',xy=(13,.98),xytext=(4.5,1.8),
            ha='center',fontsize=9,arrowprops={'arrowstyle':'->','color':'#666666'})
ax.annotate('Hydrogen-burning\nminimum mass',xy=(78,.88),xytext=(78,.32),
            ha='center',fontsize=9,arrowprops={'arrowstyle':'->','color':'#666666'})
examples=[(.7,1.35,'HD 209458 b',(0,16)),(.36,.73,'HD 149026 b',(-4,-25)),(22.,1.0,'CoRoT-3b',(0,15))]
for m,r,label,offset in examples:
    ax.scatter([m],[r],s=30,color='#b93a36',zorder=5)
    ax.annotate(label,xy=(m,r),xytext=offset,textcoords='offset points',ha='center',fontsize=9,color='#983331')
ax.set_xlim(.1,300)
ax.set_ylim(.1,3.3)
ax.set_xlabel(r'Mass $M/M_J$')
ax.set_ylabel(r'Radius $R/R_J$')
ax.set_title('Solar-composition mass–radius trends (schematic)')
ax.legend(loc='upper left',fontsize=9,frameon=False)
fig.savefig(Path.cwd()/'paper-315-mass-radius.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
