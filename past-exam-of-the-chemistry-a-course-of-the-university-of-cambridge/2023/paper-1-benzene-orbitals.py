"""Original real benzene Hückel orbitals; phases above the molecular plane."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import ring, finish
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

th=np.arange(6)*np.pi/3
points=np.column_stack([np.sin(th),np.cos(th)])
vectors=np.array([[1,1,1,1,1,1], [2,1,-1,-2,-1,1], [0,1,1,0,-1,-1],
                  [2,-1,-1,2,-1,-1], [0,1,-1,0,1,-1], [1,-1,1,-1,1,-1]],float)
vectors/=np.linalg.norm(vectors,axis=1)[:,None]
labels=[r'$\psi_0$: $\alpha+2\beta$', r'$\psi_{c1}$: $\alpha+\beta$',
        r'$\psi_{s1}$: $\alpha+\beta$', r'$\psi_{c2}$: $\alpha-\beta$',
        r'$\psi_{s2}$: $\alpha-\beta$', r'$\psi_3$: $\alpha-2\beta$']
fig=plt.figure(figsize=(10.8,5.7),layout='constrained')
gs=fig.add_gridspec(2,4,width_ratios=[1,1,1,1.45])
for k,(v,label) in enumerate(zip(vectors,labels)):
    ax=fig.add_subplot(gs[k//3,k%3]);ring(ax,points,color='0.65')
    for j,(p,c) in enumerate(zip(points,v)):
        rad=.28*np.sqrt(abs(c)/np.max(abs(v))) if c else .055
        ax.add_patch(Circle(p,rad,facecolor='#245c9f' if c>0 else '#c56527' if c<0 else 'white',
                            edgecolor='0.3',lw=.6,zorder=3))
        ax.text(*(p*1.39),str(j+1),ha='center',va='center',fontsize=9)
    finish(ax,(-1.55,1.55),(-1.55,1.55));ax.set_title(label,fontsize=11,pad=2)
ax=fig.add_subplot(gs[:,3]);ax.axis('off');ax.set(xlim=(-.4,3),ylim=(-2.7,2.7))
ax.annotate('',(-.25,2.4),(-.25,-2.3),arrowprops={'arrowstyle':'->'})
ax.text(-.35,0,'energy',rotation=90,ha='right',va='center',fontsize=10)
for y,xs,energy,occ in [(-2,[.65],r'$\alpha+2\beta$',2),(-1,[.3,1.],r'$\alpha+\beta$',2),
                        (1,[.3,1.],r'$\alpha-\beta$',0),(2,[.65],r'$\alpha-2\beta$',0)]:
    for x in xs:
        ax.plot([x-.23,x+.23],[y,y],color='#245c9f',lw=2)
        if occ:
            for dx,start,end in [(-.055,y-.16,y+.16),(.055,y+.16,y-.16)]:
                ax.annotate('',(x+dx,end),(x+dx,start),arrowprops={'arrowstyle':'->','lw':1.1})
    ax.text(1.5,y,energy,fontsize=12,va='center')
ax.set_title('Six $\\pi$ electrons\n$\\beta<0$',fontsize=12)
fig.suptitle('Benzene: real orbital coefficients and energy levels',fontsize=14)
fig.supxlabel('Blue: positive upper lobe; orange: negative upper lobe; open dot: zero coefficient. Circle area ∝ |coefficient|.',fontsize=9)
fig.savefig(Path(__file__).stem+'.png',dpi=135,facecolor='white')
plt.close(fig)
