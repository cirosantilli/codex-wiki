"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(8,4));x=np.linspace(-3,3,900);ec=np.where(x<0,.9-.15*np.maximum(x+1,0),np.minimum(-.5+.33*x,.45));ax.plot(x,ec,color='#166b9b',lw=2,label='Conduction-band edge');ax.axhline(0,color='.4',ls='--',label='Fermi level');ax.axvline(0,color='.6',ls=':')
wave=np.where(x>=0,np.exp(-((x-.6)/.55)**2),np.exp(-(.6/.55)**2)*np.exp(x*4));ax.plot(x,-.2+.28*wave,color='#ba6a20',label='Ground envelope (offset/scaled)');ax.plot([0,1.0],[-.2,-.2],color='#ba6a20',ls=':')
for xx in np.linspace(-2.7,-1.3,6):ax.text(xx,.66,'+',ha='center',color='#aa4c44')
ax.text(-2,1.05,'Doped AlGaAs',ha='center');ax.text(-.5,1.05,'Undoped\nspacer',ha='center');ax.text(1.6,1.05,'GaAs',ha='center');ax.annotate('2DEG',xy=(.6,-.35),xytext=(1.5,-.6),arrowprops={'arrowstyle':'->'});ax.set(xlabel='Depth across interface (schematic)',ylabel='Energy (arbitrary reference)',ylim=(-.7,1.3));ax.set_xticks([]);ax.legend(loc='lower left',fontsize=8,frameon=False);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
