"""Original educational figure. Python3.14, NumPy2.3.5, Matplotlib3.10.7.
PNG basename is written in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
t=np.linspace(-np.pi,np.pi,700)
fig,ax=plt.subplots(figsize=(7.3,4.5),layout='constrained')
for lam,label in [(.45,'Below threshold'),(1.,'At threshold'),(1.8,'Above threshold')]:
 # lambda=a^2 omega^2/(2gl); subtract the downward-state potential.
 V=-np.cos(t)+lam/2*np.cos(t)**2-(-1+lam/2)
 ax.plot(t,V,lw=2,label=label+rf': $\lambda={lam:g}$')
 if lam>1:
  q=np.arccos(1/lam);v=-np.cos(q)+lam/2*np.cos(q)**2-(-1+lam/2)
  ax.scatter([-q,q],[v,v],s=25,color='#258a62',zorder=5)
ax.axhline(0,color='.5',lw=.7)
ax.set(xlabel=r'Slow angle $\Theta$ (radians)',ylabel=r'$[V_{\rm eff}(\Theta)-V_{\rm eff}(0)]/(mgl)$',title=r'Horizontal support vibration: $\lambda=a^2\omega^2/(2gl)$')
ax.legend(fontsize=9);ax.grid(alpha=.2)
fig.savefig('paper-1-horizontal-pendulum.png',dpi=160)
