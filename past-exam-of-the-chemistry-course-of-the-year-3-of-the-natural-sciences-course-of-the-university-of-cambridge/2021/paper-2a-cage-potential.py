#!/usr/bin/env python3
"""Original explanatory schematic; Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

r=np.linspace(0,2.18,1000);v=(1/(3-r))**12-(1/(3-r))**6
r0=3-2**(1/6)
fig,ax=plt.subplots(figsize=(7.5,4.7));ax.plot(r,v,lw=2.3,c='#286b9b')
ax.scatter([0,r0],[(1/3)**12-(1/3)**6,-.25],c=['#2d7f32','#bd3b31'],zorder=4)
ax.annotate(r'$r_{\min}=1.878\ \AA,\ V_{\min}=-0.25E_h$',(r0,-.25),xytext=(.32,-.20),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.annotate('Centre: nonzero radial slope',(0,-.00137),xytext=(.2,.22),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.axhline(0,c='0.7',lw=.7);ax.set(xlabel=r'$r$ ($\AA$)',ylabel=r'$V/E_h$',xlim=(0,2.18),ylim=(-.29,.65))
ax.set_title('Nearest-wall radial model; physical domain 0 ≤ r < 3 Å')
ax.text(2.16,.57,'Wall divergence\ncontinues beyond plot',ha='right',fontsize=9)
fig.tight_layout()
fig.savefig("paper-2a-cage-potential.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
