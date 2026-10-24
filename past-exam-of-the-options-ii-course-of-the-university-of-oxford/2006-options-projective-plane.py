"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig=plt.figure(figsize=(10,3.7),facecolor="white",layout="constrained")
ax=fig.add_subplot(131);ax.add_patch(Circle((0,0),.9,facecolor="#d7ebf7",edgecolor="#12679b",lw=3))
ax.text(0,0,r"$D^2$",ha="center",va="center",fontsize=27)
ax.text(.72,.7,"b",color="#12679b",fontsize=15)
ax.text(0,-1.2,"Single-edge identification",ha="center",fontsize=10)
ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),aspect="equal",title="First triangle becomes a disc")
ax.axis("off")
ax=fig.add_subplot(132,projection="3d")
u,v=np.meshgrid(np.linspace(0,2*np.pi,180),np.linspace(-.3,.3,24))
x=(1+v*np.cos(u/2))*np.cos(u);y=(1+v*np.cos(u/2))*np.sin(u);z=v*np.sin(u/2)
ax.plot_surface(x,y,z,color="#f0ba85",alpha=.95,linewidth=0,antialiased=True,rstride=1,cstride=3)
t=np.linspace(0,4*np.pi,500);v=.3
ax.plot((1+v*np.cos(t/2))*np.cos(t),(1+v*np.cos(t/2))*np.sin(t),v*np.sin(t/2),color="#12679b",lw=2)
ax.view_init(elev=24,azim=-55);ax.set_box_aspect((1,1,.45));ax.set_title("Second triangle becomes a Möbius band",fontsize=11)
ax.axis("off")
ax=fig.add_subplot(133);ax.axis("off")
ax.text(.5,.82,"Glue the blue boundaries",ha="center",fontsize=12)
ax.text(.5,.58,r"$D^2\cup_{\partial}\mathrm{M\ddot obius}$",ha="center",fontsize=17)
ax.text(.5,.36,r"$=\ \mathbb{RP}^2$",ha="center",fontsize=26)
ax.text(.5,.13,r"$\chi=2-3+2=1$",ha="center",fontsize=15)
fig.savefig("2006-options-projective-plane.png",dpi=160,facecolor="white")
