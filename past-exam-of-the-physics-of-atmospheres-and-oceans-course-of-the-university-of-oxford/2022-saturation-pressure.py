"""Original solution illustration. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; this script writes only its PNG basename there.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})

T_star, T_c = 273.15, 647.0
L_s, L_star, R = 2.84e6, 2.49e6, 462.0
cold = np.linspace(170, T_star, 250)
warm = np.linspace(T_star, T_c, 450)
y_cold = L_s/R * (1/cold-1/T_star)
y_variable = L_star/(R*(T_c-T_star)) * (T_c*(1/warm-1/T_star)+np.log(warm/T_star))
y_fixed = L_star/R*(1/warm-1/T_star)
fig, ax = plt.subplots(figsize=(7.6,4.6), layout="constrained")
ax.plot(cold,y_cold,color="#3b5b92",lw=2,label="Common ice–vapour branch")
ax.plot(warm,y_variable,color="#c04d20",lw=2.4,label="Temperature-dependent latent heat")
ax.plot(warm,y_fixed,color="#278367",lw=2,ls="--",label="Fixed vaporization latent heat")
ax.axhline(0,color="0.75",lw=.8)
ax.axvline(T_star,color="0.65",lw=.8,ls=":")
ax.axvline(T_c,color="0.65",lw=.8,ls=":")
ax.scatter([T_star],[0],color="black",s=25,zorder=4)
ax.annotate("Triple point",(T_star,0),xytext=(290,4),arrowprops={"arrowstyle":"->"})
ax.annotate("Horizontal limiting tangent\n(model extrapolation)",(T_c,y_variable[-1]),
            xytext=(408,-1.5),arrowprops={"arrowstyle":"->"})
ax.set(xlim=(170,665),ylim=(-13,16),xlabel="Temperature T (K)",ylabel=r"$-\ln(p/p_*)$",
       title="Saturation pressure from integrated latent heat")
ax.legend(loc="upper right",fontsize=9,frameon=False)
ax.grid(alpha=.15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
            dpi=120, facecolor="white", transparent=False,
            metadata={"Software": "Matplotlib"})
plt.close(fig)
