from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig=plt.figure(figsize=(12,5.9),layout='constrained');ax=fig.add_subplot(121,projection='3d');bx=fig.add_subplot(122)
x=np.linspace(-np.pi,np.pi,125);X,Y=np.meshgrid(x,x);arg=-2*(np.cos(X)+np.cos(Y));mask=np.abs(arg)<=1;Z=np.where(mask,np.arccos(np.clip(arg,-1,1)),np.nan)
for sign,col in [(1,'#71a9c9'),(-1,'#b5d0df')]:ax.plot_surface(X/np.pi,Y/np.pi,sign*Z/np.pi,color=col,linewidth=0,antialiased=False,alpha=.87,rstride=1,cstride=1)
ax.set(xlabel=r'$k_xa/\pi$',ylabel=r'$k_ya/\pi$',zlabel=r'$k_zc/\pi$',title='Exact half-filled surface',xlim=(-1,1),ylim=(-1,1),zlim=(-1,1));ax.view_init(elev=22,azim=38)
p=np.linspace(-2*np.pi/3,2*np.pi/3,700);q=np.arccos(np.clip(.5-np.cos(p),-1,1));xx=np.r_[p,p[::-1]]/np.pi;yy=np.r_[q,-q[::-1]]/np.pi
bx.fill(xx,yy,color='#e6eff5');bx.plot(xx,yy,color='#174c75',lw=2.7,label=r'electron at $k_zc=\pi$');bx.plot(xx,yy,color='#b35b15',lw=1.7,ls='--',label=r'hole at $k_zc=0$, recentered')
bx.set_aspect('equal');bx.set(xlim=(-.9,.9),ylim=(-.9,.9),xlabel='Pocket-centred x / pi',ylabel='Pocket-centred y / pi',title='The two closed orbit areas coincide');bx.legend(loc='upper right',fontsize=9,frameon=False);bx.text(0,-.8,r'$A_e=A_h=12.17169/a^2$',ha='center');bx.grid(alpha=.15)
fig.suptitle('Tetragonal nearest-neighbor band: particle-hole symmetry constrains the orbits',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
