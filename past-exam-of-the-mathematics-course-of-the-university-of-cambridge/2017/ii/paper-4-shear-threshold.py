"""Original exam-solution figure; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Writes an opaque PNG with the same basename to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6.2,3.2),dpi=100,facecolor="white")
q=np.linspace(0,8,800);y=np.ones_like(q);np.divide(np.tanh(q),q,out=y,where=q!=0)
ax.plot(q,y,color="#245c88",lw=2,label=r"$\tanh(kh)/(kh)$")
ax.axhline(1,color="#9f522c",ls="--",label="All-wavelength threshold")
ax.set(xlim=(0,8),ylim=(0,1.15),xlabel="kh",ylabel="Normalized required U²",title="Finite-depth Kelvin–Helmholtz threshold")
ax.legend(fontsize=8);ax.grid(alpha=.15)
fig.subplots_adjust(left=.12,right=.98,top=.87,bottom=.19)

fig.savefig(Path.cwd()/(Path(__file__).stem+".png"),facecolor="white",transparent=False)
plt.close(fig)
