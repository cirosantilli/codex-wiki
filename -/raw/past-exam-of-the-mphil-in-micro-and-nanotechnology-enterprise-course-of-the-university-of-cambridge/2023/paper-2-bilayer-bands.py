"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig,axs=plt.subplots(1,3,figsize=(10,3.6),layout="constrained");k=np.linspace(-1,1,400)
for sign in [-1,1]:
    for branch in [-1,1]:
        axs[0].plot(k,sign*(np.sqrt(.4**2+k*k)+branch*.4),color="#246c99")
axs[0].set(title="AB stacking: coupled bands",xlabel="Wave vector",ylabel="Energy",xticks=[],yticks=[])
for sign in [-1,1]:
    for branch in [-1,1]:
        axs[1].plot(k,sign*(1+branch*np.sqrt((.7*k)**2+.13**2)),color="#246c99")
axs[1].annotate("",(.03,.87),(.03,-.87),arrowprops=dict(arrowstyle="<->",color="#b23a37"))
axs[1].text(.1,0,"Optical\nresonance",fontsize=9)
axs[1].set(title="Twist: avoided crossings (local cut)",xlabel="Wave vector near crossing",xticks=[],yticks=[])
w=np.linspace(1.2,3.1,300)
for center,c in [(1.65,"#b23a37"),(2.15,"#328b53"),(2.65,"#246c99")]:
    axs[2].plot(w,.2+.7*np.exp(-((w-center)/.12)**2),color=c)
axs[2].set(title="Twist shifts the optical resonance",xlabel="Photon energy (schematic)",ylabel="Absorption",yticks=[],xticks=[])
fig.suptitle("Different stacking domains can have different colours at the same layer count",fontsize=12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
