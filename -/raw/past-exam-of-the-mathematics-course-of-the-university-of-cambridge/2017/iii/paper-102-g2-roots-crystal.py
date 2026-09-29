"""Original G2 root system and seven-dimensional crystal; output PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(11,6),dpi=100,facecolor='white')
ax=fig.add_axes([.055,.12,.53,.78]);chain=fig.add_axes([.64,.09,.32,.82])
a1=np.array([np.sqrt(2),0]);a2=np.array([-3/np.sqrt(2),np.sqrt(1.5)])
positive=[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]
short={(1,0),(1,1),(2,1)}
for p in positive:
    root=p[0]*a1+p[1]*a2;color='#2468a2' if p in short else '#c53b36'
    for sign in [1,-1]:
        r=sign*root;ax.annotate('',xy=r,xytext=(0,0),arrowprops=dict(arrowstyle='->',color=color,lw=1.7))
        ax.scatter(*r,s=28,color=color,zorder=3)
        label=rf'$({sign*p[0]},{sign*p[1]})$'
        ax.text(*(1.28*r),label,color=color,ha='center',va='center',fontsize=11)
ax.axhline(0,color='#c7c7c7',lw=.6,zorder=0);ax.axvline(0,color='#c7c7c7',lw=.6,zorder=0)
ax.set(xlim=(-3.45,3.45),ylim=(-3.45,3.45),aspect='equal');ax.axis('off')
ax.set_title(r'$G_2$: six short roots and six long roots',fontsize=13,pad=15)
fig.text(.31,.102,r'Coordinates are coefficients of $(\alpha_1,\alpha_2)$; $\alpha_1$ is short.',ha='center',fontsize=10)
weights=[(2,1),(1,1),(1,0),(0,0),(-1,0),(-1,-1),(-2,-1)];colors=[1,2,1,1,2,1]
for j,w in enumerate(weights):
    y=6-j;chain.scatter([0],[y],s=80,facecolor='white',edgecolor='#253746',zorder=4)
    chain.text(.27,y,rf'$v_{j}:\ ({w[0]},{w[1]})$',fontsize=12,va='center')
for j,c in enumerate(colors):
    color='#2468a2' if c==1 else '#c53b36'
    chain.annotate('',xy=(0,5-j+.16),xytext=(0,6-j-.16),arrowprops=dict(arrowstyle='->',color=color,lw=1.8))
    chain.text(-.14,5.5-j,str(c),color=color,fontsize=12,ha='right',va='center')
chain.set(xlim=(-.45,1.6),ylim=(-.5,6.55));chain.axis('off');chain.set_title(r'Crystal of $L(\omega_1)$ (dimension 7)',fontsize=13)
fig.text(.31,.04,r'$|\alpha_2|/|\alpha_1|=\sqrt{3}$',ha='center',fontsize=12)
fig.text(.8,.035,'Each arrow subtracts the indicated simple root.',ha='center',fontsize=10)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
