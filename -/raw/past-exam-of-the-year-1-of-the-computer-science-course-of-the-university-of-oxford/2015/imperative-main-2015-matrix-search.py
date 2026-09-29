"""Generate imperative-main-2015-matrix-search.png in the current directory.

Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5 (pyproject.toml).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(8.2, 5.4), facecolor='white')
ax.set_facecolor('white')
rows, cols, mid, cut = 7, 9, 3, 4
regions = [
    (0, 0, cut, mid, '#eeeeee'),
    (cut, 0, cols-cut, mid, '#d6eafa'),
    (0, mid, cut, 1, '#dddddd'),
    (cut, mid, cols-cut, 1, '#dddddd'),
    (0, mid+1, cut, rows-mid-1, '#fce0bd'),
    (cut, mid+1, cols-cut, rows-mid-1, '#eeeeee'),
]
for x, y, w, h, color in regions:
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor='none'))
for x in range(cols+1): ax.plot([x,x],[0,rows],color='white',lw=1.4)
for y in range(rows+1): ax.plot([0,cols],[y,y],color='white',lw=1.4)
ax.add_patch(Rectangle((0,0),cols,rows,fill=False,edgecolor='#444444',lw=1.5))
for x, y, text, color in [
    (2, 1.5, 'Excluded\nall < x', '#555555'),
    (6.5, 1.5, 'Search upper right', '#15588b'),
    (2, 5.5, 'Search lower left', '#955200'),
    (6.5, 5.5, 'Excluded\nall > x', '#555555'),
    (2, 3.5, '< x', '#333333'),
    (6.5, 3.5, '> x', '#333333'),
]:
    ax.text(x,y,text,ha='center',va='center',fontsize=12,color=color)
ax.plot([cut,cut],[-.1,rows+.1],color='#333333',lw=1.3,ls='--')
ax.text(-.18,3.5,'middle row',ha='right',va='center',fontsize=11)
ax.text(cut,-.38,'binary-search cut',ha='center',va='center',fontsize=11)
ax.text(4.5,7.65,'Rows increase downward; columns increase to the right',ha='center',fontsize=11)
ax.set_title('Monotone matrix: split the middle row around x',fontsize=15,pad=16)
ax.set_xlim(-1.55,9.15);ax.set_ylim(8.0,-.75);ax.axis('off')
fig.subplots_adjust(left=.03,right=.98,bottom=.06,top=.87)
fig.savefig('imperative-main-2015-matrix-search.png',dpi=140,facecolor='white',metadata={'Software':'codex-wiki figure generator'})
plt.close(fig)
