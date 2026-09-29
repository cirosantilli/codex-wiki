"""Compare two binary-crystal powder patterns in the f=Z approximation. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'figure.facecolor':'white'})
ns=np.array([3,4,8,11,12,16])
mult=np.array([8,6,12,24,8,6])
labels=['111','200','220','311','222','400']
h=6.62607015e-34
c=299792458.
wave=h*c/(8000*1.602176634e-19)
fig,axes=plt.subplots(2,1,figsize=(9.5,6.7),sharex=True,layout='constrained')
for ax,Z,a,title,color in zip(axes,[31,13],[5.653e-10,5.660e-10],['GaAs','AlAs'],['#245fa0','#ad4828']):
    angles=np.degrees(2*np.arcsin(wave*np.sqrt(ns)/(2*a)))
    squares=np.array([Z*Z+33**2,(Z-33)**2,(Z+33)**2,Z*Z+33**2,(Z-33)**2,(Z+33)**2])
    intensity=mult*squares
    intensity=100*intensity/intensity[0]
    ax.vlines(angles,.025,intensity,color=color,lw=2.5)
    ax.scatter(angles,intensity,color=color,s=25,zorder=3)
    for x,y,label in zip(angles,intensity,labels):
        ax.annotate(label,(x,y),xytext=(0,7),textcoords='offset points',ha='center',fontsize=11)
    ax.set_yscale('log');ax.set_ylim(.025,650)
    ax.set_ylabel('Relative intensity\n(111 = 100)')
    ax.set_title(title,loc='left',fontweight='bold',color=color)
    ax.grid(axis='y',alpha=.2)
axes[-1].set_xlabel(r'Scattering angle $2\theta$ (degrees)')
axes[-1].set_xlim(24,70)
fig.suptitle('Binary-sublattice contrast in six powder reflections',fontsize=16)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
