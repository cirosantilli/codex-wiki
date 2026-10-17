"""Original vacuum-manifold schematics; output PNG basename to cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(11,3.8),layout="constrained")
a=fig.add_subplot(131);b=fig.add_subplot(132);c=fig.add_subplot(133,projection="3d")
a.scatter([-1,1],[0,0],s=130,color=["#274e82","#bc5429"])
a.text(-1,-.25,r"$-v$",ha="center");a.text(1,-.25,r"$+v$",ha="center")
a.text(0,.65,"Disconnected minima",ha="center")
a.text(0,-.75,"Different regions can meet\nacross a physical wall.",ha="center",fontsize=10)
a.set(xlim=(-1.7,1.7),ylim=(-1,1),title=r"Walls: nontrivial $\pi_0$");a.axis("off")
t=np.linspace(0,2*np.pi,300)
b.plot(np.cos(t),np.sin(t),color="#274e82",lw=2)
for phi in np.linspace(0,2*np.pi,8,endpoint=False):
 p=np.array([np.cos(phi),np.sin(phi)]);q=np.array([np.cos(phi+.14),np.sin(phi+.14)])
 b.annotate("",xy=q,xytext=p,arrowprops={"arrowstyle":"->","color":"#bc5429","lw":1.6})
b.text(0,0,r"$S^1$",ha="center",fontsize=17)
b.text(0,-1.4,"A surrounding physical loop\ncan wind around the vacuum circle.",ha="center",fontsize=9)
b.set(xlim=(-1.6,1.6),ylim=(-1.7,1.5),aspect="equal",title=r"Strings: nontrivial $\pi_1$");b.axis("off")
u=np.linspace(0,2*np.pi,20);v=np.linspace(0,np.pi,12)
xx=np.outer(np.cos(u),np.sin(v));yy=np.outer(np.sin(u),np.sin(v));zz=np.outer(np.ones_like(u),np.cos(v))
c.plot_wireframe(xx,yy,zz,color="#274e82",alpha=.6,lw=.5)
c.text(0,0,0,r"$S^2$",fontsize=15)
c.set_title(r"Monopoles: nontrivial $\pi_2$",fontsize=12)
c.set_box_aspect((1,1,1));c.set_axis_off()
fig.savefig("paper-1-defect-topology.png",dpi=150,facecolor="white")
