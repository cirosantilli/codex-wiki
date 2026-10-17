"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

n=1.5;tc=np.arcsin(1/n);th=np.linspace(0,tc,500);delta=lambda t:np.arcsin(np.clip(n*np.sin(t),-1,1))-t
fig,(ax,bx)=plt.subplots(1,2,figsize=(8,3.8),layout="constrained")
ax.plot(np.degrees(th),np.degrees(delta(th)),lw=2,color="#1565c0");ax.scatter([np.degrees(tc)],[90-np.degrees(tc)],color="#d84315");ax.set(xlabel="Internal incidence (degrees)",ylabel="Single-face deviation (degrees)",title="Finite endpoint at the critical angle")
A=np.pi/3;t=np.linspace(A-tc,tc,600);de=delta(t)+delta(A-t);mn=2*np.arcsin(n/2)-A
bx.plot(np.degrees(t),np.degrees(de),lw=2,color="#1565c0");bx.scatter([30],[np.degrees(mn)],color="#d84315");bx.axvline(30,color="#999",ls=":");bx.set(xlabel="First internal angle (degrees)",ylabel="Total prism deviation (degrees)",title="Two-face transmitted interval")
bx.annotate(f"Minimum: {np.degrees(mn):.2f}°",(30,np.degrees(mn)),xytext=(22,np.degrees(mn)+4),arrowprops={"arrowstyle":"->"},fontsize=9)
for a in (ax,bx):a.grid(alpha=.2)
fig.suptitle("Illustrative homogeneous prism, refractive index n = 1.5")

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
