#!/usr/bin/env python3
"""Generate paper-312-one-loop-matter-bispectrum.png."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def vertex(ax, x, y, label=None):
    ax.add_patch(Circle((x, y), 0.075, facecolor="black", edgecolor="none", zorder=4))
    if label:
        ax.text(x, y - 0.18, label, ha="center", va="top", fontsize=9)


def edge(ax, p, q, **kwargs):
    ax.plot((p[0], q[0]), (p[1], q[1]), color=kwargs.pop("color", "#355f8a"), linewidth=kwargs.pop("lw", 2), **kwargs)


def external(ax, p, angle):
    import numpy as np
    q = (p[0] + 0.48 * np.cos(angle), p[1] + 0.48 * np.sin(angle))
    edge(ax, p, q, color="black", lw=1.6)


fig, axes = plt.subplots(1, 5, figsize=(12.0, 4.4), layout="constrained")

# B211: one quadratic vertex connected to two linear external legs.
ax = axes[0]; p=(0,0.15); vertex(ax,*p,"$G_2$"); external(ax,p,2.5); external(ax,p,0.64); external(ax,p,-1.57)

# B222: triangle of three quadratic vertices.
ax = axes[1]; pts=((-0.35,-0.05),(0.35,-0.05),(0,0.55))
for p in pts: vertex(ax,*p,"$G_2$")
for p,q in zip(pts,(pts[1],pts[2],pts[0])): edge(ax,p,q)
for p,a in zip(pts,(-2.4,-0.75,1.57)): external(ax,p,a)

# B321 I: a bubble attached between cubic and quadratic vertices.
ax = axes[2]; a=(-0.28,0.12); b=(0.3,0.12); vertex(ax,*a,"$G_3$"); vertex(ax,*b,"$G_2$")
edge(ax,a,b); edge(ax,a,b, color="#d95f02", lw=2, linestyle="--")
external(ax,a,2.6); external(ax,a,-2.2); external(ax,b,0); external(ax,b,-1.25)

# B321 II: tadpole on a cubic vertex joined to a quadratic vertex.
ax = axes[3]; a=(-0.25,0.05); b=(0.28,0.05); vertex(ax,*a,"$G_3$"); vertex(ax,*b,"$G_2$"); edge(ax,a,b)
loop=Circle((a[0],a[1]+0.32),0.24,fill=False,color="#d95f02",linewidth=2); ax.add_patch(loop)
external(ax,a,-2.35); external(ax,b,0.55); external(ax,b,-0.65)

# B411: tadpole correction at a four-leg vertex.
ax = axes[4]; p=(0,0.02); vertex(ax,*p,"$G_4$"); ax.add_patch(Circle((0,0.38),0.24,fill=False,color="#d95f02",linewidth=2))
external(ax,p,2.7); external(ax,p,0.45); external(ax,p,-1.55)

for ax, title in zip(axes, ("$B_{211}$", "$B_{222}$", "$B_{321}^{I}$", "$B_{321}^{II}$", "$B_{411}$")):
    ax.set(title=title, xlim=(-0.75,0.75), ylim=(-0.65,0.95), aspect="equal")
    ax.axis("off")
fig.suptitle("Tree and one-loop matter-bispectrum topologies")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
