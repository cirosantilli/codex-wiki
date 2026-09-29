from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig, (ax, spin) = plt.subplots(1,2,figsize=(10,5.1),gridspec_kw={"width_ratios":[1.6,1]})
ax.set(xlim=(0,10),ylim=(0,7));ax.axis("off")
for x,y,w,h,label,col in [(0.3,2.6,1.45,1.2,"Eu source","#dfc6e8"),(2.45,2.1,2,2.2,"Magnetized\niron\n(reverse field)","#c8d6df"),(5.4,2.5,1.4,1.4,"Sm\nscatterer","#e1d3a8"),(7.15,5.05,2.3,1.3,"NaI(Tl)\n+ photomultiplier","#c6dfce")]:
 ax.add_patch(Rectangle((x,y),w,h,facecolor=col,edgecolor="#263238",lw=1.5));ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=11)
for a,b in [((1.8,3.2),(2.4,3.2)),((4.5,3.2),(5.35,3.2)),((6.4,3.8),(7.65,5.0))]:ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=2,color="#b8413d"))
ax.add_patch(Rectangle((7.1,2.5),.35,1.4,facecolor="#666666"));ax.text(8.1,2.15,"Lead shield",ha="center",fontsize=10)
ax.text(5.1,4.6,"Resonantly scattered\nphoton accepted",ha="center",fontsize=10,color="#a23030")
ax.text(4.7,.65,"Functional layout; not historical scale or dimensions",ha="center",fontsize=10)
ax.set_title("Polarization analysis + nuclear resonance selection")
spin.set(xlim=(-1,1),ylim=(0,6.5));spin.axis("off");spin.set_title("Selected negative-helicity case")
for y,lab,pm in [(5.2,r"$\nu_e$",1),(3.2,r"$\mathrm{Sm}^{*}$",-1),(1.1,r"$\gamma$",-1)]:
 spin.text(-.9,y,lab,ha="center",va="center",fontsize=15)
 spin.annotate("",xy=(-.25,y+.48*pm),xytext=(-.25,y-.48*pm),arrowprops=dict(arrowstyle="-|>",color="#234e70",lw=2.3))
 spin.annotate("",xy=(.45,y-.45*pm),xytext=(.45,y+.45*pm),arrowprops=dict(arrowstyle="-|>",color="#a43a36",lw=2.3))
spin.text(-.25,6.05,"Momentum",ha="center",fontsize=10,color="#234e70");spin.text(.45,6.05,"Spin",ha="center",fontsize=10,color="#a43a36")
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.9,wspace=.12)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
