"""Original MBQC resource diagram; Python 3.14, Matplotlib 3.10.7.
PNG basename output goes only to cwd. Caller supplies MPLCONFIGDIR unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

pos={1:(0,1),3:(2,1),2:(0,0),4:(2,0),5:(4,0)}
fig,ax=plt.subplots(figsize=(8.6,4),dpi=100,facecolor='white')
for i,j in [(1,3),(2,4),(3,4),(4,5)]:
    a,b=pos[i],pos[j];ax.plot([a[0],b[0]],[a[1],b[1]],color='#506273',lw=2.5,zorder=1)
for v,(x,y) in pos.items():
    color='#377ca6' if v in [1,2,4] else '#317d59'
    ax.scatter(x,y,s=720,color=color,zorder=2,edgecolors='white',linewidths=2)
    ax.text(x,y,str(v),color='white',ha='center',va='center',fontsize=13,fontweight='bold')
labels={1:(r'$M(\alpha)$; result $s_1$',(0,1.36)),2:(r'$M(\beta)$; result $s_2$',(0,-.39)),3:(r'$Z$ output; raw $t_3$',(2,1.36)),4:(r'$M((-1)^{s_2}\gamma)$; result $s_4$',(2,-.39)),5:(r'$Z$ output; raw $t_5$',(4,-.39))}
for _,(text,xy) in labels.items():ax.text(*xy,text,ha='center',va='center',fontsize=11)
ax.text(3.7,.9,r'All five vertices start in $|+\rangle$.'+'\n'+'Each edge is a controlled-Z gate.',ha='center',fontsize=10)
ax.set(xlim=(-.75,4.7),ylim=(-.7,1.7));ax.axis('off')
fig.suptitle('Graph-state simulation: two wire paths and one entangling edge',fontsize=13)
fig.text(.5,.07,r'Classical correction: $b_1=t_3\oplus s_1$,  $b_2=t_5\oplus s_4\oplus s_1$',ha='center',fontsize=12)
fig.subplots_adjust(left=.01,right=.99,top=.86,bottom=.20)
fig.savefig(Path('paper-67-measurement-graph.png'),facecolor='white',transparent=False)
plt.close(fig)
