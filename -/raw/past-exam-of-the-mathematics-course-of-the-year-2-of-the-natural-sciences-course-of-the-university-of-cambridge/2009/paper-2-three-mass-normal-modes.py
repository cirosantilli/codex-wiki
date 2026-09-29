"""Original mode-shape diagram, illustrative M=4; PNG into cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(9,4.6),facecolor='white');mass=4
modes=[([1,1,1],r'Translation: $\omega=0$'),([1,0,-1],r'Antisymmetric: $\omega=1$'),([1,-2/mass,1],r'Symmetric: $\omega=\sqrt{1+2/M}$')]
for row,(v,label) in enumerate(modes):
 yy=2-row
 for start,end in [(-1,0),(0,1)]:
  xx=np.linspace(start+.1,end-.13,60);zig=.055*np.sin(np.linspace(0,10*np.pi,60));ax.plot(xx,yy+zig,color='gray',lw=1.3)
 ax.scatter([-1,1],[yy,yy],s=150,color='#247ba0',zorder=3);ax.scatter([0],[yy],s=340,color='#247ba0',zorder=3)
 for xx,amp in zip([-1,0,1],v):
  if amp:ax.annotate('',(xx+.35*amp,yy+.3),(xx,yy+.3),arrowprops={'arrowstyle':'->','color':'#ba3434','lw':2})
  else:ax.text(xx,yy+.3,'fixed',ha='center',fontsize=9)
 ax.text(-1.85,yy,label,va='center',ha='right',fontsize=11)
 ax.text(1.6,yy,str(tuple(v)),va='center',fontsize=10)
ax.text(-1,-.45,'unit mass',ha='center');ax.text(0,-.45,'M = 4 shown',ha='center');ax.text(1,-.45,'unit mass',ha='center')
ax.set(xlim=(-4.2,3.2),ylim=(-.7,2.65),title='Relative displacements of the three modes; unit spring constants');ax.axis('off')
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white');plt.close(fig)
