"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(3,1,figsize=(6.3,5.7));x=np.linspace(-.5,1.5,800);phi=np.clip(1-x,0,1);field=((x>=0)&(x<=1)).astype(float)
axs[0].plot(x,phi,color='#176b9a');axs[1].plot(x,field,color='#176b9a');axs[0].set(ylabel='Potential / V');axs[1].set(ylabel='Field / (V/ℓ)',xlabel='Axial position / ℓ')
for ax in axs[:2]:ax.axvline(0,color='.6',ls=':');ax.axvline(1,color='.6',ls=':');ax.set_ylim(-.1,1.2)
t=np.linspace(0,1,800);i=np.where((t>.35)&(t<.65),.65,1);axs[2].plot(t,i,color='#b47824');axs[2].set(xlabel='Time (schematic)',ylabel='Current / I0',ylim=(.5,1.1));axs[2].text(.5,.55,'Pore occupied',ha='center',fontsize=9);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
