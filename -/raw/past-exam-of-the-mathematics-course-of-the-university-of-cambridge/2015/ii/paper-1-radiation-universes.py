import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,ax=plt.subplots(1,2,figsize=(8,3.6),dpi=100)
for a,lam,end in ((ax[0],1.4,4),(ax[1],.6,2*np.arctanh(.6))):
 t=np.linspace(0,end,500);y=1-np.cosh(t)+lam*np.sinh(t)
 a.plot(t,np.sqrt(np.maximum(y,0)),lw=2,label=rf'$\lambda={lam}$');a.set(xlabel=r'Rescaled time $\kappa t$',ylabel=r'Rescaled size $a\sqrt{2\Lambda/3}$',xlim=(0,end),ylim=(0,None));a.grid(alpha=.2);a.legend()
ax[0].set_title('Expansion continues forever')
ax[1].set_title('Turnaround and recollapse')
t=np.arctanh(.6);ax[1].axvline(t,color='.6',ls=':');ax[1].annotate('Maximum size',xy=(t,np.sqrt(1-np.sqrt(1-.6**2))),xytext=(.28,.3),arrowprops=dict(arrowstyle='->'))
fig.tight_layout();fig.savefig('paper-1-radiation-universes.png',facecolor='white',transparent=False)
