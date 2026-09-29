"""Original particle diagrams. Tested with Python 3.14 and Matplotlib 3.10.

Run in the corresponding _media directory; save the white PNG to cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

INK = "#213b58"
BOSON = "#a74526"


def fermion(ax, start, end, reverse=False):
    x0, y0 = start
    x1, y1 = end
    ax.plot([x0, x1], [y0, y1], color=INK, lw=1.7)
    low, high = (0.63, 0.40) if reverse else (0.40, 0.63)
    ax.add_patch(FancyArrowPatch((x0 + low*(x1-x0), y0 + low*(y1-y0)), (x0 + high*(x1-x0), y0 + high*(y1-y0)), arrowstyle="-|>", mutation_scale=12, color=INK, lw=1.4))


def boson(ax, start, end, gluon=False):
    start, end = np.asarray(start, dtype=float), np.asarray(end, dtype=float)
    delta = end-start
    direction = delta/np.linalg.norm(delta)
    normal = np.array([-direction[1], direction[0]])
    t = np.linspace(0, 1, 350)
    phase = 2*np.pi*8*t
    points = start[:, None]+delta[:, None]*t
    points += normal[:, None]*(0.075*np.sin(phase))
    if gluon:
        points += direction[:, None]*(0.042*np.sin(2*phase))
    ax.plot(points[0], points[1], color=BOSON, lw=1.5)


def dot(ax, pos):
    ax.plot(*pos, "o", ms=3.2, color=INK)


def annihilation(ax, incoming, outgoing, title):
    left, right = (1.45, 0), (3.3, 0)
    fermion(ax, (0, 1.1), left)
    fermion(ax, (0, -1.1), left, reverse=True)
    boson(ax, left, right)
    fermion(ax, right, (4.8, 1.1))
    fermion(ax, right, (4.8, -1.1), reverse=True)
    for point in (left, right): dot(ax, point)
    for text, x, y in [(incoming[0], -.12, 1.25), (incoming[1], -.12, -1.25), (outgoing[0], 4.85, 1.25), (outgoing[1], 4.85, -1.25)]:
        ax.text(x, y, text, ha="center", va="center", fontsize=14)
    ax.text(2.4, .3, r"$\gamma^*$", ha="center", fontsize=14, color=BOSON)
    ax.set_title(title, fontsize=13, pad=12)


fig, axes = plt.subplots(2, 3, figsize=(13.2, 8.4), facecolor="white")
for ax in axes.flat:
    ax.set_xlim(-.7, 5.9)
    ax.set_ylim(-1.8, 1.8)
    ax.axis("off")
    ax.set_facecolor("white")
    ax.set_aspect("equal")
annihilation(axes[0,0], (r"$e^-$", r"$e^+$"), (r"$\mu^-$", r"$\mu^+$"), "Muon-pair continuum")
annihilation(axes[0,1], (r"$e^-$", r"$e^+$"), (r"$q$", r"$\bar q$"), "Quark-pair continuum")
axes[0,1].text(4.0, -1.7, "quarks hadronize into jets", fontsize=10, ha="center")
annihilation(axes[0,2], (r"$b$", r"$\bar b$"), (r"$e^-$", r"$e^+$"), r"$\Upsilon(nS)$ electronic annihilation")
axes[0,2].text(.0, 0, r"$\Upsilon$", fontsize=14, ha="center")
ax=axes[1,0]
ax.set_title(r"$\Upsilon(nS)$: three-gluon annihilation", fontsize=13, pad=12)
fermion(ax, (0,1.15), (2.0,1.15))
fermion(ax, (2.0,1.15), (2.0,0))
fermion(ax, (2.0,0), (2.0,-1.15))
fermion(ax, (2.0,-1.15), (0,-1.15))
ax.text(-.1, 1.4, r"$b$", fontsize=14, ha="center")
ax.text(-.1, -1.4, r"$\bar b$", fontsize=14, ha="center")
for y, end_y in [(1.15,1.4),(0,0),(-1.15,-1.4)]:
    boson(ax,(2.0,y),(4.7,end_y),gluon=True)
    dot(ax,(2.0,y))
    ax.text(4.95,end_y,r"$g$",fontsize=14,ha="center",va="center")
ax.text(2.6,-1.75,"one representative ordering",fontsize=10,ha="center")
ax=axes[1,1]
ax.set_title(r"Open-bottom channel: $\Upsilon(4S)\to B\bar B$",fontsize=13,pad=12)
fermion(ax,(0,1.15),(4.5,1.15),reverse=True)
fermion(ax,(0,-1.15),(4.5,-1.15))
boson(ax,(1.35,1.15),(2.3,0),gluon=True)
fermion(ax,(2.3,0),(4.5,.55))
fermion(ax,(2.3,0),(4.5,-.55),reverse=True)
for point in [(1.35,1.15),(2.3,0)]:dot(ax,point)
for label,x,y in [(r"$\bar b$",-.1,1.4),(r"$b$",-.1,-1.4),(r"$\bar b$",4.5,1.4),(r"$q$",4.5,.34),(r"$\bar q$",4.5,-.34),(r"$b$",4.5,-1.4)]:
    ax.text(x,y,label,fontsize=13,ha="center")
for y0,y1,label in [(.5,1.2,r"$B=(\bar bq)$"),(-1.2,-.5,r"$\bar B=(b\bar q)$")]:
    ax.plot([4.8,4.95,4.95,4.8],[y0,y0,y1,y1],color="#687484",lw=1)
    ax.text(5.12,(y0+y1)/2,label,fontsize=10,ha="left",va="center")
ax.text(2.6,-1.75,"light-pair creation: quark-line topology",fontsize=10,ha="center")
ax=axes[1,2]
ax.set_title("The threshold changes the total width",fontsize=13,pad=12)
ax.text(.02,.87,"Below the B-pair threshold",fontsize=12,weight="bold",va="top",transform=ax.transAxes)
ax.text(.02,.72,"Annihilation and transitions\nto lower quarkonium dominate.",fontsize=11,linespacing=1.5,va="top",transform=ax.transAxes)
ax.text(.02,.42,"Above the B-pair threshold",fontsize=12,weight="bold",va="top",transform=ax.transAxes)
ax.text(.02,.27,"An open strong-decay channel\ncan dominate the total width.",fontsize=11,linespacing=1.5,va="top",transform=ax.transAxes)
fig.suptitle("Annihilation diagrams and quarkonium decay mechanisms",fontsize=18,y=.985)
fig.text(.5,.025,"Fermion arrows show particle-number flow. The open-bottom panel is a hadronization topology, not a free-quark decay calculation.",ha="center",fontsize=10)
fig.subplots_adjust(left=.035,right=.96,top=.91,bottom=.08,hspace=.44,wspace=.38)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
plt.close(fig)
