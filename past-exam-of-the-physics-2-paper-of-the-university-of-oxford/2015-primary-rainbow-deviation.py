from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8),layout="constrained")
a=np.linspace(.001,np.pi/2-.001,600)
for n,col in [(1.33,"#ba3c39"),(4/3,"#246c94"),(1.34,"#7553a4")]:
 b=np.arcsin(np.sin(a)/n);delta=np.pi+2*a-4*b
 ax.plot(np.degrees(a),np.degrees(delta),lw=2,color=col,label=f"n = {n:.4f}")
 bm=np.arcsin(np.sqrt((4-n*n)/(3*n*n)));am=np.arcsin(n*np.sin(bm));dm=np.pi+2*am-4*bm
 ax.plot(np.degrees(am),np.degrees(dm),"o",color=col)
ax.annotate("Minimum at 137.97°\nfor n = 4/3",xy=(59.39,137.97),xytext=(14,151),arrowprops={"arrowstyle":"->","color":"#246c94"},fontsize=11)
ax.set(xlabel=r"Incidence angle $\alpha$ (degrees)",ylabel=r"Deviation $\delta$ (degrees)",title="One internal reflection",xlim=(0,90),ylim=(130,182));ax.legend(fontsize=10);ax.grid(alpha=.18)
n=np.linspace(1.31,1.36,400);b=np.arcsin(np.sqrt((4-n*n)/(3*n*n)));a=np.arcsin(n*np.sin(b));theta=4*b-2*a
bx.plot(n,np.degrees(theta),color="#246c94",lw=2.5);bx.plot(4/3,42.0296588657,"o",color="#246c94")
bx.annotate("Larger index\n→ smaller bow radius",xy=(1.347,40.1),xytext=(1.314,39.2),arrowprops={"arrowstyle":"->"},fontsize=11)
bx.set(xlabel="Refractive index n",ylabel="Angle from antisolar direction (degrees)",title="Dispersion separates the colours",xlim=(1.31,1.36));bx.grid(alpha=.18)
fig.suptitle("Geometrical primary rainbow; indices are illustrative",fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
