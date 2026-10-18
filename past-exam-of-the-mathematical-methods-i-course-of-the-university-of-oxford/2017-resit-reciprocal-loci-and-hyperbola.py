"""Original exact geometric plots. Python 3.14; NumPy 2.3; Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,ax=plt.subplots(1,2,figsize=(10.2,4.8),layout='constrained');a=np.linspace(0,2*np.pi,1001)
ax[0].plot(.5+.5*np.cos(a),.5*np.sin(a),label=r'$\operatorname{Re}(1/z)=1$')
ax[0].plot(.5*np.cos(a),-.5+.5*np.sin(a),label=r'$\operatorname{Im}(1/z)=1$')
ax[0].plot(np.cos(a),np.sin(a),color='.4',ls='--',label='unit circle')
ax[0].plot(0,0,'o',mfc='white',mec='black',ms=7,zorder=5);ax[0].annotate('excluded',xy=(0,0),xytext=(-.9,.25),arrowprops={'arrowstyle':'->'},fontsize=10)
ax[0].plot(.5,-.5,'o',color='black',ms=5);ax[0].annotate('right-angle crossing',xy=(.5,-.5),xytext=(-1.05,-.75),arrowprops={'arrowstyle':'->'},fontsize=9)
ax[0].plot([1,0],[0,-1],'o',color='.4',ms=4)
ax[0].set(xlim=(-1.15,1.2),ylim=(-1.2,1.15),xlabel=r'$x=\operatorname{Re}z$',ylabel=r'$y=\operatorname{Im}z$',title='Two reciprocal loci');ax[0].legend(fontsize=8,loc='upper left');ax[0].set_aspect('equal');ax[0].grid(alpha=.18)
q=np.array([[2,-1],[1,2]])/np.sqrt(5);t=np.linspace(-2.5,2.5,1001)
for sign in [-1,1]:
 uv=np.array([sign*np.sqrt(2)*np.cosh(t),np.sqrt(3)*np.sinh(t)]);xy=q@uv
 ax[1].plot(*xy,color='tab:blue',lw=2,label=r'$2x^2+4xy-y^2=6$' if sign==1 else None)
x=np.linspace(-6,6,101)
for m in [2+np.sqrt(6),2-np.sqrt(6)]:ax[1].plot(x,m*x,'--',color='.5',lw=1,label='asymptotes' if m>0 else None)
for col,label in [(0,"x′"),(1,"y′")]:
 v=q[:,col];ax[1].annotate('',xy=3.5*v,xytext=-3.5*v,arrowprops={'arrowstyle':'->','color':'tab:red','lw':1});ax[1].text(*(3.7*v),label,color='tab:red')
ax[1].set(xlim=(-5,5),ylim=(-5,5),xlabel=r'$x$',ylabel=r'$y$',title='Orthogonal principal axes');ax[1].set_aspect('equal');ax[1].legend(fontsize=9,loc='lower right');ax[1].grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
plt.close(fig)
