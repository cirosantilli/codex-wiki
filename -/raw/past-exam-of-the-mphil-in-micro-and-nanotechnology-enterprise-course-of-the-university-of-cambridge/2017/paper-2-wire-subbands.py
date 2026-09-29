"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.5));y=np.linspace(0,1,401)
for n in [1,2,3]:axs[0].plot(y,n*n+.5*np.sin(n*np.pi*y),label=f'n={n}')
axs[0].axvline(0,color='.4');axs[0].axvline(1,color='.4');axs[0].set(xlabel='Transverse position y/W',ylabel='Threshold energy + scaled envelope',yticks=[1,4,9]);axs[0].legend(frameon=False,fontsize=8)
k=np.linspace(-2.5,2.5,400)
for n in [1,2,3]:axs[1].plot(k,n*n+k*k)
axs[1].set(xlabel='Longitudinal wave vector (scaled)',ylabel='Energy (scaled)',ylim=(0,15));axs[1].text(-2.2,13.5,'Each branch has continuous k',fontsize=8);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
