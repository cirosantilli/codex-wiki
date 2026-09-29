"""Original Bondi branch sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Outputs paper-70-bondi-branches.png to caller CWD; respects caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

mach=np.geomspace(.002,6,1800)
h=.5*mach**1.5+1.5*mach**-.5
fig,ax=plt.subplots(figsize=(7.4,4.7),facecolor='white')
for eta,colour in [(0.4,'#1864ab'),(1.0,'#2b8a3e'),(1.6,'#c92a2a')]:
 x=(np.sqrt(eta)*h-2)/3
 for branch,style in [(mach<=1,'-'),(mach>=1,'--')]:
  good=branch&(x>=0)
  ax.plot(x[good],mach[good],color=colour,lw=2,ls=style,label=rf'$\dot M/\dot M_{{\max}}={eta:g}$' if style=='-' else None)
 if eta>=1:ax.scatter([(2*np.sqrt(eta)-2)/3],[1],color=colour,s=35,zorder=5)
ax.axhline(1,color='#7b868e',lw=.9,ls=':')
ax.text(2.05,1.06,'Mach one',fontsize=10,color='#56626b')
ax.annotate('No continuation\nto smaller radius',xy=((2*np.sqrt(1.6)-2)/3,1),xytext=(.75,1.65),fontsize=10,color='#c92a2a',arrowprops=dict(arrowstyle='->',color='#c92a2a'))
ax.annotate('Critical central limit',xy=(0,1),xytext=(.3,.45),fontsize=10,color='#2b8a3e',arrowprops=dict(arrowstyle='->',color='#2b8a3e'))
ax.set(xlim=(0,2.7),ylim=(0,3.8),xlabel=r'$r\,v_{s0}^{\,2}/(GM)$',ylabel=r'$\mathcal{M}=|u_r|/v_s$')
ax.set_title(r'Monatomic accretion: $\gamma=5/3$')
ax.grid(alpha=.18);ax.legend(loc='upper right',fontsize=10)
fig.text(.51,.025,'Solid: subsonic branch. Dashed: supersonic branch with the wrong outer state.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.055,1,1))
fig.savefig('paper-70-bondi-branches.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
