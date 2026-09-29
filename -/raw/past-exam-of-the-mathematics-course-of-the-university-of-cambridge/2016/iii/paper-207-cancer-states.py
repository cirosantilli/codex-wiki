"""Cancer progression state diagram; Python 3.14, matplotlib 3.10.7.
Run from the desired output directory; writes paper-207-cancer-states.png there.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(7,2),dpi=120,facecolor='white')
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
for x,label in zip([.16,.5,.84],['1: Disease-free','2: Pre-clinical','3: Clinical']):
 ax.add_patch(FancyBboxPatch((x-.125,.25),.25,.32,boxstyle='round,pad=0.01',facecolor='#edf3fa',edgecolor='#244b77',linewidth=1.5))
 ax.text(x,.41,label,ha='center',va='center',fontsize=11)
for x1,x2,label in [(.30,.36,r'$\lambda=q_{12}$'),(.64,.70,r'$\nu=q_{23}$')]:
 ax.annotate('',xy=(x2,.41),xytext=(x1,.41),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#244b77'})
 ax.text((x1+x2)/2,.64,label,ha='center',fontsize=13)
ax.text(.5,.89,'Irreversible cancer progression',ha='center',fontsize=13)
ax.text(.5,.09,'Clinical state is absorbing; no direct disease-free to clinical transition.',ha='center',fontsize=9)
fig.subplots_adjust(left=.01,right=.99,bottom=.03,top=.98)
fig.savefig('paper-207-cancer-states.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
