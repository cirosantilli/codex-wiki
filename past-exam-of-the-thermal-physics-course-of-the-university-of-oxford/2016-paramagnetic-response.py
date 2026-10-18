from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
fig,ax=plt.subplots(figsize=(6.8,4.3),dpi=130,facecolor='white')
t=np.linspace(.35,4,500)
ax.plot(t,1/t,lw=2.5,color='#2268a3')
ax.scatter([1],[1],color='#b13939',s=30)
ax.axhline(0,color='0.6',lw=.8)
ax.annotate(r'$m=\alpha B/T$',xy=(1.5,2/3),xytext=(2.1,1.4),arrowprops={'arrowstyle':'->','color':'0.3'})
ax.text(.57,2.47,'Weak-field model only:\nsaturation not represented',fontsize=10)
ax.set(xlim=(.25,4.1),ylim=(-.04,3),xlabel=r'$T/T_*$ ',ylabel=r'$m/(\alpha B/T_*)$',title='Fixed positive field, zero high-temperature offset')
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
