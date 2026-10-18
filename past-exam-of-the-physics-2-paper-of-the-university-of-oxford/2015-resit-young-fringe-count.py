from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.5,4.4));xi=np.linspace(-2.5,2.5,1000)
ax.plot(xi,np.cos(np.pi*xi)**2,color="#236a9b",lw=1.8,label="Equal optical paths");ax.plot(xi,np.cos(np.pi*(xi+.25))**2,color="#b74d38",lw=1.4,ls="--",label="Quarter-period phase shift");ax.set(xlim=(-2.5,2.5),ylim=(-.04,1.3),xlabel=r"$sz/(\lambda d)$",ylabel=r"$I/I_{\max}$",title="A cell changes the relative slit phase");ax.legend(fontsize=9,loc="upper right");ax.grid(alpha=.13)
u=np.linspace(0,1,4001);I=np.cos(20*np.pi*u)**2;bx.plot(u,I,color="#236a9b",lw=1.25);peaks=np.arange(1,21)/20;bx.scatter(peaks,np.ones(20),s=13,color="#b74d38",zorder=4);bx.scatter([0],[1],s=45,facecolor="white",edgecolor="#263743",zorder=5);bx.text(.5,1.19,"20 new maxima after the initial maximum",ha="center",fontsize=10)
bx.set(xlim=(-.02,1.02),ylim=(-.04,1.32),xlabel="Fraction of the total optical-path change",ylabel=r"$I(0)/I_{\max}$",title="Evacuation produces 20 full periods");bx.grid(alpha=.13);fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
