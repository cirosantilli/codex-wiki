from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12})

from matplotlib.patches import Rectangle
fig,axs=plt.subplots(3,1,figsize=(10,6),layout='constrained',facecolor='white')
for ax,nb,title,achrom in zip(axs,[2,5,1],['Double-bend achromat','Multi-bend achromat','Non-achromatic minimum-emittance cell'],[True,True,False]):
 ax.plot([0,10],[0,0],color='gray');positions=np.linspace(2,8,nb) if nb>1 else [5]
 for z in positions:ax.add_patch(Rectangle((z-.24,-.2),.48,.4,color='#126782'));ax.text(z,-.5,'B',ha='center')
 for z in [1,9]:ax.add_patch(Rectangle((z-.1,-.3),.2,.6,color='#75458d'));ax.text(z,-.5,'Q',ha='center')
 xx=np.linspace(0,10,400);eta=.25+.65*np.sin(np.pi*xx/10)**2
 if achrom:eta=np.sin(np.pi*xx/10)**2
 ax.plot(xx,eta+.3,'--',color='#b14c2e',label='Schematic dispersion (offset)')
 ax.set(xlim=(-.2,10.2),ylim=(-.8,1.7));ax.axis('off');ax.set_title(title);ax.legend(loc='upper right',fontsize=9)
fig.suptitle('B: bending magnet; Q: quadrupole. Layouts are schematic, not optimized lattices.',fontsize=12)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
