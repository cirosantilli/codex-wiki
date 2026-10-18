"""Original illustration for the 2016 Oxford Mathematical Methods I solution.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

theta=np.linspace(0,2*np.pi,700)
fig,axs=plt.subplots(1,2,figsize=(9.4,4.8),layout='constrained')
for i,r in enumerate([np.pi,2*np.pi,3*np.pi]):
 axs[0].plot(r*np.cos(theta),r*np.sin(theta),color=['#226bb0','#368948','#9b3d2e'][i],label=[r'$\pi$',r'$2\pi$',r'$3\pi$'][i],lw=1.8)
axs[0].scatter([0],[0],color='black',s=28,label='origin',zorder=3)
axs[0].set(title=r'$\sin |z|=0$, $|z|<10$',xlim=(-10.5,10.5),ylim=(-10.5,10.5));axs[0].legend(fontsize=9,loc='upper right')
r=np.exp(2);axs[1].plot(r*np.cos(theta),r*np.sin(theta),color='#774da3',lw=2)
axs[1].annotate(r'radius $e^2$',(r/np.sqrt(2),r/np.sqrt(2)),xytext=(-2,2),arrowprops={'arrowstyle':'->'},bbox={'facecolor':'white','edgecolor':'none'})
axs[1].set(title=r'$\operatorname{Re}\log z=2$',xlim=(-9,9),ylim=(-9,9))
for ax in axs:
 ax.axhline(0,color='.6',lw=.8);ax.axvline(0,color='.6',lw=.8);ax.set_aspect('equal');ax.set(xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$');ax.grid(alpha=.16)
fig.savefig(Path.cwd()/'2016-complex-loci.png',dpi=140,transparent=False)
plt.close(fig)
