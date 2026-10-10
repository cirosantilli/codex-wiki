"""Original cold-plasma ramp/virtual-height model. Python 3.14; numpy/matplotlib.

Run from _media; writes basename.png to CWD. Stipulated profile:
fp(z) = 3 MHz sqrt((z-70 km)/(30 km)). Vertical geometrical-ray delay,
with frequency-independent turning phase. No measured ionospheric data.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.8, 4.6), layout='constrained')
z = np.linspace(70, 99.85, 600)
n = np.sqrt(1-(z-70)/30)
ax.plot(n,z,color='#216a9d',lw=2.3,label='Phase index $n$')
ax.plot(1/n,z,color='#b54b20',lw=2.3,label='Group index $n_g=1/n$')
ax.plot([1,1],[0,70],color='#777777',lw=1.5)
ax.scatter([0],[100],color='#216a9d',s=22,zorder=4)
ax.axhline(70,ls=':',color='#777777',lw=1)
ax.axhline(100,ls='--',color='#555555',lw=1)
ax.text(2.3,72,'Ramp begins: 70 km',fontsize=9)
ax.text(1.3,103,r'Turning region: $n\to0$, $n_g\to\infty$',fontsize=9)
ax.text(2.3,33,'Below ramp: $n=n_g=1$',fontsize=9)
ax.set(xlim=(-0.15,5),ylim=(0,115),xlabel='Refractive index (dimensionless)',ylabel='Altitude (km)')
ax.set_title('Local response at $f=3$ MHz',fontweight='bold')
ax.legend(loc='upper left',bbox_to_anchor=(0.12,0.62),frameon=False,fontsize=9)
ax.grid(alpha=.15)

f=np.linspace(1,4,400)
turn=70+30*(f/3)**2
virtual=70+60*(f/3)**2
bx.plot(f,turn,color='#216a9d',lw=2.3,label='Real turning height $z_t$')
bx.plot(f,virtual,color='#b54b20',lw=2.3,label="Virtual height $h'=c\\tau_g/2$")
bx.axvline(3,color='#777777',lw=1,ls=':')
bx.scatter([3,3],[100,130],color=['#216a9d','#b54b20'],s=30,zorder=4)
bx.annotate('100 km',(3,100),xytext=(3.17,91),fontsize=9,color='#216a9d')
bx.annotate('130 km',(3,130),xytext=(2.05,143),fontsize=9,color='#b54b20',arrowprops={'arrowstyle':'->','color':'#b54b20'})
bx.set(xlim=(1,4),ylim=(65,190),xlabel='Probing frequency (MHz)',ylabel='Height (km)')
bx.set_title('Turning height versus delay height',fontweight='bold')
bx.legend(loc='upper left',fontsize=9,frameon=False)
bx.text(1.13,119,"$h'-z_t=u_t$\nExtra delay within the ramp",fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
bx.grid(alpha=.15)
for axis in (ax,bx):axis.spines[['top','right']].set_visible(False)
fig.supxlabel('Illustrative linear density ramp; vertical propagation, no magnetic field or collisions', fontsize=10)
fig.savefig(Path(__file__).stem + '.png',dpi=120,facecolor='white',transparent=False)
