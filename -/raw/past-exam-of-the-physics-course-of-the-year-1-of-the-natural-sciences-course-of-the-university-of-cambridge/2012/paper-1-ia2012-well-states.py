import numpy as np
import matplotlib.pyplot as plt
def root(f,lo,hi):
 for _ in range(100):
  mid=(lo+hi)/2
  if f(lo)*f(mid)<=0:hi=mid
  else:lo=mid
 return (lo+hi)/2
x=np.linspace(-3,3,1600)
fig,axes=plt.subplots(1,2,figsize=(9,3.8),sharey=True,layout='constrained')
for ax,z0,odd in [(axes[0],np.hypot(.9,1.14),False),(axes[1],2.4,True)]:
 if odd:
  z=root(lambda z:-z/np.tan(z)-np.sqrt(z0*z0-z*z),np.pi/2+1e-8,z0-1e-8)
 else:
  z=root(lambda z:z*np.tan(z)-np.sqrt(z0*z0-z*z),1e-8,min(z0,np.pi/2)-1e-8)
 w=np.sqrt(z0*z0-z*z)
 psi=np.where(abs(x)<=1,np.sin(z*x) if odd else np.cos(z*x),(np.sign(x)*np.sin(z) if odd else np.cos(z))*np.exp(-w*(abs(x)-1)))
 psi/=np.max(abs(psi))
 ax.axvspan(-1,1,color='#e7eef5');ax.axvline(-1,color='#777',ls=':');ax.axvline(1,color='#777',ls=':');ax.axhline(0,color='#888',lw=.7)
 ax.plot(x,psi,color='#8f59a4' if odd else '#2475aa',lw=2)
 ax.set(xlabel=r'$x/(a/2)$',xticks=[-3,-1,0,1,3],xlim=(-3,3),ylim=(-1.15,1.2));ax.grid(alpha=.15)
axes[0].set(title='Ground state in the numerical well',ylabel='Wavefunction (arbitrary scale)')
axes[1].set_title('First excited state in a deeper well')
axes[1].text(0,-1.08,'Illustrative deeper well: the numerical well has no odd bound state.',ha='center',fontsize=8)
fig.savefig('paper-1-ia2012-well-states.png',dpi=160,facecolor='white')
