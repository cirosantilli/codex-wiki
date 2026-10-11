"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(8,3.3),layout='constrained');w=np.linspace(0,2.6,1300);gamma=.12
chi=1/(1-w*w-1j*gamma*w)
axs[0].plot(w,1+chi.real);axs[0].axhline(1,color='0.6',ls=':');axs[0].axhline(0,color='0.7',lw=.7);axs[0].set(ylabel=r'$\mathrm{Re}\,\epsilon_r$',title='Dispersive real response')
axs[1].plot(w,chi.imag,color='tab:orange');axs[1].set(ylabel=r'$\mathrm{Im}\,\epsilon_r$',title='Positive absorption')
for a in axs:a.axvline(1,color='0.6',ls='--');a.set(xlabel=r'$\omega/\omega_T$',xlim=(0,2.6));a.grid(alpha=.2)
fig.suptitle(r'Illustrative model: $\omega_p=\omega_T$, $\gamma=0.12\omega_T$, convention $e^{-i\omega t}$')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
