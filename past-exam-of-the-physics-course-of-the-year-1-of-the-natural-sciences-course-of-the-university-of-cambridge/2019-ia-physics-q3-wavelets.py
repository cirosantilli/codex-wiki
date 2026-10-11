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
    fig,ax=plt.subplots(figsize=(8.2,5))
    A=np.array([0.,0.]);C=np.array([4.,0.]);s1=.7;s2=.45
    B=C-2.8*np.array([s1,-np.sqrt(1-s1*s1)])
    D=np.array([1.8*s2,-1.8*np.sqrt(1-s2*s2)])
    ax.axhline(0,color="#555555",lw=1.7)
    ax.plot([A[0],B[0]],[A[1],B[1]],color="#245e87",lw=2.4)
    ax.plot([D[0],C[0]],[D[1],C[1]],color="#2c7a5c",lw=2.4)
    angles=np.linspace(-np.pi,0,220)
    ax.plot(1.8*np.cos(angles),1.8*np.sin(angles),color="#a4cbbb",ls="--",lw=1.4)
    arrow(ax,B,C,"#245e87");arrow(ax,A,D,"#2c7a5c")
    incoming=-1.7*np.array([s1,-np.sqrt(1-s1*s1)])
    arrow(ax,incoming,A,"#245e87")
    ax.plot([0,0],[-2.05,1.9],color="#999999",ls=":",lw=1)
    for p,label,offset in [(A,"A",(-.26,.13)),(B,"B",(.06,.16)),(C,"C",(.08,.13)),(D,"D",(.1,-.17))]:
        ax.plot(*p,"o",color="#333333",ms=4)
        ax.text(p[0]+offset[0],p[1]+offset[1],label,fontsize=12)
    ax.text(.4,1.25,"incident wavefront AB",color="#245e87",fontsize=10,rotation=44)
    ax.text(2.0,-1.25,"refracted wavefront CD",color="#2c7a5c",fontsize=10,rotation=26.7)
    ax.text(3.0,1.2,r"$BC=v_1\Delta t$",color="#245e87",fontsize=12)
    ax.text(.55,-.9,r"$AD=v_2\Delta t$",color="#2c7a5c",fontsize=12)
    ax.text(-1.85,1.9,r"medium 1: $v_1=c/n_1$",fontsize=11)
    ax.text(-1.85,-2.45,r"medium 2: $v_2=c/n_2$",fontsize=11)
    ax.add_patch(Arc((0,0),1.3,1.3,theta1=90,theta2=90+np.degrees(np.arcsin(s1)),color="#245e87"))
    ax.text(-.43,.72,r"$\theta_1$",fontsize=12)
    ax.add_patch(Arc((0,0),1.15,1.15,theta1=270,theta2=270+np.degrees(np.arcsin(s2)),color="#2c7a5c"))
    ax.text(.05,-.73,r"$\theta_2$",fontsize=12)
    ax.set(xlim=(-2.2,4.8),ylim=(-2.7,2.7),aspect="equal",title="Secondary wavelet and its tangent refracted wavefront")
    ax.axis("off");fig.tight_layout();save(fig)

if __name__=="__main__":main()
