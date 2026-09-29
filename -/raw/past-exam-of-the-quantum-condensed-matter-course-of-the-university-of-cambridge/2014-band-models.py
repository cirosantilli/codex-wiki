"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.7),layout='constrained');k=np.linspace(-1,1,501);g=np.arange(-4,5);out=[]
for q in k:
 H=np.diag((q+2*g)**2);H+=np.diag(np.full(8,.25),1)+np.diag(np.full(8,.25),-1);out.append(np.linalg.eigvalsh(H)[:3])
out=np.array(out)
for j in range(3):axs[0].plot(k,out[:,j],label=f'Band {j+1}')
axs[0].set(xlabel=r'$ka/\pi$',ylabel='Energy (model units)',title='Nearly-free plane waves: weak periodic coupling',ylim=(-.2,5));axs[0].legend(fontsize=8)
EA=-.7;EB=.7;t1=-.6;t2=-.35;off=t1+t2*np.exp(-1j*np.pi*k);split=np.sqrt((EA-EB)**2/4+abs(off)**2)
axs[1].plot(k,(EA+EB)/2-split,label='Lower');axs[1].plot(k,(EA+EB)/2+split,label='Upper');axs[1].axhline(EA,ls=':',color='0.6',label='Isolated on-site energies');axs[1].axhline(EB,ls=':',color='0.6');axs[1].set(xlabel=r'$ka/\pi$',ylabel='Energy (separate model units)',title='Two-orbital tight binding: hopping splits levels');axs[1].legend(fontsize=8)
for a in axs:a.axvline(-1,color='0.6',ls='--');a.axvline(1,color='0.6',ls='--');a.grid(alpha=.15)
fig.suptitle('Original reduced-zone spectra from two illustrative Hamiltonians')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
