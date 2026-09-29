"""Original explanatory calculation. Save the PNG basename in the working directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False})
def finish(fig,name):
    fig.savefig(name+".png",dpi=150,bbox_inches="tight",facecolor="white")
    plt.close(fig)

r=np.linspace(6,25,600)
fig,axs=plt.subplots(1,2,figsize=(10,3.6),layout="constrained")
for angle,color in [(0,"#009e73"),(45,"#d55e00"),(90,"#0072b2")]:
 base=(1-3/r)**(-.5);beta=1/np.sqrt(r-2);s=np.sin(np.deg2rad(angle))
 axs[0].plot(r,base*(1+beta*s),color=color,label=rf"$i={angle}^\circ$, receding")
 if angle:axs[0].plot(r,base*(1-beta*s),"--",color=color)
axs[0].set(xlabel=r"$r/r_g$",ylabel=r"$1+z=E_0/E_\infty$",title="Direct-projection circular-ring model")
axs[0].legend(fontsize=8)
axs[0].text(12,.84,"Dashed: approaching edge",fontsize=9)
i=np.linspace(0,90,300);z=np.sqrt(2)*(1+.5*np.sin(np.deg2rad(i)))
axs[1].plot(i,z,color="#0072b2")
axs[1].axhline(3/np.sqrt(2),ls=":",color="#999999")
axs[1].set(xlabel="Inclination (degrees)",ylabel=r"Receding $1+z$ at ISCO",title=r"$r_{\rm ISCO}=6r_g,\quad v=c/2$")
axs[1].text(5,2.05,r"Edge-on envelope: $3/\sqrt{2}$",fontsize=10)
finish(fig,"paper-1-disc-redshift")
