from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,ax=plt.subplots(figsize=(8,4.4));ax.set(xlim=(-1,5),ylim=(-.2,3.1));ax.axis("off")
ax.add_patch(Rectangle((-1,-.2),6,1.65,facecolor="#e6f2f8",edgecolor="none"));ax.axhline(1.45,color="#234e70",lw=1.8)
ax.text(-.7,.1,"Glass: n = 1.55",fontsize=13);ax.text(-.7,2.7,"Air: n = 1",fontsize=13)
p=np.array([.2,.2]);hit=p+np.array([1.25*np.tan(np.radians(49.82)),1.25]);end=hit+np.array([1.2*np.tan(np.radians(49.82)),-1.2])
for a,b in [(p,hit),(hit,end)]:ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=2.4,color="#b7483d"))
ax.plot([hit[0],hit[0]],[.4,2.7],color="#888888",ls="--",lw=1)
ax.annotate("",xy=(p[0],1.25),xytext=p,arrowprops=dict(arrowstyle="->",lw=2,color="#234e70"));ax.text(-.05,.7,"Beam",rotation=90,ha="center",fontsize=11)
ax.text(.55,.9,r"$\theta_C\simeq49.8^\circ$",fontsize=13);ax.text(2.35,2.3,r"$\theta_{\rm crit}=\arcsin(1/n)\simeq40.2^\circ$",ha="center",fontsize=13)
ax.text(3.1,1.75,"No direct transmitted ray",color="#a43530",ha="center",fontsize=12);ax.text(3.4,.45,"Total internal\nreflection",color="#a43530",ha="center",fontsize=12)
ax.set_title("A flat glass–air exit traps the ideal electron Cherenkov cone")
fig.tight_layout()

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
