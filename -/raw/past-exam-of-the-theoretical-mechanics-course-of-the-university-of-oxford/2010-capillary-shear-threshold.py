"""Python 3.14; numpy 2.3; matplotlib 3.10. Output is written to the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7,4),layout='constrained',facecolor='white')
r=1.2
for sign in [-1,1]:
    q=np.linspace(.035,4.2,900);v=np.sqrt((q+1/q)/2)
    ax.plot(sign*q,v,color='#1767a3',lw=2,label='threshold' if sign==1 else None)
    ax.fill_between(sign*q,v,r,where=v<r,color='#c46c00',alpha=.25,label='unstable band' if sign==1 else None)
ax.axhline(r,color='#c46c00',ls='--',label='sample velocity jump')
ax.axvline(0,color='gray',ls=':',lw=.8)
ax.plot([-1,1],[1,1],'o',color='#1767a3')
ax.set(xlabel=r'$k/k_*$',ylabel=r'$U_*(k)/U_{\min}$',xlim=(-4.2,4.2),ylim=(.75,2.3))
ax.grid(alpha=.18);ax.legend(frameon=False)
fig.savefig(Path.cwd()/'2010-capillary-shear-threshold.png',dpi=150,facecolor='white')
