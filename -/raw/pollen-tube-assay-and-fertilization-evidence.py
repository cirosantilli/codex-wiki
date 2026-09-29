"""Original pollen-tube assay/evidence diagram; Python 3.14 / matplotlib 3.10.7.
Run from _media; writes an opaque PNG named after this generator to the CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyBboxPatch, Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':11})
fig, ax = plt.subplots(figsize=(11.2, 6.9), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 14), ylim=(0, 9))
ax.axis('off')
ax.set_facecolor('white')
ax.text(7, 8.65, 'Pollen-tube emergence is one step, not proof of fertilization',
        ha='center', fontsize=17, weight='bold')
ax.text(.3, 7.95, 'Outside the flower: published slide assay', fontsize=13, weight='bold', color='#286b7b')

def box(x, y, w, h, text, color='#eef5f6', fontsize=11):
    ax.add_patch(FancyBboxPatch((x,y), w,h, boxstyle='round,pad=.1',
                               facecolor=color, edgecolor='#59747a', lw=1.2))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=fontsize)

def arrow(start, end, dashed=False):
    ax.annotate('', xy=end, xytext=start,
                arrowprops={'arrowstyle':'->', 'color':'#286b7b', 'lw':1.8,
                            'linestyle':'--' if dashed else '-'})

# The chamber contains an uncovered slide and a schematic culture droplet.
ax.add_patch(FancyBboxPatch((.45,4.55),4.7,2.75,boxstyle='round,pad=.1',
                           facecolor='#fafcfd', edgecolor='#758b98', lw=1.6))
ax.text(2.8, 7, 'Covered humid chamber', ha='center', fontsize=12)
ax.add_patch(Rectangle((.72,4.72),4.12,.16,facecolor='#c5dfe9',edgecolor='none'))
ax.text(2.8, 4.25, 'Wet filter paper; no slide coverslip', ha='center', fontsize=10)
ax.add_patch(Rectangle((1,5.15),3.6,.12,facecolor='#dceceb',edgecolor='#7a9696'))
ax.add_patch(Ellipse((2.8,5.78),2.6,.9,facecolor='#e1f1f7',edgecolor='#76a8bb'))
for x,y,tube in [(2,5.78,True),(2.8,5.95,False),(3.35,5.62,True)]:
    ax.add_patch(Circle((x,y),.12,facecolor='#ecc15d',edgecolor='#9d6818'))
    if tube:
        ax.plot([x+.1,x+.28,x+.52],[y,y+.08,y+.1],color='#9d6818',lw=2)
ax.text(2.8,6.43,'Pollen + sucrose + salt medium',ha='center',fontsize=10)
arrow((5.35,5.9),(6,5.9))
box(6.2,4.9,2.8,2.0,'Calibrated microscope\n100× observation\n\nRecord elapsed time')
arrow((9.15,5.9),(9.8,5.9))
box(10,4.9,3.25,2.0,'Readouts\n\nFraction with tubes\nLength among tubes')
ax.text(7,3.6,'No stigma, style or ovule in this drop: these steps are not observed',
        ha='center',fontsize=12,weight='bold',color='#94522c')
ax.plot([.3,13.7],[3.25,3.25],color='#c3ccd1',lw=1)
ax.text(.3,2.9,'Inside a compatible flower: additional evidence is needed',
        fontsize=13,weight='bold',color='#26675d')
steps=[('Pollen reaches\nstigma',.4,2.1),('Tube grows\nthrough style',3.1,2.1),
       ('Delivery into\novule',5.8,2.1),('Two gamete\nfusions',8.5,2.1),
       ('Embryo and\nseed develop',11.2,2.1)]
for text,x,w in steps:
    box(x,1.05,w,1.18,text,color='#edf6ee')
for i in range(4):
    arrow((steps[i][1]+2.28,1.65),(steps[i+1][1]-.16,1.65))
ax.text(9.55,.65,'Double fertilization',ha='center',fontsize=10,color='#26675d')
ax.text(7,.17,'Original schematic • No measured proportions, lengths or growth curve • Timing depends on material and conditions',
        ha='center',fontsize=10,color='#48515b')
fig.subplots_adjust(left=.025,right=.99,bottom=.03,top=.98)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),facecolor='white',transparent=False)
plt.close(fig)
