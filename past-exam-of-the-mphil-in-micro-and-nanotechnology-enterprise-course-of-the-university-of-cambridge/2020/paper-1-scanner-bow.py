"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.6));x=np.linspace(-50,50,200);sample=200*(1-(x/50)**2);bow=100*(x/50)**2
axs[0].plot(x,sample,label='True sample');axs[0].plot(x,bow,label='Scanner background',ls='--');axs[0].plot(x,sample+bow,label='Recorded sum',lw=2);axs[0].set(xlabel='Lateral position (μm)',ylabel='Height (nm)');axs[0].legend(fontsize=8,frameon=False)
axs[1].plot(x,sample+bow,color='#1b6c9b',label='Recorded profile');axs[1].plot(x,np.zeros_like(x),color='#c27021',label='After quadratic subtraction');axs[1].set(xlabel='Lateral position (μm)',ylabel='Height (nm)',ylim=(-10,220));axs[1].legend(fontsize=8,frameon=False);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
