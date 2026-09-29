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

from matplotlib.patches import Rectangle

def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4));rng=np.random.default_rng(201702)
    ax=axes[0]
    for x0 in [.8,3.1,5.4]:
        t=np.linspace(0,1,600)
        x=x0+.42*np.sin(4*np.pi*t)*np.sin(np.pi*t)+.18*np.sin(15*np.pi*t)*np.sin(np.pi*t)
        y=.7*(1-np.cos(np.pi*t))+.27*(1+np.sin(12*np.pi*t))*np.sin(np.pi*t)
        ax.plot(x,y,color=BLUE,lw=1.4);ax.plot(x0,0,"o",color=ORANGE,ms=5)
    ax.text(3.1,2.5,r"$D\gg R$: isolated coils",ha="center",color=BLUE)
    ax.annotate("",xy=(.8,-.35),xytext=(3.1,-.35),arrowprops={"arrowstyle":"<->","color":GREY});ax.text(1.95,-.65,r"$D$",ha="center")
    ax.set_title("Mushroom regime")
    ax=axes[1];t=np.linspace(0,1,300)
    for j,x0 in enumerate(np.linspace(.25,5.9,17)):
        x=x0+.10*np.sin(9*np.pi*t+j*.9)*np.sin(np.pi*t)
        y=(2.3+.12*np.sin(j))*t
        ax.plot(x,y,color=BLUE,lw=1.1);ax.plot(x0,0,"o",color=ORANGE,ms=3)
    ax.annotate("",xy=(6.5,0),xytext=(6.5,2.4),arrowprops={"arrowstyle":"<->","color":GREY});ax.text(6.7,1.2,r"$H$",va="center")
    ax.text(3.1,2.8,r"$D<R$: stretching relieves crowding",ha="center",color=BLUE,fontsize=10)
    ax.set_title("Brush regime")
    for ax in axes:
        ax.plot([0,6.9],[0,0],color=GREY,lw=3);ax.fill_between([0,6.9],[-.12,-.12],[0,0],color="#eeeeee")
        ax.set(xlim=(-.1,7.2),ylim=(-.8,3.15));ax.axis("off")
    fig.tight_layout(w_pad=1);save(fig)
if __name__=="__main__":main()
