"""Original connectivity graphs, not molecular coordinates or exam artwork.

Python 3.14, matplotlib, numpy. Output paper-2-phosphazenes.png is in cwd.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(13.5, 5), facecolor="white")
def setup(ax, title):
    ax.set(xlim=(-1.8, 1.8), ylim=(-2.2, 2.2), aspect="equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12)
def node(ax, pos, label, color="black", size=12):
    ax.text(*pos, label, ha="center", va="center", fontsize=size, color=color,
            bbox=dict(fc="white", ec="none", pad=1))
def bond(ax, a, b, style="-", color="0.3"):
    ax.plot([a[0], b[0]], [a[1], b[1]], style, color=color, lw=1.6)

ax = axes[0]
setup(ax, "C: one of three identical spiro units")
q = {"P(V)": (-.9, 0), "N(Cy)": (0, .7), "P(III)": (.9, 0), "N(Cy) ": (0, -.7)}
ks = list(q)
for i in range(4): bond(ax, q[ks[i]], q[ks[(i+1)%4]])
for label, pos in q.items(): node(ax, pos, label.strip(), "#2b6f82")
for b in [(-1.6, .7), (-1.6, -.7)]:
    bond(ax, q["P(V)"], b); node(ax, b, "ring N", size=10)
bond(ax, (.9, 0), (1.45, .9)); node(ax, (1.45, .9), "Cl")
node(ax, (1.0, -.5), ":", size=17)
ax.text(0, -1.35, "Three P–Cl directions: +++ or ++−\nCy = cyclohexyl; P(III) retains a lone pair",
        ha="center", va="center", fontsize=10)

def cluster(ax, tri=False):
    p, f1, f2 = (0., .5), (-.9, -.6), (.9, -.6)
    ring = [p,(-.7,1.05),(-.7,1.65),(0,1.8),(.7,1.65),(.7,1.05)]
    for a,b in zip(ring,ring[1:]+ring[:1]): bond(ax,a,b)
    for i,a in enumerate(ring):
        node(ax,a, [r"$P_1$","N",r"$P_2Cl_2$","N",r"$P_3Cl_2$","N"][i],size=11)
    for a,b in [(p,f1),(p,f2),(f1,f2)]: bond(ax,a,b)
    node(ax,f1,r"$Fe_1$"); node(ax,f2,r"$Fe_2$")
    if tri:
        f3=(-1.2,.25)
        for f in [f1,f2]:bond(ax,f,f3)
        bond(ax,ring[1],f3,"--","#2b6f82")
        node(ax,f3,r"$Fe_3$")
        co=(0,-1.35)
        for f in [f1,f2]:bond(ax,f,co)
        node(ax,co,r"$\mu$-CO", "#9a4d26")
        ax.text(0,-1.95,"3 terminal CO on every Fe\nDashed: ring N → Fe₃ donation",ha="center",fontsize=10)
    else:
        ax.text(0,-1.7,"4 terminal CO on each Fe\nAll eight CO are terminal",ha="center",fontsize=10)
setup(axes[1], "D: spiro PFe₂ triangle")
cluster(axes[1])
setup(axes[2], "E: Fe₃ triangle + ring N donation")
cluster(axes[2],True)
fig.tight_layout()
fig.savefig("paper-2-phosphazenes.png", dpi=180, facecolor="white")
