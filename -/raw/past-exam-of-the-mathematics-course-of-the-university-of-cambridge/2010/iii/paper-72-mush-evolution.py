"""Solid fraction in a salt-sealed column: qualitative transient and final budget.
Python 3.14; NumPy/Matplotlib. Output basename to caller CWD.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
H,c,d,D=4.0,1.0,0.5,1.0
h0=H-c-d
N=c*(h0+d*np.log1p(h0/c))
lf=(np.sqrt((c+d)**2+4*N)-(c+d))/2
hf=h0-lf
z=np.linspace(0,h0,401)
initial=(h0-z)/(c+h0-z)
# Illustrative intermediate cut through the exact interior characteristics;
# the roof location is schematic, not a numerical moving-boundary solution.
t=0.5
zs=H-np.sqrt(H*H-2*D*t)
hm=0.82*h0
zm=np.linspace(zs,hm,300)
phim=1-c/(np.sqrt((H-zm)**2+2*D*t)-d)
fig,ax=plt.subplots(figsize=(6.5,5.5),facecolor="white")
ax.set_facecolor("white")
ax.plot(initial,z/h0,lw=2.5,label=r"$t=0$",color="#398150")
px=np.r_[1,1,phim,0,0]
py=np.r_[0,zs/h0,zm/h0,hm/h0,1]
ax.plot(px,py,lw=2.5,label="Intermediate (schematic)",color="#c67b2f")
ax.plot([1,1,0,0],[0,hf/h0,hf/h0,1],lw=2.5,label="Final closed-column equilibrium",color="#246ba1",ls="--")
ax.axhline(1,color="#444444",lw=1)
ax.text(0.5,1.025,r"Salt-impermeable membrane at $h_0$",ha="center",fontsize=10)
ax.text(0.15,0.68,"Brine cap",color="#246ba1",fontsize=10)
ax.text(0.72,0.20,"Pure ice",color="#246ba1",fontsize=10)
ax.set_xlim(-0.03,1.06)
ax.set_ylim(0,1.09)
ax.set_xlabel(r"Solid fraction $\phi$")
ax.set_ylabel(r"Height $z/h_0$")
ax.legend(frameon=False,loc="lower left",fontsize=8)
ax.set_title("Solid-fraction evolution in a sealed column")
fig.tight_layout()
fig.savefig("paper-72-mush-evolution.png",dpi=150,facecolor="white",transparent=False)
plt.close(fig)
