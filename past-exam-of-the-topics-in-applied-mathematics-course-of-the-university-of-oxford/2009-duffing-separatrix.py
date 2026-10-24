"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(7,4.8),layout='constrained');x=np.linspace(-1.8,1.8,500);y=np.linspace(-1.6,1.6,450);X,Y=np.meshgrid(x,y);E=Y*Y/2-X*X/2+X**4/4;cs=ax.contour(X,Y,E,levels=[-.2,-.1,.2,.7],colors=['#538daa'],linewidths=.9);ax.clabel(cs,fontsize=8);ax.contour(X,Y,E,levels=[0],colors='black',linewidths=2);xx=np.linspace(-1.8,1.8,25);yy=np.linspace(-1.6,1.6,23);XX,YY=np.meshgrid(xx,yy);U=YY;V=XX-XX**3;N=np.sqrt(U*U+V*V);ax.quiver(XX,YY,U/(N+.01),V/(N+.01),alpha=.3,scale=45);ax.scatter([-1,1],[0,0],color='#227caa',s=35);ax.scatter([0],[0],marker='x',color='black',s=50);ax.set(xlabel='x',ylabel='y',title='Conserved energy: centres and a figure-eight separatrix');ax.set_aspect('equal')
fig.savefig(Path.cwd()/'2009-duffing-separatrix.png',dpi=150,facecolor='white');plt.close(fig)
