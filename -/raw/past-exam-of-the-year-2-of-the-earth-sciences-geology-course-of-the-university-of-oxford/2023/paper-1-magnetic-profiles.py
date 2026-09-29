"""Induced dipole total-field shapes; not an inversion of the exam data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x=np.linspace(-5,5,1201)
z=-1.
fig,ax=plt.subplots(figsize=(8.5,4.2),layout="constrained")
for inc,label,col in [(-36,"Southern inclination −36°","#276792"),(36,"Northern inclination +36°","#bd493c")]:
 i=np.deg2rad(inc)
 # N and down components of field and induced moment; receiver is above source.
 dot=np.cos(i)*x+np.sin(i)*z
 anomaly=(3*dot**2/(x*x+z*z)-1)/(x*x+z*z)**1.5
 ax.plot(x,anomaly,label=label,color=col)
ax.axhline(0,color=".5",lw=.8)
ax.axvline(0,color=".6",lw=.8,ls=":")
ax.set(xlabel="South ← along-profile distance / source depth → North",ylabel="Total-field anomaly (arbitrary units)",title="5(e–f): hemispheric reversal mirrors induced-field asymmetry")
ax.legend(fontsize=9)
ax.text(-4.7,.55,"Same induced source and field strength\nOnly inclination changes sign",fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
