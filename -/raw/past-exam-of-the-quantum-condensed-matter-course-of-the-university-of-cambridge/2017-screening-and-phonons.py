"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(2,2,figsize=(9,6.6),layout='constrained');r=np.linspace(.2,4,500)
a=axs[0,0];a.plot(r,1/r,label='Bare');a.plot(r,np.exp(-r)/r,label='Screened');a.set(xlabel=r'$r/\lambda_{TF}$',ylabel=r'$4\pi\varepsilon_b\lambda_{TF}\phi/Q$',title='Point-charge potential');a.legend();a.grid(alpha=.2)
a=axs[0,1];k=np.linspace(0,np.pi,500);M=3;m=1;S=1/M+1/m;D=np.sqrt(S*S-4/(M*m)*np.sin(k/2)**2)
a.plot(k/np.pi,np.sqrt(S-D),label='Acoustic');a.plot(k/np.pi,np.sqrt(S+D),label='Optical');a.set(xlabel=r'$ka/\pi$',ylabel=r'$\omega/\sqrt{K/m}$',title=r'Diatomic model: $M=3m$');a.legend();a.grid(alpha=.2)
for ax,optical in [(axs[1,0],False),(axs[1,1],True)]:
 for j in range(5):
  xx=j*.9;heavy=j%2==0
  ax.scatter(xx,0,s=360 if heavy else 120,c='tab:blue' if heavy else 'tab:orange',zorder=3)
  disp=.15 if heavy else (-.45 if optical else .15)
  ax.annotate('',(xx+disp,.35),(xx,.35),arrowprops=dict(arrowstyle='->',lw=2,color='0.2'))
  ax.text(xx,-.26,r'$M$' if heavy else r'$m$',ha='center')
  if j<4:ax.plot([xx,xx+.9],[0,0],color='0.65',zorder=1)
 ax.set(xlim=(-.6,4.3),ylim=(-.6,.8));ax.axis('off');ax.set_title('Zone-centre optical: $Mu+mv=0$' if optical else 'Zone-centre acoustic: $u=v$')
fig.suptitle('Original local-screening and lattice-vibration models; displacements are schematic')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
