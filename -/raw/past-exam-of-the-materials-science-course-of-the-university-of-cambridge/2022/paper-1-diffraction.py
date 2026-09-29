import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":11,"savefig.facecolor":"white","figure.facecolor":"white"})
fig,axes=plt.subplots(1,2,figsize=(10.2,5.2))
for ax,ordered in zip(axes,[False,True]):
 for h in range(-2,3):
  for k in range(-2,3):
   if h*h+k*k>8:continue
   fundamental=h%2==0 and k%2==0
   if not ordered and not fundamental:continue
   ax.scatter(h,k,s=90 if fundamental else 40,c="#224e77" if fundamental else "#dd8b24",zorder=3)
   ax.annotate(f"({h},{k},0)",(h,k),xytext=(0,8),ha="center",textcoords="offset points",fontsize=7)
 ax.set(xlim=(-2.65,2.65),ylim=(-2.6,2.8),xlabel=r"$g_x a$",ylabel=r"$g_y a$",title="Ordered precipitate" if ordered else "Disordered FCC matrix")
 ax.set_aspect("equal");ax.set_xticks(range(-2,3));ax.set_yticks(range(-2,3));ax.grid(alpha=.15)
axes[1].scatter([],[],c="#224e77",s=90,label="Fundamental / direct")
axes[1].scatter([],[],c="#dd8b24",s=40,label="Superlattice")
axes[1].legend(loc="lower center",bbox_to_anchor=(.5,-.29),fontsize=9,frameon=False)
fig.suptitle(r"[001] zone; $h^2+k^2\leq8$ (separate normalized cell scales)")
fig.tight_layout();fig.savefig("paper-1-diffraction.png",dpi=140)
