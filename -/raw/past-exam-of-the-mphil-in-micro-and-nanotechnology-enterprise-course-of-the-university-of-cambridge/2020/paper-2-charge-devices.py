"""Original electronic-device schematics; Python 3.14 and Matplotlib."""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
fig,axs=plt.subplots(1,3,figsize=(14,4.5),layout="constrained")
ax=axs[0];ax.set(xlim=(0,6),ylim=(0,5),title="A  Single-electron transistor")
ax.add_patch(Circle((3,2.4),.62,color="#ccdfed"));ax.text(3,2.4,"island\nN, Ctotal",ha="center",va="center")
ax.plot([.3,1.65],[2.4,2.4],"k");ax.plot([4.35,5.7],[2.4,2.4],"k")
for left in [1.65,3.65]:
 ax.add_patch(Rectangle((left,2.15),.7,.5,fill=False));ax.text(left+.35,1.65,"tunnel\nR || C",ha="center")
ax.plot([2.35,2.4],[2.4,2.4],"k");ax.plot([3.6,3.65],[2.4,2.4],"k")
ax.text(.3,2.75,"source");ax.text(4.8,2.75,"drain")
ax.plot([3,3],[3.02,3.65],"k");ax.plot([2.7,3.3],[3.65,3.65],"k");ax.plot([2.7,3.3],[3.8,3.8],"k");ax.plot([3,3],[3.8,4.35],"k")
ax.text(3.45,3.65,"Cg");ax.text(3,4.55,"insulated gate Vg",ha="center")
ax.text(3,.55,r"$E_C=e^2/(2C_\Sigma)$",ha="center");ax.axis("off")
ax=axs[1];ax.set(xlim=(0,5),ylim=(0,5),title="B  Heterostructure cross-section")
for y,h,col,label in [(3.1,1,"#dae3f0","doped AlGaAs: + donors"),(2.5,.6,"#ebeff5","undoped AlGaAs spacer"),(.6,1.9,"#f1dfcf","GaAs")]:
 ax.add_patch(Rectangle((.3,y),4.4,h,facecolor=col,edgecolor="gray"));ax.text(2.5,y+h/2,label,ha="center",fontsize=10)
ax.plot([.5,4.5],[2.44,2.44],color="#235caa",lw=4);ax.text(2.5,2.15,"2DEG: normal motion quantized",ha="center",fontsize=9)
ax.text(2.5,4.45,"surface gates above the channel",ha="center",fontsize=9);ax.axis("off")
ax=axs[2];ax.set_aspect("equal");ax.set(xlim=(-2.7,2.7),ylim=(-2.4,2.4),title="C  Gate-defined region: plan view")
ax.add_patch(Rectangle((-2.5,-2),5,4,color="#d9e2ee"))
ax.add_patch(Rectangle((-1.5,-1.1),3,2.2,color="white",ec="k"));ax.text(0,0,"electron island",ha="center")
for y in [-.2,.2]:ax.plot([-2.6,-1.5],[y,y],color="#356baa");ax.plot([1.5,2.6],[y,y],color="#356baa")
ax.text(0,1.5,"depleted exterior / gates",ha="center",fontsize=9)
ax.text(-2,0,"S",ha="center");ax.text(2,0,"D",ha="center");ax.text(0,-1.6,"finite steep lateral barriers",ha="center",fontsize=9);ax.axis("off")
fig.savefig("paper-2-charge-devices.png",dpi=155,facecolor="white")

