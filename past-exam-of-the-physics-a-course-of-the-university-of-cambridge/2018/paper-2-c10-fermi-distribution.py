"""Original solution figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig,ax=plt.subplots(figsize=(7.7,3.7),layout="constrained")
e=np.linspace(.45,1.55,1200)
ax.plot([.45,1,1,1.55],[1,1,0,0],color="0.15",lw=1.7,label="T = 0")
for t,col in [(.02,"#1565a8"),(.06,"#ca6720"),(.12,"#33865b")]:
    mu=1-np.pi**2*t**2/12
    f=1/(np.exp((e-mu)/t)+1)
    ax.plot(e,f,color=col,lw=1.7,label=f"T/T_F = {t:g}")
ax.axvline(1,color="0.5",ls="--",lw=1)
ax.axhline(.5,color="0.6",ls=":",lw=1)
ax.set(xlabel=r"Energy $\epsilon/E_F$",ylabel=r"Occupation probability $f(\epsilon)$",xlim=(.45,1.55),ylim=(-.04,1.04))
ax.legend(frameon=False)
ax.set_title(r"Fixed N, V; $\mu/E_F\simeq1-\pi^2(T/T_F)^2/12$ at low temperature")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=135)
