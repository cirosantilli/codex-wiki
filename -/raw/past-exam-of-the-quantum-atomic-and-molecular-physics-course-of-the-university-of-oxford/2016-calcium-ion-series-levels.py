"""Original theoretical illustration; Python3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,2,figsize=(12,6.3),constrained_layout=True,facecolor='white')
ax=axs[0]
def level(ax,x1,x2,y,label):
 ax.plot([x1,x2],[y,y],color='.25',lw=1.8);ax.text((x1+x2)/2,y+.17,label,ha='center',fontsize=10)
def transition(ax,x,y,xx,yy,col,label,tx,ty):
 ax.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops={'arrowstyle':'->','lw':1.6,'color':col});ax.text(tx,ty,label,color=col,fontsize=9,ha='center')
level(ax,0,2,0,r'$4s\ ^2S_{1/2}$');level(ax,0,2,6.5,r'$5s\ ^2S_{1/2}$')
level(ax,3.5,5.6,3.0,r'$4p\ ^2P_{1/2}$');level(ax,6.4,8.5,3.6,r'$4p\ ^2P_{3/2}$')
ax.plot([-.5,9.5],[11.4,11.4],ls='--',color='.4');ax.text(4.6,11.58,'Common Ca2+ + electron continuum',ha='center',fontsize=10)
transition(ax,4.1,3,0.3,0,'#1864ab','396.9 nm',2.1,1.0)
transition(ax,7.8,3.6,1.7,0,'#1864ab','393.4 nm',5.2,.65)
transition(ax,.4,6.5,4.9,3.0,'#2b8a3e','370.6 nm',2.1,4.45)
transition(ax,1.6,6.5,7.2,3.6,'#2b8a3e','373.7 nm',5.5,5.2)
for x,bot,txt,tx in [(-.9,0,'104.4 nm',-.95),(9.2,3.3,'about142 nm',9.2)]:
 ax.annotate('',xy=(x,11.3),xytext=(x,bot),arrowprops={'arrowstyle':'<->','color':'#862e9c'});ax.text(tx,(11.3+bot)/2,txt,rotation=90,ha='right' if x<0 else 'left',va='center',color='#862e9c',fontsize=9)
ax.set_title('First doublets and their series limits');ax.set(xlim=(-1.65,10.2),ylim=(-.8,12.2));ax.axis('off')
ax=axs[1]
level(ax,0,2,3.4,r'$4p\ ^2P_{1/2}$');level(ax,4.2,6.2,4.3,r'$4p\ ^2P_{3/2}$');level(ax,0,2,.4,r'$3d\ ^2D_{3/2}$');level(ax,4.2,6.2,1.0,r'$3d\ ^2D_{5/2}$')
ax.plot([-.3,7.2],[6.6,6.6],ls='--',color='.4');ax.text(3.4,6.78,'Same continuum',ha='center')
transition(ax,.5,3.4,.5,.4,'#e67700','866.2 nm',1.25,1.75)
transition(ax,4.7,4.3,1.5,.4,'#c92a2a','849.8 nm',3.4,2.45)
transition(ax,5.6,4.3,5.6,1.0,'#862e9c','854.2 nm',6.1,2.2)
ax.annotate('',xy=(7,6.5),xytext=(7,.7),arrowprops={'arrowstyle':'<->','color':'.45'});ax.text(7.1,4,'about121.8 nm',rotation=90,ha='left',va='center',fontsize=9)
ax.text(3.7,-.35,'D term about1.70 eV; P term about3.14 eV',ha='center',fontsize=9)
ax.set_title('Infrared triplet (fine splittings enlarged)');ax.set(xlim=(-.5,7.9),ylim=(-.7,7.5));ax.axis('off')
fig.suptitle('Ca+ term connections: schematic level heights, emission arrows downward',fontsize=13)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
