from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig=plt.figure(figsize=(10,4.9));ax=fig.add_subplot(121,projection="3d");bx=fig.add_subplot(122,projection="3d")
t=np.linspace(0,1,300);ax.plot(t*t,2*t,t**3,color="#236a9b",lw=2.1,label="Curved path");route=np.array([[0,0,0],[1,0,0],[1,2,0],[1,2,1]]);ax.plot(*route.T,color="#b74c38",lw=2,label="Axis-parallel path");ax.scatter([0,1],[0,2],[0,1],color="#263743",s=25);ax.text(0,0,-.13,"O",fontsize=11);ax.text(.7,1.5,1.15,"(1, 2, 1)",fontsize=10)
ax.set(xlim=(-.05,1.15),ylim=(-.05,2.2),zlim=(-.15,1.25),xlabel="x",ylabel="y",zlabel="z",title="Same endpoint potential difference: 4");ax.legend(loc="upper left",fontsize=9);ax.view_init(elev=22,azim=-59)
polar=np.linspace(0,np.pi/2,32);az=np.linspace(0,2*np.pi,80);pp,tt=np.meshgrid(polar,az);xx=np.sin(pp)*np.cos(tt);yy=np.sin(pp)*np.sin(tt);zz=np.cos(pp)
bx.plot_surface(xx,yy,zz,color="#bad9e8",alpha=.3,edgecolor="none",shade=False);phi=np.linspace(0,2*np.pi,250);bx.plot(np.cos(phi),np.sin(phi),0*phi,color="#b74c38",lw=2)
for angle in [.2,2.2,4.2]:bx.quiver(np.cos(angle),np.sin(angle),0,-.23*np.sin(angle),.23*np.cos(angle),0,color="#b74c38",arrow_length_ratio=.45,linewidth=1.4)
bx.quiver(0,0,.7,0,0,.5,color="#236a9b",arrow_length_ratio=.25,linewidth=2);bx.text(0,0,1.28,r"$\nabla\times\mathbf{A}=\hat{\mathbf{z}}$",fontsize=11,ha="center")
bx.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),zlim=(0,1.5),xlabel="x",ylabel="y",zlabel="z",title=r"Oriented hemisphere: both integrals $\pi$");bx.view_init(elev=24,azim=-55)
for aa in [ax,bx]:
 aa.tick_params(labelsize=9);aa.xaxis.pane.set_facecolor("white");aa.yaxis.pane.set_facecolor("white");aa.zaxis.pane.set_facecolor("white")
fig.subplots_adjust(left=.02,right=.94,bottom=.08,top=.86,wspace=.12)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
