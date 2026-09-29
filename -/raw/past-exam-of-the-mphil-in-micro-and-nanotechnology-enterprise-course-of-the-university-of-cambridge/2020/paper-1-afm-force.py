"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(7,3.7));ax.axhline(0,color='.6',lw=1)
# Idealized branches: horizontal coordinate is separation, not scanner extension.
x=np.linspace(.15,1,150);ax.plot(x,-.03/x**2,color='#136f9c',lw=2,label='Approach')
ax.plot([.15,.08],[-1.33,-2.1],color='#136f9c',lw=2);ax.plot([.08,-.28],[-2.1,5],color='#136f9c',lw=2)
ax.plot([-.28,.02,.02,.13,1],[5,-2.8,-3.3,-.4,-.03],color='#d27615',ls='--',lw=1.6,label='Retraction (additional)')
ax.annotate('Jump to contact',xy=(.11,-1.7),xytext=(.36,-1.9),arrowprops={'arrowstyle':'->'})
ax.annotate('Repulsive contact',xy=(-.16,2.6),xytext=(.15,3.1),arrowprops={'arrowstyle':'->'})
ax.annotate('Pull-off on retraction',xy=(.02,-3.3),xytext=(.25,-3.6),arrowprops={'arrowstyle':'->'})
ax.annotate('Approach direction',xy=(.45,-.35),xytext=(.9,-.35),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Tip-surface separation (schematic)',ylabel='Normal force; repulsion positive',xlim=(-.32,1.02),ylim=(-4.2,5.6));ax.set_xticks([]);ax.set_yticks([0]);ax.legend(loc='upper right',frameon=False);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
