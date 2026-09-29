"""Original tricritical Landau diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory. Respects the caller's MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

fig=plt.figure(figsize=(12,9),layout='constrained',facecolor='white')
gs=fig.add_gridspec(2,6,height_ratios=[1.5,1])
ax=fig.add_subplot(gs[0,:3],projection='3d')
q,b=np.meshgrid(np.linspace(0,1,35),np.linspace(.015,.55,35))
a=q*b;s=a+b;p=a*b
u=2*(-2*s*s+3*p)/3
r=(s**4-s*s*p+3*p*p)/3
h=s**3*p/3
for sign,col in [(1,'#c35b2b'),(-1,'#2375b9')]:
 ax.plot_surface(u,r,sign*h,color=col,alpha=.55,linewidth=0)
u0,rho=np.meshgrid(np.linspace(-1,.65,35),np.linspace(0,1,25))
rmax=np.where(u0<0,3*u0*u0/16,0)
r0=-.35+(rmax+.35)*rho
ax.plot_surface(u0,r0,np.zeros_like(u0),color='#989898',alpha=.3,linewidth=0)
x=np.linspace(-1,0,80)
ax.plot(x,3*x*x/16,0,color='#222222',lw=2)
ax.plot(np.linspace(0,.65,50),np.zeros(50),np.zeros(50),color='#008851',lw=3)
for sign in (-1,1):
 ax.plot(x,9*x*x/20,sign*6*x*x*np.sqrt(-3*x/10)/25,color='#7a2182',lw=2)
ax.scatter([0],[0],[0],color='red',s=55,depthshade=False)
ax.set(xlabel='quartic u',ylabel='thermal r',zlabel='field h',title='Three-dimensional phase diagram (v = 1)')
ax.view_init(24,-63)
ax.legend(handles=[Line2D([0],[0],color='#008851',label='continuous critical line'),Line2D([0],[0],color='#222222',label='three-phase line'),Line2D([0],[0],color='#7a2182',label='wing critical edges'),Line2D([0],[0],marker='o',color='red',ls='',label='tricritical point')],fontsize=8,loc='upper left')
ax.text2D(.03,.2,'Orange/blue: first-order wings\nGrey: opposite-magnetization coexistence',transform=ax.transAxes,fontsize=9)
ax2=fig.add_subplot(gs[0,3:])
u=np.linspace(-1,.8,500);coex=np.where(u<0,3*u*u/16,0)
ax2.fill_between(u,-.4,coex,color='#ddeaf5',label='ordered phase')
ax2.fill_between(u,coex,.4,color='#f5ece2',label='disordered phase')
ax2.plot(u[u<0],coex[u<0],c='#c35b2b',lw=2,label='first order')
ax2.plot(u[u>=0],coex[u>=0],c='#008851',lw=2,label='continuous')
ax2.plot(u[u<0],u[u<0]**2/4,'--',c='#888888',label='ordered spinodal')
ax2.plot(u[u<0],np.zeros(np.sum(u<0)),'--',c='#555555',label='disordered spinodal')
ax2.scatter([0],[0],c='red',s=55,zorder=5)
ax2.annotate('tricritical point',(0,0),(.05,.16),arrowprops={'arrowstyle':'->'})
ax2.set(xlabel='u',ylabel='r',ylim=(-.4,.4),title='Zero-field slice h = 0')
ax2.legend(fontsize=8,loc='lower right')
M=np.linspace(-1.2,1.2,600)
for j,title in enumerate(['Ordinary critical point','First-order coexistence','Tricritical point']):
 ap=fig.add_subplot(gs[1,2*j:2*j+2])
 if j==0:
  for rv,col in [(.3,'#c35b2b'),(0,'#008851'),(-.3,'#2375b9')]:
   ap.plot(M,rv*M*M/2+M**4/4+M**6/6,color=col,label=f'r = {rv:g}, u = 1')
 elif j==1:
  ap.plot(M,3*M*M/32-M**4/4+M**6/6,c='#c35b2b',label='r = 3/16, u = -1')
  mm=np.array([-np.sqrt(.75),0,np.sqrt(.75)])
  ap.scatter(mm,np.zeros(3),c='black',s=24,zorder=5)
 else:
  ap.plot(M,M**6/6,c='#7a2182',label='r = u = 0')
 ap.axhline(0,color='#888888',lw=.6)
 ap.set(xlabel='order parameter M',ylabel='V(M)',ylim=(-.07,.32),title=title)
 ap.legend(fontsize=8)
fig.savefig('paper-50-landau.png',dpi=120,facecolor='white')
plt.close(fig)
