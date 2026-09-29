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
    fig,axes=plt.subplots(2,1,figsize=(8,6.6))
    ax=axes[0];u=np.linspace(0,7*np.pi,1000);q=.1
    y=-np.exp(-q*u)*(np.cos(u)+q*np.sin(u));env=np.sqrt(1+q*q)*np.exp(-q*u)
    ax.plot(u,y,color="#245e87",lw=1.9)
    for sign in [-1,1]:ax.plot(u,sign*env,color="#b06737",ls="--",lw=1.1)
    ax.axhline(0,color="#999999",lw=.7)
    ax.set(xlabel=r"Phase $\omega_dt$",ylabel=r"$x/|x_0|$",title=r"Illustrative underdamped release from rest ($\beta/\omega_d=0.1$)")
    ax.text(11,.48,r"envelopes $\pm A e^{-\beta t}$",color="#b06737",fontsize=10)
    ax=axes[1];beta=.005;wd=np.sqrt(10-beta*beta);tp=np.pi/wd
    def x(t):return -.26*np.exp(-beta*t)*(np.cos(wd*t)+beta/wd*np.sin(wd*t))
    lo,hi=0,tp
    for _ in range(70):
        mid=(lo+hi)/2
        if x(mid)<.25:lo=mid
        else:hi=mid
    hit=(lo+hi)/2
    before=np.linspace(0,hit,450);after=np.linspace(hit,1.08,150)
    ax.plot(before,x(before),color="#245e87",lw=2,label="motion before contact")
    ax.plot(after,x(after),color="#777777",lw=1.5,ls="--",label="free continuation")
    ax.axhline(.25,color="#a54a37",lw=1.2,label="stop at 0.25 m")
    ax.plot(hit,.25,"o",color="#a54a37")
    ax.annotate(f"first contact: {hit:.3f} s",(hit,.25),xytext=(.35,.12),arrowprops={"arrowstyle":"->","color":"#a54a37"},fontsize=10)
    ax.plot(tp,x(tp),"o",mfc="white",mec="#777777")
    ax.set(xlabel="Time (s)",ylabel="Displacement down slope (m)",title="First swing for the supplied parameters",xlim=(0,1.08),ylim=(-.29,.29))
    ax.legend(fontsize=8,loc="lower right")
    for ax in axes:ax.grid(alpha=.16);ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout(h_pad=2);save(fig)

if __name__=="__main__":main()
