"""Plot the original mathematical region and its centroid; output PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(8.5,6),dpi=100,facecolor='white')
y=np.linspace(-2,2,601);w=2-np.sin(np.pi*y/2)
ax.fill_betweenx(y,-w,w,color='#dbeafe',edgecolor='#315b86',lw=1.7)
ys=-.9;ws=2-np.sin(np.pi*ys/2)
ax.fill_between([-ws,ws],ys-.035,ys+.035,color='#eea23d',alpha=.9)
ax.annotate('',(ws,ys),(-ws,ys),arrowprops={'arrowstyle':'<->','color':'#9a4f08','lw':1.3})
ax.text(0,ys-.2,'strip width = 4 − 2 sin(πy/2)',ha='center',va='top',fontsize=12,color='#92400e')
ax.scatter([0],[-1/np.pi],s=65,color='#b91c1c',zorder=4)
ax.annotate('centroid (0, −1/π)',(0,-1/np.pi),(.75,.25),arrowprops={'arrowstyle':'->','color':'#b91c1c'},color='#b91c1c')
ax.axhline(0,lw=.8,color='#64748b');ax.axvline(0,lw=.8,color='#64748b')
ax.set(xlabel='x',ylabel='y',xlim=(-3.3,3.3),ylim=(-2.3,2.3),aspect='equal',title='Uniform plate: area 16, centroid below the axis')
fig.subplots_adjust(left=.1,right=.97,bottom=.12,top=.9)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white')
plt.close(fig)
