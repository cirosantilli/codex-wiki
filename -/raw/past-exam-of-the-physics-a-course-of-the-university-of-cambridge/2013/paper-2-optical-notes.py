"""Original ideal optical intensity curves; no source figures. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=(12,3.8),layout='constrained',facecolor='white')
x=np.linspace(0,6,601);ax[0].plot(x,4*np.sin(np.pi*x/2)**2,label='Circular aperture');ax[0].axhline(1,color='C1',ls='--',label='Opaque disk, on axis');ax[0].set(xlabel=r'$N_F=a^2/(\lambda z)$',ylabel='Axial intensity / unobstructed',title='Scalar Fresnel prediction');ax[0].legend(fontsize=8,loc='upper right')
d=np.linspace(-np.pi,np.pi,1801)
for R in [.4,.85]:
 F=4*R/(1-R)**2;ax[1].plot(d/np.pi,1/(1+F*np.sin(d/2)**2),label=fr'$\mathcal{{R}}={R}$')
ax[1].set(xlabel=r'Round-trip phase / $\pi$',ylabel='Transmission',title='Symmetric lossless Fabry–Pérot');ax[1].legend(fontsize=8)
s=np.linspace(-3.9,3.9,4001);N=8;b_over_d=.24;array=(np.sinc(N*s)/np.sinc(s))**2;integer=np.abs(s-np.rint(s))<1e-10;array[integer]=1;env=np.sinc(b_over_d*s)**2
ax[2].plot(s,env*array,lw=1.1,label='Eight slits');ax[2].plot(s,env,'--',color='.5',lw=1,label='Single-slit envelope');ax[2].set(xlabel=r'$d\sin\theta/\lambda$',ylabel=r'Intensity / $N^2I_{1,0}$',title='Uniform grating, b/d = 0.24');ax[2].legend(fontsize=8)
for a in ax:a.grid(alpha=.15)
fig.savefig('paper-2-optical-notes.png',dpi=150,facecolor='white')
