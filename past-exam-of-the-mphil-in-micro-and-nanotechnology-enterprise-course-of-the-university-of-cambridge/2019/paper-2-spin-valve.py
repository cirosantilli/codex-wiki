"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(2,1,figsize=(7,5.5),sharex=True);hu=np.linspace(-4,2,1000);hd=hu[::-1]
for h,up,color in [(hu,True,'#166c9c'),(hd,False,'#c06822')]:
 sp=np.where(h>(1 if up else -3),1,-1);sf=np.where(h>(.3 if up else -.3),1,-1)
 axs[0].plot(h,2*sp+sf,color=color,label='Increasing field' if up else 'Decreasing field');axs[1].plot(h,(1-sp*sf)/2,color=color)
axs[0].set(ylabel='Total magnetization / M',yticks=[-3,-1,1,3]);axs[0].legend(fontsize=9,frameon=False);axs[1].set(xlabel='Applied field (arbitrary units)',ylabel='Resistance',yticks=[0,1],yticklabels=['RP','RAP'],ylim=(-.15,1.2));axs[0].grid(alpha=.15);axs[1].grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
