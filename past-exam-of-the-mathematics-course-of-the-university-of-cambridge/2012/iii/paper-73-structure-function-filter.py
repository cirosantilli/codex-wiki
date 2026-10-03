"""Original spectrum-filter plot. Tested Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Writes PNG basename to caller cwd; preserves MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,12,2401)
H=np.zeros_like(x)
small=x<.08
H[small]=x[small]**2/10-x[small]**4/280+x[small]**6/15120
large=~small
H[large]=1+3*np.cos(x[large])/x[large]**2-3*np.sin(x[large])/x[large]**3
sharp=(x>=np.pi).astype(float)
improved=np.where(x<np.pi,x*x/10,1)
fig,ax=plt.subplots(figsize=(8.0001,4.4001),dpi=100,facecolor='white')
fig.subplots_adjust(left=.10,right=.97,bottom=.17,top=.88)
ax.plot(x,H,color='#1767b3',lw=2.5,label='Exact isotropic longitudinal filter')
ax.plot(x,sharp,color='#a06b27',lw=1.8,ls=':',label='Sharp cutoff at π')
ax.plot(x,improved,color='#ba4c45',lw=1.8,ls='--',label='Small-x correction below cutoff')
ax.axvline(np.pi,color='#888888',lw=.8,alpha=.5)
ax.text(np.pi+.12,.16,r'$x=\pi$',fontsize=11)
ax.annotate(r'$H(x)\simeq x^2/10$ — large scales still contribute',xy=(1.2,.136),xytext=(3.85,.46),fontsize=10,arrowprops={'arrowstyle':'->','color':'#1767b3'},color='#1767b3')
ax.set_xlim(0,12);ax.set_ylim(-.04,1.18)
ax.set_xlabel(r'$x=kr$');ax.set_ylabel('Spectral weight')
ax.set_title('Velocity increments attenuate large scales; they do not remove them',fontsize=12,pad=11)
ax.grid(alpha=.16);ax.legend(loc='lower right',fontsize=9,framealpha=.97)
fig.savefig('paper-73-structure-function-filter.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
