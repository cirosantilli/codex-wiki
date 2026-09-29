from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

w=np.linspace(0,2*np.pi,900);a=2/3;e=.5
r=np.array([a*(e+np.cos(w)),a*np.sqrt(1-e*e)*np.sin(w)])
t=(w+e*np.sin(w))/np.sqrt(2/a**3);R=np.array([np.zeros_like(t),t/2])
fig,ax=plt.subplots(1,2,figsize=(9,4.5))
for j,lab in enumerate(['Center-of-mass frame','Laboratory frame: center of mass drifts']):
 c=np.zeros_like(R) if j==0 else R
 for sign,name,color in [(-1,'A','tab:blue'),(1,'B','tab:orange')]:
  xy=c+sign*r/2
  ax[j].plot(*xy,label=name,color=color,lw=2)
  ax[j].scatter(*xy[:,0],color=color,s=40,marker='o')
  i=np.argmin(abs(w-np.pi));ax[j].scatter(*xy[:,i],color=color,s=48,marker='s')
 ax[j].plot(*c,color='gray',ls=':',lw=1.5)
 ax[j].set(xlabel=r'$x/a_1$',ylabel=r'$y/a_1$',title=lab,aspect='equal');ax[j].grid(alpha=.2);ax[j].legend()
ax[0].scatter(0,0,color='black',s=18);ax[0].text(.03,-.08,'CM',fontsize=9)
fig.suptitle('Dots: initial positions; squares: first closest approach',y=1.02)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
