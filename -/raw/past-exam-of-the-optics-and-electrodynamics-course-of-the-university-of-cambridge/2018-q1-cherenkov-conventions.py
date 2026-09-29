"""Original solution figure; tested with Python 3.14.

Uses the NumPy and Matplotlib dependencies in the root pyproject.toml.
Writes the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Arc

def main():
    fig,(photon,front)=plt.subplots(1,2,figsize=(10.8,4.3),layout="constrained")
    alpha=97.5;half=np.deg2rad(alpha/2)
    for ax in (photon,front):
        ax.axhline(0,color="#999999",ls=":",lw=1)
        ax.annotate("",xy=(1.25,-1.2),xytext=(-.1,-1.2),arrowprops={"arrowstyle":"->","color":"#555555"})
        ax.text(.4,-1.5,"Particle velocity",ha="center",fontsize=10)
        ax.plot(0,0,"o",color="#333333")
        ax.set_aspect("equal");ax.axis("off")
    for sign in (-1,1):
        end=np.array([np.cos(half),sign*np.sin(half)])*2
        photon.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","lw":2,"color":"#0068a0"})
    photon.add_patch(Arc((0,0),1.05,1.05,theta1=-alpha/2,theta2=alpha/2,color="#0068a0"))
    photon.text(.58,.02,"α",fontsize=13,color="#0068a0")
    photon.text(.75,.8,"Photon directions",fontsize=10,color="#0068a0",rotation=35)
    photon.text(-.15,1.55,r"$\theta_C=\alpha/2$"+'\n'+r"$n=1/[\beta\cos(\alpha/2)]=1.52$",fontsize=12)
    photon.set(xlim=(-.4,2.25),ylim=(-1.8,2.15),title="α is the photon-cone opening")
    for sign in (-1,1):
        front.plot([0,-2*np.cos(half)],[0,sign*2*np.sin(half)],color="#b55713",lw=2)
    front.add_patch(Arc((0,0),1.05,1.05,theta1=180-alpha/2,theta2=180+alpha/2,color="#b55713"))
    front.text(-.69,-.04,"α",fontsize=13,color="#b55713")
    start=np.array([-.85,.85*np.tan(half)]);normal=np.array([np.sin(half),np.cos(half)])
    front.annotate("",xy=start+1.3*normal,xytext=start,arrowprops={"arrowstyle":"->","lw":2,"color":"#0068a0"})
    front.text(-.3,1.35,"Photon normal",fontsize=10,color="#0068a0")
    front.text(-1.9,1.9,r"$\theta_C=90^\circ-\alpha/2$"+'\n'+r"$n=1/[\beta\sin(\alpha/2)]=1.33$",fontsize=12)
    front.text(-1.95,-.9,"Wavefront",color="#b55713",fontsize=10,rotation=49)
    front.set(xlim=(-2.2,1.4),ylim=(-1.8,2.55),title="α is the trailing wavefront opening")

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
