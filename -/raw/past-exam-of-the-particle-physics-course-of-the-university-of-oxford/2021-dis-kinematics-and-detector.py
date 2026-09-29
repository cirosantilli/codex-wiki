from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
from matplotlib.patches import Rectangle, Arc
fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), layout="constrained")
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlim(-1.1, 6.5)
    ax.set_ylim(-1.9, 3.5)
    ax.axis("off")
def arrow(ax, start, end, color="black", style="-"):
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 1.8, "color": color, "linestyle": style})
a=axes[0]
a.set_title("Laboratory kinematics")
arrow(a, (-0.7,0), (1.6,0), "#1769aa")
a.plot(1.7,0,"ko",ms=7)
a.text(0,0.3,r"$e^-:\ p_1, E$",ha="center")
a.text(1.7,-0.7,r"$p_2=(m_p,\mathbf{0})$",ha="center")
arrow(a, (1.7,0), (4.9,2.35), "#1769aa")
a.text(4.3,2.8,r"$e^-:\ p_3, E'$",ha="center")
a.plot([1.7,5.8],[0,0],color="0.65",lw=1,ls=":")
a.add_patch(Arc((1.7,0),2,2,theta1=0,theta2=36.3,color="#1769aa"))
a.text(2.85,0.43,r"$\theta$")
arrow(a, (1.7,0), (4,-1.2), "#ba4a00", "--")
a.text(4.7,-1.2,r"$q=p_1-p_3$",ha="center",color="#ba4a00")
a.text(1.5,-1.7,"The proton starts at rest; the hadronic system receives q.",ha="center",fontsize=9)
b=axes[1]
b.set_title("One possible fixed-target arrangement")
arrow(b,(-0.8,0),(0.45,0),"#1769aa")
b.text(-0.2,0.45,"known beam E",ha="center",fontsize=10)
b.add_patch(Rectangle((0.5,-0.45),0.12,0.9,color="#ba4a00"))
b.text(0.55,-0.9,"H target",ha="center",fontsize=10)
arrow(b,(0.62,0),(4.8,2.0),"#1769aa")
for x in (1.7,3.1):
    y=(x-0.62)*2/(4.8-0.62)
    b.plot([x-0.28,x+0.28],[y+0.55,y-0.55],color="#388e3c",lw=3)
b.add_patch(Rectangle((2.05,0.45),0.65,1.1,fill=False,ec="#7b1fa2",lw=1.7))
b.text(2.3,2.25,"tracking + magnet",ha="center",fontsize=9)
b.add_patch(Rectangle((4.5,1.55),0.55,1.0,fc="#bbdefb",ec="#1769aa",lw=1.6))
b.text(4.9,3.0,"EM calorimeter: E'",ha="center",fontsize=9)
b.text(2.3,1.85,r"track direction: $\theta$",ha="center",fontsize=9)
for y in (-0.9,-0.6,-0.2): arrow(b,(0.62,0),(4.6,y),"#ba4a00")
b.add_patch(Rectangle((4.7,-1.3),0.65,1.4,fc="#ffe0b2",ec="#ba4a00",lw=1.6))
b.text(3.9,-1.7,"hadronic activity / containment checks",ha="center",fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
