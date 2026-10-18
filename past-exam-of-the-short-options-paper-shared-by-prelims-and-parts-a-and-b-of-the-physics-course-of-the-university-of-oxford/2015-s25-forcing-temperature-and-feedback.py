"""Original climate-model diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,2,figsize=(12.8,5),layout='constrained',facecolor='white')
a=axs[0];ang=np.linspace(0,2*np.pi,500);u=1+.5*np.cos(ang);v=1+.5*np.sin(ang);a.fill(u,v,color='#dbeafe',alpha=.8);a.plot(u,v,color='#2563eb',lw=2);a.plot(1,1,'o',color='#2563eb');a.axhline(1,color='#94a3b8',ls=':',lw=1);a.axvline(1,color='#94a3b8',ls=':',lw=1)
ms=np.roots([.75,-2,.75]);xx=np.linspace(0,1.65,500)
for m in sorted(ms):a.plot(xx,m*xx,color='#dc2626',ls='--',lw=1.6)
a.plot(xx,xx,color='#475569',lw=1,label='Central ratio = 1');a.set(xlim=(0,1.65),ylim=(0,1.65),xlabel=r'Normalized cooling-forcing magnitude $f/f_0$',ylabel=r'Normalized cooling magnitude $x/x_0$',title='Independent uncertainties and ratio tangents');a.set_aspect('equal');a.text(.1,1.5,'Ellipse: unit covariance radius\nRatio slopes: 0.451 and 2.215',fontsize=10);a.legend(loc='lower right',fontsize=9)
b=axs[1];t=np.linspace(0,30,600);R=1.5*t-.05*t*t;lo=t<=15;b.plot(t[lo],R[lo],lw=2.5,color='#2563eb',label='Stable branch');b.plot(t[~lo],R[~lo],lw=2.5,color='#dc2626',ls='--',label='Unstable branch');b.axhline(7.5,color='#475569',lw=1.4,label='Quadrupling forcing: 7.5');roots=np.roots([.05,-1.5,7.5]);b.scatter(roots,[7.5,7.5],color='#475569',zorder=4);b.scatter([15],[11.25],color='#7c3aed',zorder=4);b.annotate('Fold: 15 K, 11.25 W/m²',xy=(15,11.25),xytext=(9,12.1),arrowprops=dict(arrowstyle='->'),fontsize=10);b.set(xlim=(0,30),ylim=(0,13),xlabel='Warming (K)',ylabel='Restoring flux (W/m²)',title='Assumed quadratic feedback model');b.legend(loc='lower center',fontsize=9);b.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
