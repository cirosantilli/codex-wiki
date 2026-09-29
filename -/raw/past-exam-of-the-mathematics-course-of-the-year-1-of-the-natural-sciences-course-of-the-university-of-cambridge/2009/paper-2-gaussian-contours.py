"""Original contours and graph surface; write PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
f=lambda x,y:(x-1)*y*np.exp(-((x-1)**2+y*y)/2)
fig=plt.figure(figsize=(12,5.3),facecolor='white');ax=fig.add_subplot(121)
x=np.linspace(-2,4,450);y=np.linspace(-3,3,450);xx,yy=np.meshgrid(x,y);zz=f(xx,yy)
levels=[-.34,-.26,-.16,-.06,.06,.16,.26,.34]
cs=ax.contour(xx,yy,zz,levels=levels,cmap='coolwarm',linewidths=1.2);ax.clabel(cs,inline=True,fontsize=8,fmt='%.2f')
ax.axvline(1,color='gray',lw=1);ax.axhline(0,color='gray',lw=1)
for x,y,text in [(2,1,'max'),(0,-1,'max'),(0,1,'min'),(2,-1,'min'),(1,0,'saddle')]:
 ax.scatter([x],[y],color='black',s=20,zorder=4);ax.annotate(text,(x,y),(x+.13,y+.14),fontsize=9)
ax.plot([0,1],[1,1],color='#20814c',lw=3);ax.annotate('',(.25,1),(.8,1),arrowprops={'arrowstyle':'->','color':'#20814c','lw':2})
ax.scatter([1],[1],color='#20814c',zorder=5);ax.annotate('Start (1, 1)',(1,1),(1.25,1.6),fontsize=9,arrowprops={'arrowstyle':'-','color':'gray'})
ax.set(xlim=(-2,4),ylim=(-3,3),aspect='equal',xlabel='x',ylabel='y',title='Contours and downhill path');ax.grid(alpha=.15)
ax=fig.add_subplot(122,projection='3d');xx,yy=np.meshgrid(np.linspace(-1,3,90),np.linspace(-2,2,90));zz=f(xx,yy)
ax.plot_surface(xx,yy,zz,cmap='coolwarm',alpha=.55,linewidth=0,antialiased=True)
x=np.linspace(0,1,120);y=np.ones_like(x);z=f(x,y);ax.plot(x,y,z,color='#176f3b',lw=4)
ax.scatter([1,0],[1,1],[0,-1/np.e],color='#176f3b',s=24)
x0=.65;dx=-.2;dz=dx*(1-(x0-1)**2)*np.exp(-((x0-1)**2+1)/2)
ax.quiver(x0,1,f(x0,1),dx,0,dz,color='black',lw=2,arrow_length_ratio=.4)
ax.set(xlabel='x',ylabel='y',zlabel='height z',title='Same path on the graph surface');ax.view_init(elev=26,azim=115)
fig.suptitle(r'$z=(x-1)y\exp(-[(x-1)^2+y^2]/2)$',fontsize=14)
fig.tight_layout(rect=(0,0,1,.94));fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white');plt.close(fig)
