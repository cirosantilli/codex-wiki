from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

from matplotlib.patches import Rectangle
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,5),layout="constrained",gridspec_kw={"width_ratios":[1.15,1]})
ax.add_patch(Rectangle((-1.2,0),2.4,.95,color="#e4f1fa",zorder=0))
ax.axhline(0,color="#4e7d9c",ls="--",lw=1.4)
for x in [-.95,-.05,.85]:
 for y in [.62,.85]:ax.text(x,y,"×",color="#497d9f",ha="center",va="center")
ax.plot([-.5,.5,.5,-.5,-.5],[.35,.35,-.65,-.65,.35],color="#202c38",lw=3)
def arrow(x,y,dx,dy,col):ax.annotate("",xy=(x+dx,y+dy),xytext=(x,y),arrowprops={"arrowstyle":"-|>","color":col,"lw":2.4,"mutation_scale":15})
current="#d16b10";force="#794a9b"
arrow(-.18,.35,.35,0,current);arrow(.5,-.16,0,-.24,current);arrow(.18,-.65,-.35,0,current);arrow(-.5,-.4,0,.24,current)
arrow(0,.39,0,.37,force);ax.text(.07,.69,r"$IaB$",color=force)
arrow(.54,.18,.39,0,force);arrow(-.54,.18,-.39,0,force)
ax.text(.79,.27,r"$IBh$",ha="center",color=force);ax.text(-.79,.27,r"$IBh$",ha="center",color=force)
arrow(0,-.1,0,-.35,"#b73239");ax.text(.07,-.3,r"$Mg$",color="#b73239")
ax.text(.68,-.62,"No magnetic\nforce below",ha="left",fontsize=10)
ax.text(-1.1,-.93,"Orange: clockwise current\nPurple: magnetic forces",fontsize=11)
ax.set(xlim=(-1.2,1.36),ylim=(-1.03,1),aspect="equal",title="Straddling the field boundary");ax.axis("off")
t=np.linspace(0,1.6,200);bx.plot(t,t,color=force,lw=2.5,label=r"Magnetic drag: $F_B/Mg=v/v_s$")
bx.axhline(1,color="#b73239",lw=2,label="Weight / Mg = 1");bx.plot(1,1,"o",color="#202c38");bx.axvline(1,ls=":",color="gray")
bx.annotate(r"$v_s=0.0239$ m/s",xy=(1,1),xytext=(.35,1.35),arrowprops={"arrowstyle":"->"})
bx.set(xlabel=r"Speed $v/v_s$",ylabel=r"Force magnitude / $Mg$",xlim=(0,1.6),ylim=(0,1.65),title="Steady fall: drag balances weight");bx.legend(loc="lower right",fontsize=9);bx.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
