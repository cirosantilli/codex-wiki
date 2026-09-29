from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'savefig.facecolor':'white'})
fig,ax=plt.subplots(figsize=(7.3,5.2),constrained_layout=True)
x=np.linspace(-3.2,4.8,700);ax.plot(x,(x*x-1)/2,lw=2,color='#126d8a',label=r'$y=(x^2-1)/2$');ax.plot(x,4.5-x*x/18,lw=2,color='#b64d36',label=r'$y=9/2-x^2/18$')
q=np.array([3.,4.]);v=np.array([1.,3.])/np.sqrt(10);w=np.array([-3.,1.])/np.sqrt(10)
for d,c in [(v,'#126d8a'),(w,'#b64d36')]:
 ends=q+np.array([-1.,1.])[:,None]*d;ax.plot(ends[:,0],ends[:,1],'--',lw=1.4,color=c)
e=.28;mark=np.array([q+e*v,q+e*(v+w),q+e*w]);ax.plot(mark[:,0],mark[:,1],color='.25',lw=1)
ax.scatter([3],[4],color='black',s=30,zorder=5);ax.annotate('$(3,4)$',xy=(3,4),xytext=(3.35,3.35),arrowprops={'arrowstyle':'-','color':'.4'})
ax.axhline(0,color='.6',lw=.8);ax.axvline(0,color='.6',lw=.8);ax.set(xlim=(-3.4,4.9),ylim=(-1,7),xlabel='$x$',ylabel='$y$',title='Two solution branches, orthogonal tangents');ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18);ax.legend(loc='upper left',framealpha=.95)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110)
