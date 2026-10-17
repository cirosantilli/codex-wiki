"""Original periodic focusing-NLSE simulation. Python 3.14, numpy, matplotlib; output cwd."""
import numpy as np
import matplotlib.pyplot as plt
omega=np.linspace(0,2.3,500);gain=.5*omega*np.sqrt(np.maximum(4-omega**2,0));gain[omega>2]=0
period=2*np.pi/np.sqrt(2);n=2048;length=4*period;t=np.arange(n)*length/n-length/2
A=(1+.01*np.cos(np.sqrt(2)*t)).astype(complex);w=2*np.pi*np.fft.fftfreq(n,d=length/n);dz=.002;linear=np.exp(-.25j*w*w*dz)
snaps={0:A.copy()};mass0=np.mean(abs(A)**2)
for j in range(1,2501):
 A=np.fft.ifft(np.fft.fft(A)*linear);A*=np.exp(1j*abs(A)**2*dz);A=np.fft.ifft(np.fft.fft(A)*linear)
 if j in [1500,2500]:snaps[j*dz]=A.copy()
assert abs(np.mean(abs(A)**2)-mass0)<1e-10
fig,ax=plt.subplots(1,2,figsize=(10,3.5),layout='constrained')
ax[0].plot(omega,gain,lw=2);ax[0].axvline(np.sqrt(2),color='.5',ls=':');ax[0].set(xlabel=r'Frequency offset $\Omega$ ($|\beta_2|=\gamma P_0=1$)',ylabel=r'Amplitude growth rate $G$',title='Finite unstable sideband band');ax[0].grid(alpha=.2)
for z,a in snaps.items():ax[1].plot(t/period,abs(a),label=f'z = {z:g}')
ax[1].set(xlabel='Retarded time / initial ripple period',ylabel=r'Envelope amplitude $|A|$',title='Nonlinear pulse formation from a 1% ripple');ax[1].legend();ax[1].grid(alpha=.2)
fig.suptitle('Chosen ideal periodic model; late propagation need not relax to a permanent train',fontsize=10)
fig.savefig('paper-1-modulational-instability.png',dpi=150,facecolor='white')
