"""Original E/D field-line schematic, dielectricepsilon_r=3 and positive sphere."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

fig,axs=plt.subplots(1,2,figsize=(10,4.8),dpi=100,facecolor="white")
for ax,kind in zip(axs,["E","D"]):
    ax.axhspan(-2.2,0,color="#e9f1f8");ax.axhline(0,color="0.55",lw=1)
    angles=list(np.linspace(.12,np.pi-.12,9))+list(np.linspace(np.pi+.12,2*np.pi-.12,9 if kind=="E" else 27))
    for angle in angles:
        u=np.array([np.cos(angle),np.sin(angle)]);a=u*1.05;b=u*1.96
        ax.plot([a[0],b[0]],[a[1],b[1]],color="#2e648b",lw=1)
        ax.annotate("",xy=u*1.60,xytext=u*1.41,arrowprops={"arrowstyle":"-|>","color":"#2e648b","lw":.8,"mutation_scale":8})
    ax.add_patch(Circle((0,0),1,facecolor="#f4f4f4",edgecolor="black",lw=1.5,zorder=4));ax.text(0,0,"+Q",ha="center",va="center",fontsize=16,zorder=5)
    ax.text(-2.05,1.85,"Air",fontsize=10);ax.text(-2.05,-1.97,r"Dielectric: $\epsilon_r=3$",fontsize=10)
    ax.set(xlim=(-2.2,2.2),ylim=(-2.2,2.2));ax.set_aspect("equal");ax.axis("off")
    ax.set_title("E: equal magnitude at equal r" if kind=="E" else "D: threefold flux density below",fontsize=12)
fig.suptitle("Half immersion: field directions match, displacement flux differs",fontsize=14,y=.97)
fig.text(.5,.035,"Original ideal electrostatic schematic; line density represents the indicated field's flux.",ha="center",fontsize=10.5)
fig.subplots_adjust(left=.025,right=.98,top=.86,bottom=.09,wspace=.08)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
