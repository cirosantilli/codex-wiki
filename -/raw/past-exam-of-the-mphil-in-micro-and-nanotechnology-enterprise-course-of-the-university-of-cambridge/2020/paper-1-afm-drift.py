"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,4));
for ax in axs:
 ax.set(xlim=(-.25,1.4),ylim=(-.2,1.35),aspect='equal');ax.set_xlabel('Fast scan coordinate (μm)');ax.set_ylabel('Slow scan coordinate (μm)');ax.grid(alpha=.15)
axs[0].plot([0,0],[0,1],color='.65',lw=5,label='Without drift');axs[0].plot([0,.2844],[0,1],color='#b64b39',lw=2,label='Acquired trace');axs[0].annotate('',xy=(.2844,1.08),xytext=(0,1.08),arrowprops={'arrowstyle':'<->'});axs[0].text(.34,.6,'51.2 s\nbetween ends');axs[0].set_title('Wire along slow axis');axs[0].legend(fontsize=8,loc='lower right')
axs[1].plot([0,1],[.3,.300556],lw=4,color='#197c84');axs[1].text(.15,.52,'≤ 0.1 s between ends');axs[1].annotate('Slow-axis drift',xy=(1.15,.8),xytext=(1.15,.05),arrowprops={'arrowstyle':'->'},rotation=90,ha='center');axs[1].set_title('Wire along fast axis');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
