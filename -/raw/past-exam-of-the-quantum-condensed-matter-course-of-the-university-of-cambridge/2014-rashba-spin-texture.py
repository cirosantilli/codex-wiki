"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(8.5,4),layout='constrained');theta=np.linspace(0,2*np.pi,400);ang=np.linspace(0,2*np.pi,12,endpoint=False)
for ax,sign,label in zip(axs,[-1,1],[r'Outer: $k_1=0.11\,\AA^{-1}$, lower band',r'Inner: $k_2=0.01\,\AA^{-1}$, upper band']):
 ax.plot(np.cos(theta),np.sin(theta),color='0.45');xx=np.cos(ang);yy=np.sin(ang);sx=sign*(-yy);sy=sign*xx
 ax.quiver(xx,yy,sx,sy,angles='xy',scale_units='xy',scale=3.5,color='tab:orange' if sign==-1 else 'tab:purple',width=.009)
 ax.annotate(r'$\mathbf{k}$',(.65,0),(.1,0),arrowprops=dict(arrowstyle='->',color='0.4'),va='bottom',color='0.4');ax.axhline(0,color='0.8',lw=.6);ax.axvline(0,color='0.8',lw=.6)
 ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),xlabel=r'$k_x/k_i$',ylabel=r'$k_y/k_i$',title=label);ax.set_aspect('equal')
fig.suptitle(r'Original tangential spin expectations for $\lambda>0$; circle radii normalized separately')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
