"""Original explanatory figure; run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained');t=np.linspace(0,12,900)
for g in [.2,1,2]:
 if g<1:w=np.sqrt(1-g*g);z=1-np.exp(-g*t)*(np.cos(w*t)+g/w*np.sin(w*t))
 elif g==1:z=1-(1+t)*np.exp(-t)
 else:w=np.sqrt(g*g-1);z=1-np.exp(-g*t)*(np.cosh(w*t)+g/w*np.sinh(w*t))
 axs[0].plot(t,z,label=rf'$\gamma/\omega_0={g:g}$')
for u in [0,.8,1,1.6]:axs[1].plot(t,1+(-1+(u-1)*t)*np.exp(-t),label=rf'$v_0/(\omega_0z_{{eq}})={u:g}$')
for a in axs:a.axhline(1,color='0.6',ls=':');a.set(xlabel=r'$\omega_0t$',ylabel=r'$z/z_{eq}$');a.grid(alpha=.2);a.legend(fontsize=8)
axs[0].set_title('Initially at rest');axs[1].set_title('Critical damping with downward impact')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
