from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axs=plt.subplots(2,2,figsize=(11.3,8),layout='constrained')
ax=axs[0,0]
for x,w,label,col in [(0,.6,'source','#ece8df'),(1.1,.6,'polarizer','#e4e9ef'),(2.55,.28,'thin\nsample','#b2cfdf'),(3.8,.7,'detector','#e6ebdf')]:
 ax.add_patch(Rectangle((x,-.55),w,1.1,fc=col,ec='black'));ax.text(x+w/2,0,label,ha='center',va='center',fontsize=10)
for a,b in [(.65,1.05),(1.75,2.5),(2.87,3.75)]:ax.annotate('',xy=(b,0),xytext=(a,0),arrowprops=dict(arrowstyle='->',color='#b35b15',lw=2))
ax.annotate('B',xy=(3.5,.9),xytext=(1.8,.9),arrowprops=dict(arrowstyle='->',lw=2));ax.text(2.8,-.95,'B parallel to propagation',ha='center');ax.set(xlim=(-.2,4.8),ylim=(-1.3,1.4));ax.axis('off');ax.set_title('Semiconductor: bulk transmission')
ax=axs[0,1];ax.axvspan(0,2.8,color='#eaf0f5');ax.axvspan(0,.25,color='#eac79c',alpha=.8);ax.add_patch(Circle((1.25,0),1.15,fill=False,ec='#174c75',lw=2))
ax.text(1.3,0,'electron orbit',ha='center');ax.text(.12,1.23,'skin\nlayer',ha='center',fontsize=9);ax.text(2.15,.8,'B out of plane\n(parallel to surface)',ha='center',fontsize=9)
ax.annotate('',xy=(.13,.55),xytext=(.13,-.5),arrowprops=dict(arrowstyle='<->',lw=2,color='#b35b15'));ax.text(-.15,0,'rf E',rotation=90,ha='right');ax.text(1.4,-1.45,'Detect reflection / cavity loss',ha='center');ax.set(xlim=(-.7,2.9),ylim=(-1.75,1.75));ax.set_aspect('equal');ax.axis('off');ax.set_title('Metal: surface-sensitive coupling')
ax=axs[1,0];b=np.linspace(.4,1.6,700);T=1-.7/(1+((b-1)/.055)**2);ax.plot(b,T,color='#174c75',lw=2);ax.set(xlabel=r'$B/B_{res}$',ylabel='Transmission (schematic)',title='Fundamental cyclotron dip');ax.grid(alpha=.2)
ax=axs[1,1];x=np.linspace(.4,4.7,1000);loss=sum((.7/n)/(1+((x-n)/.06)**2) for n in range(1,5));ax.plot(x,loss,color='#b35b15',lw=2)
for n in range(1,5):ax.text(n,.76/n,str(n),ha='center')
ax.set(xlabel=r'$B_1/B$ (proportional to $1/B$)',ylabel='Surface loss (schematic)',title=r'Return harmonics: $\omega=n\omega_c$');ax.grid(alpha=.2)
axs[1,1].set_ylim(0,.88)
fig.suptitle('Cyclotron resonance: different screening implies different apparatus',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
