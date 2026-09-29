"""Write the three opaque surface sketches to cwd, without media mirroring.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(10,4),dpi=100,facecolor='white')
fig.subplots_adjust(left=.02,right=.92,bottom=.05,top=.82,wspace=.08)
for i,(lam,name) in enumerate([(.5,'Disk cap'),(1.,'Cone'),(2.,'Annular strip')],1):
 ax=fig.add_subplot(1,3,i,projection='3d');z=np.linspace(np.sqrt(max(1-lam,0)),1,45);phi=np.linspace(0,2*np.pi,90)
 zz,pp=np.meshgrid(z,phi);rr=np.sqrt(np.maximum(zz**2+lam-1,0));xx=rr*np.cos(pp);yy=rr*np.sin(pp)
 ax.plot_surface(xx,yy,zz,color='#86b6d5',edgecolor='none',alpha=1,shade=True)
 angle=np.linspace(0,2*np.pi,200);ro=np.sqrt(lam)
 ax.plot(ro*np.cos(angle),ro*np.sin(angle),np.ones_like(angle),color='#b66212',lw=2.2)
 if lam>1:
  ri=np.sqrt(lam-1);ax.plot(ri*np.cos(angle),ri*np.sin(angle),np.zeros_like(angle),color='#285b8f',lw=2.2)
 else:ax.scatter([0],[0],[z[0]],color='#285b8f',s=18)
 ax.plot([0,0],[0,0],[0,1.12],color='#555555',ls=':',lw=1)
 ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),zlim=(0,1.12),xlabel='x',ylabel='y',zlabel='z')
 ax.set_zlabel('z',labelpad=0);ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_zticks([0,1]);ax.tick_params(labelsize=8,pad=0)
 ax.set_title(name+'\n'+r'$\lambda='+str(lam)+r'$',fontsize=11);ax.view_init(elev=24,azim=-55);ax.set_box_aspect((1,1,.8))
fig.suptitle('Outer boundary at z = 1; an inner boundary appears only for λ > 1',fontsize=13,y=.96)
fig.savefig(Path.cwd()/'paper-3-stokes-surfaces.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
