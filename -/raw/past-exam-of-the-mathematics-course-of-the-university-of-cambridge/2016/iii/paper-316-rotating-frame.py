import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
mu2=.03;mu1=1-mu2
f=lambda x:x-mu1*(x+mu2)/abs(x+mu2)**3-mu2*(x-mu1)/abs(x-mu1)**3
intervals=[(-2,-mu2-1e-5),(-mu2+1e-5,mu1-1e-5),(mu1+1e-5,2)]
roots=[]
for a,b in intervals:
 for _ in range(85):
  c=(a+b)/2
  if f(c)>0:b=c
  else:a=c
 roots.append((a+b)/2)
fig,ax=plt.subplots(figsize=(8,3.6),dpi=100)
xx=np.linspace(-2,2,500)
ax.plot(xx,xx,color='tab:orange',label='Centrifugal acceleration x',lw=2)
ax.plot(xx,-xx,color='gray',ls=':',label='Balance reference -x')
for k,(a,b) in enumerate(intervals):
 x=np.linspace(a,b,2000);g=f(x)-x;g[np.abs(g)>5]=np.nan
 ax.plot(x,g,color='tab:blue',lw=2,label='Gravitational acceleration' if k==0 else None)
for r,name in zip(roots,['L3','L1','L2']):
 ax.scatter([r],[-r],color='black',zorder=3);ax.annotate(name,(r,-r),xytext=(4,9),textcoords='offset points')
for x,name in [(-mu2,'M1'),(mu1,'M2')]:
 ax.axvline(x,color='black',ls='--',alpha=.4);ax.text(x+.015,3.05,name)
ax.axhline(0,color='gray',lw=.7);ax.set(xlabel='Barycentric rotating coordinate x',ylabel='Acceleration (normalized)',xlim=(-2,2),ylim=(-3.5,3.5))
ax.legend(fontsize=9,loc='lower left');fig.tight_layout();fig.savefig('paper-316-rotating-frame.png',facecolor='white',transparent=False)
