"""Original analytic explanatory figure; Python 3.14, NumPy and Matplotlib.
Run in the desired output directory. No examination figure or external image used.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
t0=8.253968253968253
t1=9.849206349206348
t=np.linspace(0,40,700)
fig,axs=plt.subplots(1,2,figsize=(9.4,4),layout='constrained')
y0=np.exp(-t/t0);y1=np.exp(-t/t1)
axs[0].plot(t,y0,label='Initial: lifetime 8.254 y',lw=2)
axs[0].plot(t,y1,label='Added hydrogen: lifetime 9.849 y',lw=2)
axs[0].fill_between(t,y0,y1,where=t<=20,color='#e6b67d',alpha=.8,label='Extra integrated forcing to 20 y')
axs[0].axvline(20,color='#777777',ls='--',lw=.9)
axs[0].set(xlabel='Time after equal methane pulse (years)',ylabel='Normalized pulse forcing',title='Unchanged radiative efficiency')
axs[0].legend(fontsize=8)
h=np.linspace(.1,100,600)
r=t1*(-np.expm1(-h/t1))/(t0*(-np.expm1(-h/t0)))
axs[1].plot(h,100*(r-1),lw=2,color='#803d81')
axs[1].plot(20,13.7483975,'o',color='#bb5029')
axs[1].annotate('20 years: +13.75%',(20,13.7483975),(30,9),arrowprops=dict(arrowstyle='->'))
axs[1].axhline(100*(t1/t0-1),color='#777777',ls='--',lw=.9,label='Infinite-horizon lifetime ratio')
axs[1].set(xlabel='GWP integration horizon (years)',ylabel='Increase in pulse GWP (%)',title='Finite horizon limits the increase',ylim=(0,22))
axs[1].legend(fontsize=8,loc='lower right')
fig.savefig('paper-id-methane-lifetime.png',dpi=170,facecolor='white')
