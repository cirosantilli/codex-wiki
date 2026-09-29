"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(10,3.9),layout='constrained');x=np.linspace(-2,2,700)
for V in [-.5,0,.25]:
 B=.5-V;w=np.sqrt(B/.5);u=x/w;s=np.where(u<-1,0,np.where(u<0,(u+1)**2/2,np.where(u<1,1-(1-u)**2/2,1)))
 axs[0].plot(x,-B*s,label=rf'$V={V:g}$ V')
axs[0].set(xlabel='Position / zero-bias half-width',ylabel='Conduction-edge shift / eV',title='Bias changes barrier and depleted width');axs[0].legend(fontsize=8);axs[0].grid(alpha=.15)
eps=12*8.8541878188e-12;e=1.602176634e-19;N=2e19;d=1e-5;area=1e-7;Vfd=.5-e*N*d*d/eps;Cfd=eps*area/(2*d);V=np.linspace(-5,.4998,1800)
C=np.maximum(area/2*np.sqrt(eps*e*N/(.5-V)),Cfd);axs[1].plot(V,C*1e12);axs[1].axvline(Vfd,color='tab:red',ls='--');axs[1].axvline(.5,color='0.6',ls=':');axs[1].plot([0,Vfd],[area/2*np.sqrt(eps*e*N/.5)*1e12,Cfd*1e12],'o');axs[1].annotate('Full depletion\n−2.52 V, 0.531 pF',(Vfd,Cfd*1e12),(-4.7,2.4),fontsize=9,arrowprops=dict(arrowstyle='->'));axs[1].text(-.55,6.5,'Formal divergence;\ndepletion model fails',fontsize=8,ha='center');axs[1].set(xlabel='Forward voltage V / volts',ylabel='Total capacitance / pF',xlim=(-5,.6),ylim=(0,8),title='Specified finite device');axs[1].grid(alpha=.15)
fig.suptitle('Original depletion calculation with an ideal fully depleted geometrical plateau')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
