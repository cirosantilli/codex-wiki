"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(8,4.7),facecolor="white",layout="constrained")
for ax,sgn,name in[(axs[0],-1,"Lower-frequency mode"),(axs[1],1,"Higher-frequency mode")]:
 k=3+sgn*6/np.sqrt(7);ratio=(9-8*k)/(3*k);theta=.24;phi=ratio*theta
 a=np.array([0.,0.]);b=np.array([np.sin(theta),-np.cos(theta)]);c=b+np.array([np.sin(phi),-np.cos(phi)])
 ax.plot([0,0],[0,-2],ls="--",color="0.7",lw=1)
 ax.plot([a[0],b[0]],[a[1],b[1]],color="#12679b",lw=6,solid_capstyle="round")
 ax.plot([b[0],c[0]],[b[1],c[1]],color="#b86a16",lw=6,solid_capstyle="round")
 for q,label,off in[(a,"A",(-.14,.04)),(b,"B",(.09,.02)),(c,"C",(.09,0))]:
  ax.scatter(*q,color="black",s=23,zorder=5);ax.text(*(q+off),label,fontsize=12)
 ax.text(-.7,-2.35,fr"$\omega^2=(g/a)(3{'-'if sgn<0 else'+'}6/\sqrt{{7}})$",fontsize=12)
 ax.text(-.7,-2.62,fr"$\phi/\theta\approx{ratio:.3f}$",fontsize=11)
 ax.set(aspect="equal",xlim=(-.9,1.2),ylim=(-2.8,.25),title=name)
 ax.axis("off")
fig.suptitle("Two equal uniform rods: schematic normal-mode amplitudes",fontsize=12)
fig.savefig("2006-options-rod-modes.png",dpi=160,facecolor="white")
