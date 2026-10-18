"""Original theoretical illustration; Python3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(10,4.5),constrained_layout=True,facecolor='white')
for ax,four in zip(axs,[False,True]):
 levels=[(0,'Ground / lower laser'),(2.3,'Upper laser'),(3.6,'Pump')] if not four else [(0,'Ground reservoir'),(.9,'Lower laser'),(2.7,'Upper laser'),(3.8,'Pump')]
 for y,label in levels:ax.plot([0,3.3],[y,y],color='.3',lw=1.8);ax.text(3.45,y,label,va='center',fontsize=9)
 top=levels[-1][0];upper=levels[-2][0];lower=.9 if four else 0
 for x,y,yy,col,txt in [(.35,0,top,'#1864ab','Pump'),(1.35,top,upper,'.45','Fast'),(2.2,upper,lower,'#c92a2a','Laser')]:
  ax.annotate('',xy=(x,yy),xytext=(x,y),arrowprops={'arrowstyle':'->','color':col,'lw':2});ax.text(x+.1,(y+yy)/2,txt,fontsize=9,color=col)
 if four:ax.annotate('',xy=(2.8,0),xytext=(2.8,.9),arrowprops={'arrowstyle':'->','color':'.45','lw':2});ax.text(2.85,.45,'Fast',fontsize=9,color='.45')
 ax.set(xlim=(-.2,5.8),ylim=(-.5,4.3));ax.axis('off');ax.set_title('Four-level: lower level emptied' if four else 'Three-level: ground-state lower level')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
