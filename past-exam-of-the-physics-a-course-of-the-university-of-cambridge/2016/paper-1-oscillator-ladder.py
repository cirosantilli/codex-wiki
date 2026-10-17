"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,ax=plt.subplots(figsize=(5.8,4.2));ax.set(xlim=(-.5,3.9),ylim=(-.1,5.1));ax.set_xticks([]);ax.set_yticks([.5,1.5,2.5,3.5,4.5],['1/2','3/2','5/2','7/2','9/2']);ax.set_ylabel('Energy / (ℏω)')
for n in range(5):ax.plot([0,2.5],[n+.5,n+.5],color='#3d657b');ax.text(2.65,n+.5,f'n = {n}',va='center',fontsize=9)
for n in range(4):
 ax.annotate('',xy=(.65,n+1.47),xytext=(.65,n+.53),arrowprops={'arrowstyle':'->','color':'#b87826','lw':1.5});ax.annotate('',xy=(1.85,n+.53),xytext=(1.85,n+1.47),arrowprops={'arrowstyle':'->','color':'#176d97','lw':1.5})
ax.text(.65,4.87,'a† raises',ha='center');ax.text(1.85,4.87,'a lowers',ha='center');ax.text(1.25,.08,'a|0⟩ = 0; no state below the ground state',ha='center',fontsize=8);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
