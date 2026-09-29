"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(6.5,3.8));x=np.linspace(-1,5.2,1200);n=np.arange(0,5);ideal=sum((x>q).astype(float) for q in n);smooth=sum(1/(1+np.exp(-(x-q)/.12)) for q in n)
ax.plot(x,ideal,color='#146c9b',label='Ideal mode thresholds');ax.plot(x,smooth,color='#c47721',ls='--',label='Finite broadening');ax.set(xlabel='Increasing gate opening (arbitrary scale)',ylabel='G / (2e²/h)',ylim=(-.1,5.3),yticks=np.arange(6));ax.grid(alpha=.2);ax.legend(frameon=False,fontsize=9);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
