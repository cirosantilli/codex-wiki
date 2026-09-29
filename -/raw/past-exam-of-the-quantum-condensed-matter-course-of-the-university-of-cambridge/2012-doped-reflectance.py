"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

# A dimensionless model: no effective mass or experimental curve is fitted.
lambda_over_ref=np.linspace(.25,2.8,2200);omega=1/lambda_over_ref;epsb=15.;gamma=.015
fig,ax=plt.subplots(figsize=(7.5,4),layout="constrained")
for density,color in zip([.5,1,2],['#2563eb','#059669','#dc2626']):
 wp=np.sqrt((epsb-1)*density);eps=epsb-wp*wp/(omega*(omega+1j*gamma));N=np.sqrt(eps);R=np.abs((N-1)/(N+1))**2
 ax.plot(lambda_over_ref,R,label=rf"$n_c/n_{{\rm ref}}={density:g}$",color=color)
ax.axhline(((np.sqrt(epsb)-1)/(np.sqrt(epsb)+1))**2,color="#777",ls="--",lw=.8,label="Bound-electron background")
ax.set(xlabel=r"$\lambda/\lambda_{\min,\rm ref}$",ylabel="Power reflectance R",ylim=(0,1),xlim=(.25,2.8),title=r"Original illustrative carrier model: $\epsilon_b=15$, weak finite damping");ax.legend();ax.grid(alpha=.15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
