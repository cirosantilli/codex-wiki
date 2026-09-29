"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.5));ax=axs[0];ax.set(xlim=(-1.7,1.7),ylim=(-1.5,1.6),aspect='equal');ax.axis('off')
ax.add_patch(Circle((0,.9),.4,facecolor='#4da2b1',edgecolor='#30566a'));ax.add_patch(Polygon([(-.18,.5),(-.7,-1),(.7,-1),(.18,.5)],facecolor='#ddb36d',edgecolor='#80632f'));ax.annotate('',xy=(-.4,1.4),xytext=(.4,1.4),arrowprops={'arrowstyle':'<->'});ax.text(0,1.53,'Head area a0',ha='center',fontsize=9);ax.text(0,-.45,'Tail\nvolume v',ha='center');ax.annotate('',xy=(1,-1),xytext=(1,.5),arrowprops={'arrowstyle':'<->'});ax.text(1.1,-.3,'ℓc',va='center')
ax=axs[1];ax.set(xlim=(0,1.1),ylim=(0,1));ax.set_yticks([]);ax.set_xlabel('Packing parameter P = v / (a0 ℓc)')
for lo,hi,col,t in [(0,1/3,'#b9dfe7','Spherical\nmicelles'),(1/3,.5,'#ebd4a8','Cylinders'),(.5,1,'#d7c9e3','Bilayers /\nvesicles')]:ax.axvspan(lo,hi,color=col);ax.text((lo+hi)/2,.5,t,ha='center',va='center',fontsize=9)
ax.set_xticks([0,1/3,.5,1],['0','1/3','1/2','1']);ax.set_title('Approximate geometrical regimes');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
