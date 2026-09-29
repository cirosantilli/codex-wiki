"""Original failure probability plots; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Uses the independent-lifetime assumption for the two joint curves. PNG to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

s = np.linspace(0,1,500)
fig, axes = plt.subplots(2,3,figsize=(9.5,5.6),layout='constrained',facecolor='white')
plots = [
    (np.ones_like(s), r'$Tf_1(t)$', 'Uniform density'),
    (2*s, r'$Tf_2(t)$', 'Linear density'),
    (s, r'$P_1(t)$', 'First failure CDF'),
    (s*s, r'$P_2(t)$', 'Second failure CDF'),
    (s**3, r'$P(t)$', 'Both failed (independent)'),
    (s+s*s-s**3, r'$R(t)$', 'At least one failed (independent)'),
]
for i,(ax,(vals,label,title)) in enumerate(zip(axes.flat,plots)):
    ax.plot(s,vals,color='#0072b2',lw=2)
    if i<2:
        ax.plot([1,1.4],[0,0],color='#0072b2',lw=2)
        ax.plot([1,1],[0,vals[-1]],ls=':',color='#777777')
        ax.plot(1,vals[-1],'o',mfc='white',mec='#0072b2',ms=4)
        ax.plot(1,0,'o',color='#0072b2',ms=4)
    else:
        ax.plot([1,1.4],[1,1],color='#0072b2',lw=2)
    ax.set(xlim=(0,1.4),ylim=(-.05,2.15 if i==1 else 1.15),
           xlabel=r'$t/T$',ylabel=label,title=title)
    ax.set_title(title.replace(' (independent)', '\n(independent)'), fontsize=10)
    ax.axvline(1,lw=.8,color='#999999',ls=':')
    ax.grid(alpha=.17)
ax=axes.flat[-1]
ax.plot(1/3,11/27,'o',color='#d55e00',ms=5)
ax.annotate(r'$(1/3,11/27)$',(1/3,11/27),xytext=(.48,.2),fontsize=9,
            arrowprops={'arrowstyle':'-', 'color':'#777777'})
fig.suptitle('Dimensionless failure densities and probabilities',fontsize=13)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
