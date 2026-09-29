"""Original critical-point illustrations; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Write opaque paper-25-critical-points.png to caller CWD; preserve MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(11,4.6),dpi=120,facecolor='white')
u=np.linspace(0,np.pi,401);U,V=np.meshgrid(u,u)
H=np.sin(U)*np.sin(V)*np.sin(U-V)
axes[0].contourf(U,V,H,levels=np.linspace(-.66,.66,23),cmap='RdBu_r')
axes[0].contour(U,V,H,levels=[0],colors='#333',linewidths=.9)
axes[0].scatter([np.pi/3,2*np.pi/3],[2*np.pi/3,np.pi/3],color=['#1769aa','#be3030'],s=35,edgecolor='white',zorder=5)
axes[0].text(np.pi/3,2*np.pi/3+.2,'min',ha='center',color='white',fontsize=10)
axes[0].text(2*np.pi/3,np.pi/3+.2,'max',ha='center',color='white',fontsize=10)
axes[0].scatter([0,np.pi,0,np.pi],[0,0,np.pi,np.pi],color='#202020',s=35,zorder=6,clip_on=False)
axes[0].set(xticks=[0,np.pi/2,np.pi],xticklabels=['0',r'$\pi/2$',r'$\pi$'],yticks=[0,np.pi/2,np.pi],yticklabels=['0',r'$\pi/2$',r'$\pi$'],xlabel='$u$',ylabel='$v$',title='Torus function: three critical points')
axes[0].text(.5,-.31,'Opposite edges identified; four corners are one point',transform=axes[0].transAxes,ha='center',fontsize=8)
x=np.linspace(-1,1,350);X,Y=np.meshgrid(x,x)
for ax,t,title in zip(axes[1:],[0,.6],['One degenerate saddle','Two ordinary saddles']):
 Z=X**3-3*X*Y**2-t*X
 ax.contourf(X,Y,Z,levels=np.linspace(-2.2,2.2,31),cmap='RdBu_r')
 ax.contour(X,Y,Z,levels=[0],colors='#333',linewidths=.8)
 if t==0:ax.scatter([0],[0],s=35,color='black',zorder=5)
 else:ax.scatter([-np.sqrt(t/3),np.sqrt(t/3)],[0,0],s=35,color='black',zorder=5)
 ax.set(xlabel='$x$',ylabel='$y$',title=title,aspect='equal')
 ax.text(.5,-.31,r'$x^3-3xy^2-tx$'+f', t={t:g}',transform=ax.transAxes,ha='center',fontsize=9)
for ax in axes:ax.set_aspect('equal')
fig.tight_layout(rect=(0,.12,1,.93));fig.savefig('paper-25-critical-points.png',facecolor='white',transparent=False);plt.close(fig)
