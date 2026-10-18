"""Original scientific figure; Python 3.14 with numpy/matplotlib. Writes one PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

def rootH(target):
    if target>=4/27-1e-14:return 1.5
    lo=1e-8;hi=1.5
    for _ in range(75):
        mid=(lo+hi)/2;value=(mid-1)/mid**3
        if value<target:lo=mid
        else:hi=mid
    return (lo+hi)/2
fig,axs=plt.subplots(1,2,figsize=(11,4.3),layout="constrained")
H=np.linspace(.78,3,900);A=(H-1)/H**3
axs[0].plot(H,A,color="#165b91",lw=2);axs[0].plot(1.5,4/27,"o",color="#bf5a13")
axs[0].axhline(4/27,color="#bf5a13",ls="--",label="maximum 4/27");axs[0].axvline(1.5,color="gray",ls=":")
axs[0].set(xlabel="Dimensionless thickness H",ylabel="(H - 1) / H cubed",title="Upward transport turning point",ylim=(-.1,.19));axs[0].legend(fontsize=9)
theta=np.linspace(0,2*np.pi,700)
for alpha,color in [(.03,"#165b91"),(.10,"#488523"),(4/27,"#bf5a13")]:
    profile=np.array([rootH(alpha*np.cos(t)) for t in theta]);axs[1].plot(theta*180/np.pi,profile,color=color,lw=1.7,label=f"alpha={alpha:.5f}")
axs[1].set(xlabel="Angle theta (degrees)",ylabel="H = U h / Q",title="Continuous wall-entrained film branch",xticks=[0,90,180,270,360],ylim=(.85,1.55));axs[1].legend(fontsize=9)
for ax in axs:ax.grid(alpha=.2)
save(fig)
