"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6.5,4));ax.set(xlim=(-1,6.4),ylim=(-.3,4.6),aspect='equal');ax.axis('off');ax.add_patch(Rectangle((0,.2),6,3.6,facecolor='#e6b466'));ax.add_patch(Rectangle((0,.2),6,.5,facecolor='#75b3b8'))
for x in [.4,1.6,2.8,4,5.2]:ax.add_patch(Rectangle((x,.7),.55,2.6,facecolor='#75b3b8'))
ax.add_patch(Rectangle((0,0),6,.2,facecolor='#576877'));ax.add_patch(Rectangle((0,3.8),6,.2,facecolor='#576877'));ax.text(3,-.17,'Hole-selective contact',ha='center',fontsize=9);ax.text(3,4.2,'Electron-selective contact',ha='center',fontsize=9)
ax.annotate('Photon',xy=(1.2,2.2),xytext=(-.9,3.6),arrowprops={'arrowstyle':'->','color':'#8e8037'});ax.annotate('',xy=(1.2,3.6),xytext=(1.2,2.2),arrowprops={'arrowstyle':'->','color':'#ad5e1e'});ax.annotate('',xy=(1.85,.6),xytext=(1.85,2.2),arrowprops={'arrowstyle':'->','color':'#216c81'});ax.text(4.4,2.7,'Donor',color='#1d5868');ax.text(4.8,3.5,'Acceptor',color='#8c5615');ax.text(3,4.5,'Illustrative interpenetrating domains',ha='center',fontsize=9);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
