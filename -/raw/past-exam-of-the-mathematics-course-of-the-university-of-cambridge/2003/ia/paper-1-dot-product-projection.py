"""Original dot-product projection sketch; Python 3.14, NumPy and Matplotlib.

Write paper-1-dot-product-projection.png to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

angle=np.deg2rad(55)
x=np.array([3.8,0.0])
y=3.0*np.array([np.cos(angle),np.sin(angle)])
fig,ax=plt.subplots(figsize=(7.2,4.8),dpi=150,facecolor='white')
ax.set_facecolor('white')
for endpoint,color,label,offset in [(x,'#245ca6',r'$\mathbf{x}$',(0.1,0)),(y,'#ba3d38',r'$\mathbf{y}$',(0.1,0.08))]:
 ax.annotate('',xy=endpoint,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',lw=2.5,color=color,mutation_scale=18))
 ax.text(*(endpoint+offset),label,color=color,fontsize=17,va='center')
ax.plot([y[0],y[0]],[0,y[1]],'--',color='#666666',lw=1.4)
ax.plot([y[0]-.15,y[0]-.15,y[0]],[0,.15,.15],color='#666666',lw=1.2)
ax.plot([0,y[0]],[-.48,-.48],color='#268362',lw=2.0)
for xx in [0,y[0]]:ax.plot([xx,xx],[-.4,-.56],color='#268362',lw=1.2)
ax.text(y[0]/2,-.73,r'$\|\mathbf{y}\|\cos\alpha$',ha='center',color='#268362',fontsize=14)
ax.text(2.9,.19,r'$\|\mathbf{x}\|$',color='#245ca6',fontsize=14)
ax.text(.55,1.45,r'$\|\mathbf{y}\|$',color='#ba3d38',fontsize=14)
ax.add_patch(Arc((0,0),1.15,1.15,theta1=0,theta2=55,color='#333333',lw=1.3))
ax.text(.73,.30,r'$\alpha$',fontsize=16)
ax.scatter([0],[0],color='#222222',s=14,zorder=5)
ax.text(-.13,-.21,r'$O$',fontsize=13)
ax.text(2.1,3.18,r'$\mathbf{x}\cdot\mathbf{y}=\|\mathbf{x}\|\,\|\mathbf{y}\|\cos\alpha$',ha='center',fontsize=17)
ax.set_title('Dot product as a signed projection',fontsize=16,pad=12)
ax.set_xlim(-.35,4.35);ax.set_ylim(-.95,3.6)
ax.set_aspect('equal');ax.axis('off')
fig.tight_layout(pad=1.0)
fig.savefig('paper-1-dot-product-projection.png',facecolor='white',transparent=False)
plt.close(fig)
