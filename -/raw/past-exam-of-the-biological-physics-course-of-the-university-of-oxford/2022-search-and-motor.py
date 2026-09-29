"""Original model curves; Python 3.14, numpy 2.3.5, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), layout='constrained')
u=np.logspace(-1, 1, 400)
a=axes[0]
a.plot(u, (u+1/u)/2, label='total', lw=2)
a.plot(u, 1/(2*u), '--', label='3D contribution')
a.plot(u, u/2, ':', label='1D contribution')
a.plot(1,1,'ko')
a.set(xscale='log', xlabel=r'$\lambda/\lambda_*$', ylabel=r'$\tau/\tau_{\min}$', title='Balanced search optimum', ylim=(0,5.2))
a.legend(fontsize=8)
x1=.3;k1=4.;k2=1.;v=.025;B0=k1/(k1+k2)
x=np.linspace(0,1,1600)
A=np.exp(-(k1+k2)*x1/v);Q=np.exp(-k2*(1-x1)/v)
incoming=Q*B0*(1-A)/(1-A*Q)
B=np.where(x<x1,B0+(incoming-B0)*np.exp(-(k1+k2)*x/v),B0*(1-A)/(1-A*Q)*np.exp(-k2*(x-x1)/v))
a=axes[1]
a.plot(x,B,lw=2)
a.axhline(B0,ls=':',color='0.5',label=r'$B_0$')
a.axvline(x1,ls='--',color='0.5')
a.text(x1+.025,.38,r'$x_1$')
a.set(xlabel=r'$x/P$',ylabel='bound probability',title='Motor occupancy',ylim=(-.04,1.0))
a.legend(fontsize=9)
a=axes[2]
a.plot([0,x1],[1/x1,1/x1],lw=2,color='#a64330',label='per bound motor')
a.plot([x1,1],[-1/(1-x1)]*2,lw=2,color='#a64330')
a.plot(x,B*np.where(x<x1,1/x1,-1/(1-x1)),ls='--',color='#23699b',label='per ensemble motor')
a.axhline(0,color='0.6',lw=.8)
a.axvline(x1,ls=':',color='0.5')
a.set(xlabel=r'$x/P$',ylabel=r'$F/(G_0/P)$',title='Conditional and weighted force')
a.legend(fontsize=8,loc='upper right')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
