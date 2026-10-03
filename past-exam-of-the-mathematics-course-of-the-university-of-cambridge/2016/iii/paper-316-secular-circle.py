import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,axes=plt.subplots(1,2,figsize=(7.2,3.6),dpi=100)
u=np.linspace(0,1,9)
for ax,growing in zip(axes,[False,True]):
 ph=np.linspace(0,2*np.pi,400);ax.plot(1-np.cos(ph),-np.sin(ph),color='gray',alpha=.6)
 phase=np.pi*u*u if growing else 2*np.pi*u
 z=1-np.exp(1j*phase)
 ax.scatter(z.real,z.imag,c=u,cmap='viridis',s=38,zorder=4)
 for k in [0,2,4,6,8]:
  ax.annotate(f'{u[k]:.2f}',(z.real[k],z.imag[k]),xytext=(5,5 if k!=8 else -13),textcoords='offset points',fontsize=8)
 ax.scatter([1],[0],marker='+',s=60,color='black');ax.text(1.05,.07,r'$z_f$')
 ax.axhline(0,color='gray',lw=.5);ax.axvline(0,color='gray',lw=.5)
 ax.set(xlabel=r'Re$(z/z_f)$',ylabel=r'Im$(z/z_f)$',xlim=(-.2,2.35),ylim=(-1.3,1.3),title='Growing mass: half circuit' if growing else 'Fixed mass: full circuit')
 ax.set_aspect('equal')
fig.suptitle(r'Equal-time samples labelled $t/t_p$; $z_f$ placed on the real axis',fontsize=10)
fig.tight_layout();fig.savefig('paper-316-secular-circle.png',facecolor='white',transparent=False)
