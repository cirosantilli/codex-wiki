"""Original solution illustration. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; this script writes only its PNG basename there.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})

x=np.linspace(-400,0,200);y=np.linspace(0,1000,250)
X,Y=np.meshgrid(x,y);eta=np.exp(X/100)*np.cos(2*np.pi*(Y-150)/800)
fig,axes=plt.subplots(1,2,figsize=(8.4,5.3),sharey=True,layout="constrained")
for ax,sign,name in zip(axes,[1,-1],["Northern hemisphere","Southern hemisphere"]):
 im=ax.contourf(X,Y,eta,levels=np.linspace(-1,1,17),cmap="RdBu_r",vmin=-1,vmax=1)
 ax.axvspan(0,105,color="#ddd8cb")
 ax.axvline(0,color="black",lw=1.5)
 qx=np.array([-300,-200,-100,-25]);qy=np.arange(80,1000,120)
 QX,QY=np.meshgrid(qx,qy);v=sign*np.exp(QX/100)*np.cos(2*np.pi*(QY-150)/800)
 ax.quiver(QX,QY,np.zeros_like(v),v,angles="uv",scale_units="inches",scale=1.8,width=.007,color="#162c3d",pivot="mid")
 ax.annotate("",(50,800 if sign>0 else 200),xytext=(50,200 if sign>0 else 800),arrowprops={"arrowstyle":"->","lw":3,"color":"#226a49"})
 ax.text(65,500,"Poleward propagation",rotation=90,ha="center",va="center",fontsize=9,color="#226a49")
 ax.text(-215,960,"Ocean",ha="center",color="#172d4b")
 ax.text(50,960,"Land",ha="center")
 ax.set(xlim=(-400,105),ylim=(0,1000),xlabel="Eastward distance (km)",title=name)
 ax.set_xticks([-400,-200,0])
axes[0].set_ylabel("Northward distance along coast (km)")
fig.colorbar(im,ax=axes,location="bottom",shrink=.85,pad=.06,label=r"Normalized layer-thickness anomaly $(h-h_0)/\eta_0$")
fig.suptitle(r"Eastern-boundary Kelvin wave: $L_d=100$ km, $c=2.53$ m/s",fontsize=12)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            dpi=120, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
plt.close(fig)
