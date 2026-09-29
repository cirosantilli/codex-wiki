"""Original bifurcation and numerical phase diagrams.
Python 3.14, NumPy 2.3, Matplotlib 3.10; only basename PNG to caller CWD.
Respects caller MPLCONFIGDIR. Phase panels use the exact rescaled field
u'=v, v'=u²-sign(lambda)+0.1(beta+u)v. The repelling cycle is
computed by backward RK4 integration, rather than drawn as an ellipse.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

EPS=.1

def field(p,beta,sgn=1):
 u,v=p
 return np.array([v,u*u-sgn+EPS*(beta+u)*v])

def rk4(p,dt,beta,sgn=1):
 k1=field(p,beta,sgn);k2=field(p+dt*k1/2,beta,sgn)
 k3=field(p+dt*k2/2,beta,sgn);k4=field(p+dt*k3,beta,sgn)
 return p+dt*(k1+2*k2+2*k3+k4)/6

def path(seed,dt,beta,sgn=1,steps=6000):
 p=np.array(seed,dtype=float);pts=[p.copy()]
 for _ in range(steps):
  p=rk4(p,dt,beta,sgn)
  if not np.all(np.isfinite(p)) or abs(p[0])>3.3 or abs(p[1])>3.5:break
  pts.append(p.copy())
 return np.array(pts)

def periodic_cycle(beta=.85):
 pts=path([-.85,0],-.025,beta,steps=80000)
 # Cross u=-1 with positive v: use interpolated sections to check convergence.
 indices=np.flatnonzero((pts[:-1,0]>-1)&(pts[1:,0]<=-1)&(pts[1:,1]>0))
 if len(indices)<10:raise RuntimeError('No converged periodic return')
 values=[]
 for i in indices[-10:]:
  lo,hi=0.,1.
  for _ in range(36):
   mid=(lo+hi)/2
   if rk4(pts[i],-.025*mid,beta)[0]>-1:lo=mid
   else:hi=mid
  values.append(rk4(pts[i],-.025*(lo+hi)/2,beta)[1])
 if np.ptp(values)>2e-5:raise RuntimeError('Periodic section has not converged')
 return pts[indices[-2]:indices[-1]+2],float(np.ptp(values)),float(np.mean(values))

if __name__=='__main__':
 cycle,spread,cross=periodic_cycle()
 fig=plt.figure(figsize=(10.2,10.0),dpi=130,facecolor='white')
 grid=fig.add_gridspec(3,2,height_ratios=[.9,1,1],hspace=.64,wspace=.24)
 ax=fig.add_subplot(grid[0,:]);lam=np.linspace(0,.00022,500);a=np.sqrt(lam)
 ax.plot(lam,a,color='#a83339',lw=2,label='Hopf: μ = √λ')
 ax.plot(lam,5*a/7,'--',color='#256daa',lw=2,label='Saddle loop: leading μ = (5/7)√λ')
 ax.axvline(0,color='black',lw=1.7,label='Saddle-node')
 ax.scatter([0],[0],color='black',s=30)
 cases=[(-1,.8,'No equilibria'),(1,.5,'Stable focus, no nearby cycle'),(1,.85,'Stable focus + repelling cycle'),(1,1.3,'Unstable focus, no nearby cycle')]
 for i,(sgn,beta,title) in enumerate(cases):
  ax.scatter([sgn*1e-4],[beta*.01],s=24,color='black')
  ax.annotate(str(i+1),(sgn*1e-4,beta*.01),xytext=(5,5),textcoords='offset points')
 ax.set(xlim=(-.00014,.00023),ylim=(-.002,.018),xlabel='λ',ylabel='μ',title='Nearby bifurcation curves; global curve shown to leading order')
 ax.ticklabel_format(style='sci',axis='x',scilimits=(0,0));ax.legend(loc='upper left',fontsize=8);ax.grid(alpha=.15)
 uu=np.linspace(-2.65,1.65,120);vv=np.linspace(-2.4,2.4,110);U,V=np.meshgrid(uu,vv)
 for i,(sgn,beta,title) in enumerate(cases):
  panel=fig.add_subplot(grid[1+i//2,i%2])
  panel.streamplot(uu,vv,V,U*U-sgn+EPS*(beta+U)*V,color='#a5b4b9',density=.85,linewidth=.65,arrowsize=.8)
  if sgn==1:
   panel.scatter([-1],[0],s=35,color='#224b6e' if beta<1 else '#a83339',zorder=5)
   panel.scatter([1],[0],marker='x',s=55,color='black',zorder=5)
   roots=np.linalg.eig(np.array([[0,1],[2,EPS*(beta+1)]]))
   for eig,vec in zip(roots[0],roots[1].T):
    for sign in [-1,1]:
     points=path(np.array([1,0])+sign*.002*vec,.015 if eig>0 else -.015,beta,steps=1200)
     panel.plot(points[:,0],points[:,1],color='#94653e',lw=1.15)
  if i==2:
   panel.plot(cycle[:,0],cycle[:,1],color='#aa2d68',lw=2)
   panel.text(-2.5,1.95,'Repelling periodic orbit',fontsize=8,color='#aa2d68')
  panel.tick_params(labelsize=9)
  panel.set(xlim=(-2.65,1.65),ylim=(-2.4,2.4),xlabel='u = x/√|λ|',ylabel='v = y/|λ|^(3/4)',title=f'{i+1}. {title}\nβ = μ/√|λ| = {beta}, ε = 0.1')
 for panel in fig.axes:
  panel.title.set_fontsize(11);panel.xaxis.label.set_fontsize(9);panel.yaxis.label.set_fontsize(9)
 fig.savefig('paper-51-bogdanov-takens-portraits.png',facecolor='white',transparent=False);plt.close(fig)
 print(f'Backward RK4 periodic section spread={spread:.3g}, v crossing={cross:.8g}')
