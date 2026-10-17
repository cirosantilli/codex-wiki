"""Original direct-impact overlap plot for 2020 NE4.
Python 3.14; numpy and matplotlib. PNG output goes to the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
dose=np.linspace(0,5.5,700)
fraction=-np.expm1(-dose)
fig,axes=plt.subplots(1,2,figsize=(10.2,4.1),layout="constrained")
axes[0].plot(dose,fraction,color="#175782",lw=2.5,label="Random overlap: 1 − exp(−dose)")
axes[0].plot(dose[dose<=1],dose[dose<=1],color="#aa6526",ls="--",label="Initial linear approximation")
axes[0].scatter([1,np.log(100)],[1-np.exp(-1),.99],color="#63528d",zorder=5)
axes[0].annotate("At dose 1: 63.2% amorphous",(1,1-np.exp(-1)),xytext=(1.4,.43),arrowprops={"arrowstyle":"->","color":"#63528d"},fontsize=9,color="#63528d")
axes[0].axhline(.99,color="#888888",ls=":",lw=1)
axes[0].set(xlabel="Dimensionless accumulated dose R t Vα",ylabel="Amorphous fraction",ylim=(0,1.04),xlim=(0,5.5),title="Previously damaged regions can be hit again")
axes[0].legend(loc="lower right",fontsize=8)
axes[1].plot(dose,1-fraction,color="#175782",lw=2.5)
axes[1].set_yscale("log")
axes[1].axhline(.01,color="#63528d",ls=":",lw=1)
axes[1].axvline(np.log(100),color="#63528d",ls=":",lw=1)
axes[1].scatter([np.log(100)],[.01],color="#63528d",zorder=5)
axes[1].annotate("1% crystalline at dose ln(100)",(np.log(100),.01),xytext=(.55,.025),arrowprops={"arrowstyle":"->","color":"#63528d"},fontsize=9,color="#63528d")
axes[1].set(xlabel="Dimensionless accumulated dose R t Vα",ylabel="Surviving crystalline fraction",xlim=(0,5.5),title="Zero-hit probability decays exponentially")
for ax in axes:ax.grid(alpha=.23)
fig.savefig(Path.cwd()/"paper-ne4-overlap-model.png",dpi=150,facecolor="white")
plt.close(fig)
