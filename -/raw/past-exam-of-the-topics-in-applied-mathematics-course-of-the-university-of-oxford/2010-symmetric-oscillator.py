"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

Om=-2
def field(x,y):return y,x-Om*y-x**3-x*x*y
def orbit(x,y,T=80,dt=.003):
 out=[]
 for i in range(int(T/dt)):
  if i%5==0:out.append((x,y))
  a=field(x,y);b=field(x+dt*a[0]/2,y+dt*a[1]/2);c=field(x+dt*b[0]/2,y+dt*b[1]/2);d=field(x+dt*c[0],y+dt*c[1]);x+=dt*(a[0]+2*b[0]+2*c[0]+d[0])/6;y+=dt*(a[1]+2*b[1]+2*c[1]+d[1])/6
 return np.array(out)
fig,ax=plt.subplots(figsize=(7.2,5.5),layout='constrained');x=np.linspace(-2.8,2.8,36);y=np.linspace(-9,9,45);X,Y=np.meshgrid(x,y);U,V=field(X,Y);ax.streamplot(X,Y,U,V,color='.82',density=.75,linewidth=.6,arrowsize=.7)
for ic in [(1.03,0),(-1.03,0),(.02,.05),(2.5,0)]:
 q=orbit(*ic);ax.plot(q[:,0],q[:,1],lw=.7,alpha=.8)
q=orbit(2.5,0);q=q[len(q)*3//4:];ax.plot(q[:,0],q[:,1],color='black',lw=2,label='Attracting cycle')
for lam,ls,name in [(1-np.sqrt(2),'--','Stable saddle direction'),(1+np.sqrt(2),':','Unstable saddle direction')]:
 xx=np.linspace(-.35,.35,60);ax.plot(xx,lam*xx,ls=ls,color='black',label=name)
ax.scatter([0],[0],marker='x',color='black',s=55);ax.scatter([-1,1],[0,0],facecolors='white',edgecolors='black',s=45,zorder=5);ax.set(xlabel='x',ylabel='y',title='Half-turn symmetry, not time reversibility',xlim=(-2.8,2.8),ylim=(-9,9));ax.legend(fontsize=8,loc='upper left')
fig.savefig(Path.cwd()/'2010-symmetric-oscillator.png',dpi=150,facecolor='white');plt.close(fig)
