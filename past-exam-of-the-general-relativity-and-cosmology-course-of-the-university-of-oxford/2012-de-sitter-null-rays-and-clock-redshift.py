from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.8),layout="constrained")
t=np.linspace(0,3,600);ax.plot(t,np.tanh(t),lw=2.6,color="#286c94",label="Outgoing ray from the centre")
delay=np.arctanh(.5)
for te,col,lab in [(0,"#b96b30","First inward pulse"),(.5,"#8b56a1","Later inward pulse")]:
 q=np.linspace(te,te+delay,180);ax.plot(q,np.tanh(delay-(q-te)),color=col,lw=2.3,label=lab);ax.plot(te+delay,0,"o",color=col)
ax.axhline(1,ls="--",lw=1,color="gray");ax.axhline(.5,ls=":",lw=1,color="gray");ax.text(2.05,.52,"Emitter radius",fontsize=10);ax.text(2.02,1.015,"Horizon",fontsize=10)
ax.set(xlabel=r"Static coordinate time $ct/r_S$",ylabel=r"$r/r_S$",xlim=(0,3),ylim=(-.03,1.08),title="Coordinate light rays; local speed stays c");ax.legend(fontsize=9,loc="upper left");ax.grid(alpha=.12)
u=np.linspace(0,.99,500);ratio=1/np.sqrt(1-u*u);bx.plot(u,ratio,lw=2.6,color="#286c94");bx.plot(.5,2/np.sqrt(3),"o",color="#b96b30");bx.annotate(r"$r_E=r_S/2$: ratio $2/\sqrt{3}$",xy=(.5,2/np.sqrt(3)),xytext=(.07,3.2),arrowprops={"arrowstyle":"->"},fontsize=11)
bx.set(xlabel=r"Static emitter radius $r_E/r_S$",ylabel=r"Received period / emitted proper period",xlim=(0,1),ylim=(.8,7.5),title="Central observer receives a redshift");bx.grid(alpha=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
