"""Original discriminant sketch. Tested Python 3.14 / matplotlib 3.10.7.

Emit paper-46-beetles.png to the caller's CWD. Respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(7.2,5.1),dpi=150,facecolor='white')
x=np.linspace(-.5,10,300);equal=.4*x+4.4;shift=equal+.8*math.log(2)
ax.fill_between(x,0,equal,color='#dceef6');ax.fill_between(x,equal,11,color='#f4e1e1')
ax.plot(x,equal,color='#244e73',lw=2,label='Equal priors: eating/2 - 5 rest/4 + 5.5 = 0')
ax.plot(x,shift,color='#8b4c18',lw=2,ls='--',label='Fattus : apathus = 2 : 1')
points=np.array([[0,5],[0,3],[4,7],[5,6],[9,8]])
colours=['#a13f3f','#236c89','#a13f3f','#236c89','#555555']
for i,((a,b),colour) in enumerate(zip(points,colours),start=1):
    ax.scatter(a,b,color=colour,edgecolors='white',s=65,zorder=5)
    offset={1:(8,8),2:(8,-15),3:(-14,10),4:(8,-16),5:(8,-16)}[i]
    ax.annotate(str(i),xy=(a,b),xytext=offset,textcoords='offset points',fontsize=11,fontweight='bold')
ax.text(6.9,1.7,'Fattus region',color='#236c89',fontsize=13)
ax.text(1.5,9.8,'Apathus region',color='#a13f3f',fontsize=13)
ax.annotate('5 is a tie with equal priors',xy=(9,8),xytext=(5.2,9.1),arrowprops={'arrowstyle':'->','color':'#555'},fontsize=10)
ax.set_xlim(-.5,10);ax.set_ylim(0,11);ax.set_xlabel('Time eating');ax.set_ylabel('Time at rest')
ax.set_title('Beetle classification and the effect of prior odds')
ax.legend(loc='lower left',fontsize=8.4,framealpha=1)
ax.grid(alpha=.17);fig.tight_layout()
fig.savefig(Path('paper-46-beetles.png'),facecolor='white',transparent=False);plt.close(fig)
