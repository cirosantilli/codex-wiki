"""Schematic sigma-only, metal-d-derived MO energies and d8 fillings."""
from pathlib import Path
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(8.5, 4.5), layout='constrained')
def level(ax, x, y, occupied):
    ax.plot([x-.13,x+.13], [y,y], lw=2, color='#245c9f')
    for k in range(occupied):
        xx=x+(-.035 if occupied==2 and k==0 else .035 if occupied==2 else 0)
        start,end=(y-.23,y+.23) if k==0 else (y+.23,y-.23)
        ax.annotate('', (xx,end), (xx,start), arrowprops={'arrowstyle':'->','lw':1.15})
for ax in axes:
    ax.set(xlim=(-.7,1.55), ylim=(-.6,3.5));ax.axis('off')
    ax.annotate('', (-.59,3.15), (-.59,-.35), arrowprops={'arrowstyle':'->','lw':1})
    ax.text(-.64,1.4,'energy',rotation=90,ha='right',va='center',fontsize=10)
ax=axes[0]
for x in [-.28,.07,.42]:level(ax,x,0,2)
level(ax,.07,1.05,2);level(ax,.07,2.85,0)
ax.text(.66,0,'$B_{2g}+E_g$\n$\\sigma$-nonbonding',va='center',fontsize=11)
ax.text(.33,1.05,'$A_{1g}$\nweakly antibonding',va='center',fontsize=10)
ax.text(.33,2.85,'$B_{1g}$\nstrongly antibonding',va='center',fontsize=10)
ax.set_title('Square planar $D_{4h}$\nfully paired $d^8$, $S=0$',fontsize=12)
ax=axes[1]
for x in [-.1,.25]:level(ax,x,0,2)
for x,n in zip([-.28,.07,.42],[2,1,1]):level(ax,x,1.8,n)
ax.text(.6,0,'$E$\n$\\sigma$-nonbonding',va='center',fontsize=11)
ax.text(.6,1.8,'$T_2$\nantibonding',va='center',fontsize=11)
ax.set_title('Tetrahedral $T_d$\n$e^4t_2^4$, $S=1$',fontsize=12)
fig.suptitle('Five principally Ni 3d orbitals only; gaps are schematic',fontsize=11)
fig.savefig(Path(__file__).stem+'.png', dpi=140, facecolor='white')
plt.close(fig)
