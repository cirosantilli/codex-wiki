"""Original determinant cone and its radial section; write output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,4.8),dpi=100,facecolor='white')
ax=fig.add_subplot(121,projection='3d')
r=np.linspace(0,2.25,25);theta=np.linspace(0,2*np.pi,81)
R,T=np.meshgrid(r,theta);X=R*np.cos(T);Y=R*np.sin(T)
for sign in (-1,1):
    ax.plot_surface(X,Y,sign*R,color='#8a929a',alpha=.23,edgecolor='none',shade=False)
for point,color,text in [((0,0,2.65),'#1264a3',r'$X_1$'),((0,0,-2.65),'#b54827',r'$X_2$'),((2.15,0,0),'#27813b',r'$X_3$')]:
    ax.scatter(*point,color=color,s=35,depthshade=False)
    ax.text(point[0]+.12,point[1],point[2]+.08,text,color=color,fontsize=12)
ax.set(xlabel='x',ylabel='y',zlabel='z',xlim=(-2.4,2.4),ylim=(-2.4,2.4),zlim=(-2.9,2.9),title=r'Excluded cone: $z^2=x^2+y^2$')
ax.view_init(elev=19,azim=-54);ax.set_box_aspect((1,1,1.15))
ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);ax.set_zticks([-2,0,2]);ax.tick_params(labelsize=9)
ax=fig.add_subplot(122)
x=np.linspace(-2.4,2.4,401)
ax.fill_between(x,np.abs(x),2.8,color='#d9e8f6')
ax.fill_between(x,-2.8,-np.abs(x),color='#f5ddd4')
ax.fill_between(x,-np.abs(x),np.abs(x),color='#dcefdc')
ax.plot(x,np.abs(x),'--',color='#555555',lw=1.5);ax.plot(x,-np.abs(x),'--',color='#555555',lw=1.5)
ax.axvline(0,color='#999999',lw=.7);ax.axhline(0,color='#999999',lw=.7)
ax.text(0,2.1,r'$X_1$: positive definite',ha='center',fontsize=11,color='#1264a3')
ax.text(0,-2.1,r'$X_2$: negative definite',ha='center',fontsize=11,color='#b54827')
for px in (-1.7,1.7):ax.text(px,.1,r'$X_3$',ha='center',fontsize=12,color='#27813b')
ax.set(xlim=(-2.4,2.4),ylim=(-2.8,2.8),xlabel='x (with y = 0)',ylabel='z',title='Radial section through the cone')
ax.set_aspect('equal');ax.spines[['top','right']].set_visible(False)
fig.text(.74,.025,'The two green wedges connect around the cone in 3D.',ha='center',fontsize=10)
fig.subplots_adjust(left=.015,right=.98,top=.88,bottom=.17,wspace=.17)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
