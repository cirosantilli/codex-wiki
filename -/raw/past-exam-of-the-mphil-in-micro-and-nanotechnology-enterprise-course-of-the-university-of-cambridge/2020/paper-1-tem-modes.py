"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,5));labels=['Specimen','Objective lens','Back focal plane','Objective image plane','Intermediate lens','Projector → camera']
ys=[5,4.3,3.5,2.6,1.6,.4]
for ax,title in zip(axs,['Bright-field image','Selected-area diffraction']):
 ax.set(xlim=(0,5),ylim=(0,5.5));ax.axis('off');ax.set_title(title)
 for y,t in zip(ys,labels):ax.plot([.3,1.8],[y,y],color='.45');ax.text(2,y,t,va='center',fontsize=9)
 ax.annotate('',xy=(1,.05),xytext=(1,5.4),arrowprops={'arrowstyle':'->','color':'.5'})
axs[0].scatter([1],[3.5],s=130,color='#c37718',marker='s');axs[0].text(.1,3.15,'BF aperture',fontsize=9)
axs[1].scatter([1],[2.6],s=130,color='#c37718',marker='s');axs[1].text(.05,2.25,'Area aperture',fontsize=9)
for ax,y in [(axs[0],2.6),(axs[1],3.5)]:
 ax.annotate('',xy=(1.4,.4),xytext=(1.4,y),arrowprops={'arrowstyle':'->','lw':2,'color':'#197c84'});ax.text(1.5,.9,'Plane imaged',rotation=90,fontsize=9)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
