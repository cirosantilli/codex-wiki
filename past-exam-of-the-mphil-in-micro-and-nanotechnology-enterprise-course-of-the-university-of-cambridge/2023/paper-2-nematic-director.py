"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig,ax=plt.subplots(figsize=(5.8,5.1),layout="constrained")
for x in np.linspace(-3,3,27):
    for y in np.linspace(-3,3,27):
        r=np.hypot(x,y)
        if r<1.08 or min(np.hypot(x-1.35,y),np.hypot(x+1.35,y))<.23:continue
        z=complex(x,y);theta=np.angle(z)
        psi=theta-.5*np.angle(z-1.35)-.5*np.angle(z+1.35)+np.pi/2
        w=np.exp(-((r-1)/.5)**2)
        director=(1-w)*np.exp(2j*psi)+w*np.exp(2j*theta)
        psi=.5*np.angle(director);v=.075*np.array([np.cos(psi),np.sin(psi)])
        ax.plot([x-v[0],x+v[0]],[y-v[1],y+v[1]],color="#246c99",lw=1)
ax.add_patch(Circle((0,0),1,fc="#e5e5e5",ec="black",lw=1.2))
for t in np.linspace(0,2*np.pi,24,endpoint=False):
    a=np.array([np.cos(t),np.sin(t)])
    ax.plot([a[0],1.18*a[0]],[a[1],1.18*a[1]],color="#246c99")
ax.plot([-1.35,1.35],[0,0],"o",color="#b23a37",ms=6)
ax.annotate("Equatorial defect ring\n(two intersections in this section)",(1.35,0),(.2,-2.3),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.annotate(r"$\mathbf{n}_\infty$",(-2.5,2.8),(-2.5,1.9),arrowprops=dict(arrowstyle="<->"))
ax.text(-.65,-.15,"Homeotropic\nsphere",fontsize=10)
ax.set(aspect="equal",xlim=(-3.2,3.2),ylim=(-3.1,3.2));ax.axis("off")
ax.set_title("Plausible Saturn-ring texture (schematic director field)")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
