"""Original kinematic plots; Python 3.14, numpy/matplotlib. Writes only one current-directory PNG."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

s=np.linspace(0,6,600);gamma=np.sqrt(1+s*s);beta=s/gamma
fig,axs=plt.subplots(1,3,figsize=(12,3.9),layout="constrained")
axs[0].plot(s,gamma,lw=2,color="#165b91",label="sqrt(1 + s squared)");axs[0].plot(s,s,"k--",alpha=.6,label="large-s asymptote")
axs[0].set(xlabel="s = force times t / (mc)",ylabel="Lorentz factor",title="Energy grows without bound",ylim=(0,6.5));axs[0].legend(fontsize=8)
axs[1].plot(s,beta,lw=2,color="#bf5a13");axs[1].axhline(1,color="black",ls="--",alpha=.6)
axs[1].set(xlabel="s = force times t / (mc)",ylabel="Speed / c",title="Speed approaches c",ylim=(0,1.08))
axs[2].plot(gamma-1,s,lw=2,color="#488523",label="accelerated world line");axs[2].plot(s,s,"k--",alpha=.6,label="light from initial event")
axs[2].set(xlabel="Distance / (mc squared / force)",ylabel="ct / (mc squared / force)",title="Constant proper acceleration",xlim=(0,6),ylim=(0,6));axs[2].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
save(fig)
