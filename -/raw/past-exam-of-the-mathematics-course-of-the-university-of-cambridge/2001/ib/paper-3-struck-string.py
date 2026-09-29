"""Fixed-end impulsive string at t=l/(2c).
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes only paper-3-struck-string.png to the caller's current directory.
Caller may supply MPLCONFIGDIR; this script does not override it.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.2, 3.7), layout='constrained')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
colour='#185c9b'
for xs, ys in [([0,.25],[0,0]),([.25,.75],[1,1]),([.75,1],[0,0])]:
    ax.plot(xs, ys, color=colour, lw=2.5)
for x in [.25,.75]:
    ax.plot([x,x],[0,1],ls=':',color='#999999',lw=1)
    ax.scatter([x,x],[0,1],s=62,facecolor='white',edgecolor=colour,zorder=5)
    ax.scatter([x],[.5],s=52,color=colour,zorder=6)
ax.scatter([0,1],[0,0],color=colour,s=35,zorder=5)
ax.set(xlim=(-.035,1.035),ylim=(-.12,1.22),xlabel=r'$x/l$',ylabel=r'$2c\,y(x,l/(2c))$',title='Impulsively struck fixed-end string')
ax.set_xticks([0,.25,.5,.75,1],labels=['0','1/4','1/2','3/4','1'])
ax.set_yticks([0,.5,1],labels=['0','1/2','1'])
ax.spines[['top','right']].set_visible(False)
ax.text(.5,1.10,r'Plateau height $y=1/(2c)$',ha='center',fontsize=10)
ax.grid(axis='x',alpha=.13)
fig.savefig(Path('paper-3-struck-string.png'),dpi=140,facecolor='white',transparent=False)
plt.close(fig)
