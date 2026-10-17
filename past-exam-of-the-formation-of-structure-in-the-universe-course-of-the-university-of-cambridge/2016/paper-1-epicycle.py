"""Original explanatory calculation. Save only the PNG basename to the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

phi=np.linspace(0,2*np.pi,500)
omega=1.;kappa=np.sqrt(2)*omega
x=np.cos(phi)
y=-2*omega/kappa*np.sin(phi)
fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout="constrained")
axs[0].plot(phi/(2*np.pi),x,color="#0072b2")
axs[0].set(xlabel=r"$\kappa t/(2\pi)$",ylabel=r"$x/A$",title=r"Stable radial oscillation: $\ddot{x}+\kappa^2x=0$")
axs[1].plot(x,y,color="#d55e00")
axs[1].plot(0,0,"+",color="black",ms=10)
axs[1].annotate("",xy=(x[45],y[45]),xytext=(x[15],y[15]),arrowprops={"arrowstyle":"->","color":"#d55e00"})
axs[1].set(xlabel=r"Radial offset $x/A$",ylabel=r"Azimuthal offset $y/A$",title=r"Guiding-centre frame, flat curve: $\kappa=\sqrt{2}\Omega$",aspect="equal")
finish(fig,"paper-1-epicycle")
