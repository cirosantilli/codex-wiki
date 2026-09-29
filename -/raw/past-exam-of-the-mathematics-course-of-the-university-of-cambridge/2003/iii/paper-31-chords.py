"""Original geometry diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-31-chords.png to caller CWD. Honors caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes=plt.subplots(1,2,figsize=(9,4.8),layout='constrained',facecolor='white')
theta=np.array([0.0,0.07])
p=np.array([0.25,0.55])
normals=np.column_stack((np.cos(theta),np.sin(theta)))
intersection=np.linalg.solve(normals,p)
a=np.linspace(0,2*np.pi,600)
colors=['#1768ac','#d15c22']
for ax in axes:
 ax.plot(np.cos(a),np.sin(a),color='#777777',lw=1.6)
 ax.fill(np.cos(a),np.sin(a),color='#ebf1f7')
 for n,dist,color in zip(normals,p,colors):
  tangent=np.array([-n[1],n[0]])
  t=np.linspace(-7,7,300)
  line=dist*n+t[:,None]*tangent
  ax.plot(line[:,0],line[:,1],color=color,lw=1.8)
 ax.scatter([0],[0],color='black',s=14,zorder=5)
 ax.set_aspect('equal')
 ax.set_xlabel('x / r');ax.set_ylabel('y / r')
 ax.spines[['top','right']].set_visible(False)
axes[0].set_xlim(-1.2,1.2);axes[0].set_ylim(-1.2,1.2)
axes[0].set_title('Two lines cross the disk')
axes[1].set_xlim(-1.4,1.4);axes[1].set_ylim(-1.3,5.0)
axes[1].scatter(*intersection,color='black',s=26,zorder=5)
axes[1].annotate('Intersection outside the disk',xy=intersection,xytext=(-1.15,4.8),arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=9)
axes[1].set_title('Their intersection lies far away')
fig.savefig('paper-31-chords.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
