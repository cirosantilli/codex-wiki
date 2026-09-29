"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

th=np.linspace(0,2*np.pi,800);rp=(2-(np.cos(2*th)+2*np.sin(2*th))/5)**-.5;fig,ax=plt.subplots(figsize=(5.8,5.5),layout='constrained')
for r,label,ls in [(1/np.sqrt(3),'Inner limiting circle','--'),(1,'Outer limiting circle',':')]:ax.plot(r*np.cos(th),r*np.sin(th),ls=ls,color='.5',label=label)
ax.plot(rp*np.cos(th),rp*np.sin(th),color='#227caa',lw=2,label='Stable periodic orbit');xx=np.linspace(-1.2,1.2,38);X,Y=np.meshgrid(xx,xx);G=X*X+3*Y*Y;U=X-2*Y-X*G;V=2*X+Y-Y*G;ax.streamplot(X,Y,U,V,color='.8',density=.65,linewidth=.6);ax.scatter([0],[0],facecolors='white',edgecolors='black',s=30);ax.set(xlabel='x',ylabel='y',title='Constant angular speed; modulated stable radius',xlim=(-1.2,1.2),ylim=(-1.2,1.2));ax.set_aspect('equal');ax.legend(fontsize=8,loc='upper left')
fig.savefig(Path.cwd()/'2009-polar-limit-cycle.png',dpi=150,facecolor='white');plt.close(fig)
