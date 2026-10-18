"""Twin reunion in Earth coordinates; no source illustration copied."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

T=221/35;t1=13/5;x=-17/7
fig,ax=plt.subplots(figsize=(7.6,7.2),layout='constrained')
ax.plot([0,1,x],[0,t1,T],lw=2.5,color='#156db5',label=r'Alison: $\tau=134/35$ yr')
ax.plot([0,x],[0,T],lw=2.5,color='#c55319',label=r'Belinda: $\tau=204/35$ yr')
ax.axvline(0,color='.5',ls=':',label='Earth')
ax.scatter([0,1,x],[0,t1,T],color='black',zorder=5)
ax.annotate('turnaround\n(1, 13/5)',(1,t1),xytext=(1.22,t1+.12),fontsize=10)
ax.annotate('reunion\n(−17/7, 221/35)',(x,T),xytext=(x+.35,T-.4),fontsize=10)
ax.plot([x,0],[T,T],color='.6',ls='--',lw=.8)
ax.set(xlabel='Earth-frame position (light years)',ylabel='Earth-frame time (years)',xlim=(-3,2.5),ylim=(-.2,6.9))
ax.grid(alpha=.18);ax.legend(loc='upper right',fontsize=10)
ax.set_title('Clock comparison along two different worldlines')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
