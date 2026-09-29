"""Original educational diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Save the PNG basename in the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(9,3.9),layout='constrained')
t=np.linspace(0,2*np.pi,300);eps=.22
for ax,scale,title in zip(axs,[(1,1),(1+eps,1-eps/2)],['Initially circular cloud','Short-time relative deformation']):
 ax.plot(scale[0]*np.cos(t),scale[1]*np.sin(t),color='#2563a6',lw=2)
 ax.scatter([0],[0],c='black',s=18)
 for a in np.linspace(0,2*np.pi,9)[:-1]:
  p=np.array([np.cos(a),np.sin(a)])
  ax.scatter([scale[0]*p[0]],[scale[1]*p[1]],c='#2563a6',s=18)
  if ax is axs[1]:
   d=np.array([2*p[0],-p[1]])*.22
   start=np.array(scale)*p
   ax.annotate('',xy=start+d,xytext=start,arrowprops={'arrowstyle':'->','color':'#b44b36','lw':1.7})
 ax.set(xlim=(-1.9,1.9),ylim=(-1.6,1.6),xlabel='Radial separation',ylabel='Transverse separation',title=title)
 ax.axhline(0,color='.85',lw=.7);ax.axvline(0,color='.85',lw=.7);ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
fig.suptitle(r'Tidal eigenvalues: $(2,-1,-1)GM/r^3$ (centre-of-mass fall removed)')
fig.savefig('paper-1-tidal-deviation.png',dpi=160)
