"""Original local bifurcation diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Write an opaque PNG basename to the caller's CWD; respect caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

d=np.linspace(.0001,.9999,1000)
c0=(d-2)**2
cn=d*(8+4*d-d*d)/(12-d)
fig,ax=plt.subplots(figsize=(9.6,6.2),dpi=130,facecolor='white')
ax.fill_betweenx(d,d,c0,color='#dcf1df',label='Stable origin')
ax.fill_betweenx(d,cn,d,color='#dceafa',label='Stable paired equilibria')
ax.plot(c0,d,color='#a93235',lw=2.3,label='Origin Hopf (subcritical)')
ax.plot(cn,d,color='#256eaa',lw=2.3,label='Paired Hopf (supercritical)')
dp=np.linspace(0,1.5,400)
ax.plot(dp,dp,'k-',lw=2,label='Pitchfork')
ax.scatter([1],[1],s=65,color='black',zorder=5)
ax.annotate('Double zero (1, 1)',(1,1),xytext=(1.55,1.12),arrowprops={'arrowstyle':'->'})
ax.text(2.12,.43,'stable origin',fontsize=11)
ax.annotate('stable pair',(.47,.50),xytext=(.88,.29),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.text(.07,1.33,'All equilibria unstable for d ≥ 1',fontsize=10)
ax.set(xlim=(0,4.15),ylim=(0,1.5),xlabel='c',ylabel='d',title='Local bifurcations of the three-variable excitable model')
ax.grid(alpha=.16);ax.legend(loc='upper right',fontsize=8,framealpha=.96)
fig.tight_layout();fig.savefig('paper-51-fitzhugh-bifurcations.png',facecolor='white',transparent=False)
plt.close(fig)
