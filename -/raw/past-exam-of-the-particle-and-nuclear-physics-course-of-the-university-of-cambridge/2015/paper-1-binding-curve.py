from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(figsize=(8,3.6))
x=np.linspace(0,1,500);y=(1-np.exp(-9*x))*(1-.35*x);peak=x[np.argmax(y)]
ax.plot(x,y,lw=2,color='tab:blue');ax.fill_between(x,0,y,color='tab:blue',alpha=.06)
ax.annotate('Light-nucleus fusion',xy=(.28,float(np.interp(.28,x,y))),xytext=(.02,.43),arrowprops={'arrowstyle':'->','lw':1.8,'color':'tab:orange'},fontsize=10)
ax.annotate('Heavy-nucleus fission',xy=(.62,float(np.interp(.62,x,y))),xytext=(.71,.4),arrowprops={'arrowstyle':'->','lw':1.8,'color':'tab:orange'},fontsize=10)
ax.annotate('Broad maximum\n(iron/nickel region)',xy=(peak,float(y.max())),xytext=(peak+.16,1.01),arrowprops={'arrowstyle':'->'},ha='center',fontsize=10)
ax.set(xlim=(0,1),ylim=(0,1.19),xticks=[.02,peak,.97],xticklabels=['Light nuclei','Intermediate nuclei','Heavy nuclei'],yticks=[],ylabel='Binding energy per nucleon (schematic)',xlabel='Increasing nucleon number',title='Energy release follows an increase in total nuclear binding')
ax.text(.01,.04,'Qualitative curve only; not fitted nuclear mass data',transform=ax.transAxes,fontsize=8)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white',bbox_inches='tight')
plt.close(fig)
