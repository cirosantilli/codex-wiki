"""Original toric fan and fibre schematics; write opaque basename PNG to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11})
fig=plt.figure(figsize=(10.5,7.2),facecolor='white')
grid=fig.add_gridspec(2,2,height_ratios=[1.5,1],width_ratios=[1.75,1])
fan=fig.add_subplot(grid[0,0]);cycle=fig.add_subplot(grid[0,1]);chain=fig.add_subplot(grid[1,:])
for i in range(-3,3):
 fan.fill([0,i,i+1],[0,1,1],color=('#d9eaf2' if i%2 else '#f2e3d6'),zorder=0)
 fan.text(i+.5,.86,rf'$\sigma_{{{i}}}$',ha='center',fontsize=10)
for i in range(-3,4):
 fan.plot([0,i],[0,1],color='#256b92',lw=1.5)
 fan.scatter([i],[1],s=20,color='#256b92')
 fan.text(i,1.07,rf'$v_{{{i}}}$',ha='center')
fan.axhline(0,color='#7b858c',lw=.7);fan.axvline(0,color='#7b858c',lw=.7)
fan.plot([-3.3,3.3],[1,1],'--',color='#a4aeb5',lw=.8)
fan.text(-3.3,.45,'…',ha='right',fontsize=20);fan.text(3.3,.45,'…',fontsize=20)
fan.set(xlim=(-3.8,3.8),ylim=(-.12,1.34),xticks=range(-3,4),yticks=[0,1],
        xlabel='First lattice coordinate',ylabel='Second lattice coordinate',title=r'Consecutive rays $v_i=(i,1)$')

pts=np.array([[0,1.05],[-.92,-.6],[.92,-.6]])
colors=['#256b92','#c0783c','#657f4b']
for i in range(3):
 a,b=pts[i],pts[(i+1)%3];cycle.plot([a[0],b[0]],[a[1],b[1]],lw=3,color=colors[i])
 mid=(a+b)/2;shift=[(-.2,.05),(0,-.18),(.2,.05)][i]
 cycle.text(mid[0]+shift[0],mid[1]+shift[1],rf'$D_{{{i}}}$',ha='center',fontsize=12)
cycle.scatter(pts[:,0],pts[:,1],s=45,color='#38444d',zorder=3)
cycle.text(0,.02,r'$i\sim i+3$',ha='center',fontsize=13)
cycle.set(xlim=(-1.4,1.4),ylim=(-1,1.5),aspect='equal',title='Period-three quotient fibre')
cycle.axis('off')

for i in range(-3,4):
 x=i+3
 chain.plot([x,x+1],[0,0],lw=4,color=colors[i%3])
 chain.text(x+.5,.16,rf'$D_{{{i}}}\cong\mathbf{{P}}^1_{{\mathbf{{Z}}}}$',ha='center',fontsize=11)
for i in range(-3,3):
 x=i+4
 chain.scatter([x],[0],s=42,color='#38444d',zorder=3)
 chain.text(x,-.16,rf'$p_{{{i}}}$',ha='center',fontsize=10)
chain.text(-.45,0,'…',va='center',fontsize=22);chain.text(7.35,0,'…',va='center',fontsize=22)
chain.text(3.5,-.48,r'At every node: $q=x_i y_i$; the branches are $D_i$ and $D_{i+1}$.',ha='center')
chain.set(xlim=(-.8,7.8),ylim=(-.7,.6),title='Infinite special fibre (schematic)')
chain.axis('off')
fig.tight_layout()
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=130,facecolor='white',transparent=False)
plt.close(fig)
