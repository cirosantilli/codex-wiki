from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.8,4.7),layout="constrained")
th=np.linspace(0,2*np.pi,900);r=1-np.cos(th);ax.plot(r*np.cos(th),r*np.sin(th),lw=2.5,color="#286b96",label="Cardioid");ax.plot(1.5*np.cos(th),1.5*np.sin(th),lw=2,color="#b46c2b",label="Circle r = 3/2")
u=np.linspace(2*np.pi/3,4*np.pi/3,350);ro=1-np.cos(u);xp=np.r_[ro*np.cos(u),1.5*np.cos(u[::-1])];yp=np.r_[ro*np.sin(u),1.5*np.sin(u[::-1])];ax.fill(xp,yp,color="#abcddd",alpha=.8)
for t in [2*np.pi/3,4*np.pi/3]:ax.plot([0,1.5*np.cos(t)],[0,1.5*np.sin(t)],ls=":",lw=1,color="gray");ax.plot(1.5*np.cos(t),1.5*np.sin(t),"o",color="#324f64")
ax.axhline(0,color="gray",lw=.5);ax.axvline(0,color="gray",lw=.5);ax.set(xlabel="x",ylabel="y",aspect="equal",xlim=(-2.2,1.65),ylim=(-1.65,1.65),title="Selected cap is outside the inner circle");ax.legend(fontsize=10,loc="lower right")
gap=.5*((1-np.cos(u))**2-2.25);bx.plot(u,gap,color="#286b96",lw=2.5);bx.fill_between(u,0,gap,color="#abcddd",alpha=.8);bx.set(xlabel=r"Polar angle $\theta$",ylabel="Area per unit angle",xlim=(2*np.pi/3,4*np.pi/3),ylim=(0,1.02),title=r"Integrate $\frac{1}{2}(r_{\rm outer}^2-r_{\rm inner}^2)$");bx.set_xticks([2*np.pi/3,np.pi,4*np.pi/3],[r"$2\pi/3$",r"$\pi$",r"$4\pi/3$"]);bx.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
