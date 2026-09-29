"""Mean-variance geometry for Paper 35; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes only paper-35-frontiers.png in the caller's current directory.
The caller may supply MPLCONFIGDIR; this script does not modify it.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mu=np.array([10.,17.,24.])
cov=np.array([[4.,1.,1.],[1.,9.,2.],[1.,2.,16.]])
one=np.ones(3)
a=one@np.linalg.solve(cov,one)
b=one@np.linalg.solve(cov,mu)
c=mu@np.linalg.solve(cov,mu)
d=a*c-b*b
mean_min=b/a
means=np.linspace(-25,75,1600)
sigma_min=np.sqrt((a*means*means-2*b*means+c)/d)
fig,axs=plt.subplots(1,2,figsize=(12,6),sharex=True,sharey=True,layout='constrained')
for ax,r in zip(axs,[3.,25.]):
    ax.fill_betweenx(means,sigma_min,6,where=sigma_min<=6,color='#d8eaf1',label='Risky opportunity set')
    upper=means>=mean_min
    ax.plot(sigma_min[upper],means[upper],color='#237498',lw=2,label='Efficient risky frontier')
    ax.plot(sigma_min[~upper],means[~upper],color='#237498',ls='--',lw=1.5,label='Inefficient risky boundary')
    z=np.linalg.solve(cov,mu-r*one)
    weights=z/(one@z)
    tangent_mean=mu@weights
    tangent_sigma=np.sqrt(weights@cov@weights)
    theta=np.sqrt((mu-r*one)@z)
    x=np.linspace(0,6,400)
    ax.plot(x,r+theta*x,color='#ab3b27',lw=2,label='Efficient bank + risky ray')
    ax.scatter([0],[r],color='black',s=35,zorder=4)
    ax.annotate('Risk-free asset',(0,r),xytext=(12,4),textcoords='offset points',fontsize=9)
    ax.scatter([1/np.sqrt(a)],[mean_min],color='#237498',s=30,zorder=4)
    ax.scatter([tangent_sigma],[tangent_mean],color='#6f348c',s=35,zorder=5)
    if r==3:
        ax.annotate('Market portfolio',(tangent_sigma,tangent_mean),xytext=(15,-23),textcoords='offset points',fontsize=9,arrowprops={'arrowstyle':'-','color':'#6f348c'})
    else:
        ax.plot(x,r-theta*x,color='#6f348c',ls=':',lw=1.5,label='Negative-premium tangent ray')
        ax.annotate('Normalized tangency portfolio',(tangent_sigma,tangent_mean),xytext=(10,-29),textcoords='offset points',fontsize=9,arrowprops={'arrowstyle':'-','color':'#6f348c'})
        reflected=2*r-tangent_mean
        ax.scatter([tangent_sigma],[reflected],color='#ab3b27',s=35,zorder=5)
        ax.annotate('Short one tangency portfolio;\nlend twice initial wealth',(tangent_sigma,reflected),xytext=(8,14),textcoords='offset points',fontsize=9,arrowprops={'arrowstyle':'-','color':'#ab3b27'})
    ax.set(xlim=(0,6),ylim=(-25,75),xlabel='Return standard deviation (percentage points)',title=f'Risk-free return = {r:g}%')
    ax.grid(alpha=.18)
    ax.legend(loc='lower right',fontsize=7,framealpha=.95)
axs[0].set_ylabel('Expected return (%)')
fig.suptitle('Risky opportunity sets and efficient risk-free combinations')
fig.savefig(Path.cwd()/'paper-35-frontiers.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
