"""Original parallel averaged-channel illustration (CIP, not CPP).
Python3.14/NumPy2.3/Matplotlib3.10. PNG basename output in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(1,2,figsize=(9,3.8),layout="constrained")
for ax,anti in zip(axes,[False,True]):
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.set_title("Antiparallel moments" if anti else "Parallel moments")
    ax.text(.5,.87,r"$G_{AP}=8D^2/(a+b)$" if anti else r"$G_P=2D^2(1/a+1/b)$",ha="center")
    for i,y in enumerate([.61,.3]):
        text=r"$G_\uparrow=4D^2/(a+b)$" if anti and i==0 else r"$G_\downarrow=4D^2/(a+b)$" if anti else r"$G_\uparrow=2D^2/a$" if i==0 else r"$G_\downarrow=2D^2/b$"
        color="#dcecf5" if anti else "#cfeacb" if i==0 else "#f2d7cf"
        ax.add_patch(FancyBboxPatch((.15,y-.085),.7,.17,boxstyle="round,pad=0.02",facecolor=color,edgecolor="0.4"))
        ax.text(.5,y,text,ha="center",va="center")
        ax.plot([.08,.15],[y,y],color="0.3");ax.plot([.85,.92],[y,y],color="0.3")
    for xx in [.08,.92]:ax.plot([xx,xx],[.3,.61],color="0.3",lw=1.5)
    ax.text(.5,.04,"Two parallel spin conductances",ha="center",color="0.3")
fig.suptitle(r"Thickness-averaged CIP model; $a=t_1\rho_L+t_2\rho_N$, $b=t_1\rho_H+t_2\rho_N$")
fig.savefig("paper-1-aqc2013-spin-channel-conductance.png",dpi=140,facecolor="white",bbox_inches="tight")
