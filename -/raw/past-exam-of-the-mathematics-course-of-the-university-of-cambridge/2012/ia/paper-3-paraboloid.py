"""Original solution sketch. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only paper-3-paraboloid.png to cwd; preserves caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
fig=plt.figure(figsize=(11,5.4),dpi=100,layout='constrained')
a=fig.add_subplot(121,projection='3d',computed_zorder=False);b=fig.add_subplot(122)
r=np.linspace(1/3,1,32);theta=np.linspace(0,2*np.pi,100);R,T=np.meshgrid(r,theta)
a.plot_surface(R*np.cos(T),R*np.sin(T),R**2,color='#8abbd3',edgecolor='none',alpha=1)
for rr,col in [(1,'#b52b40'),(1/3,'#1857b2')]:
 a.plot(rr*np.cos(theta),rr*np.sin(theta),np.full_like(theta,rr**2),color=col,lw=3)
a.quiver(.7,-.7,.98,-1.4,1.4,1,length=.5,normalize=True,color='black',linewidth=2,zorder=10)
a.text(.35,-.4,1.28,'upward normal',fontsize=9,zorder=20)
a.set(xlabel='x',ylabel='y',zlabel='z',zlim=(0,1.4),title='Open paraboloid band: 1/9 ≤ z ≤ 1')
a.view_init(elev=27,azim=-57);a.set_box_aspect((2,2,1.3))
b.add_patch(Wedge((0,0),1,0,360,width=2/3,facecolor='#dcebf2',edgecolor='none'))
for rr,col in [(1,'#b52b40'),(1/3,'#1857b2')]:b.plot(rr*np.cos(theta),rr*np.sin(theta),color=col,lw=2)
for angle in [np.pi/6,7*np.pi/6]:
 b.annotate('',xy=(np.cos(angle+.4),np.sin(angle+.4)),xytext=(np.cos(angle),np.sin(angle)),arrowprops=dict(arrowstyle='->',color='#b52b40',lw=2,connectionstyle='arc3,rad=.2'))
for angle in [np.pi/6,7*np.pi/6]:
 b.annotate('',xy=(np.cos(angle-.5)/3,np.sin(angle-.5)/3),xytext=(np.cos(angle)/3,np.sin(angle)/3),arrowprops=dict(arrowstyle='->',color='#1857b2',lw=2,connectionstyle='arc3,rad=-.2'))
b.text(0,1.2,'outer boundary: counterclockwise',ha='center',color='#b52b40',fontsize=10)
b.text(0,-1.22,'inner boundary: clockwise',ha='center',color='#1857b2',fontsize=10)
b.text(0,0,'r < 1/3\nnot in S',ha='center',va='center',fontsize=9)
b.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xlabel='x',ylabel='y',title='Induced directions viewed from above');b.set_aspect('equal');b.grid(alpha=.15)
fig.savefig('paper-3-paraboloid.png',facecolor='white',transparent=False)
