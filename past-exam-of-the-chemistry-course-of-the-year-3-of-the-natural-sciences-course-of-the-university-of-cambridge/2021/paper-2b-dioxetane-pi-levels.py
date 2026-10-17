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

levels=[((1+np.sqrt(21))/2,'B₁u',True,r'$\alpha+\frac{1+\sqrt{21}}{2}\beta$'),((1+np.sqrt(5))/2,'B₂g',True,r'$\alpha+\frac{1+\sqrt{5}}{2}\beta$'),(1,'B₁u',True,r'$\alpha+\beta$'),(1,'B₃g',True,''),((1-np.sqrt(5))/2,'B₂g',False,r'$\alpha+\frac{1-\sqrt{5}}{2}\beta$'),((1-np.sqrt(21))/2,'B₁u',False,r'$\alpha+\frac{1-\sqrt{21}}{2}\beta$')]
fig,ax=plt.subplots(figsize=(8.4,6));ax.set(xlim=(-.3,3.5),ylim=(-3.25,2.25),ylabel=r'$(E-\alpha)/|\beta|$, with $\beta<0$');ax.set_xticks([])
for i,(lam,sym,filled,form) in enumerate(levels):
 x=.35 if i==2 else 1.1 if i==3 else .72;y=-lam
 ax.plot([x-.25,x+.25],[y,y],lw=2.5,c=BLUE if filled else '0.45');ax.text(x,y-.16,sym,ha='center',fontsize=10)
 if filled:ax.text(x,y+.05,'↑↓',ha='center',fontsize=15)
 if form:ax.text(1.65,y,form,va='center',fontsize=12)
ax.axhline(0,color='0.8',lw=.7,ls='--');ax.text(3.15,.07,r'$\alpha$',fontsize=10)
ax.set_title('Six pi orbitals: four occupied and two empty')
fig.tight_layout()
fig.savefig("paper-2b-dioxetane-pi-levels.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
