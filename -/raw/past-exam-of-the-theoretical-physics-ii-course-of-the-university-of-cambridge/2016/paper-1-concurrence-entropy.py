"""Original explanatory figure. Render with the repository Makefile into mirrored _media."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

C=np.linspace(0,1,501)
lp=(1+np.sqrt(1-C*C))/2
lm=1-lp
entropy=-(lp*np.log(np.maximum(lp,1e-300))+lm*np.log(np.maximum(lm,1e-300)))
fig,axs=plt.subplots(1,2,figsize=(9.5,3.5),layout="constrained")
axs[0].plot(C,lp,label=r"$\lambda_+$",color="#0072b2")
axs[0].plot(C,lm,label=r"$\lambda_-$",color="#d55e00")
axs[0].set(xlabel=r"Concurrence $\mathcal{C}$",ylabel="Reduced eigenvalue",title="Spectrum from the determinant",ylim=(-.03,1.03))
axs[0].legend()
axs[1].plot(C,entropy,color="#009e73")
axs[1].axhline(np.log(2),ls=":",color="#999999")
axs[1].set(xlabel=r"Concurrence $\mathcal{C}$",ylabel="Entanglement entropy (nats)",title=r"$S=-\lambda_+\ln\lambda_+-\lambda_-\ln\lambda_-$",ylim=(-.02,.74))
axs[1].annotate(r"$\ln 2$",xy=(.1,np.log(2)),xytext=(.1,.6))
finish(fig,"paper-1-concurrence-entropy")
