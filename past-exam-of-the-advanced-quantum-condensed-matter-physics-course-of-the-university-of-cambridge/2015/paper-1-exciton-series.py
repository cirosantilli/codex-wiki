from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,2,figsize=(8,4))
for j,(label,shift) in enumerate([('Ideal bulk exciton',0),('Ideal planar exciton',.5)]):
 a=ax[j];a.axhspan(0,.3,color='gray',alpha=.2);a.axhline(0,color='gray',ls='--');a.text(.08,.1,'Free-pair continuum',fontsize=9)
 for n in range(1,4):
  energy=-1/(n-shift)**2;a.hlines(energy,.15,.75,lw=2,color='tab:blue' if j==0 else 'tab:orange')
  a.text(.8 if n<3 else .01,energy,f'n={n}',va='center',fontsize=8)
 a.set(xlim=(0,1),ylim=(-4.35,.3),xticks=[],ylabel=r'$E/R_X$ relative to continuum',title=label)
fig.suptitle('Confinement changes the ideal binding series, not just the band-edge energy',fontsize=11,y=1.03)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
