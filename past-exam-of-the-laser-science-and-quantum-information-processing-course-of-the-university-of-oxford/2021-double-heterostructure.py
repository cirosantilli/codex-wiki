from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "savefig.facecolor": "white"})
fig,axs=plt.subplots(2,1,figsize=(9,5.8),sharex=True,layout="constrained",gridspec_kw={"height_ratios":[2,1]})
x=np.array([-3,-1,-1,1,1,3]);ec=np.array([2.4,2.4,1.7,1.7,2.4,2.4]);ev=np.array([-.6,-.6,0,0,-.6,-.6])
for ax in axs:
 ax.axvspan(-1,1,color="#e2eff8");ax.axvline(-1,color="0.6",lw=.6);ax.axvline(1,color="0.6",lw=.6)
axs[0].plot(x,ec,color="#175c9e",lw=2,label=r"$E_c$: electron well")
axs[0].plot(x,ev,color="#bd492e",lw=2,label=r"$E_v$: hole confinement")
axs[0].annotate("electrons",(.1,1.72),(.1,2.5),ha="center",arrowprops={"arrowstyle":"->"})
axs[0].annotate("holes",(-.2,-.03),(-.2,-.65),ha="center",arrowprops={"arrowstyle":"->"})
for pos,txt in [(-2,"Wide-gap cladding"),(0,"Narrow-gap active layer"),(2,"Wide-gap cladding")]:
 axs[0].text(pos,3,txt,ha="center",fontsize=10)
axs[0].set(ylabel="Electron energy (schematic)",ylim=(-1,3.4));axs[0].legend(loc="center right",fontsize=9)
axs[0].set_yticks([])
xs=np.linspace(-3,3,500);axs[1].plot(xs,np.exp(-xs*xs),color="#175c9e",lw=2,label="Guided optical intensity")
axs[1].step(x,[1,1,1.6,1.6,1,1],where="post",color="#746147",lw=1.5,label="Refractive index (schematic)")
axs[1].set(xlabel="Position transverse to laser axis (arbitrary units)",ylabel="Relative profiles",ylim=(0,2.1),xlim=(-3,3))
axs[1].legend(loc="upper right",fontsize=9);axs[1].set_yticks([])
fig.suptitle("Double heterostructure: type-I offsets, band bending omitted")

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
