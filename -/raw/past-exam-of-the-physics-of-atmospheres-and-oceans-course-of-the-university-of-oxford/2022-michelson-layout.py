"""Original solution illustration. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; this script writes only its PNG basename there.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})

from matplotlib.patches import Rectangle
fig=plt.figure(figsize=(8,5.5),layout="constrained")
gs=fig.add_gridspec(2,1,height_ratios=[4,1])
ax=fig.add_subplot(gs[0]);ax.set(xlim=(-.7,7.5),ylim=(-1,4.6));ax.axis("off")
# Orthogonal round-trip arms with a diagonal beam splitter.
ax.plot([-.1,3,6.2],[1.8,1.8,1.8],color="#bb4a28",lw=2)
ax.plot([3,3],[0,4],color="#326e9e",lw=2)
ax.plot([2.64,3.36],[1.44,2.16],color="#222222",lw=5,solid_capstyle="butt")
ax.plot([2.55,3.45],[4,4],color="#222222",lw=5)
ax.plot([6.2,6.2],[1.35,2.25],color="#222222",lw=5)
ax.add_patch(Rectangle((2.58,-.5),.84,.5,fc="#d8e6ed",ec="#222222"))
ax.text(-.4,2.15,"Collimated\ninput light",ha="left")
ax.text(3.5,4.02,"Fixed mirror",va="center")
ax.text(6.2,2.55,"Moving mirror",ha="center")
ax.text(3.5,1.05,"Beam splitter")
ax.text(3,-.83,"Detector",ha="center")
ax.annotate("",(5.7,3.2),xytext=(6.7,3.2),arrowprops={"arrowstyle":"<->","lw":1.5})
ax.text(6.2,3.45,r"Displacement $x$",ha="center")
ax.text(4.75,.15,r"Optical path change $=2x$",ha="center")
for p,q,color in [((.4,1.8),(1.4,1.8),"#bb4a28"),((4.2,1.8),(5.2,1.8),"#bb4a28"),
                   ((3,2.4),(3,3.2),"#326e9e"),((3,.9),(3,.2),"#326e9e")]:
 ax.annotate("",q,xytext=p,arrowprops={"arrowstyle":"->","color":color,"lw":2})
ax.set_title("Michelson interferometer (schematic)")
bx=fig.add_subplot(gs[1]);bx.set(xlim=(0,10),ylim=(0,1));bx.axis("off")
labels=["Scene +\ntelescope","Interferometer\n(spectral encoding)","Detector +\nelectronics","Fourier\nreconstruction"]
for k,label in enumerate(labels):
 x=.05+2.5*k
 bx.add_patch(Rectangle((x,.15),2.1,.7,fc="#edf3f6",ec="#54717f"))
 bx.text(x+1.05,.5,label,ha="center",va="center",fontsize=9)
 if k<3:bx.annotate("",(x+2.45,.5),xytext=(x+2.1,.5),arrowprops={"arrowstyle":"->"})

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            dpi=120, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
plt.close(fig)
