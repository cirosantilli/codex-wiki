"""Original illustration for the 2016 Oxford Physics 1 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import numpy as np
plt.rcParams.update({"font.size": 10.5, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

beta=.4;gamma=1/np.sqrt(1-beta*beta);clock=np.linspace(0,2.5,300)
fig,axs=plt.subplots(1,2,figsize=(9.4,5.7))
for j,ax in enumerate(axs):
 if j==0:
  A=np.array([0.,0.]);B=np.array([1.,1.]);C=np.array([0.,2.]);laser=np.zeros_like(clock);mirror=np.ones_like(clock);observer=beta*clock
 else:
  A=np.array([0.,0.]);B=np.array([gamma*(1-beta),gamma*(1-beta)]);C=np.array([-2*gamma*beta,2*gamma]);laser=-beta*clock;mirror=1/gamma-beta*clock;observer=np.zeros_like(clock)
 ax.plot(laser,clock,color='black',lw=1.5,label='laser/source');ax.plot(mirror,clock,color='.5',lw=1.5,label='mirror');ax.plot(observer,clock,color='#33834a',ls='--',lw=1.5,label='second observer')
 ax.plot([A[0],B[0]],[A[1],B[1]],color='#266ca5',lw=2.5);ax.plot([B[0],C[0]],[B[1],C[1]],color='#be7727',lw=2.5)
 for name,P,off in [('A',A,(-14,-13)),('B',B,(7,1)),('C',C,(-15,7))]:ax.scatter([P[0]],[P[1]],s=25,color='#303030',zorder=5);ax.annotate(name,P,xytext=off,textcoords='offset points',fontsize=12)
 ax.set(xlim=(-1.2,1.45),ylim=(-.18,2.55),xlabel=('$x/d$' if j==0 else "$x'/d$"),ylabel=('$ct/d$' if j==0 else "$ct'/d$"),title=('Source rest frame' if j==0 else 'Moving frame'))
 ax.set_aspect('equal');ax.grid(alpha=.17);ax.axhline(0,color='.7',lw=.7)
handles,labels=axs[0].get_legend_handles_labels();fig.legend(handles,labels,loc='lower center',ncol=3,frameon=False,fontsize=10)
fig.suptitle(r'Same emission (A), reflection (B), return-to-source (C); illustrative $\beta=0.4$',fontsize=12)
fig.tight_layout(rect=(0,.08,1,.94))
fig.savefig(Path.cwd()/'2016-resit-lorentz-light-round-trip.png',dpi=140,transparent=False);plt.close(fig)
