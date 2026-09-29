"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Writes one PNG basename to cwd; no source-image pixels or hardcoded media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
def sphere(ax):
 u=np.linspace(0,2*np.pi,100)
 for z in [-.6,0,.6]:
  r=np.sqrt(1-z*z);ax.plot(r*np.cos(u),r*np.sin(u),np.full_like(u,z),color='lightgray',lw=.6)
 for ph in [0,np.pi/2]:ax.plot(np.cos(ph)*np.sin(u),np.sin(ph)*np.sin(u),np.cos(u),color='lightgray',lw=.6)
 ax.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),zlim=(-1.1,1.1),xlabel='x',ylabel='y',zlabel='z');ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([]);ax.set_box_aspect((1,1,1));ax.grid(False);ax.view_init(20,35)
fig=plt.figure(figsize=(11,4.2),layout='constrained');a=fig.add_subplot(131,projection='3d');b=fig.add_subplot(132,projection='3d');c=fig.add_subplot(133)
sphere(a);a.quiver(0,0,0,1,0,0,color='#1766a5',linewidth=2);a.scatter([0],[0],[.5],color='#c33c29',s=40);a.text(1,0,0,'pure +x',fontsize=9);a.text(0,0,.55,'mixture',fontsize=9);a.set_title('Unit pure state; shorter mixed state')
sphere(b);t=np.linspace(0,2*np.pi,500)
for d,col,lab in [(0,'#1766a5','resonant limit'),(1,'#c33c29',r'$\delta=\Omega$')]:
 W=np.sqrt(1+d*d);xx=d/(W*W)*(1-np.cos(W*t));yy=-np.sin(W*t)/W;zz=(d*d+np.cos(W*t))/(W*W);b.plot(xx,yy,zz,color=col,lw=2,label=lab);c.plot(t,(1-zz)/2,color=col,label=lab)
b.set_title('Rotation about the Rabi vector');c.set(xlabel=r'$\Omega t$',ylabel=r'$p_2$',ylim=(-.03,1.05),title='Population transfer');c.legend(frameon=False,fontsize=9)
fig.savefig('paper-1-rabi-bloch.png',dpi=165);plt.close(fig)
