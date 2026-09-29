from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def speed(w):
 lo,hi=1+1e-12,2-1e-12
 for _ in range(70):
  c=(lo+hi)/2;q=w*np.sqrt(1-1/c**2);kap=w*np.sqrt(1/c**2-.25)
  if q>np.arctan(4*kap/q):hi=c
  else:lo=c
 return (lo+hi)/2
fig,ax=plt.subplots(1,3,figsize=(11.5,3.8),layout='constrained')
w=np.geomspace(.04,15,300);c=np.array([speed(v) for v in w]);ax[0].semilogx(2*np.pi/w,c,lw=2)
ax[0].axhline(1,color='gray',ls=':');ax[0].axhline(2,color='gray',ls=':');ax[0].set(xlabel=r'period $2\pi/\omega$',ylabel='phase speed',ylim=(.95,2.05),title='Fundamental Love mode')
z=np.linspace(0,7,500)
for om in [.4,4]:
 cc=speed(om);q=om*np.sqrt(1-1/cc**2);kap=om*np.sqrt(1/cc**2-.25)
 U=np.where(z<=1,np.cos(q*z),np.cos(q)*np.exp(-kap*(z-1)))
 ax[1].plot(U,z,label=fr'$\omega={om:g}$',lw=2)
ax[1].axhline(1,color='gray',ls=':');ax[1].invert_yaxis();ax[1].set(xlabel='mode displacement / surface value',ylabel='depth / layer thickness',title='Long periods sample deeper');ax[1].legend(fontsize=9)
p=np.sin(np.deg2rad(25));g=.25;zt=(1/p-1)/g;zz=np.linspace(0,zt,300);xx=(np.sqrt(1-p*p)-np.sqrt(np.maximum(0,1-p*p*(1+g*zz)**2)))/(p*g);xt=xx[-1]
ax[2].plot(np.r_[xx,2*xt-xx[::-1]],np.r_[zz,zz[::-1]],lw=2,color='#9e4a10');ax[2].invert_yaxis();ax[2].set(xlabel='horizontal distance',ylabel='depth',title=r'Turning ray: $c(z)=1+0.25z$');ax[2].text(.05,.07,r'$\sin i/c=$ constant',transform=ax[2].transAxes,fontsize=10)
for a in ax:a.grid(alpha=.2)
fig.suptitle(r'Synthetic models: layer $h=1$, shear speeds 1 and 2, equal densities; not Earth measurements',fontsize=10)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
