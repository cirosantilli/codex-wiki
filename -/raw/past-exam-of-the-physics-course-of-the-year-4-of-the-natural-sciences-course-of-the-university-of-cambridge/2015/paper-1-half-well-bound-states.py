"""Original dimensionless half-well matching plot, chosen nu=2pi."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

nu=2*np.pi;fig,ax=plt.subplots(figsize=(9,5.2),dpi=100,facecolor="white")
z=np.linspace(0,nu,1201);ax.plot(z,-np.sqrt(np.maximum(0,nu*nu-z*z)),color="#a74633",lw=2.5,label=r"$-qa=-\sqrt{\nu^2-z^2}$")
for n in [1,2]:
    lo=(n-.5)*np.pi;hi=n*np.pi;zz=np.linspace(lo+1e-5,hi-1e-5,501)
    ax.plot(zz,zz/np.tan(zz),color="#265b83",lw=2.3,label=r"$z\cot z$" if n==1 else None)
    root=brentq(lambda a:a/np.tan(a)+np.sqrt(nu*nu-a*a),lo+1e-6,hi-1e-6)
    ax.scatter([root],[-np.sqrt(nu*nu-root*root)],color="black",s=30,zorder=4)
ax.set(xlim=(0,nu+.15),ylim=(-7,.5),xlabel=r"$z=ka$",ylabel="Matching functions",title=r"Two normalizable intersections for $\nu=2\pi$")
ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
ax.grid(alpha=.2);ax.legend(loc="upper left")
fig.text(.5,.025,"A new bound state appears only after its zero-energy threshold is crossed.",ha="center",fontsize=11)
fig.subplots_adjust(left=.1,right=.98,top=.88,bottom=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
