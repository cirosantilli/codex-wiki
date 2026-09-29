"""Original sketches; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run in the desired output directory. Uses the supplied MPLCONFIGDIR unchanged.
"""
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
s=np.linspace(-3,3,301)
t=np.linspace(0,2*np.pi,81)
fig=plt.figure(figsize=(10,6.2),dpi=100,facecolor='white')
for panel in (1,2):
    ax=fig.add_subplot(1,2,panel,projection='3d')
    if panel==1:
        f=2-.6*np.exp(-s*s);fp=1.2*s*np.exp(-s*s);crit=[0]
    else:
        f=2+.6*(-.5*s*np.exp(-s*s)-np.sqrt(np.pi)/4*np.array([math.erf(x) for x in s]));fp=.6*(s*s-1)*np.exp(-s*s);crit=[-1,1]
    gp=np.sqrt(1-fp*fp)
    g=np.concatenate(([0],np.cumsum((gp[:-1]+gp[1:])/2*np.diff(s))))
    g-=g[len(s)//2]
    x=f[:,None]*np.cos(t);y=f[:,None]*np.sin(t);z=np.broadcast_to(g[:,None],x.shape)
    ax.plot_surface(x,y,z,color='#bedcec',alpha=.48,linewidth=0,antialiased=True,rstride=5,cstride=4,shade=True)
    for c in crit:
        i=np.argmin(abs(s-c))
        ax.plot(f[i]*np.cos(t),f[i]*np.sin(t),np.full_like(t,g[i]),color='#bd2828',linewidth=2.7)
    ax.plot(f,np.zeros_like(s),g,color='#174864',linewidth=1.5)
    ax.set(xlim=(-2.6,2.6),ylim=(-2.6,2.6),zlim=(-3,3),xlabel='x',ylabel='y',zlabel='height')
    ax.set_title(f'n = {panel}: '+('one neck ring' if panel==1 else 'one bulge ring and one neck ring'),fontsize=11,pad=15)
    ax.set_box_aspect((1,1,1.2));ax.view_init(elev=14,azim=-58)
    ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);ax.set_zticks([-2,0,2])
fig.suptitle('Geodesic parallels are critical points of the radius',fontsize=14,y=.95)
fig.text(.5,.065,'Red rings are geodesics; blue lines are meridians. Surfaces extend beyond the plotted window.',ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,bottom=.1,top=.86,wspace=.04)
fig.savefig('paper-4-geodesic-parallels.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
