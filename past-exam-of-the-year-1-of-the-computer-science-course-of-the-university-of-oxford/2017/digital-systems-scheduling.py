"""Original CPU and blocking-I/O schedules; output to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

schedules=[('Nonpreemptive: completion A = 16, B = 17; mean = 16.5 ms',[(0,4,'A'),(4,5,'B'),(5,6,'idle'),(6,10,'A'),(10,11,'B'),(11,12,'idle'),(12,16,'A'),(16,17,'B')],{'A':[(4,6),(10,12)],'B':[(5,7),(11,13)]}),('Quantum 2 ms: completion A = 18, B = 10; mean = 14 ms',[(0,2,'A'),(2,3,'B'),(3,5,'A'),(5,6,'B'),(6,7,'idle'),(7,9,'A'),(9,10,'B'),(10,12,'A'),(12,14,'idle'),(14,16,'A'),(16,18,'A')],{'A':[(5,7),(12,14)],'B':[(3,5),(6,8)]})]
colors={'A':'#3974a4','B':'#c8762e','idle':'#e3e3e3'}
fig,axes=plt.subplots(2,1,figsize=(11,6.5),dpi=100,sharex=True)
for ax,(title,cpu,waits) in zip(axes,schedules):
    for start,end,owner in cpu:
        ax.broken_barh([(start,end-start)],(2.1,.6),facecolor=colors[owner],edgecolor='white')
        ax.text((start+end)/2,2.4,'–' if owner=='idle' else owner,ha='center',va='center',color='#333' if owner=='idle' else 'white',fontsize=10)
    for owner,y in [('A',1.1),('B',.1)]:
        ax.broken_barh([(a,b-a)for a,b in waits[owner]],(y,.6),facecolor=colors[owner],alpha=.33,edgecolor=colors[owner],hatch='///')
    ax.set(xlim=(0,18),ylim=(-.2,3),yticks=[.4,1.4,2.4],yticklabels=['B in I/O','A in I/O','CPU'],xticks=range(19))
    ax.set_title(title,fontsize=12,pad=9);ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
axes[-1].set_xlabel('Time after simultaneous arrival (ms)')
fig.legend(handles=[Patch(facecolor=colors['A'],label='A'),Patch(facecolor=colors['B'],label='B'),Patch(facecolor=colors['idle'],label='idle'),Patch(facecolor='white',edgecolor='#777',hatch='///',label='blocked for I/O')],ncol=4,loc='lower center',bbox_to_anchor=(.5,.005),frameon=False)
fig.subplots_adjust(left=.1,right=.98,bottom=.16,top=.92,hspace=.55)
fig.savefig(Path.cwd()/'digital-systems-scheduling.png',facecolor='white')
