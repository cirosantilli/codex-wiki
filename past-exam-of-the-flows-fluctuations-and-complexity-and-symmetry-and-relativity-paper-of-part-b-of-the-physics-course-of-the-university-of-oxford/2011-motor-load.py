"""Generate the corrected physical motor-load construction; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Illustrative dimensionless ratio d=gamma*k1*x1/Fmax, chosen as 0.5.
d=.5
s=np.linspace(0,1.8,1601)
m=np.ones_like(s);m[1:]=-np.expm1(-1/s[1:])
def root(load):
 lo=0.;hi=1.8
 for _ in range(70):
  mid=(lo+hi)/2
  if -np.expm1(-1/mid)-d*mid-load>0:lo=mid
  else:hi=mid
 return (lo+hi)/2
s0=root(0);sh=root(.5)
fig,ax=plt.subplots(figsize=(7.5,4.8),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.plot(s,m,color='#1764a0',lw=2,label=r'Motor force $F_m/F_{\max}$')
ax.plot(s,d*s,color='#bd4b1d',lw=1.8,label=r'Drag magnitude $\gamma u/F_{\max}$')
ax.plot(s,d*s+.5,color='#bd4b1d',ls='--',lw=1.5,label=r'$\gamma u/F_{\max}+1/2$')
ax.plot(s,-d*s,color='.55',ls=':',lw=1.4,label=r'Signed drag $-\gamma u/F_{\max}$')
for sp,lab in [(sh,r'$u_{1/2}$'),(s0,r'$u_0$')]:
 yy=-np.expm1(-1/sp)
 ax.plot([sp,sp],[0,yy],ls='--',lw=1,color='.35');ax.scatter([sp],[yy],color='black',s=22,zorder=4)
 ax.annotate(lab,xy=(sp,0),xytext=(0,-20),textcoords='offset points',ha='center')
ax.axhline(0,color='.3',lw=.8)
ax.set(xlim=(0,1.8),ylim=(-.55,1.45),xlabel=r'Speed $u/(k_1x_1)$',ylabel=r'Force / $F_{\max}$',title=r'Physical balance: $F_m-\gamma u=-F_{\rm ext}$')
ax.set_yticks([-.5,0,.5,1],['−0.5','0','0.5','1'])
ax.legend(loc='upper right',fontsize=8.5,framealpha=1)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white',transparent=False)
