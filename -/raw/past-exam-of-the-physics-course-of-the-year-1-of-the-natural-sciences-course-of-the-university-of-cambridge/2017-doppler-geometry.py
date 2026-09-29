"""Original explanatory figure; run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
a=axs[0];a.axhline(1,color='0.7',lw=1);a.plot(0,0,'ko');a.text(.06,-.04,'Observer',va='top')
a.plot([-.75,0],[1,1],'o',color='tab:blue')
a.annotate('',(0,0),(-.75,1),arrowprops=dict(arrowstyle='->',color='tab:blue',lw=2))
a.annotate('',(0,0),(0,1),arrowprops=dict(arrowstyle='->',color='tab:orange',lw=2))
a.text(-.79,1.12,r'$t_e=-1.25$',ha='center');a.text(.05,1.12,r'$t_e=0$')
a.annotate('Source motion',(.65,1),(.1,1.35),arrowprops=dict(arrowstyle='->'))
a.text(-.88,.38,'Received at\nclosest approach',color='tab:blue',fontsize=9)
a.text(.12,.5,'Transverse ray\nreceived later',color='tab:orange',fontsize=9)
a.set(xlim=(-1.2,1),ylim=(-.2,1.65),xlabel=r'$x/d$',ylabel=r'$y/d$',title=r'Emission geometry, $v=0.6c$');a.set_aspect('equal')
te=np.linspace(-12,8,1200);r=np.sqrt(1+.36*te**2);tr=te+r;lam=500*(1+.36*te/r)
a=axs[1];a.plot(tr,lam,color='0.25');a.scatter([0,1],[320,500],c=['tab:blue','tab:orange'],zorder=3)
a.annotate('320 nm: received at closest approach',(0,320),(.25,230),fontsize=9,arrowprops=dict(arrowstyle='->'))
a.annotate('500 nm: emitted transversely',(1,500),(1.4,410),fontsize=9,arrowprops=dict(arrowstyle='->'))
a.set(xlim=(-2,5),ylim=(180,820),xlabel=r'Reception time $ct_r/d$',ylabel='Observed wavelength / nm',title='Rest wavelength 400 nm');a.grid(alpha=.2)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
