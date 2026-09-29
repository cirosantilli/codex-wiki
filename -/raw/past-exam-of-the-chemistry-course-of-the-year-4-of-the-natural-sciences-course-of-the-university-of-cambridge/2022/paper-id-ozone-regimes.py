"""Original atmospheric-chemistry illustration; Python 3.14, NumPy, Matplotlib.
Output is a PNG basename in the current working directory, not the source directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","savefig.facecolor":"white"})

v=np.linspace(.02,4,401);n=np.linspace(.02,4,401);V,N=np.meshgrid(v,n)
# Deliberately schematic response, not a kinetic fit or measured concentration.
O=30*V*N/(.6+N+.5*N*N/(V+.2))
fig,ax=plt.subplots(figsize=(9,6),layout="constrained")
cf=ax.contourf(V,N,O,levels=np.arange(0,91,10),cmap="YlGnBu",alpha=.8)
cs=ax.contour(V,N,O,levels=[10,20,30,40,50,60,70,80],colors=".35",linewidths=.65)
ax.clabel(cs,fmt="%d",fontsize=9)
ax.plot(v,np.sqrt(1.2*(v+.2)),color="black",ls="--",lw=1.6)
ax.text(2.65,.36,"NOₓ-limited",ha="center",bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
ax.text(2.75,3.65,"VOC-limited / NOₓ-saturated",ha="center",bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
style={"arrowstyle":"->","lw":2,"color":"#b73724"}
ax.annotate("",xy=(2.4,.55),xytext=(2.4,1.1),arrowprops=style)
ax.text(2.45,.8,"cut NOₓ:\nless ozone",va="center",color="#87251b",bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
ax.annotate("",xy=(1.1,2.65),xytext=(1.1,3.3),arrowprops=style)
ax.text(.96,2.95,"cut NOₓ:\ncan raise ozone",ha="right",va="center",color="#87251b",bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
ax.annotate("",xy=(2.65,2.95),xytext=(3.4,2.95),arrowprops=style)
ax.text(3.05,2.75,"cut VOC: less ozone",ha="center",color="#87251b",bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
ax.set(xlabel="VOC loading (arbitrary units)",ylabel="NOₓ loading (arbitrary units)",xlim=(0,4),ylim=(0,4),title="Illustrative ozone-response contours; dashed line marks the sensitivity ridge")
fig.colorbar(cf,ax=ax,label="Toy ozone index (arbitrary units)")
fig.savefig("paper-id-ozone-regimes.png",dpi=165)
plt.close(fig)
