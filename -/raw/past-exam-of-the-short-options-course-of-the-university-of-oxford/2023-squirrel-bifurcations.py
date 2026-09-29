"""Competition equilibrium branches; Python 3.14, dependencies in pyproject.toml."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

A, B = 2., .75
RED, GREY, COEXIST = '#b33336', '#276a94', '#7653a0'
fig, axes = plt.subplots(1,2,figsize=(9.6,3.8),dpi=100,facecolor='white')
for component, ax in enumerate(axes):
    g=np.linspace(0,1,501)
    s2=np.ones_like(g) if component==0 else np.zeros_like(g)
    s3=np.zeros_like(g) if component==0 else g
    ax.plot(g[g<B],s2[g<B],color=RED,lw=2.4)
    ax.plot(g[g>=B],s2[g>=B],color=RED,lw=2.4,ls='--')
    ax.plot(g[g<1/A],s3[g<1/A],color=GREY,lw=2.4,ls='--')
    ax.plot(g[g>=1/A],s3[g>=1/A],color=GREY,lw=2.4)
    gc=np.linspace(1/A,B,150)
    sc=(A*gc-1)/(A*B-1) if component==0 else (B-gc)/(A*B-1)
    ax.plot(gc,sc,color=COEXIST,lw=2.2,ls='--')
    ax.text(.625,.54 if component==0 else .3,r'$S_4$',color=COEXIST,fontsize=12)
    ax.text(.12,.93 if component==0 else .055,r'$S_2$',color=RED,fontsize=12)
    ax.text(.87,.04 if component==0 else .92,r'$S_3$',color=GREY,fontsize=12)
    for critical in (1/A,B):ax.axvline(critical,color='#aaaaaa',lw=.8,zorder=0)
    ax.set(xlim=(0,1),ylim=(-.04,1.08),xlabel=r'$\gamma=1-\delta/r_2$',ylabel=rf'Equilibrium $u_{component+1}$',title='Red squirrels' if component==0 else 'Grey squirrels')
    ax.set_xticks([0,1/A,B,1],['0',r'$1/A$',r'$B$','1'])
    ax.spines[['top','right']].set_visible(False)
axes[0].legend(handles=[Line2D([0],[0],color='#333333',lw=2,label='Stable'),Line2D([0],[0],color='#333333',lw=2,ls='--',label='Unstable')],loc='upper right',fontsize=9)
fig.suptitle(r'Boundary stability exchanges and a saddle branch ($A=2$, $B=0.75$)',fontsize=12)
fig.tight_layout(rect=(0,0,1,.94))
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
