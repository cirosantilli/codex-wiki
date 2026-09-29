"""Original diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Preserve caller MPLCONFIGDIR; output only this PNG basename to cwd.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(10,4.2),dpi=100,layout='constrained')
red='#b52b40';blue='#1857b2'
ax.add_patch(Rectangle((0,.2),4,2,facecolor='#eef4f7',edgecolor=red,lw=3))
ax.plot([2,2],[.2,2.2],color='gray',ls=':',lw=2)
ax.text(2,2.55,'Connected rectangle',ha='center',fontsize=12)
ax.text(2,-.25,'D on every exterior side; dotted line is internal',ha='center',fontsize=10)
ax.text(1,1.2,'left tile',ha='center');ax.text(3,1.2,'reflected\nright tile',ha='center')
for x,name,mixed in [(5.5,'Odd sector',False),(8,'Even sector',True)]:
 ax.add_patch(Rectangle((x,.2),2,2,facecolor='#eef4f7',edgecolor=red,lw=3))
 if mixed:ax.plot([x+2,x+2],[.2,2.2],color=blue,ls='--',lw=4)
 ax.text(x+1,2.55,name,ha='center',fontsize=12)
 ax.text(x+1,1.2,'all D' if not mixed else 'D on three sides\nN on the cut',ha='center',fontsize=10)
ax.annotate('',xy=(5.2,1.2),xytext=(4.3,1.2),arrowprops=dict(arrowstyle='->',lw=2))
ax.text(7.75,-.25,'Two disconnected components',ha='center',fontsize=10)
ax.plot([2.3,2.8],[-.9,-.9],color=red,lw=3);ax.text(2.95,-.9,'D: Dirichlet',va='center')
ax.plot([6.1,6.6],[-.9,-.9],color=blue,ls='--',lw=3);ax.text(6.75,-.9,'N: Neumann',va='center')
ax.set(xlim=(-.4,10.5),ylim=(-1.2,3.1));ax.set_aspect('equal');ax.axis('off')
fig.savefig('paper-12-reflection-transplantation.png',facecolor='white',transparent=False)
