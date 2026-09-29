"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(9,3.4));ax=axs[0];ax.set(xlim=(-.3,6.3),ylim=(-.2,3.7),aspect='equal');ax.axis('off');ax.add_patch(Rectangle((0,.5),6,2.3,facecolor='#c4e4df',edgecolor='#3f7470'))
for x,t in [(0,'Source'),(5.2,'Drain')]:ax.add_patch(Rectangle((x,.5),.8,2.3,facecolor='#c8ae69'));ax.text(x+.4,3.05,t,ha='center')
for y in [.5,1.9]:ax.add_patch(Rectangle((2.1,y),1.8,.9,facecolor='#9eabb9',hatch='//',edgecolor='#4e5860'))
ax.annotate('',xy=(5,1.65),xytext=(1,1.65),arrowprops={'arrowstyle':'->','lw':2,'color':'#276c85'});ax.text(3,3.4,'Top view: insulated split gates',ha='center');ax.text(3,.05,'Narrow gap carries current',ha='center',fontsize=9)
ax=axs[1];ax.set(xlim=(0,6),ylim=(0,3.7),aspect='equal');ax.axis('off')
for y,h,c,t in [(.3,.5,'#aeb5bf','Accumulation gate'),(.8,.6,'#e6d9be','Dielectric'),(1.4,.12,'#368e8f','2D semiconductor'),(1.52,.5,'#e9eadb','Insulating spacer')]:ax.add_patch(Rectangle((.2,y),5.6,h,facecolor=c,edgecolor='.4'));ax.text(3,y+h/2,t,ha='center',va='center',fontsize=8)
for x in [.7,3.9]:ax.add_patch(Rectangle((x,2.02),1.4,.35,facecolor='#a4adb8'));ax.text(x+.7,2.6,'Split gate',ha='center',fontsize=8)
ax.set_title('Illustrative layer stack');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
