"""Original model illustrations; tested Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Dependencies are in the repository pyproject.toml. Writes all PNGs to the output CWD.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
M=.044;Mo=1.025e3*1.35e18;b=.83e16;h=.73e17;K=7.1
I=M*5.1e14*1e5/(.0288*9.81);v=3e11;vi=1e13;weather=3e11
C0=.002;p0=C0/K;Cinf=(v+vi)/(M*b);pinf=Cinf/K+(v+vi-weather)/h
matrix=np.array([[-h/I,h/(I*K)],[h/(M*Mo),-h/(M*Mo*K)-b/Mo]])
eig,vec=np.linalg.eig(matrix);weights=np.linalg.solve(vec,np.array([p0-pinf,C0-Cinf]))
def pressure(t):return pinf+(vec@(weights[:,None]*np.exp(eig[:,None]*np.asarray(t)[None,:])))[0]
fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
for ax,t in zip(axes,[np.linspace(0,1500,700),np.geomspace(1,2e6,900)]):
 ax.plot(t,1e6*pressure(t),color='#176b9b',lw=2);ax.set_xlabel('Time after sustained emissions begin (years)');ax.set_ylabel('Atmospheric CO₂ (ppm)');ax.grid(alpha=.2)
axes[0].axhline(1e6*(p0+vi/h),color='#bd6a22',ls='--',label='Frozen-ocean balance: 419 ppm');axes[0].legend(fontsize=8);axes[0].set_title('Century-scale adjustment')
axes[1].set_xscale('log');axes[1].axhline(1e6*pinf,color='#bd6a22',ls='--',label='Final balance: 4109 ppm');axes[1].legend(fontsize=8);axes[1].set_title('Slow ocean-carbon adjustment')
fig.suptitle('Two atmospheric CO₂ response times in the stipulated model',fontsize=12);fig.savefig('2011-carbon-pressure.png',dpi=140,facecolor='white');plt.close(fig)
