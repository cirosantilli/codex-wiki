"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6.5,3.5));t=np.linspace(0,1,400);ax.plot(t,t,label='Noise power / reference power',color='#bc7725');ax.plot(t,np.sqrt(t),label='Rms amplitude / reference amplitude',color='#176d97');ax.set(xlabel='Temperature / reference temperature',ylabel='Normalized classical thermal noise',xlim=(0,1),ylim=(0,1.08));ax.legend(frameon=False,fontsize=9);ax.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
