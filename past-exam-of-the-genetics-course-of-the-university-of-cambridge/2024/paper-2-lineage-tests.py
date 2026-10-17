"""Original hypothetical lineage/validation scheme; Python 3.14, matplotlib. Output to cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch,FancyArrowPatch
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(12,6.4),facecolor='white');ax.set(xlim=(0,12),ylim=(0,6.4));ax.axis('off')
def cell(x,y,barcode,state='',color='#dcebf8'):
 ax.add_patch(Circle((x,y),.34,fc=color,ec='#315e7d',lw=1.4));ax.text(x,y,barcode,ha='center',va='center',fontsize=11)
 if state:ax.text(x,y-.6,state,ha='center',va='top',fontsize=10)
def arrow(a,b,color='#315e7d'):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color=color,lw=1.4))
ax.text(6,6.14,'Cell identity and cell ancestry are different observations',ha='center',fontsize=15,weight='bold')
ax.text(2.8,5.52,'One verified founder, two outputs',ha='center',fontsize=12,weight='bold')
cell(2.8,4.72,'a','imaged founder')
cell(1.45,3.17,'a+b','neuron X');cell(4.15,3.17,'a+c','glial cell Y',color='#e5f0d9')
arrow((2.52,4.46),(1.68,3.46));arrow((3.08,4.46),(3.92,3.46))
ax.text(2.8,2.15,'Mixed output supports clonal multipotency\nonly if labelling collisions are excluded.',ha='center',fontsize=10)
ax.text(8.95,5.52,'Two founders, the same mature state',ha='center',fontsize=12,weight='bold')
cell(7.7,4.72,'d');cell(10.2,4.72,'e');cell(7.7,3.17,'d+f','neuron X');cell(10.2,3.17,'e+g','neuron X')
arrow((7.7,4.34),(7.7,3.55));arrow((10.2,4.34),(10.2,3.55))
ax.text(8.95,2.15,'Matching expression does not establish\na recent common labelled progenitor.',ha='center',fontsize=10)
ax.plot([6,6],[1.9,5.55],color='0.85')
for x,w,t in [(2.1,3.5,'Sparse optical trace\nvalidates parent–daughter links'),(6,3.5,'Ablation + replacement tracing\ntests necessity and compensation'),(9.9,3.5,'Mosaic perturbation + rescue\ntests a proposed fate regulator')]:
 ax.add_patch(FancyBboxPatch((x-w/2,.52),w,.86,boxstyle='round,pad=.08',fc='#f0f3f7',ec='#737d8c'));ax.text(x,.95,t,ha='center',va='center',fontsize=10)
ax.text(6,.12,'Hypothetical barcodes and outputs: schematic design, not an observed zebrafish lineage.',ha='center',fontsize=10)
fig.tight_layout();fig.savefig('paper-2-lineage-tests.png',dpi=165,facecolor='white',bbox_inches='tight');plt.close(fig)
