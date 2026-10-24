"""Original descent-contour diagram. Python 3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
b=np.pi/4;R=2.7
r=np.linspace(0,np.sqrt(R),250);ray=np.exp(1j*np.pi/4)*r
s=np.linspace(0,R,250);end=np.sqrt(b*b+1j*s)
fig,ax=plt.subplots(figsize=(7,5),facecolor="white")
ax.plot([0,b],[0,0],lw=3,color=".35",label="original interval")
ax.plot(ray.real,ray.imag,color="#2166ac",lw=2,label="stationary-end descent")
ax.plot(end.real,end.imag,color="#b2182b",lw=2,label="upper-end descent")
ax.plot([ray[-1].real,end[-1].real],[ray[-1].imag,end[-1].imag],color=".5",ls="--")
for z1,z2,col in [(ray[90],ray[130],"#2166ac"),(end[100],end[60],"#b2182b")]:
 ax.annotate("",(z2.real,z2.imag),(z1.real,z1.imag),arrowprops=dict(arrowstyle="->",color=col,lw=2))
ax.text(.16,.63,r"$t=e^{i\pi/4}r$",color="#2166ac",fontsize=12,rotation=45)
ax.text(.9,.42,r"$t=\sqrt{b^2+is}$",color="#b2182b",fontsize=12,rotation=55)
ax.scatter([0,b,np.pi/2],[0,0,0],color=[".2",".2","#b2182b"],zorder=5)
ax.annotate(r"$b=\pi/4$",(b,0),(.64,-.2),fontsize=11)
ax.annotate("first tan pole",(np.pi/2,0),(1.27,-.21),fontsize=10)
ax.text(.45,1.33,r"$e^{ixt^2}=e^{ix\operatorname{Re}(t^2)}e^{-xR}$",fontsize=11)
ax.set(xlim=(-.1,1.72),ylim=(-.28,1.55),xlabel=r"$\operatorname{Re}t$",
       ylabel=r"$\operatorname{Im}t$",title="Two endpoint contributions of a quadratic phase")
ax.set_aspect("equal");ax.spines[["top","right"]].set_visible(False)
ax.text(.10,.06,"original interval",fontsize=10,color=".3")
fig.tight_layout();fig.savefig("2008-quadratic-descent.png",dpi=150,facecolor="white")
