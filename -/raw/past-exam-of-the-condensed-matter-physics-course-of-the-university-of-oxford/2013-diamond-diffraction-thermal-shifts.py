"""Original diffraction thermometry illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,2,figsize=(12.1,4.5),layout='constrained',facecolor='white')
for ax,psi,label in zip(axs,[22.8,37.6],['111','220']):
 shifted=np.degrees(2*np.arcsin(np.sin(np.radians(psi/2))/1.0018));x=np.linspace(psi-.15,psi+.1,1000);width=.009
 ax.plot(x,np.exp(-.5*((x-psi)/width)**2),color='#2563eb',lw=2.2,label='300 K reference')
 ax.plot(x,np.exp(-.5*((x-shifted)/width)**2),color='#dc2626',lw=2.2,label='900 K model')
 ax.annotate('',xy=(psi,1.05),xytext=(shifted,1.05),arrowprops=dict(arrowstyle='<->',lw=1.5,color='#475569'))
 ax.text((psi+shifted)/2,1.10,f'Shift = {shifted-psi:.4f}°',ha='center',fontsize=10)
 ax.set(title=f'Powder family {{{label}}}',xlabel='Total scattering angle 2θ (degrees)',ylabel='Separately normalized illustrative intensity',xlim=(psi-.15,psi+.1),ylim=(0,1.25));ax.legend(fontsize=9,loc='upper right');ax.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
