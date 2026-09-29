"""Channel and dilation diagrams; Python 3.14, Matplotlib 3.10.

Writes only paper-48-channel.png in the caller's current directory.
The caller controls MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, axes = plt.subplots(2, 1, figsize=(8, 5.5), layout="constrained")
for ax in axes:
    ax.set(xlim=(-0.9, 6.2), ylim=(-0.5, 2.8))
    ax.axis("off")
def wire(ax, y, start, end, dashed=False):
    ax.annotate("", xy=(end,y), xytext=(start,y), arrowprops={"arrowstyle":"->", "lw":1.6, "color":"navy", "linestyle":"--" if dashed else "-"})
def gate(ax, y, height, label):
    ax.add_patch(Rectangle((2.1,y),1.15,height,facecolor="#e5eef8",edgecolor="navy",lw=1.4))
    ax.text(2.675,y+height/2,label,ha="center",va="center",fontsize=15)
ax=axes[0]
ax.set_title("Channel on the input system; reference unchanged")
wire(ax,2,0,5.3)
wire(ax,1,0,2.1)
wire(ax,1,3.25,5.3)
gate(ax,0.65,0.7,r"$\Phi$")
ax.text(-0.2,2,r"$R$",ha="right",va="center",fontsize=13)
ax.text(-0.2,1,r"$Q$",ha="right",va="center",fontsize=13)
ax.text(5.45,2,r"$R$",va="center",fontsize=13)
ax.text(5.45,1,r"$B$",va="center",fontsize=13)
ax.text(0,0.15,r"Input: $|\Psi^\rho\rangle_{RQ}$",fontsize=12)
ax.text(3.4,0.15,r"Output: $\omega_{RB}$",fontsize=12)
ax=axes[1]
ax.set_title("Unitary dilation with pure environment")
wire(ax,2.2,0,5.3)
wire(ax,1.2,0,2.1)
wire(ax,0.2,0,2.1)
gate(ax,-0.15,1.7,r"$U$")
wire(ax,1.2,3.25,5.3)
wire(ax,0.2,3.25,5.3,True)
for y,left,right in [(2.2,r"$R$",r"$R$"),(1.2,r"$Q$",r"$B$"),(0.2,r"$|0\rangle_E$",r"$E$")]:
    ax.text(-0.2,y,left,ha="right",va="center",fontsize=13)
    ax.text(5.45,y,right,va="center",fontsize=13)
ax.text(3.5,-0.38,"Discard E to obtain the channel",fontsize=10)
fig.savefig("paper-48-channel.png",dpi=125,facecolor="white",transparent=False)
