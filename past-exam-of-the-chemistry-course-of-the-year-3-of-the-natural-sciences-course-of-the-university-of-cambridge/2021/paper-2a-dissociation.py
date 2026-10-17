#!/usr/bin/env python3
"""Original explanatory schematic; Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

R=np.linspace(.55,6,800)
def morse(r,depth,a,re):return depth*((1-np.exp(-a*(r-re)))**2-1)
exact=morse(R,1,1.45,1)
rhf=exact+.045+.37*(1-np.exp(-.25*(R-1)**2))
he=morse(R,.65,1.55,.92);hehf=he+.045+.015*(1-np.exp(-.2*(R-.92)**2))
fig,axs=plt.subplots(1,2,figsize=(11,4.8))
for ax,curves,title,ylims in [(axs[0],[exact,rhf],'H₂: neutral atoms require two configurations',(-1.1,.65)),(axs[1],[he,hehf],'HeH⁺: both electrons localize on helium',(-.74,.3))]:
 ax.plot(R,curves[0],c='black',lw=2,label='Correlated singlet (schematic)')
 ax.plot(R,curves[1],c='#c15a27',ls='--',lw=2,label='Restricted Hartree–Fock')
 ax.axhline(0,c='0.7',lw=.7);ax.set(xlim=(.6,6),ylim=ylims,xlabel='Internuclear separation (schematic)',ylabel='Relative energy (schematic)');ax.set_title(title,fontsize=11)
axs[0].text(3.6,-.12,'H + H',fontsize=10);axs[0].text(3.25,.47,'Spurious ionic weight',fontsize=10,c='#a6421b')
axs[1].text(3.3,-.13,'He + H⁺',fontsize=10);axs[1].text(2.7,.16,'Residual atomic correlation',fontsize=9,c='#a6421b')
axs[1].text(2.15,-.50,r'Bonding MO → He 1s [↑↓]'+'\n'+r'Antibonding MO → H 1s [ ]',fontsize=10,linespacing=1.6)
axs[0].legend(frameon=False,loc='lower right',fontsize=9)
fig.suptitle('Dissociation topology and orbital occupations; curves are illustrative')
fig.tight_layout()
fig.savefig("paper-2a-dissociation.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
