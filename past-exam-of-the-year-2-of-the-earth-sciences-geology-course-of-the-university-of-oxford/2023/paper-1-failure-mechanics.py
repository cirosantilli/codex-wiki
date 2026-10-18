"""Original failure diagrams. Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, ax = plt.subplots(2, 2, figsize=(10.5, 6.5), layout="constrained")
u = np.linspace(0, 2*np.pi, 721)
a = ax[0, 0]
phi = np.deg2rad(34)
mu = np.tan(phi)
c, r = 1., np.sin(phi)
a.plot(c+r*np.cos(u), r*np.sin(u), color="#276792")
s = np.linspace(0, 1.7, 200)
a.plot(s, mu*s, "k--", label=r"$\tau=\mu\sigma'_n$")
a.plot(s, -mu*s, "k--")
st, tt = c*np.cos(phi)**2, c*np.sin(phi)*np.cos(phi)
a.scatter([st, st], [tt, -tt], color="#b73535", zorder=4)
a.annotate(r"$\phi=34^\circ$, $\mu=0.675$", (st, tt), (.07, .87), textcoords="axes fraction", arrowprops={"arrowstyle": "->"})
a.set(xlim=(0, 1.7), ylim=(-1, 1), xlabel=r"Effective normal stress $\sigma'_n$ (arbitrary units)", ylabel=r"Shear stress $\tau$", title="1(b): conjugate strike-slip failure")
a.axhline(0, color=".7", lw=.7)
a.set_aspect("equal", adjustable="box")
a = ax[0, 1]
a.plot([.08, .92], [.12, .60], color="#b73535", lw=3)
a.text(.08, .88, "W", ha="center")
a.text(.92, .88, "E", ha="center")
a.annotate("", (.41, .39), (.25, .30), arrowprops={"arrowstyle": "->", "lw": 2})
a.text(.12, .48, "hanging wall up", rotation=29)
a.annotate("", (.71, .40), (.86, .49), arrowprops={"arrowstyle": "->", "lw": 2})
for start, end in [((.03,.72),(.30,.72)),((.97,.72),(.70,.72))]:
 a.annotate("",end,start,arrowprops={"arrowstyle":"->","color":"#276792","lw":2})
a.text(.5,.72,r"$\sigma_1$: E–W compression",ha="center",va="bottom")
a.annotate("",(.52,.52),(.52,.88),arrowprops={"arrowstyle":"->","color":"#389557"})
a.text(.57,.55,r"$\sigma_3$: vertical")
a.text(.1,.04,r"$\sigma_2$: N–S, perpendicular to section")
a.set(xlim=(0,1),ylim=(0,1),title="2(a): one reverse-fault stress geometry")
a.axis("off")
a = ax[1, 0]
a.plot(60+30*np.cos(u),30*np.sin(u),color="#276792")
s=np.linspace(0,100,200)
a.plot(s,s/np.sqrt(3),"k--")
a.plot(s,-s/np.sqrt(3),"k--")
a.scatter([45,45],[15*np.sqrt(3),-15*np.sqrt(3)],color="#b73535",zorder=4)
a.text(8,37,r"$C=60$, $R=30$ MPa" )
a.set(xlim=(0,105),ylim=(-60,60),xlabel=r"$\sigma'_n$ (MPa)",ylabel=r"$\tau$ (MPa)",title="2(c): shear failure, cohesionless example")
a.axhline(0,color=".7",lw=.7)
a.set_aspect("equal",adjustable="box")
a = ax[1, 1]
a.plot(3.5+6.5*np.cos(u),6.5*np.sin(u),color="#276792")
a.axvline(-3,color="k",ls="--",label=r"$\sigma'_n=-T_0=-3$ MPa")
a.scatter([-3],[0],color="#b73535",zorder=4)
a.text(-2.1,6.9,"opening at left endpoint")
a.set(xlim=(-5,12),ylim=(-9,9),xlabel=r"$\sigma'_n$ (MPa)",ylabel=r"$\tau$ (MPa)",title="2(c): tensile opening of a vertical joint")
a.axhline(0,color=".7",lw=.7)
a.legend(loc="lower center",fontsize=9)
a.set_aspect("equal",adjustable="box")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
