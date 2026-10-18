"""Original counterpropagating Gaussian envelopes in a confocal cavity; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
z=np.linspace(-.5,.5,600);b=.28;bp=.25/b
w=np.sqrt(b+z*z/b);wp=np.sqrt(bp+z*z/bp);wm=np.sqrt(.5+z*z/.5)
fig,ax=plt.subplots(figsize=(8.2,4.7),facecolor='white')
for y,color,label,ls in [(w,'#126782',r'Incident: $z_R=0.28L$','-'),(wp,'#a34100',r'Reflected: $z_R\prime=0.893L$','-'),(wm,'#68717b',r'Matched: $z_R=L/2$','--')]:
    ax.plot(z,y,color=color,label=label,lw=1.8,ls=ls);ax.plot(z,-y,color=color,lw=1.8,ls=ls)
for side in [-.5,.5]:ax.plot([side,side],[-1.30,1.30],color='#273343',lw=3)
ax.axhline(0,color='#bbbbbb',lw=.7);ax.axvline(0,color='#bbbbbb',lw=.7,ls=':')
ax.text(-.5,1.38,r'$M_1$',ha='center',fontsize=13);ax.text(.5,1.38,r'$M_2$',ha='center',fontsize=13)
ax.set(xlim=(-.56,.56),ylim=(-1.45,1.55),xlabel=r'Axial distance from central waist $z/L$',ylabel=r'Envelope radius / $\sqrt{\lambda L/\pi}$',title=r'Equal mirror spots; reciprocal waist Rayleigh ranges')
ax.legend(loc='lower center',fontsize=10,framealpha=.95)
fig.tight_layout();fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
