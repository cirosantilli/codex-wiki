"""Qualitative, original wave-energy schematic; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(-1.5,2.5,1001)
wind=np.where(x<0,np.maximum(0,(x+1.5)/1.5),np.where(x<=1,np.exp(-3*x),np.exp(-3)+.45*(x-1)))
swell=np.where(x<0,np.exp(-.6),np.where(x<=1,np.exp(-.6*(1-x)),1))
fig,ax=plt.subplots(figsize=(8,4.8),dpi=120,layout="constrained")
ax.axvspan(0,1,color="#9ebaca",alpha=.45)
ax.plot(x,wind,color="#c36920",lw=2,label="Short wind-wave energy →")
ax.plot(x,swell,color="#225b91",lw=2,label="Long swell energy ←")
ax.set(xlim=(-1.5,2.5),ylim=(0,1.65),xlabel="Position across band (schematic)",ylabel="Energy / incident component energy",title="Wind waves and counter-propagating swell at an ice band")
ax.text(-.8,1.48,"Windward polynya",ha="center")
ax.text(.5,1.48,"Ice band",ha="center")
ax.text(1.8,1.48,"Seaward polynya",ha="center")
ax.annotate("Off-ice wind",xy=(-.25,1.28),xytext=(-1.35,1.28),arrowprops={"arrowstyle":"->"},va="center")
ax.annotate("",xy=(.35,.38),xytext=(.03,.38),arrowprops={"arrowstyle":"->","color":"#c36920","lw":2})
ax.annotate("",xy=(.65,.38),xytext=(.97,.38),arrowprops={"arrowstyle":"->","color":"#225b91","lw":2})
ax.text(.5,.25,"Compaction from both sides",ha="center",fontsize=9)
ax.legend(loc="lower right",fontsize=9)
ax.grid(alpha=.15)
fig.savefig("paper-72-band-energy.png",facecolor="white",transparent=False)
