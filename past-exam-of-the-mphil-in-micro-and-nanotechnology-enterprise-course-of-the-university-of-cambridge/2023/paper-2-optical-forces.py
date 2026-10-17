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

fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained");ax.add_patch(Circle((0,0),1,fc="#e7eff4",ec="#246c99",lw=1.5))
ax.axhline(1.18,color=".4",ls="--");ax.text(1.5,1.25,"Optical axis / high intensity")
def refract(d,n,eta):
    c=-np.dot(n,d);return eta*d+(eta*c-np.sqrt(1-eta*eta*(1-c*c)))*n
for b,power,col in [(.58,2.2,"#b23a37"),(-.58,1.,"#d19829")]:
    entry=np.array([-np.sqrt(1-b*b),b]);di=np.array([1.,0.])
    inside=refract(di,entry,1.33/1.6)
    exit=entry-2*np.dot(entry,inside)*inside
    dout=refract(inside,-exit,1.6/1.33)
    end=exit+1.9*dout
    ax.plot([-2.7,entry[0],exit[0],end[0]],[b,entry[1],exit[1],end[1]],color=col,lw=power)
    ax.annotate("",entry+(exit-entry)*.63,entry+(exit-entry)*.42,arrowprops=dict(arrowstyle="->",color=col))
    dp=di-dout
    dp=dp/np.linalg.norm(dp)*(.42*power)
    start=np.array([.1,-.08 if b>0 else -.2]);ax.annotate("",start+dp,start,arrowprops=dict(arrowstyle="-|>",color=col,lw=2))
ax.text(-2.7,.79,"Stronger ray",color="#b23a37");ax.text(-2.7,-.89,"Weaker ray",color="#d19829")
ax.text(.2,.5,"Larger upward\nreaction",color="#b23a37",fontsize=9)
ax.text(.2,-.6,"Smaller downward\nreaction",color="#aa7110",fontsize=9)
ax.text(-.8,-1.48,"Ray deflection changes light momentum;\nnet particle force points toward the brighter axis.")
ax.set(aspect="equal",xlim=(-2.9,3.2),ylim=(-1.6,1.65));ax.axis("off")
ax.set_title("Local ray tracing near the waist: particle index 1.60, surrounding index 1.33")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
