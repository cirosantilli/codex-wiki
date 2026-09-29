from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})

from matplotlib.patches import Rectangle,FancyArrowPatch
fig,ax=plt.subplots(figsize=(8,4.6),layout='constrained')
ax.set(xlim=(0,10),ylim=(0,6));ax.axis('off')
for xy,w,h in [((.7,4.0),3.0,1.1),((6.2,.6),3.0,1.1)]:
 ax.add_patch(Rectangle(xy,w,h,facecolor='#d8ebf6',edgecolor='#16659c',lw=2))
ax.text(2.2,4.5,'Upper reservoir',ha='center');ax.text(7.7,1.1,'Lower reservoir',ha='center')
ax.plot([3.7,5.2,5.2,6.2],[4.2,4.2,1.1,1.1],color='#55717d',lw=9,solid_capstyle='round')
ax.add_patch(Rectangle((4.25,2.1),1.9,1.0,facecolor='white',edgecolor='#333333',lw=1.5,zorder=4))
ax.text(5.2,2.6,'Reversible\npump–turbine',ha='center',va='center',zorder=5)
ax.annotate('',(1.1,4.0),(1.1,1.7),arrowprops={'arrowstyle':'<->','lw':1.5})
ax.text(.35,2.8,'Head h',rotation=90,va='center')
ax.annotate('Charge: grid power in',(4.25,2.8),(1.1,3.4),arrowprops={'arrowstyle':'->','color':'#b45b14'},color='#b45b14',fontsize=11)
ax.annotate('Discharge: power out',(6.15,2.4),(6.4,3.6),arrowprops={'arrowstyle':'<-','color':'#11703e'},color='#11703e',fontsize=11)
ax.text(6.1,4.7,r'$E_{\rm out}=\eta\rho Vgh$',fontsize=14)
ax.text(6.1,4.1,r'$P_{\rm out}=\eta\rho Qgh$',fontsize=14)
ax.text(2.2,.75,'Pumping raises water.\nDischarge releases it.',ha='center',fontsize=11)
ax.set_title('Pumped storage: a reversible gravitational-energy store')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
