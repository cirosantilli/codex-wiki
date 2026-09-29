"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6.5,3.5));x=np.linspace(-1,5,1200);ideal=sum((x>n).astype(float) for n in range(5));smooth=sum(1/(1+np.exp(-(x-n)/.12)) for n in range(5));ax.plot(x,ideal,label='Ideal ballistic channel',color='#176b9a');ax.plot(x,smooth,'--',label='Finite broadening',color='#bc7822');ax.set(xlabel='Gate voltage toward an open channel (schematic)',ylabel='G / (2e²/h)',ylim=(-.1,5.3),yticks=range(6));ax.legend(frameon=False,fontsize=9);ax.grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
