"""Original figure. Tested Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired image directory; writes an opaque white PNG to CWD.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2.5,2.5,120);y=x.copy();X,Y=np.meshgrid(x,y)
fig,ax=plt.subplots(figsize=(6.6,5),dpi=100,facecolor="white")
ax.streamplot(x,y,-2*Y,-2*X,color="#226cb2",density=1.0,linewidth=0.9,arrowsize=1.4)
ax.plot(x,x,"--",color="#9b3a27",lw=1.4,label="stable: toward origin")
ax.plot(x,-x,"--",color="#ad7200",lw=1.4,label="unstable: away from origin")
ax.scatter([0],[0],color="black",s=24,zorder=5)
ax.set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),xlabel="$x$",ylabel="$y$",aspect="equal")
ax.legend(loc="upper center",fontsize=9,framealpha=1);ax.set_title(r"$u=-2y,\ v=-2x$; streamlines $x^2-y^2=C$")
fig.tight_layout();fig.savefig("paper-1-streamlines.png",facecolor="white",transparent=False)
