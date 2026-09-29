"""Upper hemispherical shell sketch. Python 3.14; root matplotlib/numpy; cwd PNG only."""
from pathlib import Path
import os
if not os.environ.get('MPLCONFIGDIR'):raise RuntimeError('Supply an owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(9,5.2),dpi=100,facecolor='white');ax=fig.add_subplot(1,2,1);view=fig.add_subplot(1,2,2,projection='3d')
theta=np.linspace(0,np.pi,400)
ax.fill(np.r_[3*np.cos(theta),2*np.cos(theta[::-1])],np.r_[3*np.sin(theta),2*np.sin(theta[::-1])],color='#dceaf4')
for rad,col in [(3,'#235f91'),(2,'#558cb5')]:
 ax.plot(rad*np.cos(theta),rad*np.sin(theta),lw=2,color=col)
ax.plot([-3,-2],[0,0],color='#235f91',lw=2);ax.plot([2,3],[0,0],color='#235f91',lw=2)
ax.axvline(0,color='#777777',ls=':',lw=1);ax.text(.1,3.15,'z',fontsize=11)
ax.text(-1.5,1.05,'Excluded inner half-ball',fontsize=9);ax.text(-2.7,2.3,'2 < r < 3',fontsize=10)
ax.set_aspect('equal');ax.set_xlim(-3.4,3.4);ax.set_ylim(-.2,3.5);ax.set_xlabel('Meridian coordinate');ax.set_ylabel('z')
ax.set_title('Meridian section: rotate about z',fontsize=11);ax.grid(alpha=.13)
# Remove one quarter in the 3D view to expose the shell interior; the region itself is complete.
ph=np.linspace(.05,1.5*np.pi,90);th=np.linspace(0,np.pi/2,55);P,T=np.meshgrid(ph,th)
for rad,col in [(3,'#75a7c9'),(2,'#b4d1e3')]:
 view.plot_surface(rad*np.sin(T)*np.cos(P),rad*np.sin(T)*np.sin(P),rad*np.cos(T),color=col,linewidth=0,shade=True,alpha=1)
RR,PP=np.meshgrid(np.linspace(2,3,12),ph)
view.plot_surface(RR*np.cos(PP),RR*np.sin(PP),np.zeros_like(RR),color='#387caa',linewidth=0,alpha=1)
for rad in [2,3]:view.plot(rad*np.cos(ph),rad*np.sin(ph),np.zeros_like(ph),color='#24577b',lw=1)
view.set_xlim(-3,3);view.set_ylim(-3,3);view.set_zlim(0,3.2);view.set_box_aspect((1,1,.65));view.set_xlabel('x');view.set_ylabel('y');view.set_zlabel('z')
view.view_init(elev=25,azim=-55);view.set_title('Cutaway upper shell',fontsize=11);view.set_xticks([-3,0,3]);view.set_yticks([-3,0,3]);view.set_zticks([0,2,3])
fig.suptitle('Upper hemispherical shell: 2 <= r <= 3, z >= 0',fontsize=13,y=.96)
fig.subplots_adjust(left=.07,right=.97,top=.84,bottom=.15,wspace=.15)
fig.text(.5,.04,'The flat boundary is an annulus at z = 0. Cutaway is for visibility only.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False);plt.close(fig)
