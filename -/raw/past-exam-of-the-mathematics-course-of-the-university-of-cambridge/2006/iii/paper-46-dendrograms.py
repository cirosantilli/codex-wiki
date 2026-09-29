"""Original dendrogram comparison. Python 3.14 / matplotlib 3.10.7.

Emit paper-46-dendrograms.png to caller CWD, respecting caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

order=['A','D','B','E','C']
fig,axes=plt.subplots(1,2,figsize=(9,4.6),dpi=150,facecolor='white')
def draw(ax,merges,title,colour,ticks):
    nodes={label:(i,0) for i,label in enumerate(order)}
    for left,right,height,label in merges:
        x1,h1=nodes[left];x2,h2=nodes[right]
        ax.plot([x1,x1,x2,x2],[h1,height,height,h2],color=colour,lw=2)
        nodes[label]=((x1+x2)/2,height)
    ax.set_xticks(range(len(order)),order);ax.set_ylim(0,11);ax.set_xlim(-.4,4.4)
    ax.set_yticks(ticks);ax.set_ylabel('Merge dissimilarity');ax.set_title(title)
    ax.grid(axis='y',alpha=.2)
    ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
draw(axes[0],[('A','D',1.2,'AD'),('B','E',2.6,'BE'),('AD','BE',4.2,'ADBE'),('ADBE','C',5.4,'ALL')],'Single linkage','#245b8a',[0,1.2,2.6,4.2,5.4])
draw(axes[1],[('A','D',1.2,'AD'),('B','E',2.6,'BE'),('BE','C',7.6,'BCE'),('AD','BCE',10.3,'ALL')],'Complete linkage','#804791',[0,1.2,2.6,7.6,10.3])
fig.suptitle('Same supplied dissimilarities, different cluster merges',fontsize=13)
fig.tight_layout(rect=(0,0,1,.94))
fig.savefig(Path('paper-46-dendrograms.png'),facecolor='white',transparent=False);plt.close(fig)
