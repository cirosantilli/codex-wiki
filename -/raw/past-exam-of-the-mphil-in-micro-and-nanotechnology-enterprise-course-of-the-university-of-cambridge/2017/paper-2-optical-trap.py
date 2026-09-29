"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6,4.4));ax.set(xlim=(-1.7,1.7),ylim=(-.3,3.6),aspect='equal');ax.axis('off');ax.add_patch(Polygon([(-1.2,3.1),(0,1.6),(1.2,3.1)],facecolor='#f0d9bd',edgecolor='#a87940',alpha=.65));ax.add_patch(Polygon([(-.8,0),(0,1.6),(.8,0)],facecolor='#f0e5d7',edgecolor='#c29b6e',alpha=.5));ax.add_patch(Rectangle((-1.35,3.1),2.7,.25,facecolor='#b5c7d1',edgecolor='#496572'));ax.text(0,3.45,'High-NA objective',ha='center',fontsize=9);ax.plot(0,1.6,'+',color='#b57a32');ax.text(-.1,1.75,'Focus',ha='right',fontsize=9)
ax.add_patch(Circle((.25,1.2),.18,facecolor='#d9b55d',edgecolor='#7f692f'));ax.annotate('Gradient force',xy=(.02,1.57),xytext=(-1.5,1),arrowprops={'arrowstyle':'->','color':'#186c93'},fontsize=9);ax.annotate('',xy=(.02,1.57),xytext=(.25,1.2),arrowprops={'arrowstyle':'->','color':'#186c93','lw':2});ax.annotate('',xy=(.25,.5),xytext=(.25,1.15),arrowprops={'arrowstyle':'->','color':'#b57023','lw':2});ax.text(.4,.65,'Radiation\npressure',fontsize=9);ax.text(0,-.2,'Displaced particle; stable equilibrium is shifted axially',ha='center',fontsize=8);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
