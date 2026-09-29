"""Original explanatory figure. Python 3.14, NumPy and Matplotlib.
Write the PNG basename to the current working directory for the mirrored Make target.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
nu=15e9;c=299792458.;lam=c/nu;Theta=6*np.pi/10800
fig,axs=plt.subplots(1,2,figsize=(10,4.1),layout='constrained');b=np.linspace(0,30,1200)
a=axs[0];a.plot(b,np.sinc(Theta*b/lam),color='#376b91',lw=2);a.axhline(0,color='.4',lw=.8);a.axvline(lam/Theta,color='#a85422',ls='--',label='First null: 11.45 m');a.axvline(20,color='.6',ls=':',label='20 m baseline');a.set(xlabel='Projected axial baseline (m)',ylabel=r'$V(u,0)/\Delta S_\nu$',title='Six-arcminute uniform square');a.legend(fontsize=9);a.grid(alpha=.15)
bs=np.linspace(-20,20,301);U,V=np.meshgrid(bs,bs);vis=np.sinc(Theta*U/lam)*np.sinc(Theta*V/lam);a=axs[1];im=a.imshow(vis,origin='lower',extent=[-20,20,-20,20],cmap='RdBu_r',norm=matplotlib.colors.TwoSlopeNorm(vmin=-.25,vcenter=0,vmax=1));a.set(xlabel='Projected x baseline (m)',ylabel='Projected y baseline (m)',title='Model, not actual baseline coverage');fig.colorbar(im,ax=a,label=r'$V/\Delta S_\nu$',shrink=.9)
fig.savefig('paper-1-square-cluster-visibility.png',dpi=150,facecolor='white');plt.close(fig)
