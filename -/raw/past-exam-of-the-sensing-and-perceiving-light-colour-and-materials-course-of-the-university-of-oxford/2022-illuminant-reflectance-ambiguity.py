from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,ax=plt.subplots(1,3,figsize=(10.2,3.3),layout="constrained")
x=np.linspace(380,720,681);E1=np.ones_like(x);E2=.8+.4*(x-380)/340;R1=.35+.05*np.cos(2*np.pi*(x-380)/340);R2=R1/E2
assert np.all((R1>=0)&(R1<=1)&(R2>=0)&(R2<=1));assert np.max(np.abs(E1*R1-E2*R2))<1e-14
for arr,label,col,style in [(E1,"Illuminant 1","#00549f","-"),(E2,"Illuminant 2","#b25b13","--")]:ax[0].plot(x,arr,label=label,color=col,lw=2,ls=style)
for arr,label,col,style in [(R1,"Reflectance 1","#00549f","-"),(R2,"Reflectance 2","#b25b13","--")]:ax[1].plot(x,arr,label=label,color=col,lw=2,ls=style)
ax[2].plot(x,E1*R1,label="Pair 1 outgoing spectrum",color="#00549f",lw=3);ax[2].plot(x,E2*R2,label="Pair 2: exact overlap",color="#b25b13",lw=1.6,ls="--")
ax[0].set(title="Different illumination",ylabel="Relative photon input",ylim=(.65,1.3))
ax[1].set(title="Different admissible reflectance",ylabel="Reflectance fraction",ylim=(0,.6))
ax[2].set(title="Identical product E × R",ylabel="Relative outgoing photons",ylim=(0,.6))
for a in ax:a.set_xlabel("Wavelength (nm)");a.set_xticks([400,500,600,700]);a.legend(fontsize=7.5,loc="lower left");a.grid(alpha=.15)
fig.savefig(Path.cwd()/"2022-illuminant-reflectance-ambiguity.png",dpi=110,transparent=False)
