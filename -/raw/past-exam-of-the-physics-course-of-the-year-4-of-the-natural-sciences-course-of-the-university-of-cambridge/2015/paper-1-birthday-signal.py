"""Original exact Earth-frame birthday-signal spacetime geometry."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ta=5/24;tb=5/3;t=np.linspace(0,1.8,501)
fig,ax=plt.subplots(figsize=(8.2,6.2),dpi=100,facecolor="white")
ax.plot(.6*t,t,lw=2.4,color="#a65035",label=r"Alice: $x/c=3t/5$")
ax.plot(-.8*t,t,lw=2.4,color="#2b6089",label=r"Bob: $x/c=-4t/5$")
ax.axvline(0,color="0.6",lw=1,label="Earth")
light_t=np.linspace(ta,tb,100);ax.plot(1.6*ta-light_t,light_t,color="#307f52",lw=2.5,label="Birthday light signal")
ax.scatter([.6*ta,-.8*tb],[ta,tb],s=32,color="#307f52",zorder=5)
ax.annotate(r"Emission: $\tau_A=1/6$ year",xy=(.6*ta,ta),xytext=(.35,.58),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.annotate(r"Reception: $\tau_B=1$ year",xy=(-.8*tb,tb),xytext=(-1.13,1.38),arrowprops={"arrowstyle":"->"},fontsize=11)
ax.set(xlabel=r"Earth-frame position $x$ (light-years)",ylabel="Earth-frame time (years)",xlim=(-1.7,1.45),ylim=(0,1.9),title="Emission and reception use different proper times")
ax.set_aspect("equal",adjustable="box");ax.grid(alpha=.2);ax.legend(loc="upper right",fontsize=9.5)
fig.subplots_adjust(left=.12,right=.98,top=.9,bottom=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
