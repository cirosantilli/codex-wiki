"""Original worked example; Python 3.14.4, Matplotlib 3.10.7. PNG is written to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch

assert 8+5==13 and 8+2+3==13
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axs=plt.subplots(2,1,figsize=(7.6,3.8),dpi=100,facecolor='white')
fig.subplots_adjust(left=.055,right=.975,bottom=.1,top=.9,hspace=.25)
blue='#347fac';orange='#c76a32'
top,bottom=axs
top.set(xlim=(-.6,13.6),ylim=(-.8,1.5));top.axis('off')
for i in range(13):top.add_patch(Circle((i+.5,.25),.20,facecolor=blue if i<8 else orange,edgecolor='white'))
top.text(4,1.05,'8 already represented',color=blue,ha='center')
top.text(10.5,1.05,'5 more',color=orange,ha='center')
top.text(6.5,-.48,'The sum contains 13 objects; the starting eight need not be recounted.',ha='center',fontsize=10.5)
bottom.set(xlim=(-.6,13.6),ylim=(-.65,1.15));bottom.axis('off')
bottom.plot([0,13],[0,0],color='#425563',lw=1.5)
for x in range(14):
 bottom.plot([x,x],[-.055,.055],color='#425563',lw=1.2)
 bottom.text(x,-.2,str(x),ha='center',va='top',color=blue if x==8 else '#263945')
for x in range(8,13):
 bottom.add_patch(FancyArrowPatch((x,.07),(x+1,.07),connectionstyle='arc3,rad=-.65',arrowstyle='-|>',mutation_scale=12,linewidth=1.5,color=orange))
bottom.text(8,.75,'Start at 8',ha='center',color=blue)
bottom.text(11,.75,'Five unit steps',ha='center',color=orange)
bottom.text(6.5,-.55,'8 + 5 = 13',ha='center',fontsize=13,weight='bold')
fig.suptitle('Counting on connects a known quantity with added units',fontsize=13.5,y=.98)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
