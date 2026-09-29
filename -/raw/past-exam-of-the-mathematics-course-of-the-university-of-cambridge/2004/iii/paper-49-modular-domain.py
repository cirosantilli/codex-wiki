"""Original plot of the modular fundamental domain; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-.5,.5,501)
y=np.sqrt(1-x*x)
fig,ax=plt.subplots(figsize=(7.5,5.5),dpi=120,facecolor='white')
ax.fill_between(x,y,2.75,color='#d6e9f2')
ax.plot(x,y,color='#21485c',lw=2)
for a in [-.5,.5]:ax.plot([a,a],[np.sqrt(3)/2,2.75],color='#21485c',lw=2)
ax.annotate('',xy=(.5,2.1),xytext=(-.5,2.1),arrowprops={'arrowstyle':'<->','color':'#a74a23','lw':1.8})
ax.text(0,2.19,r'Boundary identification $\tau\mapsto\tau+1$',ha='center',fontsize=10)
ax.text(0,1.6,r'$\mathcal{F}:\ |\mathrm{Re}\,\tau|\leq\frac{1}{2},\ |\tau|\geq1$',ha='center',fontsize=14)
ax.annotate('Continues toward the cusp',xy=(0,2.7),xytext=(0,2.4),ha='center',fontsize=10,arrowprops={'arrowstyle':'->','color':'#21485c'})
ax.plot(0,1,'o',color='#a74a23');ax.text(.04,.96,r'$i$',fontsize=13)
for a in [-.5,.5]:ax.plot(a,np.sqrt(3)/2,'o',color='#a74a23')
ax.text(-.54,.72,r'$e^{2\pi i/3}$',ha='right',fontsize=12)
ax.text(.54,.72,r'$e^{\pi i/3}$',ha='left',fontsize=12)
ax.text(0,.48,r'Arc sides are paired by $\tau\mapsto-1/\tau$',ha='center',fontsize=11)
ax.set(xlim=(-.95,.95),ylim=(.3,2.8),xlabel=r'$\mathrm{Re}\,\tau$',ylabel=r'$\mathrm{Im}\,\tau$')
ax.set_xticks([-.5,0,.5]);ax.set_xticklabels([r'$-1/2$',r'$0$',r'$1/2$'])
ax.set_title('Torus shapes after large-diffeomorphism identifications',fontsize=13,pad=12)
ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.11,right=.965,bottom=.11,top=.88)
fig.savefig(Path.cwd()/'paper-49-modular-domain.png',facecolor='white',transparent=False)
plt.close(fig)
