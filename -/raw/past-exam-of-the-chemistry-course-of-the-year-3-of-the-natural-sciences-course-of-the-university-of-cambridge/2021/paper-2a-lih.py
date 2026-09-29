#!/usr/bin/env python3
"""Original explanatory schematic; Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

R=np.linspace(.75,7,800)
rep=.9/R**12
cov=rep-.035*np.exp(-((R-1.65)/.65)**2)
ion=rep+.72-1.8/R
W=.09*np.exp(-((R-2.5)/1.4)**2)
e0=(cov+ion)/2-np.sqrt(((cov-ion)/2)**2+W**2)
e1=(cov+ion)/2+np.sqrt(((cov-ion)/2)**2+W**2)
fig,(ax,lab)=plt.subplots(1,2,figsize=(11,5),gridspec_kw={'width_ratios':[1.7,1]})
ax.plot(R,cov,'--',c='#2c7bb6',label='Covalent diabatic')
ax.plot(R,ion,'--',c='#c35a14',label='Ionic diabatic')
ax.plot(R,e0,c='black',lw=2,label='Lower adiabatic')
ax.plot(R,e1,c='#8e4898',lw=2,label='Upper adiabatic')
ax.set(xlim=(.75,7),ylim=(-1.,1.),xlabel='Internuclear separation (schematic)',ylabel='Relative energy (schematic)')
ax.legend(frameon=False,fontsize=9,loc='lower right');ax.axhline(0,color='0.75',lw=.7)
lab.axis('off');lab.set_title('Valence occupations',fontsize=12)
lab.text(.02,.78,'Covalent singlet',weight='bold')
lab.text(.02,.65,'Li 2s [↑]      H 1s [↓]\nSpin-adapted with [↓] / [↑]',linespacing=1.5)
lab.text(.02,.39,'Ionic',weight='bold')
lab.text(.02,.27,'Li 2s [ ]      H 1s [↑↓]')
lab.text(.02,.04,'Adiabatic states exchange\nthese characters through\nthe avoided crossing.',linespacing=1.5)
fig.suptitle('Lithium hydride: two-state avoided-crossing model')
fig.tight_layout()
fig.savefig("paper-2a-lih.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
