from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "savefig.facecolor": "white"})
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure(figsize=(12,4.4))
fig.subplots_adjust(left=.02,right=.98,bottom=.16,top=.78,wspace=.04)
u=np.linspace(0,2*np.pi,40);v=np.linspace(0,np.pi,20)
xx=np.outer(np.cos(u),np.sin(v));yy=np.outer(np.sin(u),np.sin(v));zz=np.outer(np.ones_like(u),np.cos(v))
axs=[fig.add_subplot(1,3,i+1,projection="3d") for i in range(3)]
for ax in axs:
 ax.plot_wireframe(xx,yy,zz,color="0.8",lw=.35,rstride=4,cstride=3,alpha=.5)
 for axis in np.eye(3):ax.plot(*np.array([-1.15*axis,1.15*axis]).T,color="0.65",lw=.6)
 for pos,txt in [((1.25,0,0),"x"),((0,1.25,0),"y"),((0,0,1.23),"z")]:ax.text(*pos,txt,fontsize=10)
 ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),zlim=(-1.2,1.2));ax.set_box_aspect((1,1,1));ax.set_axis_off();ax.view_init(elev=22,azim=35)
ax=axs[0]
ax.quiver(0,0,0,0,0,1,color="#175c9e",arrow_length_ratio=.12,lw=2)
ax.quiver(0,0,0,1,0,0,color="#339966",arrow_length_ratio=.12,lw=2)
ax.scatter([0],[0],[0],c="#bd492e",s=35,depthshade=False)
ax.text(0,0,1.08,r"$|1\rangle$",color="#175c9e")
ax.text(1.08,0,-.2,r"$|+\rangle$",color="#339966")
ax.text(0,-.05,-.25,r"$I/2$",color="#bd492e")
ax.set_title("Pure states: surface\nEqual incoherent mixture: centre",fontsize=11)
theta=np.linspace(0,np.pi/2,120)
for ax,phi in zip(axs[1:],[np.pi/2,np.pi]):
 a=np.linspace(0,phi,200)
 paths=[np.stack([0*theta,-np.sin(theta),np.cos(theta)]),np.stack([-np.sin(a),-np.cos(a),0*a]),np.stack([np.full_like(theta,-np.sin(phi)),-np.cos(phi)*np.cos(theta),-np.cos(phi)*np.sin(theta)])]
 for k,(p,col) in enumerate(zip(paths,["#175c9e","#bd492e","#339966"])):
  ax.plot(*p,color=col,lw=2.4,label=["First pulse","Free evolution","Final pulse"][k])
  if np.linalg.norm(p[:,-1]-p[:,0])>.1:
   m=len(p[0])//2;diff=p[:,m+4]-p[:,m];ax.quiver(*p[:,m],*diff,color=col,arrow_length_ratio=.6,lw=1.7)
 ax.scatter(*paths[0][:,0],color="black",s=18);ax.scatter(*paths[-1][:,-1],color="#339966",s=35,depthshade=False)
 ax.set_title((r"$\delta T=\pi/2$: final $-x$"+"\nFinal pulse fixes the vector") if phi<2 else (r"$\delta T=\pi$: final $+z$"+"\nReturn to initial state"),fontsize=11)
fig.legend(*axs[2].get_legend_handles_labels(),loc="lower center",ncol=3,fontsize=10)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
