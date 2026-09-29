"""Python 3.14; numpy 2.3; matplotlib 3.10. Writes its PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
q,w=np.polynomial.legendre.leggauss(240)
R=(q+1)/2;weights=w/2
t=np.linspace(1.00001,4,600)
r=(R[None,:]**3+t[:,None]**3-1)**(1/3)
ec=4*np.pi*((R[None,:]**6/r**4+2*r*r)@weights)
eh=4*np.pi/3*(3*t*t+(t**3-1)**2)
fig,ax=plt.subplots(figsize=(7,4),layout='constrained',facecolor='white')
ax.semilogy(t,ec/(8*np.pi*t*t),label='cavitating competitor',color='#1767a3',lw=2)
ax.semilogy(t,eh/(8*np.pi*t*t),label='homogeneous dilation',color='#c46c00',lw=2)
ax.axhline(1,color='gray',ls='--',label='large-t cavity limit')
ax.set(xlabel='boundary dilation t',ylabel=r'$E/(8\pi t^2)$',xlim=(1,4))
ax.grid(alpha=.18);ax.legend(frameon=False)
fig.savefig(Path.cwd()/'2010-cavitation-energy.png',dpi=150,facecolor='white')
