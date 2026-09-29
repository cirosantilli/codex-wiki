from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(9.5,4.4));xi=np.linspace(0,1,500)
ax.plot(xi,np.sin(np.pi*xi),color="#236a9b",lw=1.7,label=r"Mode 1: $\sin\pi\xi$");ax.plot(xi,.5*np.sin(2*np.pi*xi),color="#b84e37",lw=1.7,label=r"Mode 2: $\frac{1}{2}\sin2\pi\xi$");ax.plot(xi,np.sin(np.pi*xi)+.5*np.sin(2*np.pi*xi),color="#277c65",lw=2.3,label="Initial sum")
ax.set(xlim=(0,1),xlabel=r"$\xi=x/l$",ylabel="Displacement / A",title="Initial modal decomposition");ax.axhline(0,color="#999999",lw=.7);ax.grid(alpha=.18);ax.legend(fontsize=9,loc="upper right")
for tau,col,style in [(0,"#277c65","-"),(.125,"#236a9b","--"),(.25,"#b84e37","-."),(.5,"#8356a0",":")]:
 y=np.sin(np.pi*xi)*np.cos(2*np.pi*tau)+.5*np.sin(2*np.pi*xi)*np.cos(4*np.pi*tau)
 bx.plot(xi,y,color=col,ls=style,lw=1.8,label=r"$t/T_1="+str(tau)+"$")
bx.set(xlim=(0,1),ylim=(-1.4,1.4),xlabel=r"$x/l$",ylabel="Displacement / A",title="Time evolution of the mode sum");bx.axhline(0,color="#999999",lw=.7);bx.grid(alpha=.18);bx.legend(fontsize=9,loc="lower left");fig.tight_layout()

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=140,facecolor="white",transparent=False)
plt.close(fig)
