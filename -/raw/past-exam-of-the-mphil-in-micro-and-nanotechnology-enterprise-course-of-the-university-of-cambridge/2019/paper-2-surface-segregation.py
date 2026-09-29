"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6,3.7));ax.set(xlim=(-1.5,4.5),ylim=(-1.5,1.6),aspect='equal');ax.axis('off')
ax.add_patch(Circle((0,0),1,facecolor='#aab2c1',edgecolor='#414b5d'));ax.text(0,0,'Mixed alloy',ha='center')
ax.annotate('',xy=(2.15,0),xytext=(1.2,0),arrowprops={'arrowstyle':'->','lw':1.8});ax.text(1.7,.65,'Lower surface\nfree energy of B',ha='center')
ax.add_patch(Circle((3.3,0),1,facecolor='#58a7ad',edgecolor='#414b5d'));ax.add_patch(Circle((3.3,0),.72,facecolor='#aab2c1',edgecolor='#414b5d'));ax.text(3.3,0,'A-rich core',ha='center',fontsize=9);ax.text(3.3,1.22,'B-rich surface',ha='center');ax.text(1.4,-1.25,'Continuum cross-section; actual enrichment depends on composition and bonding',ha='center',fontsize=8);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
