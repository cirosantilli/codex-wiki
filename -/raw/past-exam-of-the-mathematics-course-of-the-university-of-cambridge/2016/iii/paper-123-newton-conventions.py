"""Draw both slope conventions. Run from the desired image-output directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
values=np.array([6,6,0,6,6,0]);indices=np.arange(6)
fig,axes=plt.subplots(1,2,figsize=(10,4.2),dpi=100,facecolor='white')
for ax in axes:
 ax.set_facecolor('white');ax.set_xlim(-.35,5.4);ax.set_ylim(-.65,7.05)
 ax.set_xticks(indices);ax.set_yticks([0,3,6]);ax.set_ylabel('Coefficient valuation');ax.grid(alpha=.16)
 ax.spines[['top','right']].set_visible(False)
axes[0].scatter(indices,values,color='#55606a',s=30,zorder=3)
axes[0].plot([0,2,5],[6,0,0],color='#196d9e',lw=2.4,zorder=4)
axes[0].set_title('Coefficient-exponent convention',fontsize=12)
axes[0].set_xlabel('Exponent j')
axes[0].text(.65,3.15,'slope −3\nlength 2',color='#196d9e',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','alpha':.9,'pad':2})
axes[0].text(3.45,.38,'slope 0; length 3',ha='center',color='#196d9e',fontsize=10)
axes[1].scatter(5-indices,values,color='#55606a',s=30,zorder=3)
axes[1].plot([0,3,5],[0,0,6],color='#8d3a78',lw=2.4,zorder=4)
axes[1].set_title('Reflected convention',fontsize=12)
axes[1].set_xlabel('Reflected exponent 5 − j')
axes[1].text(3.38,2.85,'slope +3\nlength 2',color='#8d3a78',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','alpha':.9,'pad':2})
axes[1].text(1.5,.38,'slope 0; length 3',ha='center',color='#8d3a78',fontsize=10)
fig.suptitle('Reduced ramification polynomial: valuation data (6, 6, 0, 6, 6, 0)',fontsize=12,y=.99)
fig.tight_layout(rect=(0,0,1,.93),pad=1.3)
fig.savefig(Path('paper-123-newton-conventions.png'),facecolor='white',transparent=False,dpi=100)
plt.close(fig)
