#!/usr/bin/env python3
"""Original explanatory schematic; Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

c2=np.linspace(-1,1,1201);c1=np.sqrt(1-c2*c2);p=c1*c2
a=-1.0;b=-.52;U=.85;V=.35
noee=2*a+4*b*p;phys=noee+U+2*(V-U)*p*p
cb=1/np.sqrt(2);Ebond=2*(a+b)+.5*(U+V);Eion=2*a+U;Eone=2*(a+b)
fig,ax=plt.subplots(figsize=(9,5.7));ax.plot(c2,phys,lw=2.4,c='#2767a0',label='Conventional: one-electron + Coulomb')
ax.plot(c2,noee,lw=2.4,c='#bf5b21',label='Fictitious: no electron–electron repulsion')
ax.axvline(cb,lw=.8,c='0.7');ax.axvline(-cb,lw=.8,c='0.8')
ax.scatter([0,-1,1],[Eion]*3,c='#2767a0',zorder=4)
ax.annotate(r'$E(\mathrm{H^+\cdots H^-})$',(0,Eion),xytext=(.12,-1.0),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.annotate(r'$E_{\rm RHF}(\mathrm{H_2})$',(cb,Ebond),xytext=(.05,-2.08),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.annotate(r'$2E(\mathrm{H^+\cdots H})$',(cb,Eone),xytext=(-.15,-3.15),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set(xlabel=r'$c_2$; $c_1=\sqrt{1-c_2^2}$',ylabel='Electronic energy (illustrative units)',xlim=(-1.05,1.05),ylim=(-3.4,.8))
ax.set_xticks([-1,-cb,0,cb,1],['−1',r'$-1/\sqrt{2}$','0',r'$+1/\sqrt{2}$','1'])
ax.legend(frameon=False,loc='upper left',fontsize=10)
ax.set_title('Same fixed nuclear attraction; nuclear repulsion excluded')
ax.text(-1.0,-3.32,'Schematic integrals; not a numerical H₂ calculation',fontsize=9,c='0.35')
fig.tight_layout()
fig.savefig("paper-2a-orbital-mixing.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
