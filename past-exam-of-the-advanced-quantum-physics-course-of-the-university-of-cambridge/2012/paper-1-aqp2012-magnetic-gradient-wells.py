"""Original figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

# Natural units ell=(hbar/|q alpha|)^(1/3), energy=hbar^2/(m ell^2).
x=np.linspace(-6.5,6.5,801);dx=x[1]-x[0];interior=x[1:-1]
fig,axes=plt.subplots(2,2,figsize=(10,7),layout='constrained')
for col,K in enumerate([-4.,4.]):
 V=.5*(K-interior**2/2)**2
 H=np.diag(np.full(len(interior),1/dx**2)+V)+np.diag(np.full(len(interior)-1,-.5/dx**2),1)+np.diag(np.full(len(interior)-1,-.5/dx**2),-1)
 ev,vec=np.linalg.eigh(H);psi=vec[:,:2]/np.sqrt(dx)
 if np.sum(psi[:,0])<0:psi[:,0]*=-1
 if np.sum(psi[interior>0,1])<0:psi[:,1]*=-1
 a,b=axes[:,col];a.plot(interior,V,lw=2.3,color='.3')
 for j,color in enumerate(['#246b94','#bd6231']):
  a.axhline(ev[j],ls='--',color=color,lw=1.3,label=fr'$E_{j}$ = {ev[j]:.4f}')
  b.plot(interior,psi[:,j],lw=2,color=color,label=['Even ground state','Odd first excited'][j])
 if K>0:a.axvline(np.sqrt(2*K),ls=':',color='.6');a.axvline(-np.sqrt(2*K),ls=':',color='.6')
 a.set(xlim=(-4.9,4.9),ylim=(0,15),title=f'K = {K:+.0f}: '+('single well' if K<0 else 'double well'),ylabel='Potential / energy scale');a.legend(fontsize=9,loc='upper center')
 b.axhline(0,color='.7',lw=1);b.set(xlim=(-4.9,4.9),xlabel=r'$X=x/\ell$',ylabel='Normalized wavefunction');b.legend(fontsize=9,loc='lower right');b.grid(alpha=.12)
fig.suptitle(r'$\mathcal{H}=-\frac{1}{2}\partial_X^2+\frac{1}{2}(K-X^2/2)^2$,  $K=k\ell$,  $q\alpha>0$',fontsize=13)
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white');plt.close(fig)
