"""Original conceptual figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(8,4.6),constrained_layout=True,facecolor='white')
dt=.002;t=np.arange(0,25+dt,dt);r=.4;b=2.;K=1.;a0=K*r/(b-r)
for mode,col,label in [('active','#1864ab','Reverse flux senses active output'),('fixed','#c92a2a','Reverse flux senses total modified pool'),('tuned','#2b8a3e','Total-pool model with fine-tuned rate')]:
 m=a0;out=[]
 for time in t:
  f=1. if time<3 else .5
  out.append(f*m/a0)
  bb=b if mode!='tuned' or time<3 else .5*b+.5*r
  substrate=f*m if mode=='active' else m
  m+=dt*(r-bb*substrate/(K+substrate))
 ax.plot(t,out,lw=2,label=label,color=col)
ax.axhline(1,color='.6',lw=1,ls=':');ax.axvline(3,color='.6',lw=1,ls=':')
ax.set(xlabel='Time (chosen unit)',ylabel='Active output / initial output',title='Adaptation property and baseline activity are distinct',ylim=(.43,1.08))
ax.legend(frameon=False,loc='center right',fontsize=10);ax.grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
