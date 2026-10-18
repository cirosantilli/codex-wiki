"""Original solution figure. Python 3.14; NumPy 2.3; Matplotlib 3.10. Writes to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig=plt.figure(figsize=(8.8,6.5),layout="constrained")
ax=fig.add_subplot(211); ax.set_aspect("equal"); ax.axis("off")
vals=[(-i)%16 for i in range(16)]
theta=np.pi/2-np.arange(16)*2*np.pi/16
xy=np.column_stack((3.3*np.cos(theta),1.75*np.sin(theta)))
for i,(x,y) in enumerate(xy):
 ax.text(x,y,format(vals[i],"04b"),ha="center",va="center",fontsize=11,bbox=dict(boxstyle="round,pad=.22",fc="white",ec="#27638b"))
 x2,y2=xy[(i+1)%16]
 ax.annotate("",xy=(x2,y2),xytext=(x,y),arrowprops=dict(arrowstyle="->",color="#27638b",shrinkA=20,shrinkB=20))
ax.set(xlim=(-4,4),ylim=(-2.2,2.2),title="Four-stage positive-edge Q cascade: settled states")
ax.text(0,0,"One input rising edge\nper arrow",ha="center",va="center",fontsize=11)
ax=fig.add_subplot(212)
t=np.arange(0,33)*1.0
states=(-np.arange(0,33))%16
q3=(states//8)%2
ax.step(t,q3,where="post",color="#27638b",lw=2)
ax.set(xlim=(0,32),ylim=(-.15,1.35),yticks=[0,1],xticks=np.arange(0,33,4),xlabel="Time (ns); first rising input edge at 1 ns",ylabel="$Q_3$",title="Ideal output: period 16 ns, frequency 62.5 MHz")
ax.grid(axis="x",alpha=.25)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=110)
