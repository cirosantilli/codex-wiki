"""Compare only displayed counts; the overall row is not a pooled estimate.
Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. Write PNG to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Rows: printed overall, then the five actually printed age strata.
counts = np.array([
[[219,47,22,112,145,54],[240,44,27,147,259,108]],
[[3,5,2,17,27,15],[8,5,4,11,48,24]],
[[36,17,8,48,71,22],[49,15,5,67,126,55]],
[[45,9,7,25,23,10],[59,10,9,39,50,18]],
[[47,8,3,12,10,6],[57,6,5,18,21,10]],
[[58,8,0,6,10,0],[41,7,3,9,12,1]],
], dtype=float)
rate = 100*counts[:,:,4:].sum(axis=2)/counts.sum(axis=2)
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"font.family":"DejaVu Sans"})
fig,ax=plt.subplots(figsize=(7.6,4.4),dpi=100,facecolor="white")
y=np.arange(6)
for k in range(6):
 ax.plot(rate[k], [y[k],y[k]], color="#a3a3a3", lw=2,zorder=1)
for i,(label,color,marker) in enumerate([("Not employed","#2166ac","o"),("Employed","#b35806","s")]):
 ax.scatter(rate[:,i],y,color=color,label=label,marker=marker,s=47,zorder=3)
 for x,yy in zip(rate[:,i],y):
  ax.annotate(f"{x:.1f}%",(x,yy),xytext=(0,-16 if i==0 else 9),textcoords="offset points",ha="center",fontsize=9,color=color)
ax.axhline(.5,color="#777777",ls="--",lw=.8)
ax.set_yticks(y,["Overall (N = 1424)","14–24 (N = 169)","25–44 (N = 519)","45–54 (N = 304)","55–64 (N = 203)","65+ (N = 155)"])
ax.invert_yaxis(); ax.set_xlim(0,82);ax.set_ylim(5.65,-.65)
ax.set_xlabel("Use at least daily: percentage within employment group")
ax.set_title("The direction persists in all five displayed age strata",loc="left",pad=25,fontweight="bold")
ax.grid(axis="x",alpha=.18);ax.set_axisbelow(True)
ax.legend(loc="lower right",frameon=True,fontsize=9)
fig.text(.02,.015,"Source qualification: the five strata total 1350, so they do not reproduce the printed overall row.",fontsize=8.2)
fig.subplots_adjust(left=.24,right=.975,bottom=.16,top=.85)
fig.savefig(Path.cwd()/"2020-age-stratum-contrasts.png",dpi=100,facecolor="white",transparent=False,metadata={"Software":"codex-wiki Matplotlib"})
plt.close(fig)
