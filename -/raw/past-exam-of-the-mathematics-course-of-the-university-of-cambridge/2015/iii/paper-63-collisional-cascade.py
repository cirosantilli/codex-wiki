from pathlib import Path
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 10, "savefig.facecolor": "white"})

d=np.geomspace(.001,100,600);Q=3*d**(-.5)+d**1.5;tc=d**.5*(Q/4)**(5/6)
fig,axes=plt.subplots(1,2,figsize=(10.,4.4),dpi=100,facecolor='white')
ax=axes[0];ax.loglog(d,tc,color='#252525',lw=2)
fronts=[.05,.5,10];colors=['#308341','#1269a8','#b52b35']
for dt,c in zip(fronts,colors):
 age=dt**.5*((3*dt**(-.5)+dt**1.5)/4)**(5/6)
 ax.axhline(age,color=c,ls='--',lw=1,label=rf'$t=t_{{c0}}({dt}D_w)$')
 ax.scatter([dt],[age],color=c,s=25,zorder=4)
ax.axvline(1,color='gray',ls=':',label=r'$D_w$ (minimum disruption threshold)')
ax.text(.008,.67,r'Strength slope $1/12$',fontsize=9)
ax.text(6,70,r'Gravity slope $7/4$',fontsize=9,rotation=30)
ax.set(xlabel=r'Diameter $D/D_w$',ylabel=r'Primordial time $t_{c0}(D)/t_{c0}(D_w)$',title='Small diameters begin processing first',ylim=(.35,5000))
ax.legend(fontsize=7);ax.grid(alpha=.15,which='both')
ax=axes[1];initial=d**.5;ax.loglog(d,initial,color='#252525',ls=':',label='Initial: number index 7/2')
for dt,c in zip(fronts,colors):
 # Sharp, continuously matched, schematic steady branches, not a kernel evolution simulation.
 m=initial.copy();at=dt**.5
 if dt<=1:
  small=d<dt;m[small]=at*(d[small]/dt)**(3/11)
 else:
  medium=(d>=1)&(d<dt);m[medium]=at*(d[medium]/dt)
  small=d<1;m[small]=(at/dt)*d[small]**(3/11)
 ax.loglog(d,m,color=c,label=rf'Schematic front $D_t={dt}D_w$')
ax.axvline(1,color='gray',ls=':');ax.set(xlabel=r'Diameter $D/D_w$',ylabel='Mass per logarithmic bin (relative units)',title='Evolved number indices: 41/11, then 3')
ax.legend(fontsize=7);ax.grid(alpha=.15,which='both');fig.tight_layout()
fig.savefig(Path.cwd()/'paper-63-collisional-cascade.png',dpi=100,facecolor='white')
