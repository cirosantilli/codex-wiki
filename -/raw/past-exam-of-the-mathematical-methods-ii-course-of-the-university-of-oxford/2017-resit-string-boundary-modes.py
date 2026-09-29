"""Original fixed/free string eigenfunctions. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axs=plt.subplots(1,3,figsize=(10.8,5.4),layout='constrained');x=np.linspace(0,1,1201)
for col,title in enumerate(['Fixed–fixed','Fixed–free','Free–free']):
 ax=axs[col]
 for j in range(3):
  n=j+1 if col!=1 else j;k=n*np.pi if col!=1 else (n+.5)*np.pi;y=np.sin(k*x) if col<2 else np.cos(k*x);offset=3.5-1.5*j
  ax.axhline(offset,color='.8',lw=.8);ax.plot(x,offset+.48*y,lw=2,label=f'n = {n}');ax.text(.04,offset+.58,f'n = {n}',fontsize=10)
  if col==0:
   nodes=np.arange(n+1)/n;ax.plot(nodes,np.full(len(nodes),offset),'o',color='black',ms=3)
  elif col==1:
   nodes=np.arange(n+1)*np.pi/k;ax.plot(nodes,np.full(len(nodes),offset),'o',color='black',ms=3)
 if col==2:
  ax.axhline(-1,color='tab:purple',lw=2);ax.text(.04,-.7,'n = 0: uniform zero mode',fontsize=9);ax.text(.04,-1.25,'translation, not oscillation',fontsize=9)
 else:ax.text(.02,-.7,'Vertical offsets separate modes.',fontsize=9)
 ax.set(xlim=(-.02,1.02),ylim=(-1.5,4.4),xlabel=r'position $x/L$',title=title,yticks=[]);ax.axvline(0,color='.5',lw=1);ax.axvline(1,color='.5',lw=1)
axs[0].set_ylabel('displacement profiles, arbitrary common scale')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
