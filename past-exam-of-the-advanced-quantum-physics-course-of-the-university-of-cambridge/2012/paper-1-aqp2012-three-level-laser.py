"""Original figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; PNG basename written to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(8.1,4.7),layout='constrained')
for y,label in [(0,'1: ground /\nlower laser state'),(2,'2: metastable\nupper laser state'),(3.6,'3: pump state')]:ax.hlines(y,.38,1.02,color='.25',lw=2.3);ax.text(.03,y,label,ha='left',va='center',fontsize=10)
ax.annotate('',(.46,3.57),(.46,.03),arrowprops={'arrowstyle':'->','color':'#2878a3','lw':2.5});ax.text(.42,1,'Pump',rotation=90,ha='center',va='center',color='#2878a3')
ax.annotate('',(.94,2.03),(.94,3.57),arrowprops={'arrowstyle':'->','color':'#387850','lw':2.5});ax.text(.99,2.78,'Fast relaxation',rotation=90,ha='center',va='center',color='#387850')
ax.annotate('',(.68,.03),(.68,1.97),arrowprops={'arrowstyle':'->','color':'#b25426','lw':2.7});ax.text(.72,1,'Stimulated emission\n'+r'$\hbar\omega=E_2-E_1$',ha='left',va='center',color='#b25426')
ax.text(.63,-.5,r'Equal degeneracies: $N_2>N_1$; $\tau_{32}\ll\tau_{21}$',ha='center',fontsize=11)
ax.set(xlim=(0,1.23),ylim=(-.8,4.08),title='Three-level laser: pump, storage and stimulated emission');ax.axis('off')
fig.savefig(Path(__file__).stem+'.png',dpi=155,facecolor='white');plt.close(fig)
