"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(2,2,figsize=(9,8),layout='constrained');x=np.linspace(-2.7,2.7,600)
axs[0,0].plot(x,x*x+2*abs(x),label=r'$E_+$');axs[0,0].plot(x,x*x-2*abs(x),label=r'$E_-$');axs[0,0].plot([-1,1],[-1,-1],'o',color='tab:orange');axs[0,0].axhline(0,color='0.6',lw=.8);axs[0,0].axhline(-1,color='0.6',ls=':');axs[0,0].set(xlabel=r'$k_x/k_R$',ylabel=r'$E/E_R$',ylim=(-1.4,5),title='Ordered spin-split dispersions');axs[0,0].legend(fontsize=8);axs[0,0].grid(alpha=.2)
for ax,ef in zip([axs[0,1],axs[1,0],axs[1,1]],[-.6,0,.8]):
 D=np.sqrt(1+ef);outer=1+D;inner=abs(1-D)
 ax.add_patch(Circle((0,0),outer,facecolor='#a9d9ed',edgecolor='black',lw=1.2))
 if ef<0:ax.add_patch(Circle((0,0),inner,facecolor='white',edgecolor='black',lw=1.2))
 elif ef>0:ax.add_patch(Circle((0,0),inner,facecolor='#496eab',edgecolor='black',lw=1.2))
 else:ax.plot(0,0,'ko',ms=4)
 ax.axhline(0,color='0.7',lw=.6);ax.axvline(0,color='0.7',lw=.6);ax.set(xlim=(-2.7,2.7),ylim=(-2.7,2.7),xlabel=r'$k_x/k_R$',ylabel=r'$k_y/k_R$',title=rf'$E_F/E_R={ef:g}$');ax.set_aspect('equal')
fig.legend(handles=[Patch(facecolor='white',edgecolor='black',label='Empty'),Patch(facecolor='#a9d9ed',edgecolor='black',label='One occupied eigenstate'),Patch(facecolor='#496eab',edgecolor='black',label='Two occupied eigenstates')],loc='outside lower center',ncol=3,fontsize=9)
fig.suptitle(r'Original Rashba model with $k_R=q_R/2$ and $E_R=\hbar^2k_R^2/(2m)$')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
