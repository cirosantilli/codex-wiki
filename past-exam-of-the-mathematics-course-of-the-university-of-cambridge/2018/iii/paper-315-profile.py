"""Supplied atmospheric profile; Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes an opaque 600 x 480 PNG into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

pressure=np.geomspace(1e-5,10,600)
temperature=np.where(pressure<=.01,500.,np.where(pressure>=1.,1400.,1400.+450.*np.log10(pressure)))
fig,ax=plt.subplots(figsize=(6,4.8),dpi=100,facecolor='white')
fig.subplots_adjust(left=.15,right=.96,bottom=.13,top=.9)
ax.semilogy(temperature,pressure,color='#235e9d',linewidth=3)
for p in [.01,1.]: ax.axhline(p,color='#888888',linestyle=':',linewidth=1)
ax.scatter([500,1400],[.01,1],color='#235e9d',s=25,zorder=5)
ax.text(570,1.2e-4,'500 K isothermal',fontsize=10)
ax.text(750,.25,'450 K per\npressure decade',ha='center',fontsize=10)
ax.text(1160,4.,'1400 K\nisothermal',ha='center',fontsize=10)
ax.set_ylim(10,1e-5)
ax.set_xlim(400,1500)
ax.set_xlabel('Temperature T (K)')
ax.set_ylabel('Pressure P (bar)')
ax.set_title('Atmospheric pressure–temperature profile')
ax.grid(axis='x',alpha=.15)
fig.savefig(Path.cwd()/'paper-315-profile.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
