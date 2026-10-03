"""Generate paper-118-radial-metric.png in the current working directory.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5;
uses the repository pyproject.toml dependencies. Cache location is set by caller.
"""
import numpy as np
import matplotlib.pyplot as plt
s=np.geomspace(.1,10,400)
a=1.
tangential=np.sqrt(s*s+a*a)/s
radial=1/tangential
fig,ax=plt.subplots(figsize=(6.4,3.6),layout='constrained')
ax.loglog(s,tangential,label='Tangential eigenvalue / Euclidean',color='#1764a6',linewidth=2)
ax.loglog(s,radial,label='Radial eigenvalue / Euclidean',color='#ac4c12',linewidth=2)
ax.axhline(1,color='#555555',linestyle=':',linewidth=1,label='Product = 1 (same volume)')
ax.set_xlabel(r'$s=|z_1|^2+|z_2|^2$  ($a=1$)')
ax.set_ylabel('Relative metric eigenvalue')
ax.set_title('Compensating stretches preserve the volume',fontsize=12)
ax.set_xlim(.1,10);ax.set_ylim(.08,13);ax.grid(alpha=.15)
ax.legend(fontsize=8,loc='upper right')
fig.savefig('paper-118-radial-metric.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
