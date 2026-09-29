"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig,ax=plt.subplots(2,2,figsize=(10,6),layout="constrained")
idx=np.arange(-2,10)
ax[0,0].vlines(idx,0,1,color=".75",lw=1.3)
ax[0,0].vlines(np.arange(8),0,1,color="#1565a8",lw=2)
ax[0,0].plot([-2,-.5,-.5,7.5,7.5,10],[0,0,1.2,1.2,0,0],color="#ca6720",lw=1.4)
ax[0,0].set(xlim=(-2,9),ylim=(-.05,1.4),xlabel="Position x/D",ylabel="Slit weights",title="Real space: finite window × an infinite comb")
def array(u,N):
 den=np.sin(np.pi*u);val=np.ones_like(u)
 mask=abs(den)>1e-10
 val[mask]=(np.sin(N*np.pi*u[mask])/(N*den[mask]))**2
 return val
u=np.linspace(-2.3,2.3,22001)
ax[0,1].plot(u,array(u,8),color="#1565a8",lw=1.1)
ax[0,1].set(xlim=(-2.3,2.3),ylim=(0,1.1),xlabel=r"$qD/(2\pi)$",ylabel="Relative intensity",title="Eight narrow slits: broadened reciprocal peaks")
v=np.linspace(-.26,.26,2000)
for N,col in [(8,"#1565a8"),(20,"#ca6720")]:ax[1,0].plot(v,array(v,N),color=col,lw=1.6,label=f"N = {N}")
ax[1,0].set(xlabel="Distance from a principal order",ylabel="Relative intensity",title="First-zero width shrinks as 1/N")
ax[1,0].legend(frameon=False)
env=np.sinc(u/2)**2
ax[1,1].plot(u,array(u,20)*env,color="#1565a8",lw=1.2)
ax[1,1].plot(u,env,color="#ca6720",ls="--",lw=1.2)
for order in [-2,2]:
 ax[1,1].axvline(order,color=".5",ls=":",lw=1)
 ax[1,1].text(order,.2,"missing\norder",ha="center",fontsize=8)
ax[1,1].set(xlim=(-2.3,2.3),ylim=(0,1.1),xlabel=r"$qD/(2\pi)$",ylabel="Relative intensity",title="Width a = D/2: envelope zeros remove ±2 orders")
for a in ax.flat:a.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
