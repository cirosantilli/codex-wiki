"""Original cylinder-geodesic sketch. Python 3.14; pinned root NumPy/Matplotlib.
Writes paper-3-cylinder-geodesics.png to caller CWD, respecting MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,4.5),layout='constrained',facecolor='white');ax=fig.add_subplot(121,projection='3d');bx=fig.add_subplot(122)
theta=np.linspace(0,2*np.pi,80);zz=np.linspace(-1.5,1.5,25);th,z=np.meshgrid(theta,zz);ax.plot_surface(np.cos(th),np.sin(th),z,color='#d5e6ed',alpha=.25,edgecolor='none',shade=False)
col=['#a53f32','#286eab','#367c53'];t=np.linspace(-np.pi,np.pi,400)
ax.plot(np.cos(t),np.sin(t),np.full_like(t,-.8),color=col[0],lw=2.5,label='circular parallel');ax.plot(np.full(100,np.cos(.4)),np.full(100,np.sin(.4)),np.linspace(-1.5,1.5,100),color=col[1],lw=2.5,label='generator');ax.plot(np.cos(t),np.sin(t),.4*t,color=col[2],lw=2.8,label='helix')
ax.set(xlabel='x/a',ylabel='y/a',zlabel='z/a',zlim=(-1.5,1.5),title='Geodesics on the cylinder');ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_box_aspect((2,2,3));ax.view_init(elev=20,azim=-48);ax.legend(loc='upper left',fontsize=8)
bx.plot(t,np.full_like(t,-.8),color=col[0],lw=2.5);bx.plot([.4,.4],[-1.5,1.5],color=col[1],lw=2.5);bx.plot(t,.4*t,color=col[2],lw=2.5);bx.axvline(-np.pi,color='gray',ls=':',lw=1);bx.axvline(np.pi,color='gray',ls=':',lw=1);bx.text(0,1.42,'The two vertical edges are identified',ha='center',fontsize=9,color='gray');bx.set(xlim=(-3.4,3.4),ylim=(-1.6,1.6),xlabel=r'$u/a=\theta$',ylabel=r'$z/a$',title='Unrolled cylinder: straight lines');bx.spines[['top','right']].set_visible(False);bx.set_aspect('equal',adjustable='box')
fig.savefig('paper-3-cylinder-geodesics.png',dpi=130,facecolor='white',transparent=False,bbox_inches='tight',pad_inches=.15)
