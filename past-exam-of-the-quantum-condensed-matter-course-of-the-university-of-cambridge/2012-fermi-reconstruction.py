"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

a=1.3;b=.8;K=np.pi/a;L=np.pi/b;kf=np.sqrt(4*np.pi/(a*b));C=.0380998211097;v=.093117443543
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4),layout="constrained")
t=np.linspace(0,2*np.pi,900)
for shift in (-2*K,0,2*K):
 ax.plot(shift+kf*np.cos(t),kf*np.sin(t),color="#9ca3af" if shift else "#2563eb",lw=1.3)
ax.set_title("Free circles and their reciprocal translates")
x=np.linspace(-3*K,3*K,4001);s=(x+K)%(2*K)-K;d=K-np.abs(s);D=kf*kf-K*K;z=np.sqrt(4*K*K*d*d+(v/C)**2)
yminus=np.sqrt(D-d*d+z);yplus2=D-d*d-z;yplus=np.sqrt(np.maximum(yplus2,0));yplus[yplus2<0]=np.nan
for sign in (-1,1):
 bx.plot(x,sign*yminus,color="#2563eb",lw=2,label="Open first-band sheets" if sign==1 else None)

qm=np.sqrt(kf*kf+K*K-np.sqrt(4*kf*kf*K*K+(v/C)**2))
theta=np.linspace(0,2*np.pi,1201);q=qm*np.cos(theta)
y=np.sqrt(np.maximum(D-q*q-np.sqrt(4*K*K*q*q+(v/C)**2),0))*np.sign(np.sin(theta))
y[0]=y[-1]=0
for centre in (-3*K,-K,K,3*K):
 bx.plot(centre+q,y,color="#dc2626",lw=2,label="Closed second-band pockets" if centre==K else None)
 bx.fill(centre+q,y,color="#fecaca",alpha=.6)
bx.set_title(r"Two-wave reconstruction, $|V_G|\simeq0.093$ eV");bx.legend(loc="upper center",fontsize=8)
for a in (ax,bx):
 a.add_patch(Rectangle((-K,-L),2*K,2*L,facecolor="#dbeafe",edgecolor="black",lw=1,alpha=.25,zorder=0));a.axvline(-K,color="black",ls=":",lw=.8);a.axvline(K,color="black",ls=":",lw=.8)
 a.set(xlim=(-3*K,3*K),ylim=(-4.25,4.25),xlabel=r"$k_x$ (nm$^{-1}$)",ylabel=r"$k_y$ (nm$^{-1}$)");a.set_aspect("equal");a.grid(alpha=.12)
fig.suptitle("Central first Brillouin zone shaded; repeated pockets represent one pocket per cell")

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
