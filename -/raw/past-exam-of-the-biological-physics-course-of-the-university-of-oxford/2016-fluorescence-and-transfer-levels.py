"""Original conceptual figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(10,4.8),constrained_layout=True,facecolor='white')
for x0,name,y1 in [(0,'Donor',3.5),(6,'Acceptor',3.0)]:
 for y in [0,.22,.44]:ax.plot([x0,x0+3.4],[y,y],color='.35',lw=1)
 for y in [y1,y1+.22,y1+.44]:ax.plot([x0,x0+3.4],[y,y],color='.35',lw=1)
 ax.text(x0-.1,y1+.65,name,fontsize=13,weight='bold');ax.text(x0+3.5,0,r'$S_0$',va='center');ax.text(x0+3.5,y1,r'$S_1$',va='center')
def arrow(x,y,xx,yy,col,label,tx,ty):
 ax.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops={'arrowstyle':'->','color':col,'lw':2});ax.text(tx,ty,label,color=col,fontsize=10)
arrow(.4,0,.4,3.94,'#1864ab','Absorption',-.03,1.65)
arrow(1.2,3.94,1.2,3.5,'.4','Relaxation',.75,4.03)
arrow(2,3.5,2,.44,'#d9480f','Donor\nfluorescence',1.5,.8)
arrow(3,3.5,3,.05,'#862e9c','',0,0)
arrow(6.5,0,6.5,3.0,'#862e9c','',0,0)
ax.annotate('',xy=(6.3,1.9),xytext=(3.2,1.9),arrowprops={'arrowstyle':'->','color':'#862e9c','lw':1.7,'linestyle':'--'})
ax.text(3.65,2.1,'Nonradiative\nenergy transfer',color='#862e9c',fontsize=10,ha='left')
arrow(8.4,3.0,8.4,.44,'#e67700','Acceptor\nfluorescence',7.4,.8)
ax.text(.1,-.67,'Alternative decay channels compete; vertical spacings are schematic.',fontsize=10)
ax.set(xlim=(-.4,10.1),ylim=(-.85,4.7));ax.axis('off');ax.set_title('Fluorescence and FRET: excitation supply versus emission yield')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
