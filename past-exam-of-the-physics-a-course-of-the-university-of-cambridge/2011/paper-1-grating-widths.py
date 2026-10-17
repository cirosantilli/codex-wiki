"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,axs=plt.subplots(2,1,figsize=(8.4,5.3),sharex=True,sharey=True,layout='constrained')
s=np.linspace(-6.1,6.1,55000);N=60
# sin(N*pi*s)/(N*sin(pi*s)) evaluated without removable singularities.
array=np.sinc(N*(s-np.rint(s)))/np.sinc(s-np.rint(s))
for ax,w in zip(axs,[1.,1.5]):
 envelope=w*w*np.sinc(w*s/5)**2;I=envelope*array**2
 ax.plot(s,I,c='#176493',lw=.8);ax.plot(s,envelope,'--',c='#b64b24',lw=1.2)
 ax.set(ylabel='Intensity / old central peak',ylim=(-.02,2.4),title=f'Slit width {w:.1f} μm; identical incoming intensity')
 ax.set_xticks(np.arange(-6,7));ax.grid(axis='x',alpha=.18)
axs[-1].set_xlabel(r'Order coordinate $s=p\sin\theta/\lambda$')
fig.savefig("paper-1-grating-widths.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
