"""Original Bloch-vector sketch. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Writes paper-58-bloch-vectors.png to caller CWD. Uses caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

theta, phi = np.pi/3, np.pi/4
upper = np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])
lower = upper * np.array([1, 1, -1])
fig = plt.figure(figsize=(8.2, 4.2), facecolor='white')
ax = fig.add_subplot(121, projection='3d')
az = np.linspace(0, 2*np.pi, 45)
pol = np.linspace(0, np.pi, 25)
xx=np.outer(np.cos(az),np.sin(pol)); yy=np.outer(np.sin(az),np.sin(pol)); zz=np.outer(np.ones_like(az),np.cos(pol))
ax.plot_wireframe(xx,yy,zz,rstride=5,cstride=4,color='#bcc6cc',linewidth=.45,alpha=.55)
for vector, color, label in [(upper,'#1864ab',r'$z$'),(lower,'#c92a2a',r'$\bar z$')]:
 ax.quiver(0,0,0,*vector,color=color,linewidth=2.7,arrow_length_ratio=.13)
 ax.text(*(1.15*vector),label,color=color,fontsize=14)
for direction,label in [(np.array([1,0,0]),'x'),(np.array([0,1,0]),'y'),(np.array([0,0,1]),'z')]:
 ax.plot(*np.array([-direction,direction]).T,color='#74828c',linewidth=.7)
 ax.text(*(1.14*direction),label,fontsize=10)
ax.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),zlim=(-1.15,1.15))
ax.set_box_aspect((1,1,1));ax.view_init(elev=18,azim=-62);ax.set_axis_off()
ax.set_title('Unit Bloch sphere',fontsize=11,pad=0)
ax2=fig.add_subplot(122)
angle=np.linspace(0,2*np.pi,250)
ax2.plot(np.cos(angle),np.sin(angle),color='#a8b5bd',linewidth=1)
ax2.axhline(0,color='#bfc7cc',linewidth=.8);ax2.axvline(0,color='#bfc7cc',linewidth=.8)
for sign,color,label in [(1,'#1864ab',r'$z$'),(-1,'#c92a2a',r'$\bar z$')]:
 v=np.array([np.sin(theta),sign*np.cos(theta)])
 ax2.annotate('',xy=v,xytext=(0,0),arrowprops=dict(arrowstyle='-|>',lw=2.7,color=color))
 ax2.text(v[0]+.06,v[1],label,color=color,fontsize=14,va='center')
ax2.plot([np.sin(theta)]*2,[-np.cos(theta),np.cos(theta)],linestyle=':',color='#8b969e',linewidth=1)
ax2.text(-.05,1.08,r'$z$',ha='center');ax2.text(1.07,-.07,r'$u_\perp$',ha='center')
ax2.text(.04,-1.15,r'$u_\perp=(\cos\varphi,\sin\varphi,0)$',fontsize=10,ha='center')
ax2.set(xlim=(-1.2,1.3),ylim=(-1.23,1.2));ax2.set_aspect('equal');ax2.set_axis_off()
ax2.set_title(r'Common meridian: $\varphi=\pi/4$',fontsize=11)
fig.suptitle(r'$\theta=\pi/3$: equal transverse components, opposite heights',fontsize=12,y=.96)
fig.subplots_adjust(left=.01,right=.98,bottom=.07,top=.82,wspace=.05)
fig.savefig('paper-58-bloch-vectors.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
