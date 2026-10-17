"""Original Fourier calculation, phase-reversed half slit. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
eta=np.linspace(-6,6,2401);s=np.pi*eta/2;phase=np.zeros_like(s);nz=s!=0;phase[nz]=np.sin(s[nz])**4/s[nz]**2
fig,ax=plt.subplots(1,2,figsize=(9.8,4),layout='constrained',facecolor='white')
ax[0].plot([-.5,0,0,.5],[-1,-1,1,1],lw=2,label=r'Phase difference $\pi$');ax[0].plot([-.5,.5],[1,1],'--',lw=1.5,label=r'Doubled layer: $2\pi$');ax[0].set(xlim=(-.6,.6),ylim=(-1.4,1.4),xlabel='Position / slit width',ylabel='Real amplitude transmission',title='Half-slit transmission');ax[0].legend(fontsize=8)
ax[1].plot(eta,phase,label=r'Phase difference $\pi$',lw=2);ax[1].plot(eta,np.sinc(eta)**2,'--',label=r'Phase difference $2\pi$',lw=1.6)
lo,hi=1.,1.4
for _ in range(60):
 mid=(lo+hi)/2
 if np.tan(mid)>2*mid:hi=mid
 else:lo=mid
sm=(lo+hi)/2;em=2*sm/np.pi;im=np.sin(sm)**4/sm**2
ax[1].scatter([-em,em],[im,im],s=20,color='C0');ax[1].annotate(r'First maxima: $\pm0.742\lambda/b$',xy=(em,im),xytext=(1.65,.73),arrowprops=dict(arrowstyle='->'),fontsize=8)
ax[1].set(xlim=(-6,6),ylim=(0,1.1),xlabel=r'$b\sin\theta/\lambda$',ylabel='Intensity / uncoated central intensity',title='Dark versus bright centre');ax[1].legend(loc='upper left',fontsize=8)
for a in ax:a.grid(alpha=.18)
fig.savefig('paper-2-phase-slit.png',dpi=150,facecolor='white')
