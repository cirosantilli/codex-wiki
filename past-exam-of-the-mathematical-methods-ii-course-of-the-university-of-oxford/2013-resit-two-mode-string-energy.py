from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10.2,4.7),layout="constrained")
x=np.linspace(0,1,500)
for tau,col in [(0,"#286c98"),(.125,"#ba6b27"),(.25,"#80549c"),(.5,"#b74c43")]:
 y=np.sin(2*np.pi*x)*np.cos(2*np.pi*tau)+.5*np.sin(4*np.pi*x)*np.cos(4*np.pi*tau)
 ax.plot(x,y,color=col,lw=2,label=f"vt/L = {tau:g}")
ax.axhline(0,lw=.6,color="gray");ax.set(xlabel="x/L",ylabel="Displacement",xlim=(0,1),title="Released n = 2 and n = 4 harmonics");ax.legend(fontsize=10);ax.grid(alpha=.12)
tau=np.linspace(0,1,700);K=np.sin(2*np.pi*tau)**2+np.sin(4*np.pi*tau)**2;V=2-K
bx.plot(tau,K,color="#b74c43",lw=2,label="Kinetic");bx.plot(tau,V,color="#286c98",lw=2,label="Potential");bx.plot(tau,K+V,color="#555555",lw=2,ls="--",label="Total")
bx.set(xlabel="vt/L",ylabel=r"Energy / $(T\pi^2/L)$",xlim=(0,1),ylim=(-.05,2.15),title="Orthogonal modes conserve total energy");bx.legend(fontsize=10,loc="lower right");bx.grid(alpha=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
