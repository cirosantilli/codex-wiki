"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig=plt.figure(figsize=(10,5.3),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[.9,1.4]);a=fig.add_subplot(gs[0,:]);a.set_title('Sparse-mask assignment (cells label regions, not dimensional geometry)')
for k,t in enumerate(['H','E','L₁','L₂','O']):
 a.text(k+.5,2.1,t,ha='center',fontweight='bold')
 for row,color,choose in [(1.0,'#3179ad',k%2==0),(.0,'#c66a31',k%2==1)]:
  a.add_patch(Rectangle((k+.1,row),.8,.65,fc=color if choose else 'white',ec=color if choose else '#ccc',ls='-' if choose else ':'));a.text(k+.5,row+.325,'open' if choose else 'blocked',ha='center',va='center',fontsize=9,color='white' if choose else '#888')
a.text(-.1,1.325,'mask A',ha='right');a.text(-.1,.325,'mask B',ha='right');a.set(xlim=(-1,5.2),ylim=(-.2,2.4));a.axis('off')
verts=np.array([[0,0],[3,0],[3,.72],[.72,.72],[.72,3],[0,3]])
for a,correct,title in [(fig.add_subplot(gs[1,0]),False,'Desired generic L opening'),(fig.add_subplot(gs[1,1]),True,'Illustrative corrected clear mask')]:
 a.add_patch(Polygon(verts,fc='#8db9d5',ec='#245978',lw=1.6))
 if correct:
  for x,y in [(0,0),(3,0),(3,.72),(.72,3),(0,3)]:a.add_patch(Rectangle((x-.16,y-.16),.32,.32,fc='#8db9d5',ec='none'))
  a.add_patch(Rectangle((2.95,0),.18,.72,fc='#8db9d5',ec='none'));a.add_patch(Rectangle((0,2.95),.72,.18,fc='#8db9d5',ec='none'));a.add_patch(Rectangle((.54,.54),.35,.35,fc='white',ec='#a15d28',lw=.8))
  a.annotate('opaque inner correction',(.6,.6),(1.5,1.3),fontsize=8,ha='left',arrowprops={'arrowstyle':'->'});a.annotate('clear serif',(3.1,.8),(2.0,2.4),fontsize=8,ha='center',arrowprops={'arrowstyle':'->'})
  a.plot(*np.vstack([verts,verts[0]]).T,color='#444',ls='--',lw=.8)
 a.set(title=title,xlim=(-.5,3.7),ylim=(-.4,3.6),aspect='equal');a.axis('off')
fig.savefig('paper-1-double-patterning.png',dpi=160);plt.close(fig)
