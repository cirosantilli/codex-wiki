"""Original timelike-geodesic velocity sketch, Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes same-basename opaque PNG to caller CWD, honoring MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
E=2.;a=np.sqrt(E*E-1);x=np.linspace(-a,a,900)
vtau=np.sqrt(np.maximum(0,a*a-x*x));vt=(1+x*x)*vtau/E
fig,ax=plt.subplots(figsize=(6.4,4.0),dpi=120,facecolor='white')
for sign in [1,-1]:
 ax.plot(x,sign*vtau,color='#136c9b',label=r'$dx/d\tau$' if sign==1 else None)
 ax.plot(x,sign*vt,color='#b15c22',ls='--',label=r'$dx/dt$' if sign==1 else None)
ax.axhline(0,color='#777777',linewidth=.7);ax.axvline(0,color='#777777',linewidth=.7)
ax.set(xlabel='$x$',ylabel='velocity',title=r'Two legs of a timelike orbit: $E=2$, $a=\sqrt{3}$')
ax.set_xticks([-a,-1,0,1,a],labels=[r'$-a$','$-1$','$0$','$1$','$a$'])
ax.legend(fontsize=11);ax.spines[['top','right']].set_visible(False);fig.tight_layout()
fig.savefig('paper-1-geodesic-speeds.png',facecolor='white',transparent=False);plt.close(fig)
