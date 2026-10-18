"""Original piecewise-uniform field-line construction for perpendicular charge sheets."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig,ax=plt.subplots(figsize=(7.2,6.2),layout='constrained')
ax.axvline(0,color='#bc473c',lw=5);ax.axhline(0,color='#2b6291',lw=5)
for sx in [-1,1]:
    for sy in [-1,1]:
        for t in np.linspace(.35,2.8,7):
            start=np.array([0,sy*t]);end=np.array([sx*t,0])
            ax.plot([start[0],end[0]],[start[1],end[1]],color='#4c5960',lw=1.2)
            p=start+.45*(end-start);q=start+.60*(end-start)
            ax.annotate('',q,p,arrowprops={'arrowstyle':'->','color':'#4c5960','lw':1.8})
for y in [-2.7,-1.8,-.9,.9,1.8,2.7]:ax.text(.08,y,'+',color='#bc473c',weight='bold',fontsize=17)
for x in [-2.7,-1.8,-.9,.9,1.8,2.7]:ax.text(x,.05,'−',color='#2b6291',weight='bold',fontsize=17,ha='center')
ax.text(.13,3.0,r'$+\sigma$',color='#bc473c',fontsize=15)
ax.text(2.4,-.35,r'$-\sigma$',color='#2b6291',fontsize=15)
ax.set(xlim=(-3.15,3.15),ylim=(-3.15,3.30),aspect='equal',xlabel='x (arbitrary units)',ylabel='y (arbitrary units)')
ax.set_title('Field lines run from the positive to the negative sheet',pad=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=115,facecolor='white',transparent=False)
