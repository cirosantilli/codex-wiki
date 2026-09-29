"""Original hyperboloid sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes its PNG basename to cwd and respects an existing MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8.8, 4), dpi=100, facecolor='white')
ax = fig.add_subplot(121, projection='3d')
t,r = np.meshgrid(np.linspace(0, 2*np.pi, 81),np.linspace(1,2,28))
ax.plot_surface(r*np.cos(t),r*np.sin(t),np.sqrt(1+r*r),color='#6da9c5',alpha=.8,linewidth=0)
t=np.linspace(0,2*np.pi,200)
for rad,color in [(1,'#db7824'),(2,'#216b91')]:
    ax.plot(rad*np.cos(t),rad*np.sin(t),np.full_like(t,np.sqrt(1+rad*rad)),color=color,lw=2)
ax.set(xlabel='x',ylabel='y',zlabel='z',zlim=(0,2.5),title=r'$z=\sqrt{1+r^2}$, $1\leq r\leq2$')
ax.view_init(elev=23,azim=-57)
ax.set_box_aspect((1,1,.65))
ax2=fig.add_subplot(122)
from matplotlib.patches import Circle
ax2.add_patch(Circle((0,0),2,facecolor='#c7e0ef',edgecolor='#216b91',lw=2))
ax2.add_patch(Circle((0,0),1,facecolor='white',edgecolor='#db7824',lw=2))
for rad,sgn,col in [(2,1,'#216b91'),(1,-1,'#db7824')]:
    ang=np.pi/4
    start=np.array([rad*np.cos(ang),rad*np.sin(ang)])
    end=np.array([rad*np.cos(ang+sgn*.22),rad*np.sin(ang+sgn*.22)])
    ax2.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color=col,lw=2))
ax2.text(0,0,'hole',ha='center',va='center')
ax2.text(0,-1.5,'S projects here',ha='center')
ax2.set(xlabel='x',ylabel='y',xlim=(-2.3,2.3),ylim=(-2.3,2.3),title='Upward orientation: outer CCW, inner CW')
ax2.set_aspect('equal')
fig.subplots_adjust(left=.01,right=.97,bottom=.13,top=.87,wspace=.24)
fig.savefig('paper-3-hyperboloid-annulus.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
