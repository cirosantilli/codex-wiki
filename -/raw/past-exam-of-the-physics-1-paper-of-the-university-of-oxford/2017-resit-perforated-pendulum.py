"""Normalized equilibrium geometry of an internally tangent circular hole."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig,ax=plt.subplots(figsize=(7.5,7),layout='constrained')
ax.add_patch(Circle((0,0),1,facecolor='#dce9f2',edgecolor='#25394b',lw=2))
ax.add_patch(Circle((0,.5),.5,facecolor='white',edgecolor='#25394b',lw=2))
ax.plot([0,0],[-1/6,1],ls='--',color='.45',lw=1)
for label,y in [('S',1),('C',.5),('O',0),('X',-1/6)]:
 ax.scatter([0],[y],s=32,color='black',zorder=5);ax.text(.07,y+.015,label,fontsize=13)
for x,y1,y2,label in [(-1.18,0,1,r'$a$'),(.8,-1/6,1,r'$7a/6$')]:
 ax.annotate('',xy=(x,y2),xytext=(x,y1),arrowprops=dict(arrowstyle='<->',color='.3'))
 ax.text(x+.05,(y1+y2)/2,label,fontsize=13)
ax.text(-.91,-.65,r'remaining mass $3m/4$',fontsize=12)
ax.text(-.37,.7,r'hole: $m/4$',fontsize=11)
ax.set(xlim=(-1.4,1.2),ylim=(-1.13,1.2),aspect='equal')
ax.axis('off');ax.set_title('Perforated disk in its stable hanging orientation\nX: remaining centre of mass; O: original centre',fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
