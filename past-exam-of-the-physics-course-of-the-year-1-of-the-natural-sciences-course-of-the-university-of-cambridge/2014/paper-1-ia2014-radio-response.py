"""Original educational diagram. Python 3.14, NumPy and Matplotlib; output is saved in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
R=50.;L=9e-6
f=np.linspace(7.5e6,11.5e6,1600)
def H(f,C):
 w=2*np.pi*f
 return 1j*w*L/(R+1j*(w*L-1/(w*C)))
fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout='constrained')
for C,color in [(35e-12,'#225c91'),(31.5e-12,'#b25424')]:
 axs[0].plot(f/1e6,np.abs(H(f,C)),color=color,label=f'{C/1e-12:g} pF')
 for freq in [9e6,10e6]:axs[0].scatter(freq/1e6,abs(H(freq,C)),color=color,s=22)
axs[0].axhline(1,color='#777777',ls=':',lw=1)
axs[0].set(xlabel='Frequency (MHz)',ylabel=r'$|V_{\rm out}/V_{\rm in}|$',title='Output across the inductor',ylim=(0,12))
axs[0].legend();axs[0].grid(alpha=.2)
t=np.linspace(0,3e-6,3600);fa,fb=9e6,10e6;C=31.5e-12
ha,hb=H(fa,C),H(fb,C)
v=np.real(ha*np.exp(2j*np.pi*fa*t)+hb*np.exp(2j*np.pi*fb*t))
env=np.sqrt(abs(ha)**2+abs(hb)**2+2*abs(ha)*abs(hb)*np.cos(2*np.pi*(fb-fa)*t+np.angle(hb)-np.angle(ha)))
axs[1].plot(t/1e-6,v,color='#225c91',lw=1)
axs[1].plot(t/1e-6,env,color='#b25424',lw=1.4,label='Exact amplitude envelope')
axs[1].plot(t/1e-6,-env,color='#b25424',lw=1.4)
axs[1].set(xlabel=r'Time ($\mu$s)',ylabel='Output (mV)',title='Two equal 1 mV input sinusoids; 31.5 pF',xlim=(0,3),ylim=(-16,16))
axs[1].legend(fontsize=8,loc='lower right');axs[1].grid(alpha=.2)
fig.savefig('paper-1-ia2014-radio-response.png',dpi=150,facecolor='white');plt.close(fig)
