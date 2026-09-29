"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,4,figsize=(10,3.2))
for i,ax in enumerate(axs):
 ax.set(xlim=(-1.2,1.2),ylim=(-1,2),aspect='equal');ax.axis('off');ax.add_patch(Rectangle((-1.1,-.9),2.2,.15,facecolor='#cccccc'));ax.add_patch(Circle((0,-.25),.5,facecolor='#d4ac63',edgecolor='#725c36'));ax.text(0,-.25,'Metal',ha='center',fontsize=8)
 if i<2:
  for x,y in [(-.6,.35),(0,.55),(.6,.3)]:ax.plot(x,y,'o',color='#243c50',ms=4)
 if i==0:ax.annotate('Feed',xy=(0,.7),xytext=(0,1.5),ha='center',arrowprops={'arrowstyle':'->'})
 if i==1:
  ax.annotate('',xy=(.35,-.3),xytext=(-.35,.2),arrowprops={'arrowstyle':'->'});ax.add_patch(Arc((0,-.25),1.25,1.25,theta1=20,theta2=150,color='#315a70'))
 if i==2:ax.add_patch(Arc((0,.1),1.2,1.2,theta1=0,theta2=180,lw=2,color='#243c50'))
 if i==3:
  for r in [.55,.67]:
   ax.add_patch(Arc((0,1),2*r,2*r,theta1=0,theta2=180,lw=1.5));ax.plot([-r,-r],[0,1],color='#243c50');ax.plot([r,r],[0,1],color='#243c50')
  ax.annotate('',xy=(0,1.9),xytext=(0,1.55),arrowprops={'arrowstyle':'->'})
 ax.set_title(['1 Adsorb / decompose','2 Carbon transport','3 Curved cap','4 Rim incorporation'][i],fontsize=9)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
