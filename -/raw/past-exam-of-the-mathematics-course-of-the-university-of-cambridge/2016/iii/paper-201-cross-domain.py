"""Generate paper-201-cross-domain.png in cwd only.
Tested with Python 3.14.4 and matplotlib 3.10.7; uses root pyproject.toml.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(6.4,4),layout='constrained')
ax.add_patch(Rectangle((-1,-3.2),2,6.4,facecolor='#e5f1fa',edgecolor='none'))
ax.add_patch(Rectangle((-3.2,-1),6.4,2,facecolor='#e5f1fa',edgecolor='none'))
colors={'a':'#a93425','b':'#6b4299','c':'#b77813','d':'#24835b'}
for label,sx,sy in [('a',1,1),('b',-1,1),('c',-1,-1),('d',1,-1)]:
 ax.plot([sx,sx],[sy,sy*3.2],color=colors[label],lw=2.4)
 ax.plot([sx,sx*3.2],[sy,sy],color=colors[label],lw=2.4)
 ax.text(sx*1.45,sy*1.45,label,color=colors[label],fontsize=16,ha='center',va='center')
ax.plot([-1,1],[1,1],color='#657386',ls='--',lw=1)
ax.text(0,.73,r'Auxiliary level $y=1$',fontsize=8,ha='center')
ax.text(0,2.2,'Upper arm',ha='center',fontsize=10)
ax.text(0,1.8,r'$b$ at left; $a$ at right',ha='center',fontsize=8)
ax.text(0,0,r'$D=\{|x|<1\}\cup\{|y|<1\}$',ha='center',fontsize=10)
ax.set_xlim(-3.2,3.2);ax.set_ylim(-3.2,3.2);ax.set_aspect('equal')
ax.set_xticks([-3,-1,0,1,3]);ax.set_yticks([-3,-1,0,1,3])
ax.set_xlabel('$x$');ax.set_ylabel('$y$');ax.set_title('Cross-shaped domain and boundary components',fontsize=12)
ax.spines[['top','right']].set_visible(False)
fig.savefig('paper-201-cross-domain.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
