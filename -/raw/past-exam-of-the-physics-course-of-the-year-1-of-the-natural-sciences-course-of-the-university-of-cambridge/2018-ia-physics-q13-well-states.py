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
    # Units: a=1 and hbar^2/(2m)=1; finite barrier is ten infinite-well ground energies.
    barrier=10*np.pi**2;lo=0.;hi=np.pi
    for _ in range(100):
        k=(lo+hi)/2
        if k*np.tan(k/2)<np.sqrt(barrier-k*k):lo=k
        else:hi=k
    k=(lo+hi)/2;kappa=np.sqrt(barrier-k*k)
    norm=1/np.sqrt(.5+np.sin(k)/(2*k)+np.cos(k/2)**2/kappa)
    x=np.linspace(-.4,1.4,1601);inside=(x>=0)&(x<=1)
    finite=norm*np.cos(k*(x-.5));finite[x<0]=norm*np.cos(k/2)*np.exp(kappa*x[x<0]);finite[x>1]=norm*np.cos(k/2)*np.exp(-kappa*(x[x>1]-1))
    infinite=np.zeros_like(x);infinite[inside]=np.sqrt(2)*np.sin(np.pi*x[inside])
    # Matching and normalization are analytic; verify the independently sampled numerical integral as well.
    assert abs(k*np.tan(k/2)-kappa)<1e-11
    assert abs(np.trapezoid(finite*finite,x)-1)<2e-5
    fig,ax=plt.subplots(figsize=(8.5,4.5));ax.axvspan(-.4,0,color="#eeeeee");ax.axvspan(1,1.4,color="#eeeeee")
    ax.plot(x,infinite,color=BLUE,lw=2,ls="--",label="Infinite barriers")
    ax.plot(x,finite,color=ORANGE,lw=2,label=r"Finite barriers: $V_w=10E_{1,\infty}$")
    for v in [0,1]:ax.axvline(v,color=GREY,lw=1,ls=":")
    ax.text(-.2,1.52,"barrier",ha="center",color=GREY);ax.text(1.2,1.52,"barrier",ha="center",color=GREY)
    ax.text(.5,.15,r"$V=0$",ha="center",color=GREY)
    ax.set(xlim=(-.4,1.4),ylim=(0,1.65),xlabel=r"Position $x/a$",ylabel=r"Normalized amplitude $\sqrt{a}\,\psi(x)$",title="Ground states with the same well width and interior potential")
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.18),ncol=2,frameon=False);fig.tight_layout();save(fig)
if __name__=="__main__":main()
