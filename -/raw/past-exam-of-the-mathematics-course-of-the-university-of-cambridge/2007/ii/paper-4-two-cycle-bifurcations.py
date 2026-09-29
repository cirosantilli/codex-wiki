"""Original cubic two-cycle diagram; Python 3.14/NumPy 2.3/Matplotlib 3.10.
Opaque PNG basename output to caller CWD; uses caller's MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig,ax=plt.subplots(figsize=(7.6,4.0),layout='constrained',facecolor='white')
def branch(mu,x,M,color):
    stable=np.abs(M)<1
    ax.plot(mu,np.where(stable,x,np.nan),color=color,lw=2.2)
    ax.plot(mu,np.where(~stable,x,np.nan),color=color,lw=1.4,ls='--')
mu=np.linspace(-1.3,2.5,2200)
branch(mu,np.zeros_like(mu),mu,'#1964a0')
m=np.linspace(1,2.5,1100)
for sign in [-1,1]:branch(m,sign*np.sqrt(m-1),3-2*m,'#1964a0')
m=np.linspace(-1+1e-6,2.5,1700)
for sign in [-1,1]:branch(m,sign*np.sqrt(m+1),(-2*m-3)**2,'#d47516')
m=np.linspace(2+1e-6,2.5,1300);sp=(m+np.sqrt(m*m-4))/2;sm=1/sp
for sign in [-1,1]:
    for sr in [sp,sm]:branch(m,sign*np.sqrt(sr),9-2*m*m,'#d47516')
for mf in [-1,1,2,np.sqrt(5)]:
    ax.axvline(mf,color='0.82',ls=':',lw=.9,zorder=0)
ax.set_xticks([-1,0,1,2,np.sqrt(5),2.5],['-1','0','1','2',r'$\sqrt{5}$','2.5'])
ax.set(xlim=(-1.3,2.5),ylim=(-2.05,2.05),xlabel=r'parameter $\mu$',ylabel='orbit point x',title=r'Fixed points and two-cycles of $F(x)=x(\mu-x^2)$')
ax.spines[['top','right']].set_visible(False)
ax.set_facecolor('white')
fig.legend(handles=[Line2D([],[],color='#1964a0',label='fixed points'),Line2D([],[],color='#d47516',label='two-cycle points'),Line2D([],[],color='black',lw=2.2,label='stable'),Line2D([],[],color='black',ls='--',label='unstable')],loc='outside lower center',ncol=4,fontsize=9)
fig.savefig('paper-4-two-cycle-bifurcations.png',dpi=140,facecolor='white',transparent=False)
plt.close(fig)
