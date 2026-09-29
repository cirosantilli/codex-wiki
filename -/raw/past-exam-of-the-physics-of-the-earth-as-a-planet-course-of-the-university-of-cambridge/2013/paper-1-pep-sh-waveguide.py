"""Original explanatory figure; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained');h=30.;b1=3.5;b2=4.5;S=np.sqrt(b1**-2-b2**-2);ic=np.arcsin(b1/b2)
x=np.linspace(0,430,1400);ax=axs[0];ax.plot(x,x/b1,'k',label='direct SH')
for m in [1,2,3]:
 xc=2*m*h*np.tan(ic);t=np.sqrt(x*x+(2*m*h)**2)/b1
 ax.plot(x[x<xc],t[x<xc],color='#b96548',label='leaking reflection' if m==1 else None)
 ax.plot(x[x>=xc],t[x>=xc],color='#316e9d',label='trapped reflection' if m==1 else None)
 ax.plot(x[x>=xc],x[x>=xc]/b2+2*m*h*S,'k--',alpha=.45,label='critical-head family' if m==1 else None)
 ax.plot(xc,np.sqrt(xc**2+(2*m*h)**2)/b1,'ko',ms=3);ax.text(3,2*m*h/b1+2,f'm = {m}',fontsize=8)
ax.set(xlim=(0,430),ylim=(0,150),xlabel='distance / km',ylabel='travel time / s',title='Direct wave and first three reverberation orders');ax.legend(fontsize=8,loc='lower right');ax.grid(alpha=.2)
ax.text(6,140,'higher orders follow the same m ≥ 1 formula',fontsize=8)
ax=axs[1];ratio=(b2/b1)**2
for n,col in zip(range(4),['#333333','#2e719e','#bc7a28','#8b5195']):
 fc=n/(2*h*S);fs=np.linspace(max(fc+1e-7,.001),.5,650);cs=[]
 for f in fs:
  om=2*np.pi*f;lo=b1;hi=b2
  for _ in range(65):
   c=(lo+hi)/2;q=om*np.sqrt(max(0,b1**-2-c**-2));s=om*np.sqrt(max(0,c**-2-b2**-2));phase=q*h-np.arctan2(ratio*s,q)-n*np.pi
   if phase>0:hi=c
   else:lo=c
  cs.append((lo+hi)/2)
 ax.plot(np.r_[fc,fs],np.r_[b2,cs],color=col,label='fundamental n = 0' if n==0 else f'overtone n = {n}')
 if n:ax.plot(fc,b2,'o',color=col,ms=4)
ax.axhline(b1,color='grey',ls=':',lw=1);ax.axhline(b2,color='grey',ls=':',lw=1)
ax.set(xlim=(0,.5),ylim=(3.45,4.57),xlabel='frequency / Hz',ylabel='phase velocity / km s⁻¹',title='Love branches; equal density illustrative only');ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.suptitle('30 km crust: shear speeds 3.5 km/s above 4.5 km/s; flat, lossless model')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
