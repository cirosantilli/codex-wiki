from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,ax=plt.subplots(1,2,figsize=(9.3,3.6),layout="constrained")
x=np.linspace(-7,9,1200);var1,var2=4.,9.;mu1,mu2=0.,3.
w=var2/(var1+var2);v=var1*var2/(var1+var2);m=w*mu1+(1-w)*mu2
pdf=lambda z,mu,var:np.exp(-(z-mu)**2/(2*var))/np.sqrt(2*np.pi*var)
for mu,var,label,color in [(mu1,var1,"Cue 1: mean 0, SD 2","#00549f"),(mu2,var2,"Cue 2: mean 3, SD 3","#ba5d00"),(m,v,"Combined: mean 0.92, SD 1.66","#80378b")]:
 ax[0].plot(x,pdf(x,mu,var),label=label,color=color,lw=2)
ax[0].set(xlabel="Common position coordinate (arbitrary units)",ylabel="Normalized likelihood / posterior density",title="Independent Gaussian cue example");ax[0].legend(fontsize=8)
s1=np.linspace(.3,7,400);weight=9/(s1*s1+9)
ax[1].plot(s1,weight,color="#00549f",lw=2,label="Weight on cue 1")
ax[1].plot(s1,1-weight,color="#ba5d00",lw=2,label="Weight on cue 2")
ax[1].axvline(3,color="gray",ls=":");ax[1].axhline(.5,color="gray",ls=":")
ax[1].set(xlabel="Cue 1 standard deviation (cue 2 SD = 3)",ylabel="Minimum-variance weight",title="Uncertainty changes the weighting",ylim=(0,1));ax[1].legend(fontsize=8)
for a in ax:a.grid(alpha=.18)
fig.savefig(Path.cwd()/"2022-cue-integration.png",dpi=110,transparent=False)
