"""Original solution figure for the 2019 Natural Sciences IA Physics paper.

Writes its PNG basename to cwd. Dependencies: numpy and matplotlib, already
specified in the repository pyproject.toml. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145,facecolor="white")
    plt.close(fig)


def arrow(ax,a,b,colour="#333333",**kwargs):
    ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"-|>","lw":1.6,"color":colour,**kwargs})


def main():
    fig,axes=plt.subplots(1,2,figsize=(8.6,4.1))
    ax=axes[0]
    ax.plot([-1.4,1.4],[0,0],lw=4,color="#777777")
    arrow(ax,(0,-.5),(0,1.6),"#555555")
    arrow(ax,(0,0),(.95,1.4),"#245e87")
    ax.text(.09,1.65,r"$+\hat{\mathbf{n}}$",fontsize=13)
    ax.text(.95,1.58,r"$\mathbf{B}(0)$",fontsize=13,color="#245e87")
    ax.add_patch(Arc((0,0),1.4,1.4,theta1=np.degrees(np.arctan2(1.4,.95)),theta2=90,color="#555555"))
    ax.text(.27,.9,r"$\theta$",fontsize=13)
    ax.text(0,-.36,"loop plane (edge view)",ha="center",fontsize=10)
    ax.set_title("Initial field orientation",fontsize=12)
    ax.set(xlim=(-1.8,1.8),ylim=(-1.6,2),aspect="equal");ax.axis("off")
    ax=axes[1]
    ax.add_patch(Circle((0,0),1.1,fill=False,color="#333333",lw=2))
    for angle in [.2,2.3,4.4]:
        start=1.1*np.array([np.cos(angle),np.sin(angle)])
        end=1.1*np.array([np.cos(angle+.45),np.sin(angle+.45)])
        arrow(ax,start,end,"#a54a37",connectionstyle="arc3,rad=.12")
    ax.text(0,.08,r"$\odot\ +\hat{\mathbf{n}}$",ha="center",fontsize=14)
    ax.text(0,-.35,r"$B_{\rm induced}$ toward viewer",ha="center",fontsize=10,color="#a54a37")
    ax.text(0,-1.5,"Current is counterclockwise\nviewed from the positive-normal side",ha="center",fontsize=10,color="#a54a37")
    ax.set_title(r"At $\omega t=\pi/2$: $B_{\rm ext}=0$, $dB_n/dt<0$",fontsize=11)
    ax.set(xlim=(-1.8,1.8),ylim=(-1.9,1.8),aspect="equal");ax.axis("off")
    fig.suptitle(r"Convention shown: $\cos\theta>0$; the current preserves the initial normal flux",fontsize=12)
    fig.tight_layout(rect=(0,.01,1,.92));save(fig)

if __name__=="__main__":main()
