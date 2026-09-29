"""Original solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; saves a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(11.4,4.9));ax.set(xlim=(0,12),ylim=(0,5));ax.axis('off')
boxes=[(1.8,3.8,'Solids concentrate\nDust → planetesimals'),(6,3.8,'Core grows\nCollisions / pebble capture'),(10.2,3.8,'Gas envelope\nThermal + tidal boundaries'),(10.2,1.1,'Envelope cools\nContraction → more capture'),(6,1.1,'Self-gravity matters\nAccelerated gas accretion'),(1.8,1.1,'Supply ends\nGap + disk dispersal')]
for x,y,label in boxes:
 ax.add_patch(FancyBboxPatch((x-1.65,y-.62),3.3,1.24,boxstyle='round,pad=.08',fc='#eaf2fb',ec='#225c94'));ax.text(x,y,label,ha='center',va='center')
for u,v in [(0,1),(1,2),(2,3),(3,4),(4,5)]:
 x,y,_=boxes[u];xx,yy,_=boxes[v];dx=xx-x;dy=yy-y;length=np.hypot(dx,dy);pad=1.85 if dy==0 else .78;start=(x+dx/length*pad,y+dy/length*pad);stop=(xx-dx/length*pad,yy-dy/length*pad);ax.annotate('',stop,start,arrowprops={'arrowstyle':'->','lw':1.7})
ax.text(6,2.45,'Bottlenecks: solid supply • envelope heat loss • remaining disk lifetime',ha='center',fontsize=12);ax.text(6,.1,'Conceptual sequence: no numerical formation times or core masses are assumed.',ha='center',fontsize=10);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
