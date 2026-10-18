"""Original operational-amplifier stages; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig,a=plt.subplots(figsize=(10,4.4),facecolor='white')
a.set_xlim(0,12)
a.axis('off')
def wire(ax, points, **kw):
    ax.plot(*zip(*points), color='#26364a', lw=1.7, **kw)

def resistor(ax, x, y, label, w=1.1, h=.3):
    ax.add_patch(Rectangle((x-w/2, y-h/2), w, h, fill=False, ec='#26364a', lw=1.7))
    ax.text(x, y+.25, label, ha='center', va='bottom')

def capacitor(ax, x, y, label):
    wire(ax, [(x-.12, y-.32), (x-.12, y+.32)])
    wire(ax, [(x+.12, y-.32), (x+.12, y+.32)])
    ax.text(x, y+.4, label, ha='center')

def ground(ax, x, y):
    wire(ax, [(x, y+.25), (x, y)])
    for i, half in enumerate([.23, .15, .07]):
        wire(ax, [(x-half,y-.09*i), (x+half,y-.09*i)])

def dot(ax, x, y):
    ax.plot(x,y,'o',color='#26364a',ms=4)

a.set_ylim(-.4,4.7)
a.set_title('Inverting amplifier followed by an integrator',loc='left',fontweight='bold')
for x,y in [(2.8,2),(7.8,1.5)]:
    a.add_patch(Polygon([(x,y-1),(x,y+1),(x+1.6,y)],fill=False,ec='#26364a',lw=1.7))
    a.text(x+.13,y+.5,'−',va='center');a.text(x+.13,y-.5,'+',va='center')
wire(a,[(.4,2.5),(.95,2.5)]);resistor(a,1.5,2.5,r'$R_a$');wire(a,[(2.05,2.5),(2.8,2.5)])
a.text(.4,2.9,r'$V_{\rm in}$',ha='center')
wire(a,[(4.4,2),(5.25,2)]);resistor(a,5.8,2,r'$R_i$');wire(a,[(6.35,2),(7.8,2)])
a.text(4.8,1.55,r'$V_1$',ha='center')
wire(a,[(2.3,2.5),(2.3,3.7),(2.95,3.7)]);resistor(a,3.5,3.7,r'$R_f$');wire(a,[(4.05,3.7),(4.7,3.7),(4.7,2)])
wire(a,[(9.4,1.5),(11.3,1.5)]);a.text(11.3,1.9,r'$V_{\rm out}$',ha='center')
wire(a,[(7.3,2),(7.3,3.7),(8.38,3.7)]);capacitor(a,8.5,3.7,r'$C_i$');wire(a,[(8.62,3.7),(9.8,3.7),(9.8,1.5)])
wire(a,[(2.8,1.5),(2.6,1.5),(2.6,1)]);ground(a,2.6,.75)
wire(a,[(7.8,1),(7.6,1),(7.6,.5)]);ground(a,7.6,.25)
wire(a,[(.4,.15),(.95,.15)],ls='--');resistor(a,1.5,.15,r'$R_b$');wire(a,[(2.05,.15),(2.3,.15),(2.3,2.5)],ls='--')
a.text(.4,-.15,r'$V_b$',ha='center');a.text(4.2,.15,'Dashed branch: offset correction',fontsize=10,va='center',color='#4e647c')
for x,y in [(2.3,2.5),(4.7,2),(7.3,2),(9.8,1.5)]:dot(a,x,y)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
