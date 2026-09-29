"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(9,3.2));ax.set(xlim=(0,12),ylim=(0,4));ax.axis('off')
def box(x,y,w,h,t):
 ax.add_patch(Rectangle((x,y),w,h,facecolor='#e8f1f6',edgecolor='#34485a'));ax.text(x+w/2,y+h/2,t,ha='center',va='center')
def arr(p,q):ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','lw':1.4})
box(.2,2.4,1.6,.9,'Peak-force\nsetpoint');box(2.4,2.4,1.1,.9,'Error');box(4.1,2.4,1.5,.9,'PI\ncontroller');box(6.2,2.4,1.8,.9,'Mean z\n+ modulation');box(8.8,2.4,2.7,.9,'Tip / sample\nforce cycle')
for p,q in [((1.8,2.85),(2.4,2.85)),((3.5,2.85),(4.1,2.85)),((5.6,2.85),(6.2,2.85)),((8,2.85),(8.8,2.85))]:arr(p,q)
box(7,.3,4.5,.9,'Deflection detector → calibrated force → peak');arr((10.15,2.4),(10.15,1.2));ax.plot([7,3],[.75,.75],color='#34485a');arr((3,.75),(3,2.4));ax.text(3.25,1.7,'−',fontsize=15)
ax.text(6.8,3.65,'Topography: mean z',ha='center');ax.text(1.5,.55,'Negative feedback',ha='center');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
