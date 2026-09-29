"""Original ray sketch. Python 3.14; numpy 2.3.5; matplotlib 3.10.7.
Run in the mirrored media directory: writes only its basename PNG to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,ax=plt.subplots(figsize=(8,3),dpi=120,facecolor='white')
ax.add_patch(Circle((1,0),1,facecolor='#e8f2fb',edgecolor='#1765a1',lw=2))
for angle in np.linspace(-1.35,1.35,11):
 endpoint=np.array([1+np.cos(2*angle),np.sin(2*angle)])
 ax.plot([0,endpoint[0]],[0,endpoint[1]],color='#8db7d5',lw=1)
 ax.annotate('',xy=.7*endpoint,xytext=.48*endpoint,arrowprops={'arrowstyle':'->','color':'#1765a1','lw':1.2})
ax.plot(0,0,'^',color='#784c1f',ms=9);ax.annotate('mountain',xy=(0,0),xytext=(.1,-.35),ha='left',fontsize=10,arrowprops={'arrowstyle':'->','color':'#784c1f'})
ax.text(1,0,'packets emitted\nthroughout 0 < t < τ',ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','alpha':.92})
ax.annotate('earliest-emission front',xy=(1.45,.893),xytext=(2.02,.92),ha='left',arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=10)
ax.set(xlim=(-.38,3),ylim=(-1.12,1.18),xlabel='x / (Uτ)',ylabel='y / (Uτ)')
ax.set_aspect('equal');ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
ax.set_title('Stationary Rossby waves in an eastward current',fontsize=12)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
