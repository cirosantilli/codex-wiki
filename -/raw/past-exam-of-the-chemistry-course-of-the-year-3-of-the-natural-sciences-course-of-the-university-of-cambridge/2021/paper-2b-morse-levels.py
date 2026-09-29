#!/usr/bin/env python3
"""Original solution figure. Python 3.14; numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#276ba2"
ORANGE="#c7602b"

x=np.linspace(-1,4.1,1400);sho=x*x;morse=(1-np.exp(-x))**2
fig,axs=plt.subplots(1,2,figsize=(10,4.8),sharey=True)
axs[0].plot(x,sho,lw=2,c=BLUE);axs[1].plot(x,morse,lw=2,c=ORANGE)
lam=5.
for n in range(5):
 eh=(2/lam)*(n+.5);em=2*(n+.5)/lam-((n+.5)/lam)**2
 a=np.sqrt(eh);axs[0].plot([-a,a],[eh,eh],c=BLUE,lw=1)
 if em<1:
  lo=-np.log(1+np.sqrt(em));hi=-np.log(1-np.sqrt(em));axs[1].plot([lo,hi],[em,em],c=ORANGE,lw=1)
for ax,title in zip(axs,['Harmonic: constant spacing','Morse: shrinking spacing']):
 ax.set(xlim=(-1,4.1),ylim=(-.04,1.6),xlabel=r'$a(r-r_e)$',ylabel=r'$V/D_e$');ax.set_title(title,fontsize=12)
axs[1].axhline(1,c='0.45',ls='--',lw=1);axs[1].text(2.25,1.05,'Dissociation threshold',fontsize=9)
fig.suptitle('Same near-equilibrium curvature; illustrative level parameters')
fig.tight_layout()
fig.savefig("paper-2b-morse-levels.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
