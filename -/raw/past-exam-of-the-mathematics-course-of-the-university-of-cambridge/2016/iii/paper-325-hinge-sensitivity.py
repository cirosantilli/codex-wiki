import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
s=np.linspace(.1,3.5,1000);x=np.select([s<1,s<=2],[(s+1)/2,1/s],default=.5)
fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=100)
for lo,hi,label,color in [(.1,1,r'Both hinges active: $(s+1)/2$','tab:blue'),(1,2,r'First margin zero: $1/s$','tab:orange'),(2,3.5,r'Only second hinge active: $1/2$','tab:green')]:
 mask=(s>=lo)&(s<=hi);ax.plot(s[mask],x[mask],label=label,color=color,lw=2.5)
for v in [1,2]:ax.axvline(v,color='gray',ls=':',alpha=.6)
ax.scatter([1,2],[1,.5],color='black',s=18,zorder=3)
ax.set(xlabel=r'First sample $s$; second sample fixed at 1',ylabel=r'Unique optimal coefficient $x(s)$',title=r'Hinge-loss sensitivity: $n=2$, $\alpha=1$',xlim=(.1,3.5),ylim=(.35,1.1))
ax.legend(fontsize=9);ax.grid(alpha=.15);fig.tight_layout();fig.savefig('paper-325-hinge-sensitivity.png',facecolor='white',transparent=False)
