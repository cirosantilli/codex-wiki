"""Original conceptual figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

from matplotlib.patches import FancyArrowPatch
fig,axs=plt.subplots(2,2,figsize=(10,6.5),gridspec_kw={'height_ratios':[1,1.15]},constrained_layout=True,facecolor='white')
for j,coherent in enumerate([True,False]):
 ax=axs[0,j];pos={'X':(.15,.35),'Y':(.5,.85),'Z':(.85,.35)}
 for name,(x,y) in pos.items():ax.text(x,y,name,ha='center',va='center',bbox={'boxstyle':'circle','fc':'white','ec':'.3'},fontsize=14)
 for start,end in [('X','Y'),('X','Z'),('Y','Z')]:
  x,y=pos[start];xx,yy=pos[end];inhib=(start=='Y' and not coherent)
  ax.add_patch(FancyArrowPatch((x,y),(xx,yy),shrinkA=20,shrinkB=20,arrowstyle='-[' if inhib else '->',mutation_scale=17,lw=1.7,color='#c92a2a' if inhib else '#1864ab'))
 ax.text(.5,.12,'Output AND gate',ha='center');ax.set(xlim=(0,1),ylim=(0,1.1));ax.axis('off');ax.set_title('Coherent C1' if coherent else 'Incoherent I1')
 t=np.linspace(0,12,1200);start=.5;end=8.;delay=-np.log(1-.65);z=np.zeros_like(t)
 if coherent:
  active=(t>=start+delay)&(t<end);z[active]=1-np.exp(-(t[active]-start-delay));last=1-np.exp(-(end-start-delay));z[t>=end]=last*np.exp(-(t[t>=end]-end))
 else:
  active=(t>=start)&(t<start+delay);z[active]=1-np.exp(-(t[active]-start));last=1-np.exp(-delay);z[t>=start+delay]=last*np.exp(-(t[t>=start+delay]-start-delay))
 ax=axs[1,j];ax.plot(t,((t>=start)&(t<end)).astype(float),color='.5',ls='--',label='Input');ax.plot(t,z,lw=2,color='#1864ab' if coherent else '#c92a2a',label='Output')
 ax.axvline(start+delay,color='.7',lw=1,ls=':');ax.set(xlabel='Time / intermediate lifetime',ylabel='Normalized level',ylim=(-.03,1.08));ax.legend(frameon=False);ax.grid(alpha=.15)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
