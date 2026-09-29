"""Original answer schematics; Python 3.14.4 / Matplotlib 3.10.7, root pyproject.
Writes same-basename opaque PNG in CWD; no source figure or external image input.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def wire(ax, points):
    ax.plot(*zip(*points), color='#222222', linewidth=1.6, solid_capstyle='round')


def mos(ax, x, y, gate, pmos=False):
    wire(ax, [(x,y+.4),(x,y+.2),(x-.12,y+.2)])
    wire(ax, [(x-.12,y-.2),(x,y-.2),(x,y-.4)])
    wire(ax, [(x-.12,y-.2),(x-.12,y+.2)])
    wire(ax, [(x-.26,y-.21),(x-.26,y+.21)])
    if pmos:
        wire(ax, [(x-.78,y),(x-.43,y)])
        ax.add_patch(Circle((x-.36,y),.07,edgecolor='#222222',facecolor='white',linewidth=1.4))
        wire(ax, [(x-.29,y),(x-.26,y)])
    else:
        wire(ax, [(x-.78,y),(x-.26,y)])
    ax.text(x-.86,y,gate,ha='right',va='center',fontsize=12)


def branch(ax,x,top,bottom,devices,pmos):
    end=top
    for y,g in devices:
        wire(ax,[(x,end),(x,y+.4)])
        mos(ax,x,y,g,pmos)
        end=y-.4
    wire(ax,[(x,end),(x,bottom)])


def main():
    fig,(left,right)=plt.subplots(1,2,figsize=(9.2,5.1),dpi=100)
    fig.patch.set_facecolor('white')
    for ax in [left,right]:
        ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-.3,4.15);ax.set_ylim(-1.3,5.85)
    left.set_title('Required pull-up: 4 PMOS devices',fontsize=11)
    for y in [5.2,3.2,1.2]:wire(left,[(1,y),(3,y)])
    for x,g1,g2 in [(1,'a','b'),(3,'b','c')]:
        branch(left,x,5.2,3.2,[(4.2,g1)],True)
        branch(left,x,3.2,1.2,[(2.2,g2)],True)
    left.text(3.2,5.2,'Vdd',va='center',fontsize=10)
    wire(left,[(3,1.2),(3.65,1.2)]);left.text(3.8,1.2,'z',va='center',fontsize=12)
    left.text(2,.25,'Join to the existing output node.\nEach parallel pair is in series\nwith the other pair.',ha='center',va='center',fontsize=9)
    right.set_title('Factored full gate: 3 PMOS + 3 NMOS',fontsize=11)
    for y in [5.2,2.2]:wire(right,[(1,y),(3,y)])
    branch(right,1,5.2,2.2,[(3.7,'b')],True)
    branch(right,3,5.2,2.2,[(4.45,'a'),(3.0,'c')],True)
    right.text(3.2,5.2,'Vdd',va='center',fontsize=10)
    wire(right,[(2,2.2),(3.65,2.2)]);right.text(3.8,2.2,'z',va='center',fontsize=12)
    branch(right,2,2.2,.7,[(1.4,'b')],False)
    for y in [.7,-.8]:wire(right,[(1,y),(3,y)])
    for x,g in [(1,'a'),(3,'c')]:branch(right,x,.7,-.8,[(-.05,g)],False)
    right.text(3.2,-.8,'Vss',va='center',fontsize=10)
    fig.suptitle('Complement the conduction network, then factor its Boolean expression',fontsize=12)
    fig.tight_layout(rect=(0,0,1,.94))
    fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,
                metadata={'Software':'Matplotlib; original Oxford 2022 resit answer schematic'})
    plt.close(fig)


if __name__=='__main__':main()
