"""Original tree-level pseudoscalar-exchange diagrams.
Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque PNG basename to the caller's CWD; preserves MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

FERMION = "#123e67"
SCALAR = "#b55119"
fig, axs = plt.subplots(2, 2, figsize=(10, 6.4), facecolor="white",
                        layout="constrained")

def line(ax, a, b, reverse=False):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=FERMION, linewidth=1.9)
    sign = -1 if reverse else 1
    center = ((a[0]+b[0])/2, (a[1]+b[1])/2)
    delta = ((b[0]-a[0])*0.14*sign, (b[1]-a[1])*0.14*sign)
    ax.add_patch(FancyArrowPatch((center[0]-delta[0], center[1]-delta[1]),
                                (center[0]+delta[0], center[1]+delta[1]),
                                arrowstyle="-|>", mutation_scale=12,
                                linewidth=1.6, color=FERMION))

def scalar(ax, a, b, label, horizontal=False):
    ax.plot([a[0],b[0]], [a[1],b[1]], color=SCALAR,
            linestyle=(0,(4,3)), linewidth=2)
    pos = ((a[0]+b[0])/2 + (0 if horizontal else 0.035),
           (a[1]+b[1])/2 + (0.065 if horizontal else 0))
    ax.text(*pos, label, color=SCALAR, fontsize=10,
            ha="center" if horizontal else "left", va="bottom" if horizontal else "center")
    ax.plot([a[0],b[0]], [a[1],b[1]], "o", color="#182d3a", markersize=4)

for ax in axs.flat:
    ax.set_facecolor("white"); ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")

lu, ll, ru, rl = (0.1,0.74),(0.1,0.26),(0.9,0.74),(0.9,0.26)
upper, lower = (0.46,0.74),(0.46,0.26)

def external_labels(ax, anti=False):
    ax.text(0.05,0.85,r"$\psi:\ (p_1,r_1)$",fontsize=11,ha="left")
    ax.text(0.95,0.85,r"$\psi:\ (p_3,r_3)$",fontsize=11,ha="right")
    species=r"\bar\psi" if anti else r"\psi"
    ax.text(0.05,0.12,rf"${species}:\ (p_2,r_2)$",fontsize=11,ha="left")
    ax.text(0.95,0.12,rf"${species}:\ (p_4,r_4)$",fontsize=11,ha="right")

ax=axs[0,0]
for a,b in [(lu,upper),(upper,ru),(ll,lower),(lower,rl)]:line(ax,a,b)
scalar(ax,upper,lower,r"$q_t=p_1-p_3$")
external_labels(ax)
ax.set_title(r"Two fermions: $t$ exchange",fontsize=12)

ax=axs[0,1]
for a,b in [(lu,upper),(upper,rl),(ll,lower),(lower,ru)]:line(ax,a,b)
scalar(ax,upper,lower,r"$q_u=p_1-p_4$")
external_labels(ax)
# Upper/right endpoint is p3; lower/right is p4 even when lines cross.
ax.set_title(r"Two fermions: $u$ exchange",fontsize=12)

ax=axs[1,0]
line(ax,lu,upper);line(ax,upper,ru)
line(ax,ll,lower,reverse=True);line(ax,lower,rl,reverse=True)
scalar(ax,upper,lower,r"$q_t=p_1-p_3$")
external_labels(ax,anti=True)
ax.set_title(r"Fermion-antifermion: $t$ exchange",fontsize=12)

ax=axs[1,1]
vl,vr=(0.36,0.5),(0.66,0.5)
line(ax,lu,vl);line(ax,ll,vl,reverse=True)
line(ax,vr,ru);line(ax,vr,rl,reverse=True)
scalar(ax,vl,vr,r"$q_s=p_1+p_2$",horizontal=True)
external_labels(ax,anti=True)
ax.set_title(r"Fermion-antifermion: $s$ annihilation",fontsize=12)
fig.suptitle("Pseudoscalar exchange at order $\\lambda^2$",fontsize=14,fontweight="bold")
fig.supxlabel("Time runs left to right; solid arrows show fermion flow; dashed lines are scalars",fontsize=10)
fig.savefig(Path("paper-48-yukawa-trees.png"),dpi=120,facecolor="white",transparent=False)
plt.close(fig)
