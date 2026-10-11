"""Original explanatory figure; run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,3,figsize=(11,3.3),layout='constrained');u=np.linspace(.001,1.7,1200);zeta=.05
D=(1-u*u)**2+(2*zeta*u)**2
axs[0].plot(u,1/np.sqrt(D));axs[0].set(xlabel=r'$\omega/\omega_0$',ylabel='Normalized displacement amplitude')
axs[1].plot(u,180-np.degrees(np.arctan2(2*zeta*u,1-u*u)));axs[1].set(xlabel=r'$\omega/\omega_0$',ylabel='Electron displacement phase / degrees')
for a in axs[:2]:a.axvspan(.2247,.4495,color='tab:blue',alpha=.15,label='400–800 nm');a.axvline(1,color='0.6',ls=':');a.grid(alpha=.2)
axs[0].legend(fontsize=8)
lam=np.linspace(400,800,400);omega0=np.sqrt(100/9.1093837e-31);u=2*np.pi*299792458/(lam*1e-9*omega0);I=u**4/((1-u*u)**2+(2*zeta*u)**2)
axs[2].plot(lam,I/I[-1],label='Bound-charge model');axs[2].plot(lam,(800/lam)**4,'--',label='Rayleigh limit');axs[2].set(xlabel='Wavelength / nm',ylabel='Intensity relative to 800 nm');axs[2].legend(fontsize=8);axs[2].grid(alpha=.2)
fig.suptitle(r'Illustrative damping $\gamma/\omega_0=0.05$; the question does not specify damping')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
