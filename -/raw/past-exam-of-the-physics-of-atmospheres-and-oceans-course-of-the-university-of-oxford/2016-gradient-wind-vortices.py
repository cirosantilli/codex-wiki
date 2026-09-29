"""Original explanatory figure. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

from matplotlib.patches import Circle
fig,axs=plt.subplots(2,2,figsize=(10,7.4),layout='constrained')
cols=['#126782','#a44418','#626767']
# Upper panels show all terms moved to a circular-parcel force balance.
for ax,title,forces in [(axs[0,0],'Cyclone: low pressure',[-.56,.40,.16]),(axs[0,1],'Normal anticyclone: high pressure',[.24,-.40,.16])]:
    ax.axvline(0,color='#cccccc',lw=1)
    for yy,val,color,label in zip([2,1,0],forces,cols,['Pressure-gradient','Coriolis','Centrifugal representation']):
        ax.annotate('',xy=(val,yy),xytext=(0,yy),arrowprops={'arrowstyle':'-|>','lw':2.5,'color':color,'mutation_scale':14})
        ax.text(-.68,yy+.25,label,color=color,fontsize=11)
    ax.set(xlim=(-.72,.72),ylim=(-.55,2.7),title=title,xlabel='Inward  ←     radial acceleration     →  Outward')
    ax.set_yticks([]);ax.set_xticks([]);ax.spines[['top','right','left','bottom']].set_visible(False)
for ax,label,actual,geo in [(axs[1,0],'L',.40,.56),(axs[1,1],'H',-.40,-.24)]:
    for rr in [.35,.65,1.0]:ax.add_patch(Circle((0,0),rr,fill=False,color='#929eaa',lw=1.3))
    ax.text(0,0,label,ha='center',va='center',fontsize=23,color='#444444')
    for xx,vv,color,name in [(1.10,geo,cols[0],'Geostrophic'),(1.38,actual,cols[1],'Actual'),(1.66,actual-geo,cols[2],'Ageostrophic')]:
        ax.annotate('',xy=(xx,vv*2),xytext=(xx,0),arrowprops={'arrowstyle':'-|>','lw':2.6,'color':color,'mutation_scale':13})
    ax.set(aspect='equal',xlim=(-1.15,1.9),ylim=(-1.2,1.2),title='Winds at the east side of the vortex')
    ax.axis('off')
handles=[plt.Line2D([],[],color=c,lw=3,label=t) for c,t in zip(cols,['Geostrophic wind','Actual wind','Ageostrophic difference'])]
fig.legend(handles=handles,loc='lower center',ncol=3,frameon=False,bbox_to_anchor=(.5,-.015),fontsize=11)
fig.suptitle('Northern Hemisphere gradient wind: the normal branches\nExample: speed = 0.4 fr; pressure contours are schematic',fontsize=15)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
