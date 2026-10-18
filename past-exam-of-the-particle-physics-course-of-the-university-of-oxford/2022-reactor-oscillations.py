from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
def panel(ax):
    ax.set(xlim=(0,10), ylim=(0,6), aspect="equal")
    ax.axis("off")
def text(ax,x,y,s,**kw):
    ax.text(x,y,s,ha="center",va="center",**kw)
def fermion(ax,a,b,color="black",reverse=False):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=1.7)
    u,v=(b,a) if reverse else (a,b)
    ax.add_patch(FancyArrowPatch(u+.43*(v-u),u+.63*(v-u),arrowstyle="-|>",mutation_scale=12,color=color,lw=1.5))
def wave(ax,a,b,color="#5b4890",gluon=False):
    a,b=np.array(a,dtype=float),np.array(b,dtype=float)
    t=np.linspace(0,1,350); d=b-a; n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    z=a[:,None]+d[:,None]*t+n[:,None]*(.10*np.sin(2*np.pi*7*t))
    if gluon:z+=d[:,None]/np.linalg.norm(d)*(.07*np.sin(2*np.pi*14*t))
    ax.plot(z[0],z[1],color=color,lw=1.4)
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False)
    plt.close(fig)

L=np.linspace(0,150,9001);k=1266.932679419849;E=3
c12=np.cos(np.deg2rad(30));s12=np.sin(np.deg2rad(30))
c13=np.cos(np.deg2rad(9));s13=np.sin(np.deg2rad(9))
a=k*8e-5*L/E;b=k*3e-3*L/E
slow=4*c13**4*c12**2*s12**2
fast=4*c13**2*s13**2
approx=1-slow*np.sin(a)**2-fast*np.sin(b)**2
average=1-slow*np.sin(a)**2-fast/2
exact=1-slow*np.sin(a)**2-fast*(c12**2*np.sin(a+b)**2+s12**2*np.sin(b)**2)
fig,axs=plt.subplots(2,1,figsize=(10.5,6.4),sharex=True)
axs[0].plot(L,approx,color="#255b9e",lw=1,label="Merged fast frequencies (exam approximation)")
axs[0].plot(L,average,color="#cf681d",lw=2,label="Fast oscillations averaged")
axs[1].plot(L,approx,color="#b9c2cf",lw=.9,label="Exam approximation")
axs[1].plot(L,exact,color="#287754",lw=1,label="Consistent three-frequency result")
for ax in axs:
    ax.set(xlim=(0,150),ylim=(.12,1.035),ylabel=r"Survival probability $P_{ee}$")
    ax.grid(alpha=.22);ax.legend(loc="lower left",fontsize=9,framealpha=.95)
axs[1].set_xlabel("Distance from reactor (km)")
fig.suptitle(r"Monoenergetic reactor beam: $E=3$ MeV, $\theta_{12}=30^\circ$, $\theta_{13}=9^\circ$")
fig.tight_layout();save(fig)
