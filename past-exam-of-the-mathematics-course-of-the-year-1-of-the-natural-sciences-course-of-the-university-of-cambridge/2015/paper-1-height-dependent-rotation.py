"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig=plt.figure(figsize=(10,5.4),layout="constrained",facecolor="white")
    gs=fig.add_gridspec(2,2,width_ratios=[1.6,1])
    ax=fig.add_subplot(gs[:,0],projection="3d")
    ax.set_facecolor("white");angle=np.linspace(0,2*np.pi,240)
    for z,color in [(-1.3,"#b84732"),(1.3,"#17648e")]:
        for rho in [.7,1.4]:
            ax.plot(rho*np.cos(angle),rho*np.sin(angle),np.full_like(angle,z),color=color,alpha=.6,lw=1)
            ph=np.linspace(0,2*np.pi,8,endpoint=False)
            xx=rho*np.cos(ph);yy=rho*np.sin(ph)
            ax.quiver(xx,yy,np.full_like(ph,z),-.18*z*yy,.18*z*xx,np.zeros_like(ph),color=color,arrow_length_ratio=.4,linewidth=1.4)
    ax.plot(1.4*np.cos(angle),1.4*np.sin(angle),np.zeros_like(angle),color=".6",ls="--",lw=1)
    ax.plot([0,0],[0,0],[-1.8,1.8],color=".5",lw=1)
    ax.set(xlim=(-1.7,1.7),ylim=(-1.7,1.7),zlim=(-1.8,1.8),xlabel="$x$",ylabel="$y$",zlabel="$z$",title=r"$v_\phi=\alpha z\rho$")
    ax.set_box_aspect((1,1,1));ax.view_init(elev=21,azim=-57)
    for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_pane_color((1,1,1,1))
    ax.text2D(.02,.97,"Middle plane and vertical axis: stationary",transform=ax.transAxes,fontsize=9)
    for row,z,color in [(0,1,"#17648e"),(1,-1,"#b84732")]:
        panel=fig.add_subplot(gs[row,1]);panel.set_facecolor("white")
        for rho in [.55,1.0]:
            panel.plot(rho*np.cos(angle),rho*np.sin(angle),color=color,alpha=.5,lw=1)
            ph=np.linspace(0,2*np.pi,8,endpoint=False);xx=rho*np.cos(ph);yy=rho*np.sin(ph)
            panel.quiver(xx,yy,-z*yy,z*xx,color=color,angles="xy",scale_units="xy",scale=3.2,width=.009)
        panel.scatter([0],[0],s=18,color=".4")
        panel.set(xlim=(-1.4,1.4),ylim=(-1.3,1.3),title="Above: anticlockwise" if z>0 else "Below: clockwise")
        panel.set_aspect("equal");panel.axis("off")
        if row==1:panel.text(0,-1.15,"Both views look down from +z",ha="center",fontsize=9)
    fig.savefig(Path("paper-1-height-dependent-rotation.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
