"""Original illustrative pressure-temperature branches; Python 3.14,
matplotlib 3.10.7 and NumPy 2.3.5. Output is relative to the current directory.
Eventual source: adjacent to paper-315.bigb; no file writes outside CWD.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

t0=1000.;alpha=.05
fig,axes=plt.subplots(1,2,figsize=(10,5),dpi=100,facecolor='white')
for ax,sign,p0 in zip(axes,(1,-1),(.01,1)):
    x=np.linspace(0,2,401)
    pressure=p0*np.exp(sign*x)
    temp=t0+(x/alpha)**2
    ax.plot(temp,pressure,color='#165a96',lw=2.7)
    ax.scatter([t0],[p0],color='#165a96',zorder=4)
    ax.set_yscale('log');ax.invert_yaxis()
    ax.set_xlim(900,2750)
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Pressure (bar; increasing downward)')
    ax.set_title('Outward cooling: α > 0' if sign==1 else 'Thermal inversion: α < 0')
    ax.grid(True,which='both',alpha=.22)
    ax.text(.04,.06,f'Assumed T₀ = 1000 K\n|α| = 0.05 K⁻¹ᐟ²\nP₀ = {p0:g} bar',
            transform=ax.transAxes,fontsize=10,bbox=dict(facecolor='white',edgecolor='.8'))
fig.suptitle('Local illustrative branches; not an observed planet',fontsize=13)
fig.subplots_adjust(left=.09,right=.98,bottom=.13,top=.83,wspace=.35)
out=Path('paper-315-pt-profile.png')
fig.savefig(out,dpi=100,facecolor='white',transparent=False)
plt.close(fig)
print(out.resolve())
