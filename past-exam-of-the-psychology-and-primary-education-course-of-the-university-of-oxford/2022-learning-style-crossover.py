"""Original factorial examples, not empirical scores. Python 3.14.4, Matplotlib 3.10.7; output in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

matching=[[80,60],[60,80]]  # rows: preference; columns: assigned format
main_effect=[[80,60],[80,60]]
def contrast(m):return (m[0][0]-m[0][1])-(m[1][0]-m[1][1])
assert contrast(matching)==40 and contrast(main_effect)==0
assert matching[0][0]>matching[0][1] and matching[1][1]>matching[1][0]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10.5})
fig,axs=plt.subplots(1,2,figsize=(7.6,4.0),dpi=100,facecolor='white')
fig.subplots_adjust(left=.085,right=.975,bottom=.26,top=.77,wspace=.3)
for ax,m,title in zip(axs,[matching,main_effect],['Matching prediction','One format helps both groups']):
 ax.plot([0,1],[m[0][0],m[1][0]],'o-',lw=2,color='#347fac',label='Read instruction')
 ax.plot([0,1],[m[0][1],m[1][1]],'s-',lw=2,color='#c76a32',label='Listen instruction')
 ax.set(xlim=(-.2,1.2),ylim=(50,90),xticks=[0,1],xticklabels=['Prefer read','Prefer listen'],yticks=[50,60,70,80,90])
 ax.set_title(title,pad=12,fontsize=11.5)
 ax.set_xlabel('Preference assessed before instruction',fontsize=9.5)
 ax.spines[['top','right']].set_visible(False)
axs[0].set_ylabel('Learning score (hypothetical)')
handles,labels=axs[0].get_legend_handles_labels()
fig.legend(handles,labels,loc='upper center',bbox_to_anchor=(.53,.95),ncol=2,frameon=False)
fig.suptitle('Matching requires opposite within-group format advantages',fontsize=13,y=.995)
fig.text(.5,.06,'Illustrative means, not study data. Randomly assign format within each preference group.\nThe right-hand pattern does not support matching, despite better reading-format scores.',ha='center',va='center',fontsize=9.5)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
