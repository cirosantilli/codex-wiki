"""Original pz SALC phases for the printed alternating C8 ring axes."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond,finish
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

a=.42
pts=np.array([[-a,1],[a,1],[1,a],[1,-a],[a,-1],[-a,-1],[-1,-a],[-1,a]])
patterns=[[1,-1,1,-1,1,-1,1,-1],[1,1,1,1,1,1,1,1],
          [1,-1,-1,1,1,-1,-1,1],[1,1,-1,-1,1,1,-1,-1]]
labels=[r'$A_{1u}$: $\alpha-\beta_S-\beta_L$',r'$A_{2u}$: $\alpha+\beta_S+\beta_L$',
        r'$B_{1u}$: $\alpha-\beta_S+\beta_L$',r'$B_{2u}$: $\alpha+\beta_S-\beta_L$']
fig,axes=plt.subplots(2,2,figsize=(7.6,6.5),layout='constrained')
for ax,pattern,title in zip(axes.flat,patterns,labels):
    for j in range(8):
        bond(ax,pts[j],pts[(j+1)%8],color='0.25' if j%2==0 else '0.60',
             style='solid' if j%2==0 else 'dashed',lw=1.6)
    for j,(p,sign) in enumerate(zip(pts,pattern)):
        ax.add_patch(Circle(p,.175,facecolor='#245c9f' if sign>0 else '#c56527',
                            edgecolor='0.25',lw=.65,zorder=3))
        ax.text(*(p*1.31),str(j+1),ha='center',va='center',fontsize=10)
    ax.annotate('',(.46,0),(0,0),arrowprops={'arrowstyle':'->','lw':.8,'color':'0.5'})
    ax.annotate('',(0,.46),(0,0),arrowprops={'arrowstyle':'->','lw':.8,'color':'0.5'})
    ax.text(.46,-.1,'x',fontsize=9,color='0.4');ax.text(-.12,.46,'y',fontsize=9,color='0.4')
    finish(ax,(-1.5,1.5),(-1.5,1.5));ax.set_title(title,fontsize=12,pad=3)
fig.suptitle('One-dimensional symmetry orbitals of the alternating planar ring',fontsize=13)
fig.supxlabel('Blue / orange: positive / negative upper pz lobe; all nonzero coefficients have magnitude 1/√8.\nSolid edges: short bonds; dashed edges: long bonds; z points out of the page.',fontsize=9)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
plt.close(fig)
