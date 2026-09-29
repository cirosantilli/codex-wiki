"""Original Oxford CP2 2013 figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

y=np.linspace(-.3,.3,12001);D=.5;d=1e-5;delta=d*y/np.sqrt(D*D+y*y)
s1=1/525e-9;s2=1/500e-9;vis=np.cos(np.pi*(s2-s1)*delta)
intensity=.5*(np.cos(np.pi*s1*delta)**2+np.cos(np.pi*s2*delta)**2)
fig,ax=plt.subplots(figsize=(9.2,4.2),layout="constrained")
ax.plot(y*100,intensity,lw=1.8,color="#146b9c",label="Sum of the two colours")
ax.plot(y*100,.5*(1+abs(vis)),lw=1.5,ls="--",color="#d76c20",label="Visibility envelopes")
ax.plot(y*100,.5*(1-abs(vis)),lw=1.5,ls="--",color="#d76c20")
ax.set(xlim=(-30,30),ylim=(-.04,1.07),xlabel="Screen position (cm)",ylabel=r"$I/(8J)$",title="500 nm + 525 nm: equal intensities, 21 local maxima")
ax.legend(loc="upper right");ax.grid(alpha=.17)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original CP2 solution figure"})
plt.close(fig)
