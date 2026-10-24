"""Original gate-block schematic of the factored correction; output to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(9.2, 5.4), dpi=100, facecolor='white')
color = '#263b50'
def wire(xs, ys): ax.plot(xs, ys, color=color, lw=1.5, zorder=1)
def gate(x, y, name, w=0.8, h=0.7):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.02',edgecolor=color,facecolor='#edf3fa',lw=1.3,zorder=3))
    ax.text(x,y,name,ha='center',va='center',fontsize=11,zorder=4)
def dot(x,y): ax.plot([x],[y],'o',color=color,ms=3,zorder=5)
for label, y in [('a',4.4),('d',3.1),('b',2.7),('c',1.8)]:
    ax.text(0.1,y,label,ha='right',va='center',fontsize=13)
    wire([0.2,0.9 if label in ('a','c') else 1.0],[y,y])
for y in (4.4,1.8): gate(1.3,y,'NOT',w=0.75,h=0.5)
gate(3.3,3.7,'OR'); gate(3.3,2.0,'OR')
gate(5.5,2.8,'AND'); gate(5.5,0.6,'AND'); gate(7.6,1.8,'OR')
# Upper OR u = not a + d.
wire([1.7,2.3,2.3,2.9],[4.4,4.4,3.9,3.9]); ax.text(1.9,4.55,r'$\bar a$',fontsize=12)
wire([1.0,2.5,2.5,2.9],[3.1,3.1,3.5,3.5])
# Lower OR v = b + not c, with branch dots only on true junctions.
wire([1.0,2.0,2.0,2.9],[2.7,2.7,2.2,2.2]); dot(2.0,2.7)
wire([1.7,2.9],[1.8,1.8]); ax.text(1.9,1.52,r'$\bar c$',fontsize=12)
# Combine u and v.
wire([3.7,4.5,4.5,5.1],[3.7,3.7,3.0,3.0]); ax.text(4.0,3.85,'u',fontsize=12)
wire([3.7,4.3,4.3,5.1],[2.0,2.0,2.6,2.6]); ax.text(3.95,1.72,'v',fontsize=12)
# Independent bc product, tapping c before its inverter.
wire([2.0,2.0,5.1],[2.7,0.8,0.8])
wire([0.65,0.65,4.6,4.6,5.1],[1.8,0.2,0.2,0.4,0.4]); dot(0.65,1.8)
wire([5.9,6.6,6.6,7.2],[2.8,2.8,2.0,2.0]); ax.text(6.15,2.95,'t',fontsize=12)
wire([5.9,6.8,6.8,7.2],[0.6,0.6,1.6,1.6]); ax.text(6.1,0.32,'bc',fontsize=12)
wire([8.0,8.6],[1.8,1.8]); ax.text(8.7,1.8,'q',va='center',fontsize=13)
ax.text(4.4,-0.35,r'$u = \bar a + d$      $v = b + \bar c$      $t = uv$      $q = bc + t$',ha='center',fontsize=12)
ax.text(4.4,-0.85,'Three OR gates, two AND gates, two NOT gates; maximum delay 40 ns',ha='center',fontsize=11)
ax.set(xlim=(-0.25,9.15),ylim=(-1.1,5.05))
ax.set_title('Hazard correction with shared Boolean factors',fontsize=15,pad=10)
ax.axis('off');fig.subplots_adjust(left=0.025,right=0.975,top=0.90,bottom=0.03)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',dpi=100)
plt.close(fig)
