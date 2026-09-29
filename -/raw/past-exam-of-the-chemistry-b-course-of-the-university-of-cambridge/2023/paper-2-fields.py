"""Original qualitative orbital diagram. Python 3.14, matplotlib; PNG to cwd."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import save
fig,axs=plt.subplots(1,2,figsize=(10,5),facecolor='white')
for ax in axs:
    ax.set(xlim=(-1,5),ylim=(-3.2,4.3));ax.axis('off')
    ax.annotate('',(-.65,3.8),(-.65,-2.6),arrowprops={'arrowstyle':'->','color':'0.35'})
    ax.text(-.95,.6,'Energy',rotation=90,ha='center',va='center',color='0.35')
def level(ax,x,y,label,occupied):
    ax.plot([x-.35,x+.35],[y,y],lw=2,color='#245c9f')
    if occupied:ax.text(x,y+.1,'↑↓',ha='center',va='bottom',fontsize=17)
    ax.text(x,y-.3,label,ha='center',va='top',fontsize=12)
a=axs[0];a.set_title('Square-planar Pt(II): d⁸',fontsize=15)
for x,label in [(1,'$d_{xz}$'),(2.2,'$d_{yz}$')]:level(a,x,-2,label,True)
level(a,3.5,-.55,'$d_{z^2}$',True);level(a,2.2,.85,'$d_{xy}$',True);level(a,2.2,3.2,'$d_{x^2-y^2}$',False)
a.text(2.1,-3.0,'8 d electrons; S = 0',ha='center',fontsize=12)
a=axs[1];a.set_title('Octahedral Pt(IV): low-spin d⁶',fontsize=15)
for x,label in [(1,'$d_{xy}$'),(2.2,'$d_{xz}$'),(3.4,'$d_{yz}$')]:level(a,x,-1.6,label,True)
for x,label in [(1.6,'$d_{z^2}$'),(2.8,'$d_{x^2-y^2}$')]:level(a,x,2.3,label,False)
a.text(4.25,-1.55,'$t_{2g}$',ha='center',fontsize=14);a.text(4.25,2.35,'$e_g$',ha='center',fontsize=14)
a.text(2.2,-2.85,'6 d electrons; S = 0',ha='center',fontsize=12)
fig.text(.5,.025,'Qualitative energies. Mixed ligands remove exact degeneracies; the lower square-planar ordering is illustrative.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.07,1,1));save(fig,'paper-2-fields.png',dpi=160)
