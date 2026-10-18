"""Original missing-outcome illustration, not empirical service data.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The output PNG is always written to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(10.8, 5.4), dpi=120, facecolor='white')
colors = ['#3b876c', '#ce8455', '#c7cbd0']
rows = [(30, 20, 50), (30, 70, 0), (80, 20, 0)]
for y, row in zip([2, 1, 0], rows):
 left = 0
 for n, color in zip(row, colors):
  if n:
   ax.barh(y, n, left=left, height=.53, color=color, edgecolor='white', linewidth=1.5)
   ax.text(left+n/2, y, str(n), ha='center', va='center', color='white' if color!=colors[2] else '#20252b', weight='bold')
  left += n
ax.set_yticks([2, 1, 0], ['Observed data', 'Missing: none recover', 'Missing: all recover'])
ax.set(xlim=(0,100), ylim=(-.55,2.6), xlabel='People in the hypothetical cohort (total = 100)')
ax.set_xticks([0,20,40,60,80,100])
ax.tick_params(axis='y', length=0, pad=12)
ax.spines[['top','right','left']].set_visible(False)
ax.spines['bottom'].set_color('#7a7a7a')
ax.legend(handles=[Patch(facecolor=c,label=t) for c,t in zip(colors,['Recovered','Not recovered','Missing'])],loc='upper center',bbox_to_anchor=(.5,-.22),ncol=3,frameon=False)
fig.suptitle('Observed-case recovery does not identify whole-cohort recovery', fontsize=15, weight='bold', y=.965)
fig.text(.5,.86,'Observed: 30 / 50 = 60%     |     Whole-cohort bounds: 30% to 80%',ha='center',fontsize=12)
fig.text(.5,.025,'Illustrative counts only. The two completed rows are compatible with the same observed data.',ha='center',fontsize=10,color='#444444')
fig.subplots_adjust(left=.235,right=.965,top=.79,bottom=.25)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), facecolor='white', transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
