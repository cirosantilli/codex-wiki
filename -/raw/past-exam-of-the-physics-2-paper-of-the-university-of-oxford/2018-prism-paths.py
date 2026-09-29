"""Original solution illustration; output the matching PNG into the cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})

fig,axes=plt.subplots(1,2,figsize=(11.5,5.1),layout="constrained")
n=1.5;alpha=np.pi/3;entry=np.array([.35,.35*np.sqrt(3)])
for ax,degrees in zip(axes,[15,45]):
    theta=np.deg2rad(degrees);r=np.arcsin(np.sin(theta)/n)
    di=np.array([np.cos(-np.pi/6-theta),np.sin(-np.pi/6-theta)])
    inside=np.array([np.cos(-np.pi/6-r),np.sin(-np.pi/6-r)])
    B=entry-entry[1]/inside[1]*inside
    ax.add_patch(patches.Polygon([[0,0],[2,0],[1,np.sqrt(3)]],closed=True,facecolor="#e9f1f4",edgecolor="#495965",lw=1.5))
    start=entry-.8*di;ax.annotate("",xy=entry,xytext=start,arrowprops={"arrowstyle":"->","lw":1.8,"color":"#a22c48"})
    ax.plot([entry[0],B[0]],[entry[1],B[1]],color="#a22c48",lw=2)
    if n*np.sin(alpha-r)>1:
        refl=inside*np.array([1,-1]);time=(2*np.sqrt(3)-np.sqrt(3)*B[0]-B[1])/(np.sqrt(3)*refl[0]+refl[1]);C=B+time*refl
        dout=np.array([np.cos(np.pi/6+theta),np.sin(np.pi/6+theta)])
        ax.plot([B[0],C[0]],[B[1],C[1]],color="#286d88",lw=2)
        ax.annotate("",xy=C+.65*dout,xytext=C,arrowprops={"arrowstyle":"->","lw":2,"color":"#286d88"})
        ax.text(.1,-.77,"B: total internal reflection\nC: exit at the original external angle",fontsize=10)
    else:
        e=np.arcsin(n*np.sin(alpha-r));dout=np.array([np.cos(-np.pi/2+e),np.sin(-np.pi/2+e)])
        ax.annotate("",xy=B+.7*dout,xytext=B,arrowprops={"arrowstyle":"->","lw":2,"color":"#b76b2d"})
        ax.text(.1,-.77,"B: transmitted principal ray\nPartial reflected rays omitted",fontsize=10)
    normal=np.array([np.cos(-np.pi/6),np.sin(-np.pi/6)])
    ax.plot([*(entry-.3*normal)[0:1],*(entry+.3*normal)[0:1]],[(entry-.3*normal)[1],(entry+.3*normal)[1]],"--",color="#888888",lw=1)
    ax.text(.05,.95,"A");ax.text(1,-.12,"B",ha="center");ax.text(1.8,.95,"C")
    ax.set(title=rf"$n=1.5,\quad\theta={degrees}^\circ$",xlim=(-.45,2.65),ylim=(-1.02,2.05));ax.set_aspect("equal");ax.axis("off")
fig.suptitle("Two routes selected by the incidence angle at the base",fontsize=14)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
