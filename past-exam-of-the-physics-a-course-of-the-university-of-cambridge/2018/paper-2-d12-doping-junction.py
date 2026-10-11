"""Original solution figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig,axes=plt.subplots(2,2,figsize=(10,6.2),layout="constrained")
ax=axes[0,0]
for left,right in [(0,1.5),(2.5,4)]:
    ax.hlines([0,3],left,right,color="#1565a8",lw=2)
    ax.fill_between([left,right],-.22,0,color="#1565a8",alpha=.15)
    ax.fill_between([left,right],3,3.22,color="#1565a8",alpha=.15)
ax.hlines(2.65,.15,1.35,color="#ca6720",ls="--",lw=2)
ax.hlines(.35,2.65,3.85,color="#ca6720",ls="--",lw=2)
ax.text(.75,2.25,"donor level",ha="center")
ax.text(3.25,.7,"acceptor level",ha="center")
ax.text(-.15,3,r"$E_C$",ha="right");ax.text(-.15,0,r"$E_V$",ha="right")
ax.text(.75,-.55,"n-type",ha="center");ax.text(3.25,-.55,"p-type",ha="center")
ax.text(2,1.5,"band gap",ha="center",color="0.4")
ax.set_xlim(-.6,4.4);ax.set_ylim(-.8,3.65);ax.axis("off")
ax.set_title("Shallow impurity levels before contact (not to scale)")
x=np.linspace(-1.5,1.5,1200)
charge=np.where((x>=-1)&(x<0),-1.,np.where((x>=0)&(x<=1),1.,0.))
field=np.where((x>=-1)&(x<0),-(x+1),np.where((x>=0)&(x<=1),x-1,0.))
pot=np.where(x<-1,0,np.where(x<0,(x+1)**2/2,np.where(x<1,.5+x-x*x/2,1.)))
for ax,y,col,title in zip([axes[0,1],axes[1,0],axes[1,1]],[charge,field,pot],["#ca6720","#1565a8","#33865b"],["Depletion charge: fixed ions","Electric field: from n to p",r"Electrostatic potential: barrier $V_{\rm bi}$"]):
    ax.plot(x,y,color=col,lw=2)
    ax.axhline(0,color="0.5",lw=.7)
    ax.axvline(0,color="0.55",ls="--",lw=.8)
    for b in [-1,1]:ax.axvline(b,color="0.7",ls=":",lw=.8)
    ax.set_title(title,fontsize=10)
    ax.set_xticks([-1,0,1],[r"$-w_p$","junction",r"$w_n$"])
    ax.set_yticks([]);ax.set_xlim(-1.5,1.5)
    ax.text(-1.3,.65,"p",transform=ax.get_xaxis_transform(),ha="center")
    ax.text(1.3,.65,"n",transform=ax.get_xaxis_transform(),ha="center")
axes[0,1].text(-.5,-.6,"− acceptors",ha="center",fontsize=9)
axes[0,1].text(.5,.55,"+ donors",ha="center",fontsize=9)
axes[1,0].set_ylabel("Field (normalized)")
axes[1,1].set_ylabel("Potential (normalized)")
fig.suptitle("Abrupt equilibrium junction; equal dopant densities chosen for the schematic")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=135)
