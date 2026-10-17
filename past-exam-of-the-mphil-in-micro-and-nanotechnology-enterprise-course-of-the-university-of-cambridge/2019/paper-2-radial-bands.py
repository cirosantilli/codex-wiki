"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(7,4));xs=[0,1,1.35,2.35];ec=[2.02,2.6,1.8];ev=[0,-.4,0]
for i in range(3):
 ax.plot(xs[i:i+2],[ec[i]]*2,color='#126c9b',lw=2);ax.plot(xs[i:i+2],[ev[i]]*2,color='#b26922',lw=2)
 if i<2:
  ax.plot([xs[i+1]]*2,[ec[i],ec[i+1]],color='#126c9b',lw=2);ax.plot([xs[i+1]]*2,[ev[i],ev[i+1]],color='#b26922',lw=2)
for x,e,lab in [(.5,2.02,'2.02 eV'),(1.85,1.8,'1.80 eV')]:
 ax.annotate('',xy=(x,0),xytext=(x,e),arrowprops={'arrowstyle':'<->','color':'.35'});ax.text(x+.05,e/2,lab,va='center')
ax.axvspan(1,1.35,color='#eee3f1',alpha=.65);ax.text(.45,2.85,'Core',ha='center');ax.text(1.175,2.85,'Al-rich\nbarrier',ha='center',fontsize=9);ax.text(1.85,2.85,'Shell',ha='center');ax.text(2.4,1.8,'Ec',va='center');ax.text(2.4,0,'Ev',va='center')
ax.set(xlim=(-.05,2.6),ylim=(-.65,3.2),xlabel='Radial path toward the outer surface (schematic)',ylabel='Energy (eV; arbitrary reference)');ax.set_xticks([]);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
