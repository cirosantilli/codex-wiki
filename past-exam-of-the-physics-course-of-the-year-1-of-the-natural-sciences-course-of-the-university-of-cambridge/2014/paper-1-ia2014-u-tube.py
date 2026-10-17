"""Original educational diagram. Python 3.14, NumPy and Matplotlib; output is saved in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
g=9.81;l=.5;rho=1500.;A=3e-4;beta=.3;v0=.015
w0=np.sqrt(2*g/l);Gamma=beta/(rho*A);wd=np.sqrt(w0*w0-Gamma**2/4)
amp=v0/w0;ad=v0/wd;period=2*np.pi/w0;te=2/Gamma*np.log(ad/1e-4)
fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained')
t=np.linspace(0,3.2*period,1000);axs[0].plot(t,1000*amp*np.sin(w0*t),color='#225c91',lw=1.5)
axs[0].scatter([period/4],[amp*1000],color='#b25424',s=24)
axs[0].annotate('2.395 mm at T/4',xy=(period/4,amp*1000),xytext=(.55,2.6),fontsize=9,arrowprops={'arrowstyle':'->','color':'#666'})
axs[0].set(xlabel='Time (s)',ylabel='One surface displacement (mm)',title='Frictionless: T = 1.003 s',ylim=(-3,3.2),xlim=(0,t[-1]))
t=np.linspace(0,11,3200);env=1000*ad*np.exp(-Gamma*t/2);y=env*np.sin(wd*t)
axs[1].plot(t,y,color='#225c91',lw=1);axs[1].plot(t,env,color='#b25424',ls='--');axs[1].plot(t,-env,color='#b25424',ls='--')
axs[1].axhline(.1,color='#777',lw=1,ls=':');axs[1].axhline(-.1,color='#777',lw=1,ls=':');axs[1].axvline(te,color='#777',lw=1,ls=':')
axs[1].annotate('Envelope reaches 0.1 mm\nat 9.53 s',xy=(te,.1),xytext=(5.7,1.65),fontsize=9,arrowprops={'arrowstyle':'->','color':'#666'})
axs[1].set(xlabel='Time (s)',ylabel='One surface displacement (mm)',title=r'Viscous damping: $Q=9.40$',ylim=(-3,3.2),xlim=(0,11))
for ax in axs:ax.axhline(0,color='#555',lw=.6);ax.grid(alpha=.2)
fig.savefig('paper-1-ia2014-u-tube.png',dpi=150,facecolor='white');plt.close(fig)
