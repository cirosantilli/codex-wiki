"""Original Gauss-law gravity profile for an infinite uniform cylinder."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,1001);g=np.where(x<=1,x,1/np.maximum(x,1e-9))
fig,ax=plt.subplots(figsize=(8.6,4.9),dpi=100,facecolor="white")
ax.plot(x,g,lw=2.6,color="#2a6189");ax.axvline(1,color="0.4",ls="--",lw=1)
ax.annotate("Cylinder surface",xy=(1,1),xytext=(1.7,.92),arrowprops={"arrowstyle":"->"},fontsize=12)
ax.text(.36,.43,r"$|g|\propto r$",rotation=48,fontsize=13);ax.text(2.7,.49,r"$|g|\propto1/r$",fontsize=13)
ax.set(xlabel=r"Radius $r/R$",ylabel=r"Inward field magnitude $|g_r|/(2\pi G\rho R)$",xlim=(0,5),ylim=(0,1.15),title="Cylindrical gravity is linear inside and inverse-radius outside")
ax.grid(alpha=.2);fig.subplots_adjust(left=.11,right=.98,top=.88,bottom=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
