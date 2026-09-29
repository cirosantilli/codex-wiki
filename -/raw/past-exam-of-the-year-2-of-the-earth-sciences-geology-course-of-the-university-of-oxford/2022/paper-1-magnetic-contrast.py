"""Original mathematical solution diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes its PNG to the current working directory; no source images are copied.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10})

I=np.arctan(2*np.tan(np.deg2rad(20)));x=np.linspace(-4,4,1001);d=1
f=(3*(x*np.cos(I)-d*np.sin(I))**2-(x*x+d*d))/(x*x+d*d)**2.5
f=f/np.max(np.abs(f))
fig,ax=plt.subplots(figsize=(7.1,3.3),dpi=100)
ax.axhline(0,color='#9da9af',lw=.8)
ax.plot(x,f,color='#b34c27',lw=2,label='positive induced magnetization contrast')
ax.plot(x,-f,color='#177ca4',lw=2,label='negative contrast: weak replacement / missing host')
ax.set(xlim=(-4,4),ylim=(-1.18,1.18),xlabel='South ← northing / dipole depth → North',
       ylabel='Normalized total-field anomaly')
ax.grid(color='#e6ebee',lw=.6)
ax.set_title(f'Illustrative induced dipole, inclination {np.rad2deg(I):.1f}°',fontsize=11)
ax.legend(frameon=False,fontsize=9,loc='upper right')
fig.tight_layout(pad=1.1)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
