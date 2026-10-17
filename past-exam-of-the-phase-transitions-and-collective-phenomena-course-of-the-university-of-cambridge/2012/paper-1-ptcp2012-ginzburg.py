"""Original scalar Landau wells and illustrative Ginzburg power-counting ratios."""
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,4.4),facecolor='white',layout='constrained')
p=np.linspace(-1.7,1.7,801)
for r,col in [(1,'#235f8a'),(0,'#b07a17'),(-1,'#b44847')]:
    axes[0].plot(p,r*p*p/2+p**4/4,color=col,lw=2,label=r'$r='+str(r)+'$')
axes[0].scatter([-1,1],[-.25,-.25],s=28,color='#b44847',zorder=5)
axes[0].set(xlabel=r'$\phi$',ylabel=r'$r\phi^2/2+\phi^4/4$',ylim=(-.4,2.3),title='Uniform mean-field potentials; u = 1');axes[0].legend()
t=np.geomspace(1e-5,1,700)
for d,col in [(3,'#b44847'),(4,'#b07a17'),(5,'#235f8a')]:
    axes[1].loglog(t,.03*t**((d-4)/2),lw=2,color=col,label=r'$d='+str(d)+'$')
axes[1].axhline(1,color='.3',lw=1,ls='--');axes[1].text(2e-5,1.23,'Order-one crossover',fontsize=10)
axes[1].set(xlabel=r'$|t|$',ylabel=r'Illustrative $\mathcal{G}=0.03\,|t|^{(d-4)/2}$',title='Approaching criticality means moving left')
axes[1].legend();axes[1].grid(alpha=.15)
fig.savefig('paper-1-ptcp2012-ginzburg.png',dpi=165,facecolor='white')
plt.close(fig)
