from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12})

fig,axs=plt.subplots(2,2,figsize=(11,8),layout='constrained',facecolor='white')
x=np.linspace(-1.8,2,500);y=np.linspace(.002,2.2,380);X,Y=np.meshgrid(x,y);R=np.hypot(X,Y);V=Y*np.log(R)+X*np.arctan2(Y,X)
cs=axs[0,0].contour(X,Y,V,levels=[-3,-2,-1,-.4,0,.2,.5,1,2],colors='#126782');axs[0,0].clabel(cs,fontsize=9)
t=np.linspace(0,np.pi,200);axs[0,0].plot(np.exp(-1)*np.cos(t),np.exp(-1)*np.sin(t),'--',color='#b14c2e',label=r'$r=e^{-1}$')
axs[0,0].set(xlabel='x',ylabel='y',title=r'Equipotentials: $V\pi/V_0$');axs[0,0].legend(fontsize=10)
E=np.linspace(.00001,30,2000);q=np.sqrt(E+4);T=1/(1+4*np.sin(2*q)**2/(E*(E+4)))
axs[0,1].plot(E,T,color='#126782');axs[0,1].set(xlabel=r'$E$  (units $\hbar^2/(2m)=1$)',ylabel='Transmission probability',ylim=(0,1.05),title='Illustrative well: depth 4, width 2')
def bisect(fn,l,r):
 for _ in range(80):
  mid=(l+r)/2
  if fn(l)*fn(mid)<=0:r=mid
  else:l=mid
 return (l+r)/2
qe=bisect(lambda q:q*np.tan(q)-np.sqrt(4-q*q),.001,np.pi/2-.001)
qo=bisect(lambda q:-q/np.tan(q)-np.sqrt(4-q*q),np.pi/2+.001,1.9999)
kappas=np.sqrt(4-np.array([qe,qo])**2)
ax=axs[1,0];ax.axhline(0,color='gray');ax.axvline(0,color='gray');ax.plot(np.zeros(2),kappas,'o',color='#126782');ax.text(.15,1.5,'Bound poles of t(k)',fontsize=11);ax.text(-1.8,-.75,'Virtual / resonance poles\nrequire continuation; not bound states',fontsize=10)
ax.set(xlim=(-2,2),ylim=(-1,2.2),xlabel='Re k',ylabel='Im k',title='Physical-sheet bound poles')
ax=axs[1,1];ax.axhline(0,color='gray');ax.axvline(0,color='gray');ax.plot(-kappas*kappas,[0,0],'o',color='#126782');ax.plot([0,3],[0,0],color='#b14c2e',lw=4,alpha=.5);ax.text(.2,.35,'Continuum cut',fontsize=11);ax.text(-3.5,-.5,'Negative real bound energies',fontsize=10)
ax.set(xlim=(-4,3),ylim=(-1,1),xlabel='Re E',ylabel='Im E',title=r'$E=k^2$: sheet must be specified')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
