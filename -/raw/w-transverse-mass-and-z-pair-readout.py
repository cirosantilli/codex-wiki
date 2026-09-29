"""Original two-panel functional readout; invented events, no historical data.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5. Run from _media.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig, axes=plt.subplots(1,2,figsize=(11,6),layout="constrained")
for ax in axes:
    ax.set(xlim=(-2.1,2.1),ylim=(-2.85,2.05),aspect="equal"); ax.axis("off")
    ax.add_patch(Circle((0,0),1.15,fill=False,ec="#a1aab3",lw=1.5))
    ax.add_patch(Circle((0,0),1.5,fill=False,ec="#a1aab3",lw=9,alpha=.3))
    ax.plot(0,0,"o",color="#333333",ms=5)
    ax.text(0,1.76,"Cross section normal to the beam",ha="center",fontsize=10,color="#555555")
    ax.annotate("tracker",(-.85,.77),(-1.9,1.35),arrowprops=dict(arrowstyle="->",color="#777777"),fontsize=10)
    ax.annotate("calorimeter",(.95,1.17),(.45,1.43),arrowprops=dict(arrowstyle="->",color="#777777"),fontsize=10)
    ax.add_patch(Wedge((0,0),1.63,-9,9,width=.28,facecolor="#d58628"))
    ax.annotate("",(1.4,0),(0,0),arrowprops=dict(arrowstyle="->",color="#196b96",lw=3))
    ax.text(.72,-.25,"charged lepton",ha="center",color="#196b96",fontsize=10)
left,right=axes
left.set_title(r"W $\to\ell\nu$: transverse balance",weight="bold",pad=12)
left.annotate("",(-1.4,0),(0,0),arrowprops=dict(arrowstyle="->",color="#97475f",lw=2,ls="--"))
left.text(-.75,-.25,r"$\mathbf{p}_T^{miss}$",ha="center",color="#97475f")
left.text(-.87,.27,"no neutrino signal",ha="center",fontsize=10,color="#97475f")
left.text(0,-1.92,"Invented: pT(lepton) = pT(miss) = 40 GeV\nOpposite azimuths: mT = 80 GeV",ha="center",va="center",linespacing=1.6)
left.text(0,-2.62,"Neutrino longitudinal momentum unknown\nDashed arrow is inferred, not a detector hit",ha="center",fontsize=10,color="#97475f")
right.set_title(r"Z $\to\ell^+\ell^-$: two visible leptons",weight="bold",pad=12)
right.add_patch(Wedge((0,0),1.63,171,189,width=.28,facecolor="#d58628"))
right.annotate("",(-1.4,0),(0,0),arrowprops=dict(arrowstyle="->",color="#196b96",lw=3))
right.text(-.85,-.25,"charged lepton",ha="center",color="#196b96",fontsize=10)
right.text(0,-1.92,"Invented: each pT = 45 GeV, equal rapidity\nOpposite azimuths: pair mass = 90 GeV",ha="center",va="center",linespacing=1.6)
right.text(0,-2.62,"Both lepton four-momenta reconstructed\nPair invariant mass uses longitudinal information",ha="center",fontsize=10,color="#196b96")
fig.suptitle("Functional readout examples • massless leptons • c = 1 • no historical events",fontsize=12)
fig.savefig(Path(__file__).stem+".png",dpi=120,facecolor="white")
