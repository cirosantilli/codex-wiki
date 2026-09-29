"""Original triangle illustrating consistently oriented side vectors."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

C=np.array([0.,0.]); B=np.array([4.4,0.]); A=np.array([1.3,2.7])
fig,ax=plt.subplots(figsize=(6.5,4.5),layout="constrained")
for start,end,color in [(C,B,"#2477a1"),(C,A,"#b8632e"),(A,B,"#57883e")]:
    ax.annotate("",xy=end,xytext=start,arrowprops=dict(arrowstyle="-|>",color=color,lw=2.4,mutation_scale=16))
for point,label,offset in [(C,"C",(-.23,-.22)),(B,"B",(.06,-.22)),(A,"A",(-.12,.12))]:
    ax.text(*(point+offset),label,fontsize=14)
ax.text(2.2,-.3,r"$\mathbf{a}=\overrightarrow{CB}$",color="#2477a1",ha="center",fontsize=13)
ax.text(.24,1.5,r"$\mathbf{b}$",color="#b8632e",fontsize=15)
ax.text(3.13,1.55,r"$\mathbf{c}=\mathbf{a}-\mathbf{b}$",color="#57883e",fontsize=13)
angle=np.degrees(np.arctan2(A[1],A[0]))
ax.add_patch(Arc(C,.95,.95,theta1=0,theta2=angle,color="#555555",lw=1.2))
ax.text(.54,.28,r"$C$",fontsize=12)
ax.set(xlim=(-.55,4.95),ylim=(-.7,3.2),title="Side lengths are opposite the matching vertices")
ax.set_aspect("equal");ax.axis("off")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
