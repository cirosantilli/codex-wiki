"""Original idealized n-channel MOSFET cross-section in its inversion state."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig,ax=plt.subplots(figsize=(8.0,4.3),layout="constrained")
ax.add_patch(Rectangle((.5,.35),7.5,2.15,facecolor="#e7dcc8",edgecolor="#666666",lw=1.2))
for x,label in [(1.0,"n+ source"),(5.4,"n+ drain")]:
    ax.add_patch(Rectangle((x,1.65),1.7,.85,facecolor="#6faed0",edgecolor="#377e9f",lw=1.1))
    ax.text(x+.85,2.05,label,ha="center",va="center",fontsize=11)
ax.add_patch(Rectangle((2.7,2.5),2.7,.17,facecolor="#f5c56c",edgecolor="#9b722e",lw=1))
ax.add_patch(Rectangle((2.7,2.67),2.7,.55,facecolor="#b8b8bb",edgecolor="#555555",lw=1))
ax.add_patch(Rectangle((2.7,2.39),2.7,.11,facecolor="#2779a1",edgecolor="none"))
ax.text(4.05,2.94,"Gate",ha="center",va="center",fontsize=12)
for x,label in [(1.85,"Source"),(6.25,"Drain")]:
    ax.plot([x,x],[2.5,3.35],color="#555555",lw=1.5)
    ax.text(x,3.46,label,ha="center",fontsize=11)
ax.plot([4.05,4.05],[3.22,3.65],color="#555555",lw=1.5)
ax.text(4.05,3.8,"Positive gate bias",ha="center",fontsize=12)
ax.annotate("Insulating oxide",xy=(3.05,2.59),xytext=(.6,3.95),arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
ax.annotate("Electron inversion channel",xy=(4.25,2.43),xytext=(4.1,1.6),arrowprops=dict(arrowstyle="->",color="#555555"),ha="center",fontsize=11)
ax.text(4.25,.85,"p-type body",ha="center",fontsize=13)
ax.set(xlim=(0,8.5),ylim=(0,4.45),title="Gate-induced mobile electrons connect source and drain")
ax.axis("off")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
