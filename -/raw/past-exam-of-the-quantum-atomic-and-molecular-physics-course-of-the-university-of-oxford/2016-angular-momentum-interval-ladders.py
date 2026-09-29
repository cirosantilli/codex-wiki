"""Original theoretical illustration; Python3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axs=plt.subplots(1,3,figsize=(11.6,4.8),constrained_layout=True,facecolor='white')
for ax,first,second,qs,title,label in [(axs[0],1,1,np.arange(3),'Triplet P fine structure','J'),(axs[1],2.5,2.5,np.arange(6),'55Mn dipole hyperfine','F'),(axs[2],3,2.5,np.arange(.5,6),'56Mn dipole hyperfine','F')]:
 E=.5*(qs*(qs+1)-first*(first+1)-second*(second+1))
 for q,y in zip(qs,E):
  ax.plot([0,1],[y,y],color='#1864ab',lw=2);qtext=f'{q:g}' if q==int(q) else f'{int(2*q)}/2';ax.text(1.07,y,f'{label} = {qtext}',va='center',fontsize=10)
 for i in range(len(qs)-1):
  ax.annotate('',xy=(.35,E[i+1]),xytext=(.35,E[i]),arrowprops={'arrowstyle':'<->','color':'.45'});ax.text(.4,(E[i+1]+E[i])/2,f'{qs[i+1]:g} A',fontsize=8,va='center')
 ax.set(xlim=(-.1,1.9),ylim=(E.min()-1,E.max()+1));ax.set_title(title);ax.set_ylabel('Energy / A');ax.set_xticks([]);ax.spines['bottom'].set_visible(False)
fig.suptitle('Interval rule ladders shown for A >0; measured gap magnitudes do not fix the sign',fontsize=12)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
