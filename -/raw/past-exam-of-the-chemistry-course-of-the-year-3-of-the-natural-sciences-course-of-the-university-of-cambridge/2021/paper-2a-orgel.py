#!/usr/bin/env python3
"""Original explanatory schematic; Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

x=np.linspace(0,35,700)
r=np.sqrt(225+18*x+x*x)
ys=[.5*(15-.6*x-r),.2*x,.5*(15-.6*x+r),1.2*x]
labels=[r"$^3T_{1g}(F)$; slope $-4/5$",r"$^3T_{2g}$; slope $1/5$",r"$^3T_{1g}(P)$; slope $1/5$",r"$^3A_{2g}$; slope $6/5$"]
fig,ax=plt.subplots(figsize=(8.3,5.5))
for y,l,c in zip(ys,labels,['#2563a6','#238b45','#a34e9b','#d77900']):ax.plot(x,y,lw=2.2,label=l,color=c)
ax.axhline(0,color='0.6',lw=.8);ax.set(xlabel=r'$\Delta_o/B$',ylabel=r'$E/B$',xlim=(0,35),ylim=(-27,45))
ax.legend(frameon=False,loc='upper left');ax.set_title('Triplet terms for an octahedral d² ion')
ax.text(34,-25,'Exact supplied energy functions',ha='right',fontsize=9,color='0.35')
fig.tight_layout()
fig.savefig("paper-2a-orgel.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
