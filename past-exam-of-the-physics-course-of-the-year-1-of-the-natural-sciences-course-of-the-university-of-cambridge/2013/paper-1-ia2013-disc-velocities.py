"""Original equal-mass collision velocity construction; Python 3.14, NumPy, Matplotlib.
Run from an output directory; writes its PNG basename to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
angle=np.deg2rad(35)
n=np.array([np.cos(angle),-np.sin(angle)])
v=np.array([1.,0.]); va=v-(v@n)*n; vb=(v@n)*n
fig,axes=plt.subplots(2,2,figsize=(8.0,5.8),layout='constrained')
sets=[(v,np.zeros(2)),(va,vb),(v/2,-v/2),(va-v/2,vb-v/2)]
titles=['Laboratory: before','Laboratory: after','Centre of momentum: before','Centre of momentum: after']
for ax,(a,b),title in zip(axes.flat,sets,titles):
 ax.axhline(0,color='0.83',lw=.8);ax.axvline(0,color='0.83',lw=.8)
 for velocity,name,color,off in [(a,'A','#1565c0',(.025,.05)),(b,'B','#d66a00',(.025,-.08))]:
  if np.linalg.norm(velocity)>1e-12:ax.annotate('',xy=velocity,xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':color,'lw':2.4,'mutation_scale':16})
  else:ax.plot(0,0,'o',color=color,ms=5)
  ax.text(velocity[0]+off[0],velocity[1]+off[1],name,color=color,weight='bold')
 ax.set(xlim=(-.73,1.15),ylim=(-.7,.7),aspect='equal',title=title,xlabel=r'$v_x/v$',ylabel=r'$v_y/v$')
 ax.set_xticks([-.5,0,.5,1]);ax.set_yticks([-.5,0,.5])
fig.suptitle('Elastic collision: equal masses, one initially at rest',fontsize=13)
fig.savefig('paper-1-ia2013-disc-velocities.png',dpi=140,facecolor='white')
