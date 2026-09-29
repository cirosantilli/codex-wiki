"""Wave directions and velocity polarization; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    epsilon=.15
    khat=np.array([1.,epsilon])/np.sqrt(1+epsilon**2)
    ghat=np.array([-epsilon,1.])/np.sqrt(1+epsilon**2)
    fig,axes=plt.subplots(1,2,figsize=(9.2,4.5),dpi=100,facecolor="white")
    left,right=axes
    left.axhline(0,color="#aaaaaa",lw=.8);left.axvline(0,color="#aaaaaa",lw=.8)
    for vec,color in [(khat,"#b44728"),(ghat,"#1263a0")]:
        left.annotate("",xy=vec,xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2.8})
    left.text(.28,.24,r"$\mathbf{k}$ and phase velocity",color="#b44728",fontsize=10)
    left.text(-.15,1.12,"Group velocity",ha="center",color="#1263a0",fontsize=10)
    left.plot([0,0],[0,1.02],"--",color="#777777",lw=1)
    left.text(.25,.82,"Rotation axis",rotation=0,color="#777777",fontsize=9)
    # A small square records the right angle between the two normalized directions.
    q=.12
    corner=np.array([q*khat,q*(khat+ghat),q*ghat])
    left.plot(corner[:,0],corner[:,1],color="#555555",lw=.9)
    left.set(xlim=(-1.25,1.4),ylim=(-1.2,1.35),xlabel="Horizontal direction x",ylabel="Vertical direction z",
             title=r"Directions for $k_\parallel/k_\perp=0.15$")
    left.set_aspect("equal");left.set_xticks([-1,0,1]);left.set_yticks([-1,0,1])
    theta=np.linspace(0,2*np.pi,501)
    right.plot(np.cos(theta),np.sin(theta),color="#27806a",lw=2.2)
    # At fixed position, positive frequency gives phase -omega*t and clockwise motion.
    angles=np.linspace(0,-.6,80)
    right.plot(np.cos(angles),np.sin(angles),color="#27806a",lw=2.5)
    right.annotate("",xy=(np.cos(-.6),np.sin(-.6)),xytext=(np.cos(-.45),np.sin(-.45)),
                   arrowprops={"arrowstyle":"->","color":"#27806a","lw":2.5})
    right.plot(1,0,"ko",ms=4)
    right.text(.73,-.85,"Increasing time",ha="center",fontsize=10,color="#27806a")
    right.axhline(0,color="#aaaaaa",lw=.8);right.axvline(0,color="#aaaaaa",lw=.8)
    right.set(xlim=(-1.35,1.35),ylim=(-1.35,1.35),xlabel=r"$u_{e_1}/A$ (transverse horizontal)",
              ylabel=r"$u_{e_2}/A$ (nearly vertical)",title=r"Circular polarization, $\omega>0$")
    right.set_aspect("equal");right.set_xticks([-1,0,1]);right.set_yticks([-1,0,1])
    fig.text(.5,.015,"Left arrows are directions, not relative speeds. Right axes are an orthonormal plane perpendicular to k.",
             ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.07,1,1),w_pad=2)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white",transparent=False,metadata={"Software":"Codex Wiki"})
    plt.close(fig)

if __name__=="__main__":main()
