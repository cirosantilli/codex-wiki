"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained');k=np.linspace(-1,1,501);g=np.arange(-4,5);bands=[]
for q in k:
 H=np.diag((q+2*g)**2)+np.diag(np.full(8,-.18),1)+np.diag(np.full(8,-.18),-1);bands.append(np.linalg.eigvalsh(H)[:2])
bands=np.array(bands)
for j in range(2):axs[0].plot(k,bands[:,j],label=f'Band {j+1}')
axs[0].set(xlabel=r'$ka/\pi$',ylabel=r'$E/[\hbar^2\pi^2/(2ma^2)]$',title='Weak periodic potential opens a zone-edge gap');axs[0].legend(fontsize=8)
x=np.linspace(-1,2,600);axs[1].plot(x,np.cos(np.pi*x),label='Cosine: lower for this potential');axs[1].plot(x,np.sin(np.pi*x),label='Sine: upper for this potential')
for n in [-1,0,1,2]:axs[1].axvline(n,color='0.7',ls=':',lw=.8)
axs[1].set(xlabel=r'$x/a$',ylabel=r'$\psi\sqrt{L/2}$',title=r'Standing waves at $k=\pi/a$');axs[1].legend(fontsize=8,loc='lower right')
for a in axs:a.grid(alpha=.13)
fig.suptitle(r'Original model with $V_G<0$: potential minima at integer $x/a$')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
