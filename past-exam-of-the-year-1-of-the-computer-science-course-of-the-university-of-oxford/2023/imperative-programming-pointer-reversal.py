"""Original node-identity diagram. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
fig, axes = plt.subplots(3, 1, figsize=(9, 5.4), layout="constrained")
locations = [1.1, 3.0, 4.9, 6.8]
def node(a, identity, x, color):
 a.add_patch(FancyBboxPatch((x-.48,.30),.96,.40,boxstyle="round,pad=.04",edgecolor=color,facecolor="#f4f7f9",linewidth=1.8))
 a.text(x,.5,f"node {identity}",ha="center",va="center")
def arrow(a,x,y):
 a.annotate("",(y-.53,.5),(x+.53,.5),arrowprops={"arrowstyle":"->","lw":1.7,"color":"#364b5d"})
def pointer(a,label,x):
 a.annotate(label,(x,.73),(x,.99),ha="center",va="center",arrowprops={"arrowstyle":"->","color":"#317249"},color="#317249")
def terminal(a,x,y):
 a.annotate("",(y-.23,.5),(x+.53,.5),arrowprops={"arrowstyle":"->","lw":1.7,"color":"#364b5d"})
for a in axes:
 a.set(xlim=(0,8.4),ylim=(0,1.2))
 a.axis("off")
a=axes[0]
a.set_title("4(c): initially, prev = null and cur points to the whole original list",loc="left",fontsize=11)
for i,x in enumerate(locations):node(a,i,x,"#276792")
for x,y in zip(locations,locations[1:]):arrow(a,x,y)
pointer(a,"cur / list",locations[0])
a.text(7.65,.5,"null",ha="center")
terminal(a,locations[-1],7.65)
a=axes[1]
a.set_title("After two iterations: a reversed prefix and an untouched suffix",loc="left",fontsize=11)
for identity,x in zip([1,0,2,3],locations):node(a,identity,x,"#b14e37" if identity<2 else "#276792")
arrow(a,locations[0],locations[1])
arrow(a,locations[2],locations[3])
a.text(3.95,.5,"null",ha="center")
terminal(a,locations[1],3.95)
a.text(7.65,.5,"null",ha="center")
terminal(a,locations[-1],7.65)
pointer(a,"prev",locations[0]);pointer(a,"cur",locations[2])
a.text(1.95,.08,"reverse([1, 0]) ++ [2, 3] = [0, 1, 2, 3]",ha="left",fontsize=10)
a=axes[2]
a.set_title("At exit: cur = null; assign list = prev; the four node objects are reused",loc="left",fontsize=11)
for identity,x in zip([3,2,1,0],locations):node(a,identity,x,"#b14e37")
for x,y in zip(locations,locations[1:]):arrow(a,x,y)
pointer(a,"prev / new list",locations[0])
a.text(7.65,.5,"null",ha="center")
terminal(a,locations[-1],7.65)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
