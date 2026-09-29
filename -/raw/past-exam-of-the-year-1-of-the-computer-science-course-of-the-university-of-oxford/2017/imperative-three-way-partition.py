"""Draw the generic four-region invariant, writing the PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14})
fig,ax=plt.subplots(figsize=(11,3.5),dpi=100,facecolor='white')
ax.set(xlim=(-.6,12.6),ylim=(-1.4,2.8));ax.axis('off')
ax.text(6,2.2,'Three-way partition: save the pivot value x',ha='center',fontsize=19,weight='bold')
for left,right,label,color in [(0,3,'< x','#dbeafe'),(3,6,'= x','#dcfce7'),(6,9,'unclassified','#fef3c7'),(9,12,'> x','#ffedd5')]:
    ax.add_patch(Rectangle((left,.5),right-left,.85,facecolor=color,edgecolor='#334155',linewidth=1.5))
    ax.text((left+right)/2,.925,label,ha='center',va='center',fontsize=16)
for x,label in [(0,'l'),(3,'m'),(6,'k'),(9,'n'),(12,'r')]:
    ax.plot([x,x],[.35,.5],color='#334155');ax.text(x,.12,label,ha='center',va='center',fontsize=16)
ax.annotate('',(9,-.35),(6,-.35),arrowprops={'arrowstyle':'<->','lw':1.5,'color':'#92400e'})
ax.text(7.5,-.67,'n − k decreases by one',ha='center',color='#92400e')
ax.text(6,-1.15,'At completion k = n; the nonempty equality interval is [m, n).',ha='center',fontsize=13)
fig.subplots_adjust(left=.025,right=.975,bottom=.03,top=.97)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
