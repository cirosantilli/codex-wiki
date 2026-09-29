"""Kruskal plane and radial Minkowski conformal diagram.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Uses the supplied MPLCONFIGDIR; emits an opaque PNG basename into cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 6.5), dpi=100, facecolor='white')
fig.subplots_adjust(left=.065, right=.955, bottom=.12, top=.85, wspace=.28)
fig.suptitle('Regular horizons and conformal infinity', fontsize=18, y=.965)
ax=axes[0]
x=np.linspace(-1.9,1.9,500)
h=np.sqrt(1+x*x)
ax.fill_between(x,-h,h,color='#edf4fa')
ax.plot(x,h,color='#a73030',lw=2.8)
ax.plot(x,-h,color='#a73030',lw=2.8)
ax.plot(x,x,'--',color='#20669b',lw=1.8)
ax.plot(x,-x,'--',color='#20669b',lw=1.8)
ax.axhline(0,color='#8d949a',lw=.7)
ax.axvline(0,color='#8d949a',lw=.7)
for xx,tt,label in [(1.15,0,'I\nexterior'),(-1.15,0,'III\nexterior'),(0,.62,'II\nblack hole'),(0,-.62,'IV\nwhite hole')]:
    ax.text(xx,tt,label,ha='center',va='center',fontsize=11)
ax.text(0,1.18,r'$r=0$',ha='center',color='#a73030',fontsize=12)
ax.text(0,-1.28,r'$r=0$',ha='center',color='#a73030',fontsize=12)
ax.text(.91,1.45,r'$T=X$',color='#20669b',rotation=45,fontsize=11)
ax.text(-1.62,1.38,r'$T=-X$',color='#20669b',rotation=-45,fontsize=11)
ax.set(xlim=(-1.85,1.85),ylim=(-2.25,2.25),xlabel='Kruskal X',ylabel='Kruskal T')
ax.set_aspect('equal')
ax.set_title('Kruskal plane (not compactified)',fontsize=13,pad=18)
ax.set_xticks([-1,0,1]); ax.set_yticks([-2,-1,0,1,2])
ax=axes[1]
p=np.pi
ax.fill([0,p,0],[-p,0,p],color='#f0f6ec')
ax.plot([0,p,0],[-p,0,p],color='#347239',lw=2.5)
ax.plot([0,0],[-p,p],color='#656565',lw=2.5)
for t0 in [-1.5,0,1.5]:
    # Null rays of positive slope within the physical triangle.
    rmax=(p-t0)/2
    rr=np.linspace(0,rmax,70)
    ax.plot(rr,t0+rr,color='#81aa81',lw=.85)
for t0 in [-1.5,0,1.5]:
    rmax=(p+t0)/2
    rr=np.linspace(0,rmax,70)
    ax.plot(rr,t0-rr,color='#81aa81',lw=.85)
ax.scatter([0,p,0],[p,0,-p],color='#222222',s=25,zorder=4)
ax.text(-.22,p,r'$i^+$',ha='right',va='center',fontsize=14)
ax.text(-.22,-p,r'$i^-$',ha='right',va='center',fontsize=14)
ax.text(p+.16,0,r'$i^0$',ha='left',va='center',fontsize=14)
ax.text(1.35,2.02,r'$\mathscr{I}^+$',fontsize=17,color='#347239')
ax.text(1.35,-2.33,r'$\mathscr{I}^-$',fontsize=17,color='#347239')
ax.text(-.27,0,r'$r=0$',rotation=90,ha='right',va='center',fontsize=12,color='#555555')
ax.text(.85,0,'angular spheres\nsuppressed',ha='center',va='center',fontsize=10,color='#555555')
ax.set(xlim=(-.55,p+.45),ylim=(-p-.35,p+.35),xlabel='Compact radius R',ylabel='Compact time T')
ax.set_aspect('equal')
ax.set_title('Radial Minkowski Penrose diagram',fontsize=13,pad=18)
ax.set_xticks([0,p/2,p],['0',r'$\pi/2$',r'$\pi$'])
ax.set_yticks([-p,0,p],[r'$-\pi$','0',r'$\pi$'])
fig.text(.5,.028,'Blue dashed lines: Schwarzschild horizons. Green sloping boundaries: null infinity.',ha='center',fontsize=11)
fig.savefig('paper-52-conformal-diagrams.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
