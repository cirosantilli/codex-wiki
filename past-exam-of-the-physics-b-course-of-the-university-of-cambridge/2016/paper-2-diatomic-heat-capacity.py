"""Original explanatory figure; Python 3.14 and root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white"})

t=np.geomspace(.025,2000,1200);J=np.arange(0,301,dtype=float);ener=J*(J+1);W=(2*J[:,None]+1)*np.exp(-ener[:,None]/t[None,:]);Z=W.sum(axis=0);mean=(W*ener[:,None]).sum(axis=0)/Z;var=(W*ener[:,None]**2).sum(axis=0)/Z-mean**2;crot=var/t**2
x=50/t;ev=np.exp(-x);cvib=x*x*ev/(-np.expm1(-x))**2;total=1.5+crot+cvib
fig,ax=plt.subplots(figsize=(7.4,4.3),layout="constrained");ax.semilogx(t,total,color="#1565c0",lw=2.3,label="Translation + quantum rotation + vibration")
for v,label in [(1.5,r"$3/2$"),(2.5,r"$5/2$"),(3.5,r"$7/2$")]:ax.axhline(v,color="#bbb",ls=":",lw=1)
ax.set(xlabel=r"Temperature / rotational temperature $\Theta_r$",ylabel=r"Molar $C_V/R$",ylim=(1.3,3.7),xlim=(t[0],t[-1]),yticks=[1.5,2.5,3.5],yticklabels=[r"$3/2$",r"$5/2$",r"$7/2$"],title=r"Ideal diatomic model: $\Theta_v/\Theta_r=50$")
ax.annotate("Rotational activation",(1,total[np.argmin(abs(t-1))]),xytext=(.09,3.0),arrowprops={"arrowstyle":"->"},fontsize=9);ax.annotate("Vibrational activation",(30,total[np.argmin(abs(t-30))]),xytext=(8,3.55),arrowprops={"arrowstyle":"->"},fontsize=9)
ax.text(.04,1.38,"Fixed intact molecules; no condensation, dissociation or nuclear-spin statistics.",fontsize=8);ax.grid(alpha=.16,which="both")

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
