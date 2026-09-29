"""Original spherical-coordinate sketch. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run in the mirrored _media directory; PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

P=np.array([np.sqrt(3)/4,3/4,3/2]);Q=P*np.array([1,1,0])
fig=plt.figure(figsize=(6.4,5.5),layout='constrained',facecolor='white')
ax=fig.add_subplot(projection='3d')
for end,label in [(np.array([1.25,0,0]),'$x$'),(np.array([0,1.25,0]),'$y$'),(np.array([0,0,1.85]),'$z$')]:
    ax.quiver(0,0,0,*end,color='#444444',arrow_length_ratio=.06,lw=1)
    ax.text(*end,label,fontsize=12)
ax.plot([0,P[0]],[0,P[1]],[0,P[2]],color='#0072b2',lw=2)
ax.plot([P[0],Q[0]],[P[1],Q[1]],[P[2],0],color='#888888',ls='--')
ax.plot([0,Q[0]],[0,Q[1]],[0,0],color='#888888',ls='--')
ax.scatter(*P,color='#d55e00',s=30);ax.text(*(P+np.array([.03,.03,.08])),'$P$',fontsize=12)
phi=np.linspace(0,np.pi/3,100);rho=.48
ax.plot(rho*np.cos(phi),rho*np.sin(phi),np.zeros_like(phi),color='#009e73',lw=2)
ax.text(.44,.13,.02,r'$\phi=\pi/3$',color='#007a55',fontsize=11)
theta=np.linspace(0,np.pi/6,100);r=.7
ax.plot(r*np.sin(theta)*.5,r*np.sin(theta)*np.sqrt(3)/2,r*np.cos(theta),color='#cc79a7',lw=2)
ax.text(.03,.12,.81,r'$\theta=\pi/6$',color='#a34f8c',fontsize=11)
ax.text(0,0,-.12,'$O$',fontsize=11)
ax.set(xlim=(-.05,1.35),ylim=(-.05,1.35),zlim=(-.12,1.98))
ax.set_box_aspect((1,1,1.35));ax.view_init(elev=24,azim=-55)
ax.set_axis_off();ax.set_title(r'Polar angle from $+z$; azimuth from $+x$ toward $+y$')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
