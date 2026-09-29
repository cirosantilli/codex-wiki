"""Cylinder/cone oriented surface sketch; only own PNG basename in cwd."""
from pathlib import Path
import os
if not os.environ.get('MPLCONFIGDIR'):raise RuntimeError('Supply an owned MPLCONFIGDIR')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(8.2,5.2),dpi=100,facecolor='white');ax=fig.add_subplot(1,2,1,projection='3d');side=fig.add_subplot(1,2,2)
# A front half opening makes the absence of a base disk clear.
th=np.linspace(0,1.55*np.pi,70);z=np.linspace(-2,2,40);T,Z=np.meshgrid(th,z)
ax.plot_surface(2*np.cos(T),2*np.sin(T),Z,color='#82aecb',shade=True,linewidth=0)
z=np.linspace(2,4,40);T,Z=np.meshgrid(th,z);R=4-Z
ax.plot_surface(R*np.cos(T),R*np.sin(T),Z,color='#b3c8af',shade=True,linewidth=0)
full=np.linspace(0,2*np.pi,300)
ax.plot(2*np.cos(full),2*np.sin(full),np.full_like(full,-2),color='#a54035',lw=2)
ax.plot(2*np.cos(full),2*np.sin(full),np.full_like(full,2),color='#567562',lw=1)
ax.quiver(0,-2,-2,.8,0,0,color='#a54035',arrow_length_ratio=.25,linewidth=1.5)
ax.quiver(2,0,0,.7,0,0,color='#333333',arrow_length_ratio=.25,linewidth=1.3)
ax.quiver(1,0,3,.45,0,.45,color='#333333',arrow_length_ratio=.25,linewidth=1.3)
ax.set_xlim(-2.7,2.7);ax.set_ylim(-2.7,2.7);ax.set_zlim(-2.3,4.5);ax.set_box_aspect((1,1,1.2));ax.view_init(elev=18,azim=-55)
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z');ax.set_title('Cutaway with outward normals',fontsize=10);ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);ax.set_zticks([-2,0,2,4])
side.plot([-2,-2,0,2,2],[-2,2,4,2,-2],color='#286890',lw=2)
side.plot([-2,2],[-2,-2],color='#a54035',ls=':',lw=1.2)
side.text(-1.8,-1.65,'Open base: boundary only',fontsize=9)
side.text(-1.35,.4,'Cylindrical side',fontsize=10);side.text(-1.0,2.65,'Conical roof',fontsize=10)
side.set_aspect('equal');side.set_xlim(-2.6,2.6);side.set_ylim(-2.5,4.6);side.set_xlabel('Meridian coordinate');side.set_ylabel('z');side.grid(alpha=.15);side.set_title('Meridian outline',fontsize=10)
fig.suptitle('Outward cylinder/cone surface with an open bottom',fontsize=13,y=.96)
fig.subplots_adjust(left=.03,right=.97,top=.84,bottom=.17,wspace=.12)
fig.text(.5,.045,'Red boundary is counterclockwise viewed from +z. No bottom disk is included in S.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False);plt.close(fig)
