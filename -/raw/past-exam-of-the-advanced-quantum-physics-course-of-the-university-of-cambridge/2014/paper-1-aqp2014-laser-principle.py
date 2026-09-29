"""Original analytical diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10. Writes basename into cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

from matplotlib.patches import Rectangle
fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
a=axes[0]
for y,label in [(0,'0'),(1,'1'),(3,'2'),(4,'3')]:
 a.plot([.8,2.5],[y,y],color='0.2',lw=2);a.text(2.65,y,label,va='center')
def arrow(x,y,z,color,text,tx):
 a.annotate('',(x,z),(x,y),arrowprops={'arrowstyle':'->','lw':2,'color':color});a.text(tx,(y+z)/2,text,va='center',color=color)
arrow(1,0,4,'#235789','pump',.05)
arrow(2.1,4,3,'#555555','fast',2.3)
arrow(1.5,3,1,'#ce5a24','laser',1.65)
arrow(2.1,1,0,'#555555','fast',2.3)
a.set(xlim=(-.1,3.2),ylim=(-.4,4.6),title='Four-level gain scheme');a.axis('off')
b=axes[1];b.set(xlim=(0,10),ylim=(0,5),title='Feedback and output coupling');b.axis('off')
b.add_patch(Rectangle((2.8,1.7),3.1,1.4,fc='#dceaf3',ec='#235789'))
b.text(4.35,2.8,'gain medium',ha='center');b.annotate('pump',(4.35,3.15),(4.35,4.2),ha='center',arrowprops={'arrowstyle':'->'})
b.plot([1.4,1.4],[1.1,3.7],lw=5,color='#444444');b.plot([7.1,7.1],[1.1,3.7],lw=3,color='#777777')
b.annotate('',(6.8,2.4),(1.7,2.4),arrowprops={'arrowstyle':'<->','lw':2,'color':'#ce5a24'})
b.annotate('',(9.6,2.4),(7.2,2.4),arrowprops={'arrowstyle':'->','lw':2,'color':'#ce5a24'})
b.text(1.4,.7,'mirror',ha='center');b.text(7.1,.7,'partial mirror',ha='center');b.text(8.6,2.8,'output',ha='center')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
