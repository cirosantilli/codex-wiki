"""Original solution diagram. Python 3.14, NumPy and Matplotlib.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, wedge, save
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
def coeff(E,V=1,a=1):
 k=np.sqrt(E+0j);q=np.sqrt(E-V+0j)
 M=np.array([[1,-1,-1,0],[-k,-q,q,0],[0,np.exp(1j*q*a),np.exp(-1j*q*a),-np.exp(1j*k*a)],[0,q*np.exp(1j*q*a),-q*np.exp(-1j*q*a),-k*np.exp(1j*k*a)]],complex)
 B,C,D,F=np.linalg.solve(M,np.array([-1,-k,0,0],complex))
 return k,q,B,C,D,F
fig,axes=plt.subplots(1,2,figsize=(10,3.7),sharey=True)
for ax,E in zip(axes,[.4,8.]):
 k,q,B,C,D,F=coeff(E)
 x=np.linspace(-4,5,1400);psi=np.where(x<0,np.exp(1j*k*x)+B*np.exp(-1j*k*x),np.where(x>1,F*np.exp(1j*k*x),C*np.exp(1j*q*x)+D*np.exp(-1j*q*x)))
 ax.axvspan(0,1,color='0.9');ax.plot(x,psi.real,label=r'$\mathrm{Re}\,\psi$');ax.plot(x,psi.imag,ls='--',label=r'$\mathrm{Im}\,\psi$')
 ax.set(xlabel=r'$x$ (units with $\hbar^2/(2m)=V_0=1$)',title=rf'$E/V_0={E:g}$, $P={abs(F)**2:.3f}$',ylim=(-2,2))
 ax.spines[['right','top']].set_visible(False)
axes[0].set_ylabel('Wavefunction amplitude');axes[1].legend(frameon=False,loc='upper right')
fig.tight_layout();save(fig,'paper-3-barrier.png')
