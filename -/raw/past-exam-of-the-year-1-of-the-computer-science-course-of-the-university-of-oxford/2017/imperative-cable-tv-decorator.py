"""Draw the extended UML class diagram; write the PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(12,7),dpi=100,facecolor='white')
ax.set(xlim=(0,12),ylim=(0,7));ax.axis('off')
ax.text(6,6.85,'Cable TV accounts: optional packages as decorators',ha='center',fontsize=18,weight='bold')
def box(x,y,w,h,name,body,color='#edf3fb',italic=False):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=color,edgecolor='#334155',lw=1.5,zorder=3))
    ax.plot([x,x+w],[y+h-.48,y+h-.48],color='#334155',lw=1,zorder=4)
    ax.text(x+w/2,y+h-.24,name,ha='center',va='center',fontstyle='italic'if italic else'normal',weight='bold',zorder=4)
    ax.text(x+.12,y+h-.62,body,ha='left',va='top',linespacing=1.5,zorder=4)
def triangle_up(x,y):
    ax.add_patch(Polygon([(x,y),(x-.13,y-.25),(x+.13,y-.25)],closed=True,facecolor='white',edgecolor='#334155',lw=1.4,zorder=2))
box(4.5,5.2,3,1.35,'«trait» CableTV','+ cost: Double\n+ packages: String')
box(.7,3.3,2.6,1.1,'BasicPlan','cost £30; basic description')
box(5.1,3.15,3.2,1.45,'Packages (abstract)','− account: CableTV\nqueries delegate to account',italic=True)
box(.4,.9,3,1.15,'Movies','cost adds £10\npackages appends Movies')
box(4.5,.9,3,1.15,'HDChannels','cost adds £7\npackages appends HD channels')
box(8.5,.9,3,1.15,'Sports','cost adds £5\npackages appends Sports',color='#dcfce7')
# Interface realizations: dashed stems and hollow triangles at CableTV.
ax.plot([2,2,5.25,5.25],[4.4,4.8,4.8,4.95],ls='--',color='#334155',lw=1.4)
triangle_up(5.25,5.2)
ax.plot([6.7,6.7],[4.6,4.95],ls='--',color='#334155',lw=1.4)
triangle_up(6.7,5.2)
# Directed association: no lifetime/ownership diamond is claimed.
ax.plot([8.3,10.5,10.5,7.75],[3.85,3.85,5.85,5.85],color='#334155',lw=1.3)
ax.annotate('',(7.5,5.85),(7.85,5.85),arrowprops={'arrowstyle':'->','lw':1.3,'color':'#334155'})
ax.text(10.55,5.05,'account: CableTV\n1',ha='right',va='center',fontsize=11)
# Concrete decorators inherit Packages through a shared generalization stem.
for x in [1.9,6,10]:ax.plot([x,x],[2.05,2.55],color='#334155',lw=1.4)
ax.plot([1.9,10],[2.55,2.55],color='#334155',lw=1.4)
ax.plot([6.7,6.7],[2.55,2.9],color='#334155',lw=1.4)
triangle_up(6.7,3.15)
ax.text(6,.35,'Hollow triangle: general classifier. Dashed line: interface realization. Solid line: inheritance or association.',ha='center',fontsize=11)
fig.subplots_adjust(left=.015,right=.985,bottom=.015,top=.985)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
