"""Original explanatory figure. Python 3.14, numpy and matplotlib.
Writes one PNG basename to cwd; no source-image pixels or hardcoded media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(12,4),layout='constrained');a=fig.add_subplot(131,projection='3d');b=fig.add_subplot(132);c=fig.add_subplot(133)
u=np.linspace(0,2*np.pi,200);a.plot(np.cos(u),np.sin(u),np.zeros_like(u),color='lightgray');a.plot(np.zeros_like(u),np.sin(u),np.cos(u),color='lightgray')
q=np.linspace(0,np.pi/2,100);a.plot(np.zeros_like(q),-np.sin(q),np.cos(q),color='#1766a5',lw=3,label='First pulse');a.plot(np.sin(u),-np.cos(u),np.zeros_like(u),color='#c33c29',lw=2,label='Dark interval');a.plot(np.zeros_like(q),-np.cos(q),-np.sin(q),color='#398447',lw=3,label='Second pulse');a.scatter([0,0],[0,0],[1,-1],color='black');a.set(xlabel='x',ylabel='y',zlabel='z',title=r'Ideal sequence: $\delta T=2\pi$');a.set_xticks([]);a.set_yticks([]);a.set_zticks([]);a.set_box_aspect((1,1,1));a.view_init(20,35);a.legend(loc='upper left',fontsize=7,frameon=False)
t=np.linspace(0,18,1200);env=np.exp(-(.2*t)**2/2);rx=env*np.sin(t);ry=-env*np.cos(t);b.plot(np.cos(u),np.sin(u),color='lightgray');b.plot(rx,ry,color='#1766a5',lw=2);b.plot(0,-1,'ko');b.set(xlabel=r'$\overline{R}_x$',ylabel=r'$\overline{R}_y$',aspect='equal',title='Average spirals inward');b.text(-1.05,1.08,r'Illustration: Gaussian RMS $0.2\delta$',fontsize=8)
c.plot(t,(1+np.cos(t))/2,color='gray',alpha=.6,label='No spread');c.plot(t,(1+env*np.cos(t))/2,color='#1766a5',lw=2,label='Gaussian example');c.plot(t,(1+env)/2,'--',color='#c33c29',lw=.8);c.plot(t,(1-env)/2,'--',color='#c33c29',lw=.8);c.set(xlabel=r'$\delta T$',ylabel=r'$\overline{p}_2$',ylim=(-.03,1.04),title='Ensemble fringe contrast');c.legend(frameon=False,fontsize=8)
fig.savefig('paper-1-ramsey.png',dpi=165);plt.close(fig)
