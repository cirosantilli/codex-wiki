"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,3,figsize=(9,3.2));en=[0,1.5,3];e=np.linspace(-.3,4.5,1600)
g1=sum(np.where(e>n,1/np.sqrt(np.maximum(e-n,.0001)),0) for n in en);g2=sum((e>n).astype(float) for n in en);g3=np.sqrt(np.maximum(e,0))
for ax,g,title in zip(axs,[g1,g2,g3],['Quasi-1D','Quasi-2D','3D']):ax.plot(e,g,color='#196c9c',lw=1.6);ax.set(xlabel='Energy',ylabel='Density of states (scaled)',title=title);ax.set_yticks([]);ax.grid(alpha=.12)
axs[0].set_ylim(0,5);axs[0].text(.15,4.4,'Peak heights clipped',fontsize=8);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
