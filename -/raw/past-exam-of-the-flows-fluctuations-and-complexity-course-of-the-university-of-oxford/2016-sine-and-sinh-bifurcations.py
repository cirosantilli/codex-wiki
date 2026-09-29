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

BLUE="#165b91";ORANGE="#bf5a13"
fig,axs=plt.subplots(1,3,figsize=(12,4.2),layout="constrained")
for ax in axs[:2]:
    for n in range(7):
        x=np.linspace(2*n*np.pi+1e-5,(2*n+1)*np.pi-1e-5,1000);r=np.sin(x)/x;stable=r-np.cos(x)<0
        for sign in (1,-1):
            ax.plot(np.where(stable,r,np.nan),sign*x,color=BLUE,lw=1.5)
            ax.plot(np.where(~stable,r,np.nan),sign*x,color=ORANGE,lw=1.4,ls="--")
    ax.plot([0,1],[0,0],color=BLUE,lw=1.6);ax.plot([1,2],[0,0],color=ORANGE,lw=1.6,ls="--");ax.plot(1,0,"o",color="black",ms=4)
axs[0].set(xlabel="r",ylabel="Real equilibrium x",title="Real axis: subcritical pitchfork",xlim=(0,2),ylim=(-11,11))
axs[1].set(xlabel="r",ylabel="Real equilibrium x",title="Small-r saddle-node sequence",xlim=(0,.16),ylim=(-23,23))
y=np.linspace(1e-6,2.4,800);r=np.sinh(y)/y
for sign in (1,-1):axs[2].plot(r,sign*y,color=BLUE,lw=1.7)
axs[2].plot([0,1],[0,0],color=BLUE,lw=1.7);axs[2].plot([1,2],[0,0],color=ORANGE,lw=1.5,ls="--");axs[2].plot(1,0,"o",color="black",ms=4)
axs[2].set(xlabel="r",ylabel="Imaginary-axis coordinate y",title="Imaginary axis: supercritical pitchfork",xlim=(0,2),ylim=(-2.4,2.4))
for ax in axs:ax.grid(alpha=.2)
fig.supxlabel("Solid blue attracts; dashed orange repels. Points at mergers are nonhyperbolic.",fontsize=10)
save(fig)
