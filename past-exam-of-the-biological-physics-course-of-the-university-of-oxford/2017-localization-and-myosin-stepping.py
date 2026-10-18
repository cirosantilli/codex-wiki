"""Original localization and hand-over-hand cartoon; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(10.5,4.6),gridspec_kw={'width_ratios':[1,1.2]},constrained_layout=True,facecolor='white')
x=np.linspace(-450,450,250);X,Y=np.meshgrid(x,x);s=140.;spot=np.exp(-((X-23)**2+(Y+17)**2)/(2*s*s))
axs[0].imshow(spot,extent=(-450,450,-450,450),origin='lower',cmap='Blues',vmin=0,vmax=1)
axs[0].plot(23,-17,'+',color='#d9480f',ms=13,mew=1.6)
axs[0].add_patch(Circle((23,-17),8,fill=False,edgecolor='#d9480f',lw=1.2))
axs[0].text(-410,355,'Broad optical spot;\nprecisely fitted centre',fontsize=10)
axs[0].set(xlabel='Image-plane distance (nm)',ylabel='Image-plane distance (nm)',title='Optical width is not centroid precision')
ax=axs[1]
for row,(a,b) in enumerate([(0,37),(74,37),(74,111)]):
 y=2-row
 ax.plot([-15,145],[y,y],color='.65',lw=2)
 for pos,col,label in [(a,'#1864ab','A'),(b,'.4','B')]:
  ax.plot(pos,y,'o',color=col,ms=12);ax.text(pos,y+.13,label,ha='center',color=col,fontsize=10)
 ax.plot((a+b)/2,y-.16,'v',color='#d9480f',ms=6)
 ax.text(149,y,f'Step {row}',va='center',fontsize=10)
ax.annotate('',xy=(74,1.5),xytext=(0,1.5),arrowprops={'arrowstyle':'->','color':'#1864ab','lw':1.8})
ax.text(37,1.59,'Labelled head: about 74 nm',ha='center',fontsize=9,color='#1864ab')
ax.set(xlim=(-18,178),ylim=(-.65,2.45),yticks=[],xlabel='Position along actin (nm)',title='Alternating heads exchange leading roles')
ax.spines['left'].set_visible(False);ax.spines['bottom'].set_position(('data',-.30))
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
