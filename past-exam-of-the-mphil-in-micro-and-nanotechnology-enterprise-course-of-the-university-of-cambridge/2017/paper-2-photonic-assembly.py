"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6.6,3.6));ax.set(xlim=(-1.2,7),ylim=(-1,4.6),aspect='equal');ax.axis('off')
for j in range(4):
 for i in range(6):ax.add_patch(Circle((i+.5*(j%2),j*np.sqrt(3)/2),.47,facecolor='#8dbbbd',edgecolor='#416f7c'))
ax.annotate('Incident light',xy=(1.5,2.2),xytext=(-1,4.1),arrowprops={'arrowstyle':'->','lw':1.5});ax.annotate('Bragg reflection',xy=(5.6,4.1),xytext=(3.5,2.2),arrowprops={'arrowstyle':'->','lw':1.5});ax.annotate('',xy=(4.5,-.65),xytext=(5.5,-.65),arrowprops={'arrowstyle':'<->'});ax.text(5,-.88,'D',ha='center');ax.text(2.5,4.45,'Size sets period; index contrast sets optical strength',ha='center',fontsize=8);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
