from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})

from matplotlib.patches import Circle
fig,axs=plt.subplots(1,3,figsize=(12,4.4),layout='constrained',facecolor='white')
ax=axs[0];labels=['Central point','Saturn','Jupiter','Earth','Uniform sphere','Thin shell'];vals=[0,.21,.264,.331,.4,2/3];ax.barh(labels,vals,color=['gray','#126782','#126782','#126782','#b14c2e','#b14c2e']);ax.set(xlim=(0,.75),xlabel=r'$C/(MR^2)$',title='Central concentration benchmarks')
for ax,title,metal,core in [(axs[1],'Jupiter (schematic)',.65,.22),(axs[2],'Saturn (schematic)',.5,.3)]:
 ax.add_patch(Circle((0,0),1,color='#e9cc8c'));ax.add_patch(Circle((0,0),metal,color='#b14c2e'));ax.add_patch(Circle((0,0),core,color='#545f71'));ax.text(0,1.27,'Molecular H/He envelope',ha='center',fontsize=10);ax.text(0,-1.28,'Metallic-H-rich interior\nand central heavy-element enrichment',ha='center',fontsize=9);ax.set(xlim=(-1.3,1.3),ylim=(-1.6,1.6),title=title);ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Layer radii are illustrative; a measured moment does not uniquely fix an interior profile.',fontsize=11)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
