"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.4));theta=np.linspace(0,np.pi,500);axs[0].plot(theta,np.cos(theta/2)**2,label='P(+ℏ/2)',color='#176d97');axs[0].plot(theta,np.sin(theta/2)**2,label='P(−ℏ/2)',color='#bc7725');axs[0].set(ylabel='Outcome probability',ylim=(-.03,1.05));axs[0].legend(frameon=False)
axs[1].plot(theta,np.cos(theta),color='#176d97');axs[1].set(ylabel='Mean spin / (ℏ/2)',ylim=(-1.08,1.08));axs[1].axhline(0,color='.6',lw=.7)
for ax in axs:ax.set(xlabel='Measurement-axis angle θ',xticks=[0,np.pi/2,np.pi],xticklabels=['0','π/2','π']);ax.grid(alpha=.15)
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
