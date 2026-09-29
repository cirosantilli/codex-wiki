"""Velocity vectors of an elastic m:2m collision, laboratory and CM frames."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

v1=np.array([(1+np.sqrt(5))/4,(np.sqrt(3)+np.sqrt(15))/12])
v2=(np.array([1.,0.])-v1)/2
cm=np.array([1/3,0.])
fig,axes=plt.subplots(2,2,figsize=(10,7.2),layout='constrained')
for ax,(title,a,b) in zip(axes.flat,[('Laboratory: before',np.array([1.,0.]),np.zeros(2)),('Centre of mass: before',np.array([2/3,0.]),np.array([-1/3,0.])),('Laboratory: after',v1,v2),('Centre of mass: after',v1-cm,v2-cm)]):
 for vec,color,label in [(a,'#176bb0',r'$m$'),(b,'#d65a16',r'$2m$')]:
  if np.linalg.norm(vec)>1e-10:
   ax.annotate('',xy=vec,xytext=(0,0),arrowprops=dict(arrowstyle='->',color=color,lw=2.8))
   ax.text(*(vec+np.array([.025,.035] if vec[1]>=0 else [-.06,-.10])),label,color=color,fontsize=12)
  else:ax.text(.04,-.11,label+' at rest',color=color)
 ax.axhline(0,lw=.6,color='.5');ax.axvline(0,lw=.6,color='.5')
 ax.set(title=title,xlim=(-.48,1.18),ylim=(-.48,.65),aspect='equal',xlabel=r'$v_x/V$',ylabel=r'$v_y/V$')
 ax.grid(alpha=.15)
fig.suptitle(r'Elastic collision: projectile deflected $30^\circ$ in the laboratory',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
