"""Original teaching plot. Python3.14, NumPy and Matplotlib. Writes basename PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(10.5,4.7),layout='constrained')
for ax,title,mu in [(axs[0],'Intrinsic',.5),(axs[1],'Assumed fully ionized carriers',1.241)]:
 ax.hlines([0,1],0,1,colors='#296c9b',lw=2);ax.hlines(mu,0,1,colors='#a54d2a',linestyles='--',lw=2)
 ax.text(.04,.025,'Valence edge',fontsize=9);ax.text(.04,1.025,'Conduction edge',fontsize=9);ax.text(.04,mu-.065,'Chemical potential',fontsize=9,color='#a54d2a')
 ax.set(title=title,ylim=(-.06,1.35),xlim=(0,1));ax.set_xticks([])
axs[0].set_ylabel('Energy above valence edge (eV)')
axs[2].hlines([0,-.62963],0,1,colors=['#296c9b','#6b6b6b'],linestyles=['solid','dashed'],lw=2)
axs[2].text(.03,.10,'Conduction edge',fontsize=9);axs[2].text(.03,-.51,'Isolated donor reference',fontsize=9)
axs[2].set(title='Shallow-level energy zoom',ylabel='Energy relative to conduction edge (meV)',ylim=(-1,1.1),xlim=(0,1));axs[2].set_xticks([])
fig.suptitle('Overlap invalidates independent donor levels at this density',fontsize=12)

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=140,facecolor='white')
