"""Original qualitative CMB source sketch; no data or numerical cosmology fit.
Tested: Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Output: paper-59-cmb-components.png in caller CWD. Preserve caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ell=np.geomspace(2,2200,2000)
damping=np.exp(-(ell/1650)**1.6)
density=.22/(1+(ell/70)**2)
doppler=np.zeros_like(ell)
for center,height in [(220,1.0),(540,.65),(840,.72),(1140,.43),(1440,.4),(1740,.3)]:
    density+=height*np.exp(-.5*((ell-center)/(26+.045*center))**2)
for center,height in [(135,.52),(400,.66),(695,.56),(995,.5),(1295,.43),(1595,.32)]:
    doppler+=height*np.exp(-.5*((ell-center)/(35+.06*center))**2)
density*=damping;doppler*=damping
grav=.55/(1+(ell/65)**2)+.25*np.exp(-ell/12)+.16*np.exp(-.5*((ell-190)/85)**2)
fig,ax=plt.subplots(figsize=(8.8,4.65),dpi=135,facecolor='white')
ax.semilogx(ell,density,color='#b52d36',lw=2.2,label='Emission density / temperature')
ax.semilogx(ell,doppler,color='#23834d',lw=2.2,label='Doppler velocity')
ax.semilogx(ell,grav,color='#235aab',lw=2.2,label='Gravitational source')
ax.set_xlim(2,2200);ax.set_ylim(0,1.12);ax.set_yticks([])
ax.set_xticks([2,20,100,200,500,1000,2000]);ax.set_xticklabels(['2','20','100','200','500','1000','2000'])
ax.set_xlabel(r'Multipole $\ell$  (large angles at left)')
ax.set_ylabel(r'Schematic $\ell(\ell+1)C_\ell/(2\pi)$, arbitrary units')
ax.set_title('Qualitative CMB source contributions')
ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=9,framealpha=.94)
fig.text(.5,.025,'Source auto-powers only; correlated cross terms are omitted. Peak positions are illustrative.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.07,1,1]);fig.savefig('paper-59-cmb-components.png',facecolor='white',transparent=False);plt.close(fig)
