"""Original explanatory calculation. Save only the PNG basename to the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(11,4),layout="constrained")
x=np.linspace(.02,1,600)
axs[0].plot(x,1+np.log(1/x),label=r"Escape, $\rho\propto r^{-2}$",color="#0072b2")
axs[0].plot(x,2-x,label=r"Escape, $\rho\propto r^{-1}$",color="#d55e00")
axs[0].plot(x,np.ones_like(x),"--",label=r"Shell allocation, $r^{-2}$",color="#0072b2")
axs[0].plot(x,x,"--",label=r"Shell allocation, $r^{-1}$",color="#d55e00")
axs[0].axhline(1.5,ls=":",color="grey")
axs[0].text(.08,1.58,r"Example $Q/V_0^2=1.5$",fontsize=9)
axs[0].set(xlabel=r"$r/r_0$",ylabel=r"$B(r)/V_0^2$",title=r"Equal total mass and radius: $V_0^2=GM_0/r_0$",ylim=(0,4))
axs[0].legend(fontsize=8)
s=np.linspace(1,4,500)
axs[1].plot(s,np.exp(1-s),color="#0072b2",label=r"Escape $r^{-2}$: inward")
s1=np.linspace(1,2,200)
axs[1].plot(s1,2-s1,color="#d55e00",label=r"Escape $r^{-1}$: inward")
s2=np.linspace(0,1,200)
axs[1].plot(s2,s2,"--",color="#d55e00",label=r"Shell $r^{-1}$: outward")
axs[1].axvline(1,ls=":",color="#0072b2")
axs[1].annotate("Shell inverse-square:\nall radii at this threshold",xy=(1,.62),xytext=(1.85,.78),arrowprops={"arrowstyle":"->"},fontsize=9)
axs[1].set(xlabel=r"$Q(t)/V_0^2=q(e^{\nu t}-1)/V_0^2$",ylabel=r"Front radius / $r_0$",title="Different energy definitions give different fronts",ylim=(0,1.05))
axs[1].legend(fontsize=8,loc="upper right",bbox_to_anchor=(1,.64))
finish(fig,"paper-1-quenching-fronts")
