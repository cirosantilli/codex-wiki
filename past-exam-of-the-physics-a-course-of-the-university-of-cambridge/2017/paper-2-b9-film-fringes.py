"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
fig,ax=plt.subplots(1,2,figsize=(9.5,3.6),layout="constrained")
phase=np.linspace(0,4*np.pi,1000)
ax[0].plot(phase/np.pi,.0234+.009*np.cos(phase),color="#1565a8",lw=1.8)
ax[0].axhline(.0234,color=".5",ls=":",lw=1)
ax[0].set(xlabel=r"Relative phase $\delta/\pi$",ylabel=r"$I_r/I_{\rm inc}$",title="Specified two-beam amplitudes")
n=1.2;lam=500e-9;theta=np.deg2rad(10);spacing=np.deg2rad(.4)
d=lam*np.sqrt(n*n-np.sin(theta)**2)/(2*np.sin(theta)*np.cos(theta)*spacing)
angle=np.linspace(8.8,11.2,2500);r=np.deg2rad(angle)
p=4*np.pi*d/lam*np.sqrt(n*n-np.sin(r)**2)
ax[1].plot(angle,.0234+.009*np.cos(p),color="#ca6720",lw=1.5)
ax[1].axvline(10,color=".6",ls=":",lw=1)
ax[1].set(xlabel="Incidence angle in air (degrees)",ylabel=r"$I_r/I_{\rm inc}$",title="d ≈ 0.249 mm; local fringe spacing ≈ 0.4°")
for a in ax:a.set_ylim(.013,.034);a.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
