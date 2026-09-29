"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(8.5,3.6),layout='constrained')
x=np.linspace(-2,2,400);y=np.linspace(-1.5,1.5,300);X,Y=np.meshgrid(x,y)
phiA=np.exp(-((X+.7)**2+Y**2)/.7);phiB=np.exp(-((X-.7)**2+Y**2)/.7);density=(phiA+phiB)**2
axs[0].contourf(X,Y,density,levels=np.linspace(0,density.max(),20),cmap='Blues');axs[0].scatter([-.7,.7],[0,0],c='tab:red',s=50);axs[0].text(-.7,-.28,'Nucleus',ha='center');axs[0].text(.7,-.28,'Nucleus',ha='center');axs[0].set(title='Shared covalent bonding density',xlim=(-2,2),ylim=(-1.5,1.5));axs[0].set_aspect('equal');axs[0].axis('off')
for i in range(5):
 for j in range(5):
  pos=(i+j)%2==0;axs[1].scatter(i,j,s=330,color='tab:blue' if pos else 'tab:orange');axs[1].text(i,j,'+' if pos else '−',ha='center',va='center',color='white',fontsize=14)
axs[1].set(title='Extended ionic arrangement',xlim=(-.6,4.6),ylim=(-.6,4.6));axs[1].set_aspect('equal');axs[1].axis('off')
fig.suptitle('Original schematic models: density shape and disk sizes are illustrative')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
