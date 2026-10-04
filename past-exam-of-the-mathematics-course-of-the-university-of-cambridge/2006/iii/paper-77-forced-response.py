"""Original causal response sketch: Python 3.14 / NumPy 2.3.5 / matplotlib 3.10.7.
Writes paper-77-forced-response.png to caller CWD; honors MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# An illustrative even compact forcing; the physical fields are its real parts.
a,c,T,time=1.,.1,80.,320.
x=np.linspace(-36,36,1801);r=np.linspace(-a,a,1001)
profile=np.cos(np.pi*r/(2*a))**2;area=np.trapezoid(profile,r)
lag=np.abs(r[None,:]-x[:,None])/c
retarded=time-lag;ramp=np.where(retarded>0,1-np.exp(-np.maximum(retarded,0)/T),0.)
values=profile[None,:]*ramp
Iplus=np.trapezoid(np.where(r[None,:]>=x[:,None],values,0.),r,axis=1)/c
Iminus=np.trapezoid(np.where(r[None,:]<=x[:,None],values,0.),r,axis=1)/c
U=(Iplus+Iminus)/2;H=(Iplus-Iminus)/2
fig,axes=plt.subplots(2,1,figsize=(7.2,5.5),dpi=150,sharex=True,facecolor='white')
axes[0].plot(x,2*c*U/area,color='#286a9b',lw=2)
axes[1].plot(x,2*c*H/area,color='#a95128',lw=2)
for ax in axes:
 ax.axvspan(-a,a,color='#e8e8e8',label='forcing region')
 ax.axvline(-(c*time+a),ls='--',color='#777',lw=1);ax.axvline(c*time+a,ls='--',color='#777',lw=1)
 ax.axhline(0,color='#aaa',lw=.8);ax.grid(alpha=.15);ax.set_xlim(-36,36)
axes[0].set_ylabel('Normalized streamfunction amplitude')
axes[1].set_ylabel('Normalized buoyancy amplitude');axes[1].set_xlabel('Horizontal position x')
axes[0].set_title('Even compact forcing: broad causal streamfunction response')
axes[1].set_title('Buoyancy changes sign across the forcing region')
axes[0].legend(loc='upper right',fontsize=8)
fig.tight_layout();fig.savefig(Path('paper-77-forced-response.png'),facecolor='white',transparent=False);plt.close(fig)
