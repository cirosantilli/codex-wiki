"""Original two-photon and Raman diagrams; save basename in cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(10,4.6),layout="constrained")
def level(ax,y,label,style="-",color="#274e82"):
 ax.plot([.1,.75],[y,y],style,color=color,lw=2)
 ax.text(.8,y,label,va="center",fontsize=12)
for ax in axs:ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
ax=axs[0];level(ax,.10,r"$|i\rangle$");level(ax,.88,r"$|f\rangle$")
level(ax,.51,"Virtual","--",color=".5")
ax.annotate("",xy=(.32,.51),xytext=(.32,.10),arrowprops={"arrowstyle":"-|>","lw":2,"color":"#bc5429"})
ax.annotate("",xy=(.57,.88),xytext=(.57,.51),arrowprops={"arrowstyle":"-|>","lw":2,"color":"#bc5429"})
ax.text(.16,.3,r"$\omega_1$",fontsize=12);ax.text(.58,.67,r"$\omega_2$",fontsize=12)
ax.set_title("Absorb + absorb",fontsize=13)
ax.text(.5,-.03,r"$\Delta E=\hbar(\omega_1+\omega_2)$",ha="center")
ax=axs[1];level(ax,.10,r"$|i\rangle$");level(ax,.3,r"$|f\rangle$")
level(ax,.88,r"$|r\rangle$");level(ax,.75,"Virtual","--",color=".5")
ax.annotate("",xy=(.3,.75),xytext=(.3,.1),arrowprops={"arrowstyle":"-|>","lw":2,"color":"#bc5429"})
ax.annotate("",xy=(.6,.3),xytext=(.6,.75),arrowprops={"arrowstyle":"-|>","lw":2,"color":"#288969"})
ax.text(.11,.48,r"$\omega_1$",fontsize=12);ax.text(.61,.48,r"$\omega_2$",fontsize=12)
ax.set_title("Absorb + stimulated emission",fontsize=13)
ax.text(.5,-.03,r"$\Delta E=\hbar(\omega_1-\omega_2)$",ha="center")
fig.savefig("paper-1-two-photon-paths.png",dpi=150,facecolor="white")
