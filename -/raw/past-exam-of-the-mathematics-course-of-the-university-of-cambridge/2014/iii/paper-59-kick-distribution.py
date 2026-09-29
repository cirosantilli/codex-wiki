"""Original exam-solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only the same-basename PNG in the current working directory.
Uses MPLCONFIGDIR supplied by the caller.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
g=.2
c=np.linspace(-1,1,1600)
a=1/(1-2*g*c-g*g)
e=np.sqrt(1-(1-2*g*c-g*g)*(1+g*c)**2)
fig,ax=plt.subplots(figsize=(7.6,4.4),layout="constrained")
ax.plot(a,e,color="#2166ac",lw=2)
for cc,label,off in [(-1,"backward kick",(10,10)),(-g/3,"minimum eccentricity",(-55,20)),(1,"forward kick",(-105,-28))]:
 aa=1/(1-2*g*cc-g*g);ee=np.sqrt(1-(1-2*g*cc-g*g)*(1+g*cc)**2)
 ax.scatter(aa,ee,c="#b2182b",zorder=3)
 ax.annotate(label,(aa,ee),xytext=off,textcoords="offset points")
ax.set(xlabel="Semimajor-axis ratio a′/a",ylabel="Eccentricity e′",title="Planar kicks: γ = 0.2; both radial signs share this curve")
ax.grid(alpha=.25)
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
