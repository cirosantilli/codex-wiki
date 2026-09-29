"""Original position-dependent principal-frame diagram.
Python 3.14, NumPy 2.3, Matplotlib 3.10. Run in mirrored _media; PNG goes to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np

fig,ax=plt.subplots(figsize=(6.5,5.0),facecolor="white")
radial="#245b80";tangent="#b95528"
ax.axhline(0,color="#9ca5b1",lw=.8);ax.axvline(0,color="#9ca5b1",lw=.8)
a=np.linspace(0,2*np.pi,400)
rad=1.2
ax.plot(rad*np.cos(a),rad*np.sin(a),color="#bbc5d1",lw=1,ls="--")
for theta in [np.pi/6,5*np.pi/6,3*np.pi/2]:
    er=np.array([np.cos(theta),np.sin(theta)]);et=np.array([-np.sin(theta),np.cos(theta)])
    point=rad*er
    ax.plot([0,point[0]],[0,point[1]],color="#c7cdd6",lw=.8,ls=":")
    ax.plot(*point,"o",color="#25374d",ms=4)
    for direction,color in [(er,radial),(et,tangent)]:
        end=point+.61*direction
        ax.add_patch(FancyArrowPatch(point,end,arrowstyle="-|>",mutation_scale=15,color=color,lw=1.8))
ax.text(1.88,.1,r"$x_1$",fontsize=12);ax.text(.08,1.83,r"$x_2$",fontsize=12)
ax.text(-1.94,1.77,r"$\odot\ e_3$",fontsize=14)
ax.text(-1.94,1.51,"out of the plane",fontsize=10)
ax.set(xlim=(-2.05,2.08),ylim=(-1.98,1.96),aspect="equal",title="The principal frame changes with the observation point")
ax.legend(handles=[Line2D([0],[0],color=radial,lw=2,label=r"Radial $e_r$: eigenvalue $r^2$"),Line2D([0],[0],color=tangent,lw=2,label=r"Tangential $e_\theta$: eigenvalue $0$")],loc="upper center",bbox_to_anchor=(.5,-.025),ncol=2,frameon=True,facecolor="white",framealpha=1,fontsize=9)
ax.set_xticks([]);ax.set_yticks([]);ax.spines[:].set_visible(False)
fig.text(.5,.025,r"The third eigenvalue is $3r^2$; at $r=0$ all eigenvalues vanish and the axes are arbitrary.",ha="center",fontsize=9)
fig.tight_layout(rect=(0,.13,1,1))
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
plt.close(fig)
