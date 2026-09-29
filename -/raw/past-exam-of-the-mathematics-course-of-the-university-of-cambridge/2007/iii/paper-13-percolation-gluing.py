"""Original geometric schematics. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; preserve caller-supplied MPLCONFIGDIR.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='paper-13-mpl-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.5), constrained_layout=True)
fig.patch.set_facecolor('white')
ax = axes[0]
ax.add_patch(Rectangle((-1, 0), 2, 2, facecolor='#e3f0ff', edgecolor='#2765a8', linewidth=2, alpha=.7))
ax.add_patch(Rectangle((0, 0), 2, 2, facecolor='#ffe7d5', edgecolor='#bc6323', linewidth=2, alpha=.7))
ax.add_patch(Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='#333333', linewidth=1.5))
ax.plot([.2,.27,.2,.28,.24], [0,.25,.5,.75,1], color='#bc6323', linewidth=3)
ax.plot([.8,.74,.82,.75,.79], [0,.25,.5,.75,1], color='#2765a8', linewidth=3)
ax.plot([.2,.43,.8,1.15,1.55,2], [.5,.55,.5,.65,.5,.7], color='#bc6323', linewidth=3)
ax.plot([-1,-.65,-.2,.3,.79], [.6,.5,.68,.5,.5], color='#2765a8', linewidth=3)
ax.plot([0,.3,.65,1], [.3,.38,.3,.4], color='#398049', linewidth=3)
ax.text(-.8,1.7,"R′",color='#2765a8',fontsize=14)
ax.text(1.7,1.7,'R',color='#bc6323',fontsize=14)
ax.text(.45,.78,'S',fontsize=12)
ax.text(-.95,-.23,'Two attachments meet a horizontal crossing of S.',fontsize=10)
ax.set_title('Attachment geometry: width 3n, height 2n')
ax.set_xlim(-1.2,2.2); ax.set_ylim(-.4,2.2)
ax.set_xticks([-1,0,1,2],['−n','0','n','2n']);ax.set_yticks([0,1,2],['0','n','2n'])
ax.set_aspect('equal')
ax = axes[1]
for y in [0,3]:
 ax.add_patch(Rectangle((-1,y-1),5,2,facecolor='#e4effa',edgecolor='#2765a8',linewidth=2))
 for x in [0,3]:
  ax.add_patch(Rectangle((x-1,y-1),2,2,facecolor='white',edgecolor='#333333',linewidth=1.5))
  ax.plot([x-.2,x+.15,x-.1,x+.1],[y-1,y-.4,y+.2,y+1],color='#398049',linewidth=2.5)
 ax.plot([-1,-.5,.3,1.2,2.3,3.2,4],[y+.2,y+.1,y-.1,y+.2,y+.15,y-.2,y+.1],color='#bc6323',linewidth=3)
ax.annotate('',xy=(4.3,1),xytext=(4.3,2),arrowprops=dict(arrowstyle='<->',color='#222222'))
ax.text(4.4,1.45,'gap n',fontsize=10)
ax.text(-.8,-1.45,'Nonincident coarse bonds use disjoint fine bonds.',fontsize=10)
ax.set_title('Separated blocks: endpoint spacing 3n')
ax.set_xlim(-1.3,5);ax.set_ylim(-1.7,4.35)
ax.set_xticks([0,3],['0','3n']);ax.set_yticks([0,3],['0','3n'])
ax.set_aspect('equal')
for ax in axes:
 ax.set_facecolor('white')
 ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-13-percolation-gluing.png',dpi=130,facecolor='white',transparent=False)
plt.close(fig)
