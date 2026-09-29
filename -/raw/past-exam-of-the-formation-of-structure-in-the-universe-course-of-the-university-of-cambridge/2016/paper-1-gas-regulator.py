"""Original explanatory calculation. Save only the PNG basename to the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

x=np.linspace(0,1,401)
fig,axs=plt.subplots(1,2,figsize=(9,3.4),layout="constrained")
axs[0].plot(x,1-x,color="#0072b2",lw=2)
axs[0].set(xlabel=r"$M_s/M_{s,\max}$",ylabel=r"$\epsilon M_g^{\rm eq}/\Phi$",title="Instantaneous gas-balance nullcline")
for ratio,color in [(.2,"#0072b2"),(1,"#d55e00"),(3,"#009e73")]:
 f=ratio*(1-x)/(ratio*(1-x)+x)
 axs[1].plot(x,f,label=rf"$A/\epsilon={ratio:g}$",color=color)
axs[1].set(xlabel=r"$M_s/M_{s,\max}$",ylabel=r"$f_{\rm gas}$",title="Gas fractions on the nullcline")
axs[1].legend()
fig.suptitle("A nullcline is not a constant-gas evolutionary trajectory",fontsize=11)
finish(fig,"paper-1-gas-regulator")
