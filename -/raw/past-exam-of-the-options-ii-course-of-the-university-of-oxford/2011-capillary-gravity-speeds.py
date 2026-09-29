#!/usr/bin/env python3
"""Deep-water gravity-capillary speeds; Python 3.14, NumPy/Matplotlib.
Run from the desired PNG output directory. Dependencies: wiki pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
q=np.linspace(0.13,3.0,800)
c=np.sqrt(1/q+q)
cg=(1+3*q*q)/(2*np.sqrt(q+q**3))
fig,ax=plt.subplots(figsize=(7.6,4.6),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.plot(q,c,color='#2266aa',lw=2.4,label=r'Phase speed $c=\omega/k$')
ax.plot(q,cg,color='#b85c20',lw=2.4,label=r'Group speed $c_g=d\omega/dk$')
ax.axvline(1,color='0.5',ls=':',lw=1.2)
ax.scatter([1],[np.sqrt(2)],s=40,color='black',zorder=3)
ax.annotate(r'$c_g=c$; minimum $c$',(1,np.sqrt(2)),xytext=(1.37,0.89),arrowprops={'arrowstyle':'->','color':'0.25'},fontsize=10)
ax.text(.21,2.85,r'Gravity dominated: $c_g<c$',fontsize=10,color='#5a4c3d')
ax.text(1.6,2.85,r'Capillary dominated: $c_g>c$',fontsize=10,color='#5a4c3d')
ax.set(xlim=(.13,3),ylim=(.55,3.15),xlabel=r'Dimensionless wavenumber $q=k/\sqrt{\rho g/T}$',ylabel=r'Speed in units of $(gT/\rho)^{1/4}$',title='Deep-water gravity-capillary waves')
ax.grid(alpha=.18)
ax.legend(loc='lower right',frameon=True,facecolor='white')
fig.savefig(Path.cwd()/'2011-capillary-gravity-speeds.png',dpi=160,facecolor='white')
