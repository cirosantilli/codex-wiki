"""Original solution illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; writes the PNG basename to cwd.
Dependencies are recorded in the repository's pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
BLUE="#245d85";ORANGE="#b9651a";GREEN="#267c5a";GREY="#606975"
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=155,bbox_inches="tight",facecolor="white")
    plt.close(fig)
def arrow(ax,a,b,color=BLUE,scale=15,lw=2):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=scale,lw=lw,color=color))

def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4.1),gridspec_kw={"width_ratios":[1.6,1]})
    ax=axes[0];ax.plot([0,3.2],[0,0],color=GREY,lw=4)
    ax.plot(0,0,"o",ms=10,color="#222222");ax.plot([3.2,3.2],[-.45,.45],lw=7,color="#aaaaaa")
    ax.text(0,-.3,"pivot",ha="center");ax.text(3.2,-.68,"disk (edge seen from above)",ha="center",fontsize=10)
    arrow(ax,(3.1,.18),(1.35,.18),BLUE);ax.text(2.2,.37,r"$\mathbf{L}=-I\omega\,\hat{\mathbf{x}}$",color=BLUE,ha="center")
    arrow(ax,(0,.08),(0,1.2),ORANGE);ax.text(.12,1.08,r"$\boldsymbol{\tau}=mgl\,\hat{\mathbf{y}}$",color=ORANGE)
    arrow(ax,(2.9,-1.02),(3.7,-1.02),GREY);ax.text(3.82,-1.02,r"$+x$",va="center")
    arrow(ax,(-.7,.55),(-.7,1.1),GREY);ax.text(-.7,1.22,r"$+y$",ha="center")
    ang=np.linspace(150,-100,100)*np.pi/180
    ax.plot(.6*np.cos(ang),-.45+.6*np.sin(ang),color=GREEN,lw=1.5)
    arrow(ax,(.6*np.cos(ang[-4]),-.45+.6*np.sin(ang[-4])),(.6*np.cos(ang[-1]),-.45+.6*np.sin(ang[-1])),GREEN,lw=1.5)
    ax.text(.0,-1.25,r"Clockwise precession: $\boldsymbol{\Omega}\parallel -z$",ha="center",color=GREEN,fontsize=10)
    ax.text(3.15,.93,r"$\otimes\;\mathbf{F}_g=-mg\,\hat{\mathbf{z}}$",ha="center",fontsize=11)
    ax.text(2.5,1.35,r"$+z$ points toward the viewer",ha="center",fontsize=10)
    ax.set(xlim=(-1.1,4.3),ylim=(-1.55,1.65));ax.set_aspect("equal");ax.axis("off");ax.set_title("Instantaneous top view",pad=12)
    ax=axes[1];ax.add_patch(Circle((0,0),.85,facecolor="#eef3f6",edgecolor=GREY,lw=2))
    ax.text(0,0,r"$\otimes\;\mathbf{L}$",ha="center",va="center",fontsize=22,color=BLUE)
    theta=np.linspace(150,-105,100)*np.pi/180
    ax.plot(1.12*np.cos(theta),1.12*np.sin(theta),color=BLUE,lw=2)
    arrow(ax,(1.12*np.cos(theta[-4]),1.12*np.sin(theta[-4])),(1.12*np.cos(theta[-1]),1.12*np.sin(theta[-1])),BLUE,lw=2)
    ax.text(0,-1.45,"Clockwise spin",ha="center",color=BLUE)
    ax.text(0,1.43,"Look from outer face toward pivot",ha="center",fontsize=10)
    ax.set(xlim=(-1.65,1.65),ylim=(-1.8,1.8));ax.set_aspect("equal");ax.axis("off");ax.set_title("Disk face view",pad=12)
    fig.tight_layout(w_pad=2);save(fig)
if __name__=="__main__":main()
