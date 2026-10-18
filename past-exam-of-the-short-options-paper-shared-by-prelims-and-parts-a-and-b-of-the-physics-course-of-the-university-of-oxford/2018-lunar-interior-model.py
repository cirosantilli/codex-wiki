from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})

from matplotlib.patches import Circle
fig,axes=plt.subplots(1,2,figsize=(9.5,5.4),layout='constrained')
colors=['#c6c2bd','#e5d3ba','#db9b69','#a9c5dc','#e8c958']
ax=axes[0]
for r,col in zip([1737,1660,480,330,240],colors):ax.add_patch(Circle((0,0),r,facecolor=col,edgecolor='#555555',lw=.8))
ax.set_aspect('equal');ax.set(xlim=(-1900,2350),ylim=(-1950,1950));ax.axis('off')
ax.annotate('Regolith and crust\nmean crust ~34–43 km',(1550,700),(800,1550),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('Silicate mantle',(-1000,-500),(-1700,-1500),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set_title('Whole Moon (~1737 km radius)')
ax=axes[1]
for r,col in zip([520,480,330,240],colors[1:]):ax.add_patch(Circle((0,0),r,facecolor=col,edgecolor='#555555',lw=1))
ax.set_aspect('equal');ax.set(xlim=(-570,950),ylim=(-650,650));ax.axis('off')
for text,point,pos in [
 ('Partial-melt region\nouter radius ~480 km',(400,220),(500,480)),
 ('Fluid outer core\nouter radius ~330 km',(280,0),(500,40)),
 ('Solid inner core\nradius ~240 km',(160,-130),(500,-400))]:
 ax.annotate(text,point,pos,arrowprops={'arrowstyle':'->'},fontsize=10,va='center')
ax.set_title('Deep-interior enlargement')
fig.suptitle('Representative lunar structure available before June 2018',fontsize=14)
fig.text(.5,.025,'Original schematic; model-dependent boundaries. Crust width visually enlarged.',ha='center',fontsize=9)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
