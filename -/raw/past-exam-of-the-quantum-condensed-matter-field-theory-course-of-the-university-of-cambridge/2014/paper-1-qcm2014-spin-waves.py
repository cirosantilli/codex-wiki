"""Original analytical illustration; Python3.14/NumPy2.3/Matplotlib3.10. Saves PNG basename to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
k=np.linspace(-np.pi,np.pi,1000);a=axes[0];a.plot(k,abs(np.sin(k)),color='#235789',lw=2)
a.set(xlabel='Lattice momentum k',ylabel=r'$\omega_k/(2JS)$',title='Linear spin-wave approximation',xticks=[-np.pi,0,np.pi],xticklabels=[r'$-\pi$','0',r'$\pi$']);a.grid(alpha=.2)
N=2**np.arange(4,14);vals=[]
for n in N:
 k=2*np.pi*np.arange(1,n)/n;k=k[abs(np.sin(k))>1e-12];vals.append(np.sum(.5*(1/abs(np.sin(k))-1))/n)
a=axes[1];a.semilogx(N,vals,'o-',color='#ce5a24',base=2);a.set(xlabel='Sites N (zero modes excluded)',ylabel=r'$\delta S$',title='Infrared-regulated vacuum depletion');a.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
