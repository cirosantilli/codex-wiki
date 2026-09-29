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

phi=np.linspace(0,2*np.pi,800);sing=np.cos(phi)**2/(2*np.pi**2);trip=np.sin(phi)**2/(2*np.pi**2)
fig,ax=plt.subplots(figsize=(8,4.7));ax.plot(phi,sing,lw=2.5,color=BLUE,label='Symmetric spatial / spin singlet');ax.plot(phi,trip,lw=2.5,color=ORANGE,label='Antisymmetric spatial / spin triplet')
ax.set(xlim=(0,2*np.pi),ylim=(0,.06),xlabel=r'$\phi_2$ with $\phi_1=0$',ylabel='Joint spatial density at first angle zero')
ax.set_xticks(np.arange(5)*np.pi/2,['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'])
ax.legend(frameon=False,loc='upper center',fontsize=10)
ax.annotate('Triplet coincidence node',(0,0),xytext=(.6,.011),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set_title('Opposite circulating orbitals: different pair correlations')
fig.tight_layout()
fig.savefig("paper-2b-ring-pair-density.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
