"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(2,2,figsize=(10,7),layout='constrained');a=axs[0,0]
for lo,hi,label,mu,imp in [(-1.8,-.4,'Isolated p region',.65,.3),(.4,1.8,'Isolated n region',3.35,3.7)]:
 a.hlines([0,4],lo,hi,color='tab:blue');a.hlines(mu,lo,hi,color='tab:red',linestyle='--');a.hlines(imp,lo,hi,color='tab:green',linestyle=':');a.text((lo+hi)/2,4.5,label,ha='center',fontsize=9);a.text((lo+hi)/2,mu+.12,r'$\mu_p$' if lo<0 else r'$\mu_n$',ha='center',fontsize=9);a.text((lo+hi)/2,imp-.25,'Acceptor' if lo<0 else 'Donor',ha='center',fontsize=8)
a.annotate('',(0,.65),(0,3.35),arrowprops=dict(arrowstyle='<->'));a.text(.06,2,r'$e\Delta\phi_0$',fontsize=9);a.text(-1.95,4,r'$E_c$',va='center');a.text(-1.95,0,r'$E_v$',va='center');a.set(xlim=(-2.1,2.1),ylim=(-.7,5.1),title='Dopants and chemical potentials before contact');a.axis('off')
x=np.linspace(-2,2,900);phi=np.where(x<-1,-1,np.where(x<0,-1+(x+1)**2,np.where(x<1,1-(1-x)**2,1)))
a=axs[0,1];a.plot(x,7-5*phi,label=r'$E_c$');a.plot(x,-7-5*phi,label=r'$E_v$');a.axhline(0,color='0.25',ls='--',label=r'Equilibrium $\mu$');a.axvspan(-1,1,color='0.5',alpha=.08);a.set(xlabel='Position (schematic)',ylabel=r'Energy / $k_BT$',title='After contact: flat chemical potential');a.legend(fontsize=8)
a=axs[1,0];a.fill_between([-1,0],[-1,-1],[0,0],color='tab:orange',alpha=.4);a.fill_between([0,1],[1,1],[0,0],color='tab:blue',alpha=.4);a.axhline(0,color='0.5',lw=.7);a.text(-.5,-.5,r'$-eN_A$',ha='center');a.text(.5,.5,r'$+eN_D$',ha='center');a.annotate('Initial electron diffusion',(-.7,1.35),(.9,1.35),fontsize=8,ha='center',arrowprops=dict(arrowstyle='->'));a.annotate('Initial hole diffusion',(.7,-1.35),(-.9,-1.35),fontsize=8,ha='center',arrowprops=dict(arrowstyle='->'));a.set(xlabel='Position (schematic)',ylabel='Space-charge density (model units)',ylim=(-1.7,1.7),xlim=(-2,2),title='Fixed charges exposed by carrier transfer')
a=axs[1,1];E=np.where(x<-1,0,np.where(x<0,-(x+1),np.where(x<1,x-1,0)));a.plot(x,E);a.axhline(0,color='0.6',lw=.7);a.set(xlabel='Position (schematic)',ylabel='Electric field (model units)',title='Built-in field points from n to p');a.text(-1,-1.1,r'$-w_p$',ha='center');a.text(1,-1.1,r'$w_n$',ha='center');a.annotate('',(-.8,-.5),(.8,-.5),arrowprops=dict(arrowstyle='->'))
for a in [axs[0,1],axs[1,0],axs[1,1]]:a.axvline(-1,color='0.7',ls=':');a.axvline(1,color='0.7',ls=':');a.text(-1.5,.95,'p',transform=a.get_xaxis_transform(),ha='center');a.text(1.5,.95,'n',transform=a.get_xaxis_transform(),ha='center')
fig.suptitle('Original schematic symmetric junction; depletion boundaries at the dotted lines')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
