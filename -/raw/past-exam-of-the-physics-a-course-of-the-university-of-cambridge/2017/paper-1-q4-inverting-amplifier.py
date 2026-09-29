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

from matplotlib.patches import Polygon, Rectangle

def resistor(ax,x1,x2,y,label):
    ax.add_patch(Rectangle((x1,y-.14),x2-x1,.28,facecolor="white",edgecolor=GREY,lw=1.8))
    ax.text((x1+x2)/2,y+.27,label,ha="center",va="bottom")
def main():
    fig,ax=plt.subplots(figsize=(8.5,4.8))
    ax.add_patch(Polygon([(3.2,-1.4),(3.2,1.4),(5.5,0)],closed=True,facecolor="#edf3f6",edgecolor=BLUE,lw=2))
    ax.text(3.43,.6,"−",ha="center",va="center",fontsize=18);ax.text(3.43,-.6,"+",ha="center",va="center",fontsize=18)
    ax.text(4.1,0,"ideal\nop amp",ha="center",va="center",color=BLUE)
    ax.plot([.3,.9],[.6,.6],color=GREY,lw=1.8);resistor(ax,.9,2.1,.6,r"$R_{\rm in}=10\,\mathrm{k\Omega}$")
    ax.plot([2.1,3.2],[.6,.6],color=GREY,lw=1.8)
    ax.plot([2.7,2.7,3.4],[.6,2.3,2.3],color=GREY,lw=1.8);resistor(ax,3.4,4.8,2.3,r"$R_f=100\,\mathrm{k\Omega}$")
    ax.plot([4.8,6.2,6.2],[2.3,2.3,0],color=GREY,lw=1.8);ax.plot([5.5,7],[0,0],color=GREY,lw=1.8)
    ax.plot([3.2,2.7,2.7],[-.6,-.6,-1.65],color=GREY,lw=1.8)
    for dy,width in [(0,.32),(-.12,.22),(-.24,.12)]:ax.plot([2.7-width,2.7+width],[-1.65+dy]*2,color=GREY,lw=1.5)
    ax.plot([2.7,6.2],[.6,0],"o",color=GREY,ms=5)
    ax.plot(.3,.6,"o",mfc="white",mec=GREY,ms=6);ax.plot(7,0,"o",mfc="white",mec=GREY,ms=6)
    ax.text(.08,.6,r"$V_i$",ha="right",va="center");ax.text(7.17,0,r"$V_o$",ha="left",va="center")
    ax.text(1.25,-.28,r"$V_-\simeq0$",ha="center",color=GREEN)
    ax.annotate("virtual ground",xy=(2.7,.6),xytext=(.75,-.8),arrowprops={"arrowstyle":"->","color":GREEN},color=GREEN,fontsize=10)
    ax.text(5.25,-1.72,r"$V_o/V_i=-10$",ha="center",color=BLUE,fontsize=13)
    ax.set(xlim=(-.3,7.8),ylim=(-2.15,3.0));ax.axis("off");ax.set_title("One ideal operational amplifier and two resistors",pad=12)
    fig.tight_layout();save(fig)
if __name__=="__main__":main()
