"""Original calculated harmonic responses. Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2.7,1400)
fig,ax=plt.subplots(1,2,figsize=(10,4.2),layout='constrained',facecolor='white')
for z in [.08,.25,.6,.9]:
 response=lambda q:1/np.sqrt((1-q*q)**2+4*z*z*q*q)
 line=ax[0].plot(x,response(x),label=fr'$\zeta={z}$')[0]
 if z<1/np.sqrt(2):
  xm=np.sqrt(1-2*z*z);ax[0].scatter(xm,response(xm),color=line.get_color(),s=20)
ax[0].axhline(1,color='.7',ls=':',lw=.8);ax[0].set(xlabel=r'$\omega/\omega_0$',ylabel=r'$k|R(\omega)|$',ylim=(0,7),title='Damping lowers and shifts the amplitude peak');ax[0].legend(fontsize=9)
z=.25;den=np.sqrt((1-x*x)**2+4*z*z*x*x);charge=1/den;charge/=1/(2*z*np.sqrt(1-z*z));current=2*z*x/den
ax[1].plot(x,charge,label='Charge / peak charge');ax[1].plot(x,current,label='Resistor voltage / its peak');xr=np.sqrt(1-2*z*z)
ax[1].axvline(xr,color='C0',ls=':',lw=1);ax[1].axvline(1,color='C1',ls=':',lw=1)
ax[1].set(xlim=(.5,1.5),ylim=(0,1.14),xlabel=r'$\omega/\omega_0$',ylabel='Individually normalized response',title=r'Different observables, $\zeta=0.25$');ax[1].legend(loc='lower left',fontsize=8)
for a in ax:a.grid(alpha=.18)
fig.savefig('paper-2-response-resonance.png',dpi=150,facecolor='white')
