"""Original orbital-interaction schematic; Python 3.14, numpy, matplotlib; output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
fig,axs=plt.subplots(3,1,figsize=(10,8),facecolor='white')
blue='#2268a0';red='#b04c30'
for a in axs:a.set(xlim=(0,10),ylim=(0,2));a.axis('off')
def lob(a,x,y,w,h,phase,color):
 a.add_patch(Ellipse((x,y),w,h,facecolor=color,edgecolor=color,alpha=.24));a.text(x,y,phase,ha='center',va='center',fontsize=13,color=color)
def arrow(a,start,end,label,y):
 a.annotate('',end,start,arrowprops=dict(arrowstyle='->',lw=2,color=blue));a.text((start[0]+end[0])/2,y,label,ha='center',fontsize=11,color=blue)
a=axs[0];a.set_title('Carbonyl: axial sigma donation',loc='left',weight='bold')
a.text(1,1,'M',fontsize=17,ha='center');lob(a,2.0,1,1.45,.8,'+',blue)
a.text(6.1,1,'C',ha='center',fontsize=17);a.text(7.4,1,'O',ha='center',fontsize=17);a.plot([6.4,7.1],[1,1],color='k');lob(a,5.25,1,1.1,.68,'+',red)
arrow(a,(4.8,1),(3,1),'filled CO 5σ → empty metal acceptor',.22)
a.text(8.4,1,'M–C axis',fontsize=10,ha='center')
a=axs[1];a.set_title('Carbonyl: one of two perpendicular pi channels',loc='left',weight='bold')
a.text(1.6,1,'M',ha='center',fontsize=17);a.text(6.1,1,'C',ha='center',fontsize=17);a.text(7.4,1,'O',ha='center',fontsize=17);a.plot([6.4,7.1],[1,1],color='k')
for x,y,s in [(1.15,1.5,'−'),(2.05,1.5,'+'),(1.15,.5,'+'),(2.05,.5,'−')]:lob(a,x,y,.7,.7,s,blue)
for x,y,s,w in [(6.1,1.5,'+',.8),(6.1,.5,'−',.8),(7.4,1.5,'−',.55),(7.4,.5,'+',.55)]:lob(a,x,y,w,.7,s,red)
arrow(a,(2.7,1),(5.4,1),'filled metal dπ → empty CO 2π*',.05)
a.text(9,1,'C–O\nantibonding',ha='center',va='center',fontsize=11)
a=axs[2];a.set_title('Alkene: donation/backdonation channels',loc='left',weight='bold')
a.text(1.7,1,'M',ha='center',va='center',fontsize=19)
a.text(7.2,1.55,'C',ha='center',fontsize=16);a.text(7.2,.45,'C',ha='center',fontsize=16);a.plot([7.1,7.1],[.7,1.3],color='k');a.plot([7.3,7.3],[.7,1.3],color='k')
arrow(a,(6.5,1.4),(2.5,1.4),'filled alkene π → metal acceptor',1.7)
arrow(a,(2.5,.65),(6.5,.65),'metal d → alkene π*',.17)
a.text(9,1,'Zr(IV): d⁰\ndonation dominates',ha='center',va='center',fontsize=11)
fig.text(.5,.012,'Orbital phases are schematic; phases are not electric charges. Alkene channels shown as interactions, not literal orbit shapes.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.035,1,1));fig.savefig('paper-2-bonding.png',dpi=160,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)
