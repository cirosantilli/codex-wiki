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
ax=axs[0]
for ey,lim,hard,col,label in [(.001,.30,1.4,'#3885ae','Annealed'),(.0035,.065,.5,'#bd633c','Irradiated')]:
    e=np.linspace(0,lim,700);sy=200*ey;stress=np.where(e<=ey,200*e,sy+hard*np.maximum(e-ey,0)**.5)
    ax.plot(e,stress,c=col,lw=2.5,label=label);ax.plot(e[-1],stress[-1],'x',c=col,ms=9)
ax.set(xlabel='Tensile strain (schematic)',ylabel='Stress (arbitrary scale)',title='Higher yield, reduced uniform elongation');ax.legend(fontsize=9)
ax.text(.04,.94,'Same initial elastic slope\nEnd markers are schematic limits',transform=ax.transAxes,va='top',fontsize=9)
ax=axs[1];d=np.linspace(0,5,300)
for r0,col,label in [(.15,'#3885ae','Initially annealed'),(2.5,'#bd633c','Initially cold-worked')]:ax.plot(d,1+(r0-1)*np.exp(-d),lw=2.5,c=col,label=label)
ax.axhline(1,c='.4',ls='--');ax.set(xlabel='Scaled irradiation dose',ylabel='Dislocation density / steady-state density',title='Fixed-condition production–recovery model');ax.legend(fontsize=9)
fig.suptitle('Illustrative models, not measured austenitic stainless-steel data')
save(fig)
