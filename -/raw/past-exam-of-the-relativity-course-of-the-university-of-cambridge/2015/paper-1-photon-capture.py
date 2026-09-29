"""Original educational diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Save the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.4),layout='constrained')
b=4.8
r=np.linspace(2,14,700);barrier=(1-2/r)/r**2
axs[0].plot(r,barrier,color='#2563a6',lw=2,label=r'$\mu^2W=(1-2\mu/r)(\mu/r)^2$')
axs[0].axhline(1/b**2,color='#b44b36',label=r'Captured: $b/\mu=4.8$')
axs[0].axhline(1/27,color='.45',ls='--',label=r'Critical: $b/\mu=3\sqrt{3}$')
axs[0].axvline(3,color='.5',ls=':');axs[0].set(xlabel=r'$r/\mu$',ylabel='Dimensionless radial barrier',ylim=(0,.05),title='Photon-sphere barrier')
axs[0].legend(fontsize=8,loc='upper right');axs[0].grid(alpha=.2)
# Integrate azimuth as a function of increasing inverse radius; no horizon singularity.
u=np.concatenate([np.linspace(.028,.6,15000),np.geomspace(.60001,1e6,18000)])
f=1/np.sqrt(1/b**2-u*u+2*u**3)
p=np.r_[0,np.cumsum(np.diff(u)*(f[:-1]+f[1:])/2)]
r=1/u;x=r*np.cos(p);y=r*np.sin(p)
ax=axs[1];outside=r>=2
ax.plot(x[outside],y[outside],color='#2563a6',lw=2)
ax.plot(x[~outside],y[~outside],color='#b44b36',lw=2)
t=np.linspace(0,2*np.pi,600)
ax.fill(2*np.cos(t),2*np.sin(t),color='.9',zorder=0)
ax.plot(2*np.cos(t),2*np.sin(t),color='.35',ls='--',lw=1,label=r'Horizon $r=2\mu$')
ax.plot(3*np.cos(t),3*np.sin(t),color='.5',ls=':',lw=1,label=r'Photon sphere $r=3\mu$')
ax.scatter([0],[0],color='black',s=18,zorder=5)
for j in [500,5000,16000]:
 if abs(x[j])<13 and abs(y[j])<9:ax.annotate('',xy=(x[j+70],y[j+70]),xytext=(x[j],y[j]),arrowprops={'arrowstyle':'->','color':'#2563a6'})
ax.set(xlim=(-5,14),ylim=(-6,9),xlabel=r'$r\cos\phi/\mu$',ylabel=r'$r\sin\phi/\mu$',title='Captured ray: coordinate projection')
ax.set_aspect('equal');ax.legend(fontsize=8,loc='lower right');ax.grid(alpha=.15)
fig.savefig('paper-1-photon-capture.png',dpi=165)
