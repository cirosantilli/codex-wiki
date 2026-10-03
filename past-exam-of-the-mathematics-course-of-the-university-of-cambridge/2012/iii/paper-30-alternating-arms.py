"""Original percolation separation schematic. Python 3.14 / Matplotlib 3.10.
Emit paper-30-alternating-arms.png in cwd; respect caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(8, 4.4), dpi=100, facecolor='white')
ax.set_facecolor('white')
ax.add_patch(Rectangle((-1, -1), 2, 2, facecolor='#f1f3f5', edgecolor='#9aa1a8', linestyle='--', linewidth=1.5))
ax.plot([0, 0], [-1, 1], color='#161b22', linewidth=4, zorder=5)
ax.annotate('', xy=(0, 2.4), xytext=(0, 1), arrowprops={'arrowstyle':'->', 'color':'#161b22', 'lw':3})
ax.annotate('', xy=(0, -2.4), xytext=(0, -1), arrowprops={'arrowstyle':'->', 'color':'#161b22', 'lw':3})
ax.annotate('', xy=(-3.2, .35), xytext=(-1.25, .35), arrowprops={'arrowstyle':'->', 'color':'#1261a0', 'lw':3})
ax.annotate('', xy=(3.2, -.35), xytext=(1.25, -.35), arrowprops={'arrowstyle':'->', 'color':'#1261a0', 'lw':3})
ax.scatter([-1.25, 1.25], [.35, -.35], s=36, color='#1261a0', zorder=6)
ax.text(.16, 1.75, 'primal open ray', fontsize=11, va='center')
ax.text(.16, -1.8, 'primal open ray', fontsize=11, va='center')
ax.text(-2.28, .65, 'dual infinite tail', fontsize=11, ha='center', color='#1261a0')
ax.text(2.28, -.75, 'dual infinite tail', fontsize=11, ha='center', color='#1261a0')
ax.text(.18, .03, 'opened\nconnector', fontsize=10, va='center')
ax.text(-.92, -.87, 'finite box', fontsize=10, color='#555b62')
ax.text(-2.4, -1.65, 'one side', fontsize=11, color='#1261a0', ha='center')
ax.text(2.4, 1.4, 'other side', fontsize=11, color='#1261a0', ha='center')
ax.set_title('An opened connector separates two infinite dual tails', fontsize=13, pad=13)
ax.set_xlim(-3.7, 3.7)
ax.set_ylim(-2.6, 2.6)
ax.axis('off')
fig.subplots_adjust(left=.03, right=.97, top=.88, bottom=.06)
fig.savefig('paper-30-alternating-arms.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
