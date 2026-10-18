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

from matplotlib.patches import Circle
x=np.linspace(-3,3,380);z=np.linspace(-3,3,380);X,Z=np.meshgrid(x,z);radius=np.sqrt(X*X+Z*Z);safe=np.maximum(radius,.3)
ux=1.5*Z*X/safe**5;uz=-(1+.5/safe**3-1.5*Z*Z/safe**5);mask=radius<=1.01
ux=np.ma.masked_where(mask,ux);uz=np.ma.masked_where(mask,uz)
fig,axs=plt.subplots(1,2,figsize=(11,4.5),layout="constrained")
axs[0].streamplot(x,z,ux,uz,color="#165b91",density=1.25,linewidth=1,arrowsize=.9)
axs[0].add_patch(Circle((0,0),1,facecolor="white",edgecolor="black",lw=1.5,zorder=5));axs[0].plot([0,0],[-1,1],"o",color="#bf5a13",zorder=6,ms=5)
axs[0].set(xlabel="x / R",ylabel="z / R",title="Sphere rest frame: far velocity -v z-hat",aspect="equal",xlim=(-3,3),ylim=(-3,3))
theta=np.linspace(0,np.pi,500);cp=1-2.25*np.sin(theta)**2
axs[1].plot(theta*180/np.pi,cp,color="#bf5a13",lw=2);axs[1].axhline(0,color="gray",ls="--",alpha=.6)
axs[1].set(xlabel="Polar angle (degrees)",ylabel="(p - p infinity) / (rho v squared / 2)",title="Surface pressure coefficient",xticks=[0,45,90,135,180]);axs[1].grid(alpha=.2)
save(fig)
