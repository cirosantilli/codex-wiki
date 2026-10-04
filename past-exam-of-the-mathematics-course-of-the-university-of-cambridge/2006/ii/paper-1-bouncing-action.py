"""Original elastic-bounce phase-space cycle; Python 3.14, root Matplotlib."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,4),facecolor='white')
ax.fill([0,1,1,0],[1,1,-1,-1],color='#e6f0f7')
for start,end in [((0,1),(1,1)),((1,1),(1,-1)),((1,-1),(0,-1)),((0,-1),(0,1))]:
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#225b88','lw':2})
ax.text(.5,0,'$I=2bp_0$',ha='center',va='center',fontsize=16);ax.text(1.04,.2,'elastic\nreflection',fontsize=10)
ax.set(xlim=(-.12,1.35),ylim=(-1.35,1.4),xlabel='Position $q$',ylabel='Momentum $p$',title='One cycle between the two walls')
ax.set_xticks([0,1],['0','$b$']);ax.set_yticks([-1,0,1],['$-p_0$','0','$p_0$'])
ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig('paper-1-bouncing-action.png',dpi=150,facecolor='white')
