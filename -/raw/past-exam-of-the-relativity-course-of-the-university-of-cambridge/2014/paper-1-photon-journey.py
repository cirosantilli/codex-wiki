"""Original calculated photon-drive journey. Python 3.14; numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
c=299792458.; year=365.25*86400; a=10.; t0=c/a/year; x0=t0
eta=np.arcsinh(10.); gamma=np.cosh(eta); beta=np.tanh(eta)
z=np.linspace(0,eta,160); ta=t0*eta; xa=x0*(gamma-1); tc=(100-2*xa)/beta
T=np.r_[t0*np.sinh(z), t0*np.sinh(eta)+np.linspace(0,tc,200),t0*np.sinh(eta)+tc+t0*(np.sinh(eta)-np.sinh(eta-z))]
X=np.r_[x0*(np.cosh(z)-1),xa+beta*np.linspace(0,tc,200),100-xa+x0*(np.cosh(eta)-np.cosh(eta-z))]
Tau=np.r_[t0*z,ta+np.linspace(0,tc,200)/gamma,ta+tc/gamma+t0*z]
fig,ax=plt.subplots(1,2,figsize=(10,4),layout='constrained',facecolor='white')
ax[0].plot(T,X,label='Finite acceleration',lw=2,color='#146ca4');ax[0].plot([0,100/beta],[0,100],'--',label='Instantaneous burns',color='#c66524')
ax[0].set(xlabel='Earth time (years)',ylabel='Earth-frame distance (light years)',title='Same destination and cruise speed')
ax[0].legend(fontsize=9);ax[1].plot(T,Tau,color='#146ca4',lw=2,label='Finite acceleration');ax[1].plot([0,100/beta],[0,10],'--',color='#c66524',label='Instantaneous burns')
ax[1].set(xlabel='Earth time (years)',ylabel='Traveller proper time (years)',title=f'Traveller arrival: {Tau[-1]:.2f} versus 10 years')
for x in ax:x.grid(alpha=.23)
fig.savefig('paper-1-photon-journey.png',dpi=150,facecolor='white')
