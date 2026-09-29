"""Original cubic fixed-point diagrams; Python 3.14/NumPy 2.3/Matplotlib 3.10.
Opaque PNG basename output to caller CWD; uses caller's MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig,axs=plt.subplots(1,3,figsize=(10,3.7),layout='constrained',facecolor='white')
for ax,(a,b,title) in zip(axs,[(1.,0.,'a = 1, b = 0'),(1.,1.,'a = 1, b = 1'),(-1.,-.5,'a = -1, b = -0.5')]):
    mu=np.linspace(-1.35,1.30,1500)
    for xs,ms,M in [(np.zeros_like(mu),mu,mu)]:
        stable=np.abs(M)<1
        ax.plot(ms,np.where(stable,xs,np.nan),color='#1964a0',lw=2)
        ax.plot(ms,np.where(~stable,xs,np.nan),color='#1964a0',lw=1.5,ls='--')
    x=np.linspace(-2,2,5000);m=1-b*x-a*x*x;M=1+b*x+2*a*x*x
    stable=np.abs(M)<1
    ax.plot(np.where(stable,m,np.nan),x,color='#1964a0',lw=2)
    ax.plot(np.where(~stable,m,np.nan),x,color='#1964a0',lw=1.5,ls='--')
    ax.scatter([-1,1],[0,0],color='black',s=16,zorder=4)
    ax.annotate('origin flip',xy=(-1,0),xytext=(-1.29,-.8),fontsize=8,
                arrowprops={'arrowstyle':'->','lw':.7})
    ax.annotate('pitchfork' if b==0 else 'transcritical',xy=(1,0),xytext=(.1,.8),fontsize=8,
                arrowprops={'arrowstyle':'->','lw':.7})
    if b:
        mf=1+b*b/(4*a);xf=-b/(2*a)
        ax.scatter([mf],[xf],color='black',s=16,zorder=4)
        ax.annotate('saddle-node',xy=(mf,xf),xytext=(-.05,-1.35),fontsize=8,
                    arrowprops={'arrowstyle':'->','lw':.7})
    ax.set(xlim=(-1.35,1.30),ylim=(-1.65,1.65),xlabel=r'parameter $\mu$',title=title)
    ax.axhline(0,color='0.85',lw=.6,zorder=0)
    ax.spines[['top','right']].set_visible(False)
    ax.set_facecolor('white')
axs[0].set_ylabel('fixed point x')
fig.legend(handles=[Line2D([],[],color='#1964a0',lw=2,label='stable'),Line2D([],[],color='#1964a0',ls='--',label='unstable')],loc='outside lower center',ncol=2)
fig.savefig('paper-4-fixed-point-bifurcations.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
