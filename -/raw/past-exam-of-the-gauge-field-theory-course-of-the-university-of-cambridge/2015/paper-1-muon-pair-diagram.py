"""Original QED s-channel topology; arrows denote fermion-number flow."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 4.1), dpi=100, facecolor="white")
left=np.array([1.1, 1.0]);right=np.array([2.9, 1.0])
branches=[(np.array([0.,.2]),left,r"$e^-(p_-)$",(-.02,.03)),
          (left,np.array([0.,1.8]),r"$e^+(p_+)$",(-.02,1.93)),
          (right,np.array([4.,1.8]),r"$\mu^-(k_-)$",(3.52,1.93)),
          (np.array([4.,.2]),right,r"$\mu^+(k_+)$",(3.52,.03))]
for a,b,label,pos in branches:
    ax.plot([a[0],b[0]],[a[1],b[1]],color="#234d6b",lw=2)
    mid=(a+b)/2;v=(b-a)*.10
    ax.annotate("",xy=mid+v,xytext=mid-v,arrowprops={"arrowstyle":"-|>","color":"#234d6b","lw":1.8,"mutation_scale":14})
    ax.text(*pos,label,fontsize=14)
x=np.linspace(1.1,2.9,501);y=1+.075*np.sin(2*np.pi*9*(x-1.1)/1.8)
ax.plot(x,y,color="#a14435",lw=1.8);ax.scatter([1.1,2.9],[1,1],s=24,color="#234d6b",zorder=3)
ax.text(2,1.24,r"$\gamma^*: q^2=s$",ha="center",fontsize=14)
ax.annotate("",xy=(2.45,.73),xytext=(1.55,.73),arrowprops={"arrowstyle":"->","color":"0.3"})
ax.text(2,.5,r"$q=p_-+p_+=k_-+k_+$",ha="center",fontsize=13)
ax.set(xlim=(-.28,4.4),ylim=(-.12,2.4));ax.axis("off")
fig.suptitle("One virtual photon connects the two charged-fermion currents",fontsize=15,y=.96)
fig.text(.5,.04,"Time runs left to right. Arrows show fermion flow, not the momentum of every leg.",ha="center",fontsize=11)
fig.subplots_adjust(left=.035,right=.98,top=.87,bottom=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
