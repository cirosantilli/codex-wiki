"""Original volumetric bookkeeping figure. Python 3.14, matplotlib 3.10.7.

Run from _media; writes volumetric-solution-dilution-accounting.png to CWD.
All quantities are illustrative model inputs, not measured results.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(11, 6.5), dpi=120, facecolor='white')
ax.set(xlim=(0,11), ylim=(0,6.5))
ax.axis('off')
ax.text(5.5,6.20,'Dilute to a final volume; transfer only a portion',
        ha='center',fontsize=17,weight='bold')
ax.text(5.5,5.83,'Illustrative quantities — complete mixing and no solute loss',
        ha='center',fontsize=11,color='#45586a')

def flask(x, color):
    # Equal-sized icons intentionally do not represent relative capacities.
    pts=[(x-.23,4.97),(x-.23,3.97),(x-.78,3.02),(x-.78,2.62),
         (x+.78,2.62),(x+.78,3.02),(x+.23,3.97),(x+.23,4.97)]
    ax.add_patch(Polygon(pts,closed=False,fill=False,edgecolor='#435565',lw=2))
    liquid=[(x-.75,2.65),(x+.75,2.65),(x+.75,3.02),(x+.20,3.97),
            (x+.20,4.52),(x-.20,4.52),(x-.20,3.97),(x-.75,3.02)]
    ax.add_patch(Polygon(liquid,facecolor=color,edgecolor='none'))
    ax.plot([x-.39,x+.39],[4.52,4.52],color='#172938',lw=2)
    ax.text(x,5.14,'final solution',ha='center',fontsize=11)

xs=[1.55,5.50,9.45]
colors=['#90bfd6','#c5deeb','#e1eef4']
for x,col in zip(xs,colors): flask(x,col)
vols=['250.0 mL','100.0 mL','50.00 mL']
cs=['0.2000 mol/L','0.02000 mol/L','0.002000 mol/L']
ns=['0.05000 mol','0.002000 mol','0.0001000 mol']
for x,v,c,n in zip(xs,vols,cs,ns):
    ax.text(x,4.08,v,ha='center',fontsize=12,weight='bold')
    ax.text(x,2.34,c,ha='center',fontsize=13,weight='bold',color='#145375')
    ax.text(x,2.04,n+' in this flask',ha='center',fontsize=10.5)
for i,(v,n) in enumerate([('10.00 mL','0.002000 mol'),('5.000 mL','0.0001000 mol')]):
    a,b=xs[i]+.92,xs[i+1]-.92
    ax.add_patch(FancyArrowPatch((a,3.51),(b,3.51),arrowstyle='-|>',
                                 mutation_scale=22,color='#304e65',lw=2))
    mid=(a+b)/2
    ax.text(mid,4.00,'pipette '+v,ha='center',fontsize=11)
    ax.text(mid,3.72,'carries '+n,ha='center',fontsize=10.5)
    ax.text(mid,3.12,'then add solvent',ha='center',fontsize=10.5)
    ax.text(mid,2.87,'to the next mark',ha='center',fontsize=10.5)
ax.add_patch(Rectangle((.45,.72),10.1,1.0,facecolor='#f2f6f8',edgecolor='none'))
ax.text(5.5,1.46,'Inventory after both transfers',ha='center',weight='bold',fontsize=12)
ax.text(5.5,1.09,'0.04800 mol left in stock + 0.001900 mol left in first dilution',ha='center',fontsize=11)
ax.text(5.5,.84,'+ 0.0001000 mol in final flask = 0.05000 mol initially',ha='center',fontsize=11)
ax.text(5.5,.32,'Final volume includes solute. Flask icons are not to scale. All amounts count analytical NaCl.',
        ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
fig.savefig(Path('volumetric-solution-dilution-accounting.png'),facecolor='white',transparent=False)
plt.close(fig)
