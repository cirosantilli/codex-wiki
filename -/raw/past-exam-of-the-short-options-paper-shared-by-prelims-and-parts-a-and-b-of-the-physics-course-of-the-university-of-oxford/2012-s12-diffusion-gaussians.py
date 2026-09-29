"""Original Gaussian diffusion profiles. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes only the matching opaque PNG in CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-7,7,700)
fig,ax=plt.subplots(figsize=(6.6,3.6),layout='constrained',facecolor='white')
for t in [.5,1,2]:ax.plot(x,np.exp(-x*x/(4*t))/np.sqrt(4*np.pi*t),lw=2,label=fr'$t={t:g}$, variance $={2*t:g}$')
ax.set(xlabel='Position x (D = 1, N = 1)',ylabel='Particle density C(x,t)',xlim=(-7,7),ylim=(0,.43));ax.legend();ax.grid(alpha=.22)
fig.savefig('2012-s12-diffusion-gaussians.png',dpi=150,facecolor='white',metadata={'Software':'Matplotlib'})
