"""Original 6A contour sketch. Tested Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Caller supplies MPLCONFIGDIR; emit PNG basename to cwd.
"""
import os
from pathlib import Path
if 'MPLCONFIGDIR' not in os.environ:
    raise RuntimeError('Supply a caller-owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1.72,1.72,721);y=np.linspace(-2.85,2.85,901)
X,Y=np.meshgrid(x,y);V=X**4-X**2+2*X*Y+Y**2
fig,ax=plt.subplots(figsize=(7.4,6.2),dpi=100,facecolor='white')
ax.set_facecolor('white')
levels=[-.9,-.65,-.25,.5,1.5]
cs=ax.contour(X,Y,V,levels=levels,colors=['#286b5e','#41996b','#80af54','#658cc3','#ae81b3'],linewidths=1.25)
ax.clabel(cs,fmt='%g',fontsize=9,inline=True)
zero=ax.contour(X,Y,V,levels=[0],colors=['#333333'],linewidths=1.9)
ax.clabel(zero,fmt={0:'V = 0'},fontsize=10,inline=True)
def f(u):
    a,b=u;return np.array([-4*a**3+2*a-2*b,-2*a-2*b])
u=np.array([1.,-.5]);path=[u.copy()];h=.005
for j in range(1600):
    k1=f(u);k2=f(u+h*k1/2);k3=f(u+h*k2/2);k4=f(u+h*k3)
    u=u+h*(k1+2*k2+2*k3+k4)/6;path.append(u.copy())
path=np.array(path)
ax.plot(path[:,0],path[:,1],color='#be4c28',lw=2.2,label='trajectory from (1, −1/2)')
ax.annotate('',xy=path[80],xytext=path[25],arrowprops=dict(arrowstyle='->',color='#be4c28',lw=2))
ax.scatter([1,-1],[-1,1],marker='*',s=125,color='#a92529',edgecolor='white',linewidth=.5,zorder=6,label='minima: V = −1')
ax.scatter([0],[0],marker='x',s=50,color='#111111',linewidth=1.8,zorder=6,label='saddle: V = 0')
ax.scatter([1],[-.5],s=34,facecolor='white',edgecolor='#be4c28',linewidth=1.5,zorder=6)
ax.set(xlim=(-1.72,1.72),ylim=(-2.85,2.85),xlabel='x',ylabel='y',title='Contours of a sheared quartic double well')
ax.set_aspect('equal',adjustable='box')
ax.legend(loc='upper right',fontsize=9,framealpha=.95)
ax.grid(alpha=.12)
fig.tight_layout()
fig.savefig(Path('paper-2-double-well-contours.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
