"""Original explanatory calculation. Save the PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

b=np.linspace(-3,3,500)
root=np.sqrt(b*b+4)
plus=(b+root)/2;minus=(b-root)/2
fig,axs=plt.subplots(1,2,figsize=(10,3.6),layout="constrained")
axs[0].plot(b,plus,color="#0072b2",label=r"$\theta_+$")
axs[0].plot(b,minus,color="#d55e00",label=r"$\theta_-$")
axs[0].plot(b,b,":",color="#999999",label="Unlensed source angle")
axs[0].set(xlabel=r"$\beta/\theta_E$",ylabel=r"$\theta/\theta_E$",title="Two point-mass images")
axs[0].legend()
beta=.7;p=(beta+np.sqrt(beta*beta+4))/2;m=(beta-np.sqrt(beta*beta+4))/2
t=np.linspace(0,2*np.pi,500)
axs[1].plot(np.cos(t),np.sin(t),":",color="#999999",label="Einstein ring scale")
axs[1].plot(0,0,"+",color="black",ms=12,label="Lens centre")
axs[1].plot(beta,0,"x",color="#009e73",ms=8,label=r"Source $\beta=0.7\theta_E$")
axs[1].plot(p,0,"o",color="#0072b2",ms=9,label="Positive image")
axs[1].plot(m,0,"o",color="#d55e00",ms=6,label="Negative-parity image")
axs[1].set(xlim=(-1.5,2),ylim=(-1.4,1.4),xlabel=r"$\theta_x/\theta_E$",ylabel=r"$\theta_y/\theta_E$",title="Angular locations; source projected for comparison",aspect="equal")
axs[1].legend(fontsize=8,loc="upper center",bbox_to_anchor=(.5,-.2),ncol=2)
finish(fig,"paper-1-point-lens")
