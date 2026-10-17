"""Original perpendicular orbit speed for a thin uniform rod."""
import numpy as np
import matplotlib.pyplot as plt
x=np.geomspace(.01,100,1000)
fig,ax=plt.subplots(figsize=(7.6,4.6),facecolor='white',layout='constrained')
ax.loglog(x,(1+x*x)**(-.25),lw=2,color='#235c87',label=r'Exact $(1+(r/a)^2)^{-1/4}$')
y=np.geomspace(1,100,300);ax.loglog(y,y**(-.5),ls='--',lw=1.4,color='#b5671a',label=r'Large-r $(r/a)^{-1/2}$')
ax.axhline(1,ls=':',color='.5',lw=1)
ax.set(xlabel=r'$r/a$',ylabel=r'$v/\sqrt{GM/a}$',title='Circular orbit in the perpendicular-bisector plane')
ax.legend(loc='lower left');ax.grid(alpha=.15)
fig.savefig('paper-1-ia2010-rod-orbit.png',dpi=165,facecolor='white');plt.close(fig)
