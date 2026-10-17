"""Original explanatory diagram. Python 3.14; matplotlib 3.10, numpy 2.3. Run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,5.5),sharey=True)
for ax in axs:
 ax.axvline(0,color='.8',ls=':');ax.axhline(2,color='#424242');ax.axhline(3.5,color='#9d6218',ls='--');ax.axhline(8,color='#16784d',ls='--');ax.set(xlim=(-1.9,1.9),ylim=(8.6,-.5));ax.set_xticks([]);ax.set_yticks([])
 ax.text(-1.8,2.23,'Objective lens',fontsize=9);ax.text(-1.8,3.8,'Back focal plane',fontsize=9);ax.text(-1.8,8.3,'Image plane',fontsize=9)
# Ray propagation variable z points down the microscope.
for x in [-.5,0,.5]:
 si=(x-.4)/2;so=si-x/1.5
 axs[0].plot([.4,x,x+so*6],[0,2,8],lw=1.4)
axs[0].plot(.4,0,'ko');axs[0].plot(-1.2,8,'ko');axs[0].text(.2,-.2,'One specimen point',ha='center');axs[0].set_title('Point → image point')
for a in [-.45,0,.45]:
 slope=.35;x=a+2*slope;out=slope-x/1.5
 axs[1].plot([a,x,x+1.5*out],[0,2,3.5],color='#b33d4c',lw=1.4)
axs[1].plot(.525,3.5,'ko');axs[1].text(.1,-.2,'One outgoing direction',ha='center');axs[1].set_title('Parallel rays → diffraction point')
fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
