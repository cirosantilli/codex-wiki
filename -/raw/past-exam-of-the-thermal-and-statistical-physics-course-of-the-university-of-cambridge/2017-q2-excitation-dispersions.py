"""Rescaled low-momentum dispersion comparison; Python 3.14, numpy, matplotlib.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

k=np.linspace(0,1,400)
fig,ax=plt.subplots(figsize=(6.8,4.3),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.plot(k,k,color='#165b99',lw=2,label=r'Acoustic phonon: $\epsilon\propto k$')
ax.plot(k,k*k,color='#cc7a1d',lw=2,label=r'Gapless ferromagnetic magnon: $\epsilon\propto k^2$')
ax.text(.13,.48,r'3D: $D(\epsilon)\propto\epsilon^2$'+'\n'+r'$C_V\propto T^3$',color='#165b99',fontsize=11)
ax.text(.57,.13,r'3D: $D(\epsilon)\propto\sqrt{\epsilon}$'+'\n'+r'$C_V\propto T^{3/2}$',color='#a45d10',fontsize=11)
ax.set(xlim=(0,1),ylim=(0,1.08),xlabel='Rescaled wavenumber',ylabel='Rescaled excitation energy',title='Dispersion determines low-temperature state counting')
ax.legend(loc='upper left',fontsize=8)
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
