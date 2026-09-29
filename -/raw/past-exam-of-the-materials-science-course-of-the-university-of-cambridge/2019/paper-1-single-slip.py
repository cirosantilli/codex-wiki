"""Original mathematical illustration; write the matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"figure.facecolor":"white","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
ax=axs[0];t=np.linspace(0,3,200);u=np.stack([5+t,1+t,np.full_like(t,4)],axis=1);norm=np.linalg.norm(u,axis=1);un=u/norm[:,None]
ax.plot(un[:,1],un[:,2],lw=2.5,c='#3a83ae');ax.scatter([un[0,1],un[-1,1]],[un[0,2],un[-1,2]],c=['#3a83ae','#bd633c'],zorder=4)
ax.annotate('[514]',(un[0,1],un[0,2]),xytext=(5,5),textcoords='offset points');ax.annotate('[211]',(un[-1,1],un[-1,2]),xytext=(-45,-10),textcoords='offset points')
ax.plot([.1,.48],[.1,.48],ls='--',c='.6',label='Boundary: y = z');ax.legend(fontsize=9,loc='lower left')
ax.set(xlabel='Loading-direction component y',ylabel='Loading-direction component z',title='Tensile axis in crystal coordinates')
ax=axs[1];eps=norm/np.sqrt(42)-1;n=np.array([1,-1,1])/np.sqrt(3);s=np.array([1,1,0])/np.sqrt(2);m=np.abs(un@n)*np.abs(un@s);tau=83.5*m[0]
ax.plot(eps,tau/m,c='#3a83ae',lw=2.5,label='Stage I: fixed CRSS')
ep=eps[-1];late=np.linspace(ep,.72,100);ax.plot(late,tau/m[-1]+320*(late-ep),c='#bd633c',lw=2.5,label='Stage II: schematic')
ax.axvline(ep,c='.5',ls='--');ax.text(.02,.92,'Conjugate slip at εₚ ≈ 0.512',transform=ax.transAxes)
ax.set(xlabel='Engineering plastic strain',ylabel='Tensile flow stress / MPa',title='Geometric stage I and forest hardening');ax.legend(fontsize=9,loc='lower right')
fig.suptitle('Ideal FCC single-slip construction, without an empirical hardening fit')
save(fig)
