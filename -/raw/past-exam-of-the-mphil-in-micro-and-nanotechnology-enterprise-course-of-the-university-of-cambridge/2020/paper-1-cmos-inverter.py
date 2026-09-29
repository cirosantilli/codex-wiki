"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6,5));ax.set(xlim=(0,6),ylim=(0,7));ax.axis('off')
# MOS symbols: isolated gates, p-channel gate bubble and explicit body ties.
for y,p in [(4.8,True),(2.3,False)]:
 ax.plot([3,3],[y-.5,y+.5],color='black',lw=2);ax.plot([2.7,2.7],[y-.45,y+.45],color='black',lw=1.5)
 ax.plot([3,3.7,3.7],[y+.4,y+.4,y+.95],color='black');ax.plot([3,3.7,3.7],[y-.4,y-.4,y-.95],color='black')
 if p:ax.add_patch(Circle((2.53,y),.13,facecolor='white',edgecolor='black'));ax.plot([1.4,2.4],[y,y],color='black')
 else:ax.plot([1.4,2.7],[y,y],color='black')
 ax.text(4.05,y,'pMOS' if p else 'nMOS',va='center');ax.text(4.05,y-.4,'Body → VDD' if p else 'Body → ground',fontsize=9)
ax.plot([3.7,3.7],[3.25,3.85],color='black');ax.plot([3.7,5],[3.55,3.55],color='black');ax.text(5.1,3.55,'Output',va='center')
ax.plot([3.7,3.7],[5.75,6.2],color='black');ax.text(3.7,6.4,'VDD',ha='center');ax.plot([3.7,3.7],[1.35,.8],color='black');ax.plot([3.3,4.1],[.8,.8],color='black');ax.text(3.7,.35,'Ground',ha='center')
ax.plot([1.4,1.4],[2.3,4.8],color='black');ax.plot([.3,1.4],[3.55,3.55],color='black');ax.text(.2,3.85,'Input');ax.scatter([1.4,3.7],[3.55,3.55],s=15,color='black');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
