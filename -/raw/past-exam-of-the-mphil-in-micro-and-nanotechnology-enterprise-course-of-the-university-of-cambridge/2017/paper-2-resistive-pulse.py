"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(7,3.8));ax.set(xlim=(-.4,6.4),ylim=(-.5,4.3),aspect='equal');ax.axis('off');ax.add_patch(Rectangle((0,0),6,3,facecolor='#dceff3',edgecolor='#4b6574'))
for y in [0,1.75]:ax.add_patch(Rectangle((2.85,y),.3,1.25,facecolor='#939ca5'))
ax.add_patch(Circle((2.1,1.5),.17,facecolor='#c49449',edgecolor='#675027'));ax.annotate('',xy=(3.8,1.5),xytext=(2.3,1.5),arrowprops={'arrowstyle':'->'});ax.text(1.1,.8,'Generic particle',fontsize=9);ax.text(3.1,2.8,'Insulating membrane',ha='left',fontsize=8)
for x in [.5,5.5]:ax.plot([x,x],[.7,3.7],color='#64717a',lw=3)
ax.plot([.5,2],[3.7,3.7],color='#344f5d');ax.plot([4,5.5],[3.7,3.7],color='#344f5d');ax.add_patch(Rectangle((2,3.4),2,.6,facecolor='white',edgecolor='#344f5d'));ax.text(3,3.7,'Bias + current readout',ha='center',va='center',fontsize=9);ax.text(1.2,.15,'Electrolyte',ha='center');ax.text(4.8,.15,'Electrolyte',ha='center');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
