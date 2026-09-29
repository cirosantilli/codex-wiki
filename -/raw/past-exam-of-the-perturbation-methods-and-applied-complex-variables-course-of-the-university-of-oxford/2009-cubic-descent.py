"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. PNG output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7.4, 4.7), facecolor="white")
s = np.linspace(0, 13, 900)
a = (1j*s)**(1/3)
b = (1+1j*s)**(1/3)
ax.plot([0,1],[0,0], "--", color="0.5", label="Original interval")
ax.plot(a.real,a.imag,lw=2.5,label="Descent from zero")
ax.plot(b.real,b.imag,lw=2.5,label="Endpoint descent, reversed")
for z, k, direction in [(a,140,1),(b,180,-1)]:
 ax.annotate("", xy=(z[k+direction*35].real,z[k+direction*35].imag),xytext=(z[k].real,z[k].imag),arrowprops=dict(arrowstyle="->",lw=2,color="0.2"))
connector = (np.linspace(0,1,70)+13j)**(1/3)
ax.plot(connector.real,connector.imag,color="0.3",lw=1)
ax.annotate("Connector tends to infinity",xy=(connector[35].real,connector[35].imag),xytext=(1.15,1.65),arrowprops=dict(arrowstyle="->",color=".4"),fontsize=10)
ax.scatter([0,1],[0,0],color="black",s=20,zorder=5)
ax.text(.03,-.11,"0");ax.text(1.02,-.11,"1")
ax.text(.55,.44,r"$\arg t=\pi/6$",rotation=30)
ax.text(1.36,.49,r"$t^3=1+is$",rotation=31)
ax.set(xlabel=r"$\mathrm{Re}\,t$",ylabel=r"$\mathrm{Im}\,t$",xlim=(-.12,2.25),ylim=(-.15,1.85),title="Cubic phase: outgoing ray and returning endpoint branch")
ax.set_aspect("equal");ax.spines[["top","right"]].set_visible(False)
ax.legend(loc="upper left",frameon=False,fontsize=9)
fig.tight_layout();fig.savefig("2009-cubic-descent.png",dpi=150,facecolor="white")
