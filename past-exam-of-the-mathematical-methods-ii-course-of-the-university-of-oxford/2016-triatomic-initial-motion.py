"""Original illustration for the 2016 Oxford Mathematical Methods II solution.
Run from any output directory; writes only the matching PNG to that directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

t=np.linspace(0,8*np.pi,1400)
x=np.array([.25+.5*np.cos(t)-.75*np.cos(np.sqrt(2)*t),.25+.75*np.cos(np.sqrt(2)*t),.25-.5*np.cos(t)-.75*np.cos(np.sqrt(2)*t)])
fig,ax=plt.subplots(figsize=(9,4.7),layout='constrained')
for i,(y,c) in enumerate(zip(x,['#2069a8','#b44026','#23925b'])):ax.plot(t/(2*np.pi),y,color=c,label=f'atom {i+1}',lw=1.7)
ax.axhline(.25,color='black',ls='--',lw=1.3,label='centre of mass')
ax.scatter([0,0,0],[0,1,-1],c=['#2069a8','#b44026','#23925b'],zorder=4)
ax.set(xlabel=r'$t\omega/(2\pi)$, with $\omega=\sqrt{k/m}$',ylabel=r'$x_i/d$',title=r'$M=2m$: released from rest at $(x_1,x_2,x_3)=(0,d,-d)$',xlim=(0,4),ylim=(-1.6,1.6))
ax.grid(alpha=.2);ax.legend(ncol=2,loc='upper right')
fig.savefig(Path.cwd()/'2016-triatomic-initial-motion.png',dpi=140,transparent=False)
plt.close(fig)
