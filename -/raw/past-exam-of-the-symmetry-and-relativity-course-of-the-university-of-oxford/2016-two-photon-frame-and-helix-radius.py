"""Original kinematic plots; Python 3.14, numpy/matplotlib. Writes only one current-directory PNG."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

theta=np.linspace(0,np.pi,600)
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout="constrained")
axs[0].plot(theta*180/np.pi,np.cos(theta/2),lw=2,color="#165b91")
axs[0].plot(0,1,"o",mfc="white",mec="#165b91",ms=8,zorder=3,clip_on=False)
axs[0].annotate("Parallel endpoint: no rest frame",xy=(0,1),xytext=(32,.78),arrowprops={"arrowstyle":"->","color":"gray"},fontsize=9)
axs[0].set(xlabel="Photon opening angle (degrees)",ylabel="Center-of-momentum speed / c",title="Equal photon energies",xlim=(0,180),ylim=(0,1.05),xticks=[0,45,90,135,180])
z=np.linspace(0,1,300);axs[1].plot(z,np.ones_like(z),lw=2,color="#bf5a13")
axs[1].set(xlabel="Longitudinal distance z (m)",ylabel="Larmor radius / initial radius",title="Longitudinal electric deceleration",ylim=(.7,1.3),xlim=(0,1))
axs[1].text(.5,1.12,"Transverse momentum stays constant",ha="center",fontsize=10)
axs[1].text(.5,.83,"Longitudinal momentum reaches zero at 1 m",ha="center",fontsize=9)
for ax in axs:ax.grid(alpha=.2)
save(fig)
