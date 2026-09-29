"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig,ax=plt.subplots(1,3,figsize=(11,3.9),layout="constrained")
x=np.linspace(-1.3,1.5,500)
for a,shift,title in [(ax[0],0,"Direct band gap"),(ax[1],.8,"Indirect band gap")]:
 a.plot(x,-.6*x*x,color="#1565a8",lw=1.9)
 a.plot(x,1+.55*(x-shift)**2,color="#ca6720",lw=1.9)
 a.axvline(0,color=".7",ls=":",lw=1)
 a.set(xlim=(-1.3,1.5),ylim=(-1.15,2.2),xlabel="Crystal momentum (schematic)",ylabel="Electron energy",title=title)
 a.set_xticks([]);a.set_yticks([])
 a.annotate("",xy=(0,0),xytext=(0,1),arrowprops={"arrowstyle":"->","color":"#33865b","lw":1.7})
 a.text(-.85,.43,"photon",fontsize=9,color="#33865b")
ax[1].annotate("",xy=(0,1),xytext=(.8,1),arrowprops={"arrowstyle":"->","color":"#6e4a91","lw":1.7})
ax[1].text(.15,1.25,"phonon",fontsize=9,color="#6e4a91")
x=np.linspace(-3,3,500);ec=.25+.75*(1-np.tanh(1.7*x));ev=ec-2
ax[2].axvspan(-.85,.85,color=".85",alpha=.6)
ax[2].plot(x,ec,color="#ca6720",lw=1.9);ax[2].plot(x,ev,color="#1565a8",lw=1.9)
ax[2].axhline(0,color="#33865b",ls="--",lw=1.5)
ax[2].text(2.3,.5,r"$E_C$",color="#ca6720")
ax[2].text(2.3,-.08,r"$E_F$",color="#33865b")
ax[2].text(2.3,-1.6,r"$E_V$",color="#1565a8")
ax[2].text(-2,1.95,"p side");ax[2].text(1.3,1.95,"n side")
ax[2].text(0,-2.05,"depletion region",ha="center",fontsize=8)
ax[2].set(xlim=(-3,3),ylim=(-2.2,2.2),xlabel="Position across junction",ylabel="Electron energy",title="Equilibrium: flat Fermi level")
ax[2].set_xticks([]);ax[2].set_yticks([])
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
