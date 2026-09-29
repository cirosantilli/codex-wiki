"""Original accelerated-worldline signals and Rindler grid. Python 3.14; numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(10,5.2),layout='constrained',facecolor='white')
rap=np.linspace(-1.3,2.25,650);X=np.cosh(rap);T=np.sinh(rap);L=.4
ax[0].plot(X,T,color='#176a9a',lw=2.2,label='Ship, initially at rest')
x=np.linspace(0,4.3,300);ax[0].plot(x,x,'k--',lw=1,label='Reception horizon')
ax[0].plot([L,L],[-1.5,4.2],color='.5',lw=1,label='Stationary source')
for te,col,lab in [(-.2,'#36844e',r'$at_e=-0.2$, received'),(.2,'#c77a20',r'$at_e=0.2$, received'),(.6,'#aa3f4c',r'$at_e=0.6$, never received')]:
 xx=np.linspace(L,4.3,200);ax[0].plot(xx,te+xx-L,color=col,lw=1.2,label=lab)
 if te<L:
  eta=-np.log(L-te);ax[0].scatter([np.cosh(eta)],[np.sinh(eta)],color=col,s=28,zorder=6)
ax[0].scatter([1],[0],color='black',s=20);ax[0].set(xlim=(0,4.3),ylim=(-1.3,4.2),xlabel='ax',ylabel='at',title=r'Photon reception, $aL=0.4$');ax[0].legend(loc='upper left',fontsize=7)
for zeta in [-.8,-.4,0,.4,.8]:
 rho=np.exp(zeta);color='#176a9a' if zeta==0 else '.65';ax[1].plot(rho*np.cosh(rap),rho*np.sinh(rap),color=color,lw=2.2 if zeta==0 else .8)
for xi in [-1.2,-.6,0,.6,1.2]:
 xx=np.linspace(.01,4.3,250);ax[1].plot(xx,xx*np.tanh(xi),color='#c07826',lw=.9)
ax[1].plot(x,x,'k--',lw=.8);ax[1].plot(x,-x,'k--',lw=.8);ax[1].text(2.5,-.35,r'$\xi$ constant: rays',color='#a65f14',fontsize=9)
ax[1].annotate(r'$\zeta=0,\ \xi=\tau$',xy=(np.cosh(1),np.sinh(1)),xytext=(2.3,.85),arrowprops=dict(arrowstyle='->'),color='#176a9a',fontsize=10)
ax[1].text(.2,3.65,r'$\zeta$ constant: hyperbolae',fontsize=9,color='.4')
ax[1].set(xlim=(0,4.3),ylim=(-1.3,4.2),xlabel='ax',ylabel='at',title='Right-wedge Rindler coordinates')
for a in ax:a.set_aspect('equal',adjustable='box');a.grid(alpha=.15)
fig.savefig('paper-1-rindler-signals.png',dpi=150,facecolor='white')
