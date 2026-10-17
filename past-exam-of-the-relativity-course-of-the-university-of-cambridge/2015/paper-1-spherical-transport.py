"""Original educational diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Save the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
fig=plt.figure(figsize=(7.2,5.3),layout='constrained');ax=fig.add_subplot(projection='3d')
phi=np.linspace(0,2*np.pi,50);theta=np.linspace(0,np.pi,30)
x=np.outer(np.cos(phi),np.sin(theta));y=np.outer(np.sin(phi),np.sin(theta));z=np.outer(np.ones_like(phi),np.cos(theta))
ax.plot_wireframe(x,y,z,rcount=12,ccount=10,color='.7',alpha=.25,lw=.5)
t=np.linspace(0,np.pi/2,150)
for xyz in [(np.sin(t),0*t,np.cos(t)),(np.cos(t),np.sin(t),0*t),(0*t,np.cos(t),np.sin(t))]:
 ax.plot(*xyz,color='#2563a6',lw=3)
N=np.array([0.,0.,1.]);A=np.array([1.,0.,0.]);B=np.array([0.,1.,0.])
for p,v,label,color in [(N,[1,0,0],'initial','#d17625'),(A,[0,0,-1],'transported','#258a62'),(B,[0,0,-1],'transported','#258a62'),(N,[0,1,0],'returned','#ac4384')]:
 v=np.array(v)*.42
 ax.quiver(*p,*v,color=color,arrow_length_ratio=.22,lw=2.3)
 ax.text(*(p+1.1*v),label,color=color,fontsize=9)
for p,label in [(N,'N'),(A,'A'),(B,'B')]:ax.scatter(*p,c='black',s=15);ax.text(*(p*.9),label)
# Direction markers on each leg.
for p,v in [(np.array([.707,0,.707]),np.array([.707,0,-.707])),(np.array([.707,.707,0]),np.array([-.707,.707,0])),(np.array([0,.707,.707]),np.array([0,-.707,.707]))]:
 ax.quiver(*p,*(.14*v),color='#2563a6',arrow_length_ratio=.65,lw=1.8)
ax.set(xlim=(-1.1,1.6),ylim=(-1.1,1.6),zlim=(-1.1,1.5),title=r'Parallel transport: $N\to A\to B\to N$')
ax.text2D(.02,.01,r'Enclosed area $=\pi a^2/2$; returning vector rotates by $90^\circ$.',transform=ax.transAxes,fontsize=10)
ax.view_init(elev=24,azim=34);ax.set_box_aspect([1,1,1]);ax.set_axis_off()
fig.savefig('paper-1-spherical-transport.png',dpi=170)
