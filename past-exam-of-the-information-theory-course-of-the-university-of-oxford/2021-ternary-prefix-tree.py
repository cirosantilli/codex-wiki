"""Original ternary prefix tree; Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Writes its PNG to the current working directory, without reading exam artwork.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.6, 3.6), dpi=120, facecolor='white')
ax.set_facecolor('white')
pos = {'root': (0, 2), 'A': (-2, 1), 'B': (0, 1), 'pair': (2, 1), 'C': (1.25, 0), 'D': (2.75, 0)}
for p, q, digit in [('root','A','0'),('root','B','1'),('root','pair','2'),('pair','C','0'),('pair','D','1')]:
    x,y=pos[p]; u,v=pos[q]
    ax.plot([x,u],[y,v],color='#406982',lw=2,zorder=1)
    ax.text((x+u)/2+0.08,(y+v)/2+0.06,digit,fontsize=12,backgroundcolor='white',zorder=4)
for n in ['root','pair']:
    x,y=pos[n];ax.scatter([x],[y],s=430,facecolor='#e8f1f6',edgecolor='#406982',zorder=3)
    ax.text(x,y,'1' if n=='root' else '¼',ha='center',va='center',fontsize=10,zorder=4)
for n,label in [('A','symbol 1\np = ½   code 0'),('B','symbol 2\np = ¼   code 1'),('C','symbol 3\np = ⅛   code 20'),('D','symbol 4\np = ⅛   code 21')]:
    x,y=pos[n];ax.scatter([x],[y],s=150,facecolor='#226c54',edgecolor='white',zorder=3)
    ax.text(x,y-0.22,label,ha='center',va='top',fontsize=10)
ax.set_title('Two short words; one shared branch for the rare symbols',fontsize=12,pad=14)
ax.text(0.5,-0.01,'Expected length = ½ + ¼ + 2 × ⅛ + 2 × ⅛ = 1.25 trits',transform=ax.transAxes,ha='center',fontsize=11)
ax.set_xlim(-3,3.7);ax.set_ylim(-0.8,2.35);ax.axis('off')
fig.subplots_adjust(left=.02,right=.98,top=.87,bottom=.13)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
