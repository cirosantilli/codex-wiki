"""Original contours and gradient path; Python 3.14, NumPy 2.3,
Matplotlib 3.10, SciPy 1.16. The PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

plt.rcParams.update({'font.size':11,'figure.facecolor':'white'})
x=np.linspace(-2.6,2.6,650);y=np.linspace(-3.3,4.1,700)
X,Y=np.meshgrid(x,y)
F=2*(Y-X*X)/(1+X*X+Y*Y)

def grad(t,q):
    x,y=q;d=1+x*x+y*y
    return np.array([-4*x*(1+y+y*y),2*(1+x*x-y*y+2*x*x*y)])/d**2
sol=solve_ivp(grad,(0,16),[1.,1.],rtol=1e-10,atol=1e-12,dense_output=True)
path=sol.sol(np.linspace(0,16,650))
values=2*(path[1]-path[0]**2)/(1+path[0]**2+path[1]**2)
if np.min(np.diff(values)) < -1e-9:
    raise ValueError('Gradient trajectory does not increase f')
fig,ax=plt.subplots(figsize=(6.8,7.0),layout='constrained')
levels=[-1.8,-1.5,-1.2,-.8,-.4,.3,.6,.85,.95]
cs=ax.contour(X,Y,F,levels=levels,cmap='coolwarm',linewidths=1.1)
ax.clabel(cs,inline=True,fontsize=9,fmt='%g')
ax.plot(x,x*x,color='#38814d',lw=1.8,label='$f=0$')
ax.plot(x,-1+x,'--',color='0.35',lw=1.2,label='$f=-1$')
ax.plot(x,-1-x,'--',color='0.35',lw=1.2)
ax.plot(path[0],path[1],color='#c02a2a',lw=2.5,label='ascending trajectory')
ax.annotate('',xy=sol.sol(.42),xytext=sol.sol(.16),arrowprops={'arrowstyle':'->','color':'#c02a2a','lw':2})
ax.plot(1,1,'o',color='#c02a2a',ms=5)
ax.annotate('start $(1,1)$',xy=(1,1),xytext=(1.25,1.48),arrowprops={'arrowstyle':'-','color':'#c02a2a'},color='#a62727',fontsize=10)
ax.plot([0,0],[1,-1],'*',color='black',ms=10)
ax.annotate('maximum',xy=(0,1),xytext=(-1.45,1.35),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
ax.annotate('saddle',xy=(0,-1),xytext=(.55,-1.45),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
ax.set(xlim=(-2.6,2.6),ylim=(-3.3,4.1),aspect='equal',xlabel='$x$',ylabel='$y$',title=r'Level sets of $2(y-x^2)/(1+x^2+y^2)$')
ax.legend(loc='upper left',frameon=True,fontsize=9)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
