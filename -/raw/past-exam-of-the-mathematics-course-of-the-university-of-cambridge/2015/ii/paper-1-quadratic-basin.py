import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P=np.array([[4/3,-1/6],[-1/6,5/6]]);vals,vec=np.linalg.eigh(P)
t=np.linspace(0,2*np.pi,600);circle=np.array([np.cos(t),np.sin(t)]);ellipse=vec@np.diag(1/np.sqrt(vals))@circle
r1,r2=1/np.sqrt(vals[1]),1/np.sqrt(vals[0])
fig,ax=plt.subplots(1,2,figsize=(9,4),dpi=100)
for j,a in enumerate(ax):
 a.plot(*ellipse,color='darkviolet',lw=2,label=r'$V=1$: invariant ellipse')
 if j==0:
  a.plot(*(r1*circle),ls='--',color='teal',label=r'$r_1$: largest attraction disc');a.plot(*(r2*circle),ls=':',color='firebrick',label=r'$r_2$: escape threshold')
 else:a.fill(*ellipse,color='darkviolet',alpha=.05)
 grid=np.linspace(-1.45,1.45,13);x,y=np.meshgrid(grid,grid);rr=x*x+y*y
 fx=-x+y+x*rr;fy=-y-2*x+y*rr
 if j:fx=-fx;fy=-fy
 mag=np.hypot(fx,fy);mag=np.where(mag==0,1,mag)
 a.quiver(x,y,fx/mag,fy/mag,color='.6',alpha=.65,scale=24,width=.003)
 a.plot(0,0,'ko',ms=4);a.set(xlabel='$x$',ylabel='$y$',xlim=(-1.55,1.55),ylim=(-1.55,1.55));a.set_aspect('equal');a.legend(fontsize=8,loc='upper left')
ax[0].set_title('Origin attracts inside; exterior escapes')
ax[1].set_title('Reversed flow: unique attracting cycle')
fig.tight_layout();fig.savefig('paper-1-quadratic-basin.png',facecolor='white',transparent=False)
