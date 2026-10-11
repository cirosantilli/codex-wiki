"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,4),layout='constrained');k=np.linspace(-1.5,1.5,600)
for a,indirect in zip(axs,[False,True]):
 a.plot(k,-.22*k*k,label='Heavy hole',color='tab:blue');a.plot(k,-.85*k*k,label='Light hole',color='tab:orange');a.plot(k,-.5-.4*k*k,label='Split-off',color='tab:green')
 ec=1+.7*(k*k-.95**2)**2 if indirect else 1+.7*k*k
 a.plot(k,ec,color='tab:red',label='Conduction');a.axvline(0,color='0.6',ls=':');a.text(.04,-1.9,r'$\Gamma$');a.set(xlabel='Wavevector (schematic)',ylabel='Energy (arbitrary units)',ylim=(-2.1,2.4),xlim=(-1.5,1.5),title='Indirect gap' if indirect else 'Direct gap')
 if indirect:
  a.annotate('',(.95,1),(0,0),arrowprops=dict(arrowstyle='<->',color='0.25'));a.text(.56,.4,'Momentum\ntransfer',fontsize=9)
 else:a.annotate('',(0,1),(0,0),arrowprops=dict(arrowstyle='<->',color='0.25'));a.text(.08,.48,r'$E_g$')
 a.grid(alpha=.15)
axs[0].legend(fontsize=8,loc='upper left');fig.suptitle('Illustrative cubic-semiconductor bands; no measured material parameters')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
