"""Untwisted Whitehead satellite diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The tangle box denotes the two parallel copies of a long trefoil in its
zero Seifert framing. The two caps create the positive Whitehead clasp.
Output is the same-basename opaque PNG in the caller's current directory.
The caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(9.6,5.6),dpi=100,facecolor="white")
ax.set_facecolor("white")
def line(points,**kw):
 a=np.array(points);ax.plot(a[:,0],a[:,1],color="#17334c",lw=2.8,solid_capstyle="round",**kw)
# Four-port zero-framed two-strand satellite tangle.
ax.add_patch(Rectangle((-.85,1),1.7,2,facecolor="#edf3f7",edgecolor="#8296a5",lw=1.5))
for x in [-.5,.5]:line([(x,1),(x,3)])
ax.text(0,2.05,"Two parallel copies\nof a long trefoil\n\nzero Seifert framing",ha="center",va="center",fontsize=10,
 bbox=dict(facecolor="white",edgecolor="none",pad=4))
# Caps, with two alternating crossings in the clasp.
line([(-.5,3),(-.5,3.5),(2,3.5),(2,1.2),(1.3,1.2),(1.3,3),(.5,3)])
line([(-.5,1),(-.5,.5),(2.6,.5),(2.6,2.5),(1.65,2.5),(1.65,1),(.5,1)])
# Erase the underpassing strand, then redraw the overpassing strand.
ax.plot([1.88,2.12],[2.5,2.5],color="white",lw=8)
line([(2,2.65),(2,2.35)])
ax.plot([1.53,1.77],[1.2,1.2],color="white",lw=8)
line([(1.65,1.35),(1.65,1.05)])
ax.annotate("Whitehead clasp",xy=(1.83,1.85),xytext=(3.15,1.65),fontsize=10,
 arrowprops=dict(arrowstyle="->",color="#566575"))
ax.text(0,-.05,"Satellite knot: untwisted Whitehead double of the trefoil",fontsize=12,ha="left",weight="bold")
# Independently generated trefoil companion projection with overpass gaps.
axt=fig.add_axes([.66,.49,.28,.40],facecolor="white")
u=np.linspace(0,2*np.pi,1600)
x=(2+np.cos(3*u))*np.cos(2*u)
y=(2+np.cos(3*u))*np.sin(2*u)
z=np.sin(3*u)
axt.plot(x,y,color="#17334c",lw=2.4)
# Crossings occur at cos(3u)=0; upper strand has z=+1.
for v in [np.pi/6,5*np.pi/6,3*np.pi/2]:
 under=(v+np.pi)%(2*np.pi)
 mask=np.abs(np.angle(np.exp(1j*(u-under))))<.08
 axt.plot(x[mask],y[mask],color="white",lw=7)
 mask=np.abs(np.angle(np.exp(1j*(u-v))))<.12
 axt.plot(x[mask],y[mask],color="#17334c",lw=2.4)
axt.set_aspect("equal");axt.axis("off")
axt.set_title("Trefoil companion",fontsize=11)
ax.text(3.3,.65,r"$V=\left(\begin{array}{cc}0&1\\0&0\end{array}\right)$" if False else "Genus-one band basis:\nV = ((0, 1), (0, -1))\ndet(tV − Vᵀ) = t",fontsize=11,ha="left",va="center")
ax.set_xlim(-1.15,5.7);ax.set_ylim(-.3,4)
ax.set_aspect("equal");ax.axis("off")
fig.subplots_adjust(left=.045,right=.98,bottom=.08,top=.93)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
plt.close(fig)
