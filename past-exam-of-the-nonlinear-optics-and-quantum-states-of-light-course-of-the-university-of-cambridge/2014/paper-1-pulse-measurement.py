"""Original nonlinear gate layout and analytic Gaussian SHG spectrograms. Output cwd."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(2,2,figsize=(10,6),layout='constrained')
a=ax[0,0];a.set(xlim=(0,10),ylim=(0,5));a.axis('off')
def box(x,y,w,text):
 a.add_patch(FancyBboxPatch((x,y),w,.8,boxstyle='round,pad=.05',facecolor='#edf4fc',edgecolor='#365b80'));a.text(x+w/2,y+.4,text,ha='center',va='center',fontsize=9)
def arrow(x,y,xx,yy):a.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops=dict(arrowstyle='->',color='#365b80'))
box(.2,2,1.5,'Pulse');box(2.2,2,1.4,'Split');box(4.1,3.2,1.6,r'Delay $\tau$');box(6.6,2,1.3,'Crystal');box(8.4,2,1.4,'Readout');arrow(1.7,2.4,2.2,2.4);arrow(3.6,2.4,4.1,3.6);arrow(5.7,3.6,6.6,2.4);arrow(3.6,2.4,6.6,2.4);arrow(7.9,2.4,8.4,2.4);a.text(5,.7,'Integrated SH energy: autocorrelation\nSpectrum of SH signal: SHG-FROG',ha='center',fontsize=10);a.set_title('Functional two-replica nonlinear gate')
tau=np.linspace(-4,4,201);omega=np.linspace(-7,7,251);tt,ww=np.meshgrid(tau,omega)
a=ax[0,1];a.plot(tau,np.exp(-tau*tau/2),label='C = 0');a.plot(tau,np.exp(-tau*tau/2),'--',label='C = 2');a.set(xlabel=r'Delay $\tau$',ylabel='Normalized integrated signal',title='Same intensity autocorrelation');a.legend();a.grid(alpha=.2)
for a,C in zip(ax[1],[0,2]):
 trace=np.exp(-tt*tt/2-ww*ww/(2*(1+C*C)))
 im=a.pcolormesh(tau,omega,trace,cmap='magma',shading='auto',vmin=0,vmax=1);a.set(xlabel=r'Delay $\tau$',ylabel=r'Signal frequency offset $\omega$',title=f'Normalized SHG-FROG, chirp C = {C}');fig.colorbar(im,ax=a,label='Relative spectral signal')
fig.suptitle(r'Chosen fields $A_C(t)=e^{-t^2/2}e^{iCt^2/2}$: equal intensity, different phase',fontsize=11)
fig.savefig('paper-1-pulse-measurement.png',dpi=150,facecolor='white')
