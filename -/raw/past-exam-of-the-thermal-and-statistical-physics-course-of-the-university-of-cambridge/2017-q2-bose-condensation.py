"""Uniform three-dimensional ideal Bose gas fractions; Python 3.14, numpy, matplotlib.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

T=np.linspace(0,1.6,600)
f0=np.maximum(1-T**1.5,0)
fig,ax=plt.subplots(figsize=(6.7,4.3),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.plot(T,f0,color='#165b99',lw=2,label=r'Ground state: $N_0/N$')
ax.plot(T,1-f0,color='#cc7a1d',lw=2,label=r'Excited states: $N_{\rm ex}/N$')
ax.axvline(1,color='#777777',lw=1,ls='--')
ax.text(.45,.84,r'$1-(T/T_c)^{3/2}$',color='#165b99',fontsize=12)
ax.text(1.025,.5,r'$T_c$',fontsize=12)
ax.set(xlim=(0,1.6),ylim=(-.03,1.08),xlabel=r'$T/T_c$',ylabel='Particle fraction',title='Condensation in a uniform three-dimensional ideal gas')
ax.legend(loc='upper center',fontsize=9)
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
