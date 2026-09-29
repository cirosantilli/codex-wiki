"""Original functional xenon readout schematic, not an apparatus reproduction."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4.2),layout="constrained")
ax.add_patch(Rectangle((.2,.2),3,2.4,facecolor="#d7eaf2",edgecolor="#3b596b"))
ax.add_patch(Rectangle((.2,2.6),3,.55,facecolor="#faf0d0",edgecolor="#3b596b"))
ax.text(.35,2.83,"Gas: extracted charge makes S2",fontsize=9)
ax.text(.35,.45,"Liquid xenon",fontsize=10)
ax.scatter(1.4,1.1,marker="*",s=180,color="#cc6b32")
ax.text(.35,1.1,"Recoil",ha="left",va="center",fontsize=10)
ax.annotate("",(1.4,2.8),(1.4,1.25),arrowprops=dict(arrowstyle="->",lw=2,color="#2b6b93"))
ax.text(1.55,1.7,"Electron drift",fontsize=9)
for x in [.65,2.7]:
    ax.annotate("",(x,.25),(1.4,1.1),arrowprops=dict(arrowstyle="->",color="#cc6b32"))
ax.text(2.3,.75,"S1 light",color="#9b4e25",fontsize=9)
ax.text(1.7,3.4,"Light sensors",ha="center",fontsize=10)
ax.plot([.4,3],[3.2,3.2],lw=5,color="#3d4752")
ax.set(xlim=(0,3.6),ylim=(0,3.7),title="Signal formation");ax.axis("off")
t=np.linspace(0,10,1200)
s1=np.exp(-((t-1.5)/.11)**2);s2=2*np.exp(-((t-7.2)/.36)**2)
bx.plot(t,s1+s2,color="#275d7f",lw=2)
bx.annotate("",(1.5,1.45),(7.2,1.45),arrowprops=dict(arrowstyle="<->",color="#a35427"))
bx.text(4.35,1.58,"Drift time → depth",ha="center",fontsize=10)
bx.text(1.5,1.1,"S1",ha="center");bx.text(7.2,2.1,"S2",ha="center")
bx.set(xlabel="Time (schematic)",ylabel="Light signal (arbitrary units)",ylim=(0,2.6),title="Prompt and delayed readout")
bx.set_xticks([]);bx.set_yticks([]);bx.spines[["top","right"]].set_visible(False)
fig.suptitle("Two observables distinguish recoils; timing locates the interaction")
fig.savefig("paper-1-xenon-signals.png",dpi=155,facecolor="white")
