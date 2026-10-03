"""Pulled equilibrium mush: thermal fields and phase trajectory.
Python 3.14; NumPy/Matplotlib. Output basename to caller CWD.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
H,c,d=4.0,1.0,0.5
h=H-c-d
z=np.linspace(0,5,501)
T=z-H
C=np.where(z<=h,H-z,c+d*np.exp(-(z-h)/d))
fig,axes=plt.subplots(1,2,figsize=(10,4.6),facecolor="white")
ax=axes[0]
ax.set_facecolor("white")
ax.axvspan(0,h,color="#e0eee1",alpha=0.7)
ax.plot(z,T,label="Imposed temperature",color="#aa4034",lw=2.5)
ax.plot(z,-C,label="Local liquidus",color="#236d9d",ls="--",lw=2)
ax.axvline(h,color="#666666",ls=":",lw=1)
ax.text(h+0.07,-3.5,r"$h_0$")
ax.text(0.9,-0.8,"Mush",ha="center")
ax.text(3.6,-3.5,"Liquid",ha="center")
ax.set_xlabel(r"Height $z$ (scaled)")
ax.set_ylabel("Temperature (scaled)")
ax.set_title("Marginally tangent thermal fields")
ax.legend(frameon=False,loc="lower right",fontsize=9)
ax=axes[1]
ax.set_facecolor("white")
cc=np.linspace(0,4.4,300)
ax.plot(cc,-cc,color="#888888",ls="--",lw=1.4,label="Liquidus")
ax.plot(C,T,color="#236d9d",lw=2.5,label="Liquid composition trajectory")
ax.scatter([H,c+d],[ -H,-c-d],color="#236d9d",zorder=4)
ax.annotate("Eutectic base",xy=(H,-H),xytext=(2.5,-3.3),arrowprops={"arrowstyle":"-","color":"#555555"},fontsize=9)
ax.annotate("Mush roof",xy=(c+d,-c-d),xytext=(2.4,-0.7),arrowprops={"arrowstyle":"-","color":"#555555"},fontsize=9)
ax.axvline(c,color="#aaaaaa",ls=":",lw=1)
ax.text(c+0.05,0.8,r"$C_0$")
ax.annotate("",xy=(2.1,-2.1),xytext=(2.8,-2.8),arrowprops={"arrowstyle":"->","color":"#236d9d","lw":2})
ax.set_xlim(0,4.4)
ax.set_ylim(-4.4,1.3)
ax.set_xlabel("Liquid concentration (scaled)")
ax.set_ylabel("Temperature (scaled)")
ax.set_title("Phase-diagram path as height increases")
ax.legend(frameon=False,loc="upper right",fontsize=8)
fig.tight_layout()
fig.savefig("paper-72-mush-equilibrium.png",dpi=150,facecolor="white",transparent=False)
plt.close(fig)
