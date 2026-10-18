"""Plot the signed SIS lens equation, not the source ray diagram. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':13,'figure.facecolor':'white'})
fig,ax=plt.subplots(figsize=(9,5.3),layout='constrained')
for domain in [np.linspace(-3,-.001,400),np.linspace(.001,3,400)]:
    ax.plot(domain,domain-np.sign(domain),color='#333333',lw=2.5)
for beta,color,label in [(.5,'#205c96','inside: two images'),(1.4,'#a43c2a','outside: one image')]:
    ax.axhline(beta,color=color,linestyle='--',lw=1.6,label=rf'$\beta/\theta_E={beta}$, '+label)
    roots=[beta+1]+([beta-1] if beta<1 else [])
    ax.scatter(roots,[beta]*len(roots),color=color,s=55,zorder=5)
    for root in roots:
        ax.plot([root,root],[0,beta],color=color,linestyle=':',lw=1.2)
        ax.text(root,-.16,rf'${root:g}$',ha='center',va='top',color=color)
ax.scatter([0,0],[-1,1],facecolor='white',edgecolor='#333333',s=60,zorder=6)
ax.axhline(0,color='#888888',lw=.8)
ax.axvline(0,color='#888888',lw=.8)
ax.set_xlim(-3,3);ax.set_ylim(-2.2,2.2)
ax.set_xlabel(r'Signed image angle $\theta/\theta_E$')
ax.set_ylabel(r'Signed source angle $\beta/\theta_E$')
ax.set_title(r'Singular isothermal lens: $\beta/\theta_E=\theta/\theta_E-\mathrm{sgn}(\theta)$',fontsize=16)
ax.legend(loc='lower right',fontsize=11)
ax.grid(alpha=.18)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
