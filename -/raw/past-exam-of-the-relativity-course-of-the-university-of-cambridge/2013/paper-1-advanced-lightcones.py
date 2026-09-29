"""Original advanced-coordinate future-null schematic. Python 3.14; numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.7,4.7),layout='constrained',facecolor='white')
ax.axvspan(.1,1,color='#faf0e7');ax.axvline(1,color='black',ls='--',lw=1.2)
for r in [.55,1.,1.7,2.5]:
 f=1-1/r;ingo=np.array([-1.,1.]);out=np.array([f/2,1-f/2]);ingo*=.40/np.linalg.norm(ingo);out*=.40/np.linalg.norm(out)
 for T in [.35,1.4,2.45]:
  p=np.array([r,T]);tri=np.array([p,p+ingo,p+out]);ax.fill(tri[:,0],tri[:,1],color='#8cc5df',alpha=.4)
  for vv in [ingo,out]:ax.annotate('',xy=p+vv,xytext=p,arrowprops=dict(arrowstyle='->',lw=1.2,color='#155c83'))
rr=np.linspace(.13,2.8,200);ax.plot(rr,2.8-rr,ls=':',color='#b65d30',lw=1.6);ax.text(1.85,.68,'Ingoing light: v constant',rotation=-30,fontsize=9,color='#a15028')
ax.text(.14,3.12,'Inside: both future null\ndirections decrease r',fontsize=9)
ax.text(1.09,3.14,'Regular future horizon',fontsize=10)
ax.set(xlim=(.1,2.9),ylim=(0,3.5),xlabel=r'$r/r_s$',ylabel=r'$(cv-r)/r_s$',title='Advanced Schwarzschild chart: future light cones')
ax.grid(alpha=.15);fig.savefig('paper-1-advanced-lightcones.png',dpi=150,facecolor='white')
