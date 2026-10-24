"""Original Observer UML: associations do not imply lifetime ownership."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
fig,ax=plt.subplots(figsize=(11,6.5),dpi=100);ax.set(xlim=(0,11),ylim=(0,6.5));ax.axis('off')
def box(x,y,w,h,title,lines,interface=False):
 ax.add_patch(Rectangle((x,y),w,h,facecolor='#f4f8fc',edgecolor='#294d67',lw=1.5))
 ax.plot([x,x+w],[y+h-.6,y+h-.6],color='#294d67',lw=1)
 ax.text(x+w/2,y+h-.3,('«interface» 'if interface else '')+title,ha='center',va='center',fontsize=12)
 for i,line in enumerate(lines):ax.text(x+.15,y+h-.92-i*.31,line,ha='left',va='center',fontsize=10)
def arrow(a,b,triangle=False,dashed=False):
 p=FancyArrowPatch(a,b,arrowstyle='-|>'if triangle else '->',mutation_scale=22 if triangle else 16,lw=1.5,linestyle='--'if dashed else '-',edgecolor='#294d67',facecolor='white'if triangle else '#294d67');ax.add_patch(p)
box(.6,3.8,3.4,1.8,'Subject',['attach(o: Observer)','detach(o: Observer)','notify()'])
box(6.8,4.1,3.6,1.5,'Observer',['update()'],True)
box(.6,.7,3.4,1.8,'ConcreteSubject',['state','getState()','setState(...)'])
box(6.8,.7,3.6,1.8,'ConcreteObserver',['subject: ConcreteSubject','observerState','update()'])
arrow((2.3,2.52),(2.3,3.78),triangle=True)
arrow((8.6,2.52),(8.6,4.08),triangle=True,dashed=True)
arrow((4.02,4.75),(6.78,4.75));ax.text(5.35,5.05,'subscriptions',ha='center',fontsize=11);ax.text(6.5,4.48,'0..*',ha='center',fontsize=10)
arrow((6.78,1.5),(4.02,1.5));ax.text(5.4,1.8,'subject reference',ha='center',fontsize=10);ax.text(4.3,1.2,'1',ha='center',fontsize=10)
ax.text(5.5,6.03,'Observer: notify through an interface; pull state through a subject reference',ha='center',fontsize=13)
ax.text(5.5,.2,'Open triangle: generalization / realization     Plain arrow: navigable association',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,bottom=.01,top=.99)
fig.savefig(Path.cwd()/'imperative-resit-observer-pattern.png',facecolor='white')
