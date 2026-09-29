"""Original geometry; Python 3.14 with numpy/matplotlib. Writes exactly one PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

def msd(t,D,Dr,omega,v=1):
    z=Dr-1j*omega
    return 4*D*t+2*v*v*np.real(t/z+np.expm1(-z*t)/(z*z))
fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout="constrained")
t=np.geomspace(.003,250,1100);D=.02;Dr=.1
for omega,color in [(0,"#165b91"),(1,"#bf5a13"),(4,"#488523")]:
    axs[0].loglog(t,msd(t,D,Dr,omega),label=f"omega={omega}",color=color,lw=1.8)
axs[0].loglog(t,4*D*t,"k--",alpha=.65,label="translational: 4Dt")
axs[0].loglog(t[t<1],t[t<1]**2,"k:",label="ballistic: v squared t squared")
axs[0].set(xlabel="Time",ylabel="Mean-square displacement",title="D=0.02, rotational diffusion=0.1, speed=1")
axs[0].legend(fontsize=9);axs[0].grid(alpha=.2,which="both")
w=np.linspace(0,3,500)
for dr,color in [(.1,"#165b91"),(.5,"#bf5a13"),(1.5,"#488523")]:
    axs[1].plot(w,D+dr/(2*(dr*dr+w*w)),label=f"rotational diffusion={dr}",color=color,lw=1.8)
axs[1].axhline(D,color="black",ls="--",label="translational D")
axs[1].set(xlabel="Angular drift magnitude",ylabel="Late-time effective diffusion",title="Rotation suppresses persistent transport")
axs[1].legend(fontsize=9);axs[1].grid(alpha=.2)
save(fig)
