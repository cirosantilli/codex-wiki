from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,ax=plt.subplots(1,2,figsize=(9.5,3.7),layout="constrained",gridspec_kw={"width_ratios":[1.4,1]})
wavelength=np.linspace(380,720,681)
for mu,sd,label,col in [(440,35,"Short-wave toy filter","#6b3790"),(540,45,"Middle-wave toy filter","#267347"),(570,45,"Long-wave toy filter","#b25b13")]:
 ax[0].plot(wavelength,np.exp(-.5*((wavelength-mu)/sd)**2),label=label,color=col,lw=2)
ax[0].set(xlabel="Wavelength (nm)",ylabel="Normalized toy sensitivity",title="Broad, overlapping filters; not human data",ylim=(0,1.08));ax[0].legend(fontsize=8);ax[0].grid(alpha=.15)
B=np.array([[1,1,0],[1,-1,0],[-.5,-.5,1.]])
ax[1].imshow(B,cmap="RdBu_r",vmin=-1,vmax=1,aspect="equal")
ax[1].set(xticks=[0,1,2],xticklabels=["L contrast","M contrast","S contrast"],yticks=[0,1,2],yticklabels=["y₀","y₁","y₂"],title="Illustrative opponent transform")
for i in range(3):
 for j in range(3):ax[1].text(j,i,f"{B[i,j]:g}",ha="center",va="center",color="white" if abs(B[i,j])>.75 else "black",fontsize=14)
ax[1].set_xlabel("Linear weights: invertible, determinant −2")
fig.savefig(Path.cwd()/"2022-cone-comparisons.png",dpi=110,transparent=False)
