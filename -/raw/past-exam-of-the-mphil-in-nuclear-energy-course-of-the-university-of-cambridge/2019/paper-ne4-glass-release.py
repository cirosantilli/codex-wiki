"""Original illustrative batch-leach curves for 2019 NE4.
Python 3.14; numpy and matplotlib. Writes a basename PNG to the working directory.
The functions are invented teaching curves, not fits to measured glass data.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
t=np.linspace(0,10,700)
network=1.4*(-np.expm1(-t/1.7))+.025*t
boron=network
sodium=network+.62*(-np.expm1(-t/.32))
silicon=.62*network
fig,ax=plt.subplots(figsize=(8.0,4.7),layout="constrained")
for curve,label,color in [(sodium,"Sodium: early exchange + network release","#aa6526"),(boron,"Boron: relatively mobile tracer in this example","#176f4e"),(silicon,"Silicon: partial retention in alteration layer","#175782")]:
    ax.plot(t,curve,lw=2.4,color=color,label=label)
ax.annotate("Rapid early sodium release",(.35,float(np.interp(.35,t,sodium))),xytext=(2.8,.45),arrowprops={"arrowstyle":"->","color":"#aa6526"},color="#aa6526",fontsize=10)
ax.annotate("Small continuing release slopes",(8,float(np.interp(8,t,boron))),xytext=(5.1,1.05),arrowprops={"arrowstyle":"->","color":"#176f4e"},color="#176f4e",fontsize=10)
ax.set(xlabel="Time (arbitrary units)",ylabel="Normalised release (arbitrary units)",xlim=(0,10),ylim=(0,2.65),title="One illustrative batch-glass-alteration scenario")
ax.text(.98,.05,"Not measured data; ordering and curvature are not universal",transform=ax.transAxes,ha="right",va="bottom",fontsize=9,color="#444444")
ax.legend(loc="upper left",fontsize=8.5)
ax.grid(alpha=.22)
fig.savefig(Path.cwd()/"paper-ne4-glass-release.png",dpi=150,facecolor="white")
plt.close(fig)
