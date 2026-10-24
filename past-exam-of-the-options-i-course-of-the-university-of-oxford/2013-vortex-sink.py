"""Original diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run with CWD the matching _media directory; output is relative to CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
angle=np.linspace(0,12,1800)
r=np.exp(-angle/2)  # Gamma/Q=4: theta=2 log(a/r).
z=r*np.exp(1j*angle)
fig,ax=plt.subplots(figsize=(6.4,5.5),layout='constrained',facecolor='white')
for sign,color in [(1,'#176aa5'),(-1,'#bc5227')]:
 w=sign*z;ax.plot(w.real,w.imag,color=color,lw=1.8)
 ax.plot(w[0].real,w[0].imag,'o',color=color,ms=6)
 for v in [.7,2.7,5.0]:
  p=sign*np.exp(-v/2+1j*v);q=sign*np.exp(-(v+.14)/2+1j*(v+.14))
  ax.annotate('',xy=(q.real,q.imag),xytext=(p.real,p.imag),arrowprops=dict(arrowstyle='->',color=color,lw=1.6))
ax.scatter([0],[0],c='black',s=28,zorder=5);ax.annotate('sink / capture',(0,0),(.18,-.46),arrowprops=dict(arrowstyle='-',color='black'))
ax.axhline(0,color='#bbbbbb',lw=.7,zorder=0);ax.axvline(0,color='#bbbbbb',lw=.7,zorder=0)
ax.set(xlim=(-1.1,1.1),ylim=(-.8,.8),xlabel=r'$\mathrm{Re}\,z/a$',ylabel=r'$\mathrm{Im}\,z/a$')
ax.set_aspect('equal');ax.set_title(r'Equal vortices and a central sink: $\Gamma/Q=4$')
fig.suptitle(r'$r^2/a^2=1-t/t_*,\quad t_*=\pi a^2/Q$',fontsize=12)
ax.spines[['top','right']].set_visible(False)
fig.savefig('2013-vortex-sink.png',dpi=120,facecolor='white')
