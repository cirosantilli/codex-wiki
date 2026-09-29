from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11})

from matplotlib.patches import Ellipse
fig,axs=plt.subplots(1,2,figsize=(10,4.8),layout='constrained',facecolor='white');ax=axs[0]
ax.plot([.45,.65,1.1],[20.3,22,24],color='#126782');ax.plot([.45,.65,1,1.4],[20.3,18,16,13],color='#b14c2e');ax.plot([.0,.4,.8],[16.5,16.2,16.3],color='#75458d');ax.text(.8,22.5,'A: main sequence');ax.text(1.0,17,'B: giant branch');ax.text(.05,15.5,'C: horizontal branch');ax.annotate('D: turnoff',(.45,20.3),(.03,19.1),arrowprops={'arrowstyle':'->'});ax.annotate('E: helium ignition',(1.4,13),(1.0,14.4),arrowprops={'arrowstyle':'->'});ax.set(xlim=(-.2,1.8),ylim=(25,12),xlabel='Color (schematic)',ylabel='Apparent magnitude',title='Evolutionary regions, not copied cluster data')
ax=axs[1];ax.set_aspect('equal');ax.add_patch(Ellipse((0,0),4,4,fill=False,ls=':',edgecolor='gray'));ax.add_patch(Ellipse((0,0),2.7,2.7,facecolor='#dcebf0',edgecolor='#126782',alpha=.6));ax.add_patch(Ellipse((0,0),.7,.7,color='#e9b949'))
t=np.linspace(0,2.5*np.pi,400);r=.3+.13*t
for phase in [0,np.pi]:ax.plot(r*np.cos(t+phase),r*np.sin(t+phase),color='#126782',lw=2)
ax.text(0,0,'Bulge',ha='center',fontsize=9);ax.text(1.35,1.2,'Gas-rich disk\nand spiral arms',ha='center',fontsize=10);ax.text(0,2.2,'Extended stellar / dark halo',ha='center',fontsize=10);ax.set(xlim=(-2.3,2.3),ylim=(-2.3,2.6),title='Spiral-galaxy components');ax.axis('off')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
