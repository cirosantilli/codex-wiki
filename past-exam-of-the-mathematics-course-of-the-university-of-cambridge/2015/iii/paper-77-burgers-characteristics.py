"""Python 3.14; NumPy 2.3.5 and Matplotlib 3.10.7. PNG output is cwd-only."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(8.4,3.8),dpi=100,facecolor='white')
zmax=2.5
ax=axes[0]
for theta0 in np.linspace(-2.2,-.15,9):
 z=np.linspace(0,min(zmax,-2*theta0),80);ax.plot(np.full_like(z,theta0),z,color='#3182bd',lw=1)
for theta0 in np.linspace(.15,2.2,9):
 z=np.linspace(0,min(zmax,2*theta0),80);ax.plot(theta0-z,z,color='#e6550d',lw=1)
z=np.linspace(0,zmax,100);ax.plot(-z/2,z,color='#111111',lw=2.5,label=r'Shock: $\theta=-UZ/2$')
ax.set(title=r'$U=1$: converging characteristics',xlim=(-2.4,2.4),ylim=(0,zmax));ax.legend(fontsize=8,loc='upper right')
ax=axes[1]
for theta0 in np.linspace(-2.2,-.15,8):ax.plot([theta0,theta0],[0,zmax],color='#3182bd',lw=1)
for theta0 in np.linspace(.15,2.2,8):ax.plot([theta0,theta0+zmax],[0,zmax],color='#e6550d',lw=1)
for slope in np.linspace(0,1,9):ax.plot(slope*z,z,color='#238b45',lw=1.2)
ax.fill_betweenx(z,0,z,color='#74c476',alpha=.13)
ax.set(title=r'$U=-1$: expanding rarefaction fan',xlim=(-2.4,3.6),ylim=(0,zmax));ax.text(.72,1.9,r'$f=-\theta/Z$',color='#006d2c',fontsize=10,bbox=dict(facecolor='white',edgecolor='none',pad=2))
for ax in axes:ax.set(xlabel=r'Phase coordinate $\theta$',ylabel=r'Propagation coordinate $Z$');ax.grid(alpha=.15)
fig.tight_layout();fig.savefig('paper-77-burgers-characteristics.png',facecolor='white',transparent=False)
