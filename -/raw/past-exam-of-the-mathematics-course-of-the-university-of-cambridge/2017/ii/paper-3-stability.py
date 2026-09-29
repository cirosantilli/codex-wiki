"""2017 II3 Q12. Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.
Run from the desired output directory; writes an opaque PNG to CWD.
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/2017-ii-paper-3-mplconfig")
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(11,5.5),dpi=100,facecolor='white')
k=np.linspace(.001,.999,2500);cap=5.;upper=np.full_like(k,cap);mask=k>2/3;upper[mask]=np.minimum(cap,k[mask]**2/(3*k[mask]-2))
ax.fill_between(k,k,upper,color='#c5e9df',label='Strict linear-stability region')
ax.plot(k,k,color='#1e537a',label='Extinction boundary: μ = k')
kk=np.linspace(2/3+.005,.999,1800);uu=kk**2/(3*kk-2);ax.plot(kk,uu,color='#a34a35',label='Flip boundary: μ = k²/(3k − 2)')
ax.axvline(2/3,color='.6',ls=':',lw=1);ax.text(.14,2.8,'Stable population',fontsize=13);ax.text(.65,.15,'Extinction',fontsize=12);ax.text(.87,3.2,'Unstable\npositive state',ha='center',fontsize=11)
ax.set(xlim=(0,1),ylim=(0,cap),xlabel='Adult mortality fraction k',ylabel='Larvae produced per adult μ',title='Adult–larval model: strict linear stability of the positive equilibrium')
ax.legend(loc='upper left');ax.grid(alpha=.15);fig.tight_layout();fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False);plt.close(fig)
