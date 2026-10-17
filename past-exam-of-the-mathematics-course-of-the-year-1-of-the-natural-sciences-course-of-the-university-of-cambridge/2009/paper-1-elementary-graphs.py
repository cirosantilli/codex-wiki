"""Original graph sketches for IA 2009; write PNG into the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,3,figsize=(12,4),facecolor='white')
x=np.linspace(.025,8,900);axes[0].plot(x,np.log(x)**2,color='#247ba0',lw=2)
axes[0].scatter([1,np.e],[0,1],color='#ba3434',zorder=3)
axes[0].annotate('(1, 0)',(1,0),xytext=(1.25,.6));axes[0].annotate('(e, 1)',(np.e,1),xytext=(3.3,1.5))
axes[0].set(xlim=(0,8),ylim=(-.25,6),title=r'$y=(\log x)^2$',xlabel='x',ylabel='y')
x=np.linspace(-np.pi,np.pi,900);axes[1].plot(x,.5*np.sin(2*x),color='#247ba0',lw=2)
axes[1].set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$','0',r'$\pi/2$',r'$\pi$'])
axes[1].set(ylim=(-.7,.7),title=r'$y=\sin x\cos x$',xlabel='x',ylabel='y')
t=np.linspace(0,2*np.pi,600);axes[2].plot(np.cos(t),2*np.sin(t),color='#247ba0',lw=2)
for a in [0,np.pi/2,np.pi,3*np.pi/2]:
    b=a+.15;axes[2].annotate('',(np.cos(b),2*np.sin(b)),(np.cos(a),2*np.sin(a)),arrowprops={'arrowstyle':'->','color':'#ba3434','lw':2})
axes[2].scatter([1],[0],color='#ba3434');axes[2].annotate('t=0',(1,0),xytext=(1.15,.2))
axes[2].set(xlim=(-1.7,1.7),ylim=(-2.4,2.4),aspect='equal',title=r'$(x,y)=(\cos t,2\sin t)$',xlabel='x',ylabel='y')
for ax in axes:ax.grid(alpha=.2);ax.axhline(0,color='gray',lw=.6);ax.axvline(0,color='gray',lw=.6)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white');plt.close(fig)
