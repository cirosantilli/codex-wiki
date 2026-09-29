"""Compare the supplied model wells; Python 3.14/NumPy 2.3/Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

r=np.linspace(3.1,10,1200)
fig,ax=plt.subplots(figsize=(6.8,4.4),layout='constrained')
for sigma,depth,color in [(3.4,.06,'#245c9f'),(4.9,.05,'#b45309')]:
    v=4*depth*((sigma/r)**12-(sigma/r)**6)
    re=2**(1/6)*sigma
    ax.plot(r,v,color=color,lw=2,label=f'$\\sigma={sigma}$, $\\alpha={depth:.2f}$')
    ax.plot(re,-depth,'o',ms=5,color=color)
    ax.annotate(f'$r_e={re:.3f}$', (re,-depth), (re+.35,-depth-.005),
                fontsize=10,color=color)
ax.axhline(0,color='0.5',lw=.8)
ax.plot(5.0062646427,-.0210690864,'o',color='0.15',ms=4)
# Compute the annotation location from the potential rather than rounding it.
cross=5.0062646427
vcross=4*.06*((3.4/cross)**12-(3.4/cross)**6)
ax.lines[-1].set_ydata([vcross])
ax.annotate('curves cross', (cross,vcross),(6.35,-.040),
            arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
ax.set(xlim=(3.1,10),ylim=(-.072,.055),xlabel='internuclear separation / bohr',
       ylabel='potential energy / hartree',title='Model potential curves; spin is not a plotted variable')
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='upper right',frameon=False,fontsize=11)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
plt.close(fig)
