"""Generate the Oxford 2003 Question 7 diagram in the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(9, 4.4), facecolor='white')
fig.subplots_adjust(left=.035, right=.97, top=.82, bottom=.18, wspace=.25)
fig.suptitle('Two different failures of order completeness', fontsize=15)
ax = axes[0]
points = {'bottom': (0, 0), 'a': (-.8, 1), 'b': (.8, 1), 'u': (-.8, 2), 'v': (.8, 2)}
for a, b in [('bottom','a'),('bottom','b'),('a','u'),('a','v'),('b','u'),('b','v')]:
    ax.plot([points[a][0],points[b][0]], [points[a][1],points[b][1]], color='#557085', lw=1.8, zorder=1)
for name, (x,y) in points.items():
    ax.scatter([x],[y],s=85,color='#176aa3',edgecolor='white',zorder=2)
    label = r'$\bot$' if name=='bottom' else f'${name}$'
    ax.text(x + (-.21 if x < 0 else .21 if x > 0 else 0),y + (-.23 if name=='bottom' else .05),label,fontsize=16,ha='center')
ax.set_title('Directed-complete', fontsize=13)
ax.text(0,-.65,r'$\{a,b\}$ has upper bounds $u,v$'+'\nbut has no least upper bound.',ha='center',va='top',fontsize=11)
ax.set_xlim(-1.45,1.45);ax.set_ylim(-.55,2.4);ax.axis('off')
ax=axes[1]
for j in range(4):
    ax.plot([0,0],[j*.6,(j+1)*.6], color='#557085',lw=1.8,zorder=1)
for j in range(5):
    ax.scatter([0],[j*.6],s=70,color='#a65d14',edgecolor='white',zorder=2)
    ax.text(.22,j*.6,str(j),fontsize=13,va='center')
ax.text(0,2.75,r'$\vdots$',ha='center',fontsize=19)
ax.set_title('Bounded-complete',fontsize=13)
ax.text(0,-.64,r'$\mathbb{N}_0$ is directed but has no'+'\nupper bound inside '+r'$\mathbb{N}_0$.',ha='center',va='top',fontsize=11)
ax.set_xlim(-1.5,1.5);ax.set_ylim(-.55,3.1);ax.axis('off')
fig.savefig(Path.cwd() / 'math-prelims-2003-completeness-counterexamples.png', dpi=140, facecolor='white', metadata={'Software':'matplotlib'})
plt.close(fig)
