"""Original explanatory figure. Render with the repository Makefile into mirrored _media."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(10,3.6),layout="constrained")
x=np.geomspace(.2,5,400)
alpha=(x+1)/(2*np.sqrt(x))
beta=(x-1)/(2*np.sqrt(x))
axs[0].plot(x,alpha,label=r"$u=\alpha$",color="#0072b2")
axs[0].plot(x,-beta,label=r"$v=-\beta$ (inverse vacuum map)",color="#d55e00")
axs[0].axvline(1,ls=":",color="#999999")
axs[0].set(xscale="log",xlabel=r"Frequency ratio $\Omega/\omega$",ylabel="Real matching coefficient",title=r"$u^2-v^2=1$")
axs[0].legend(fontsize=9)
n=np.arange(7)
for i,ratio in enumerate([1,2,5]):
    r=((1-ratio)/(1+ratio))**2
    probability=(1-r)*r**n
    axs[1].bar(n+(i-1)*.23,probability,width=.23,label=rf"$\Omega/\omega={ratio}$")
axs[1].set(xlabel="Pair count n",ylabel=r"$P(n)=(1-r)r^n$",title="One distinct particle-antiparticle mode pair",xticks=n)
axs[1].legend(fontsize=9)
finish(fig,"paper-1-pair-creation")
