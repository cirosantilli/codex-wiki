"""Original zone and Fermi-surface plots; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon
import numpy as np

plt.rcParams.update({'font.size':12})
fig,(square,rect)=plt.subplots(1,2,figsize=(10,4.8),layout='constrained',facecolor='white')
square.add_patch(Rectangle((-1,-1),2,2,fill=False,color='#333333',lw=1.5))
square.add_patch(Polygon([(1,0),(0,1),(-1,0),(0,-1)],closed=True,facecolor='#d9e8ef',edgecolor='#245f9c',lw=2))
square.text(0,0,'Occupied',ha='center',va='center')
square.set(xlabel=r'$k_xa/\pi$',ylabel=r'$k_ya/\pi$',title='Square: half-filled Fermi diamond',aspect='equal',xlim=(-1.2,1.2),ylim=(-1.2,1.2),xticks=[-1,0,1],yticks=[-1,0,1])
ratio=.65;hopping_ratio=.5
y=np.linspace(-1,1,1001)
x=np.arccos(-hopping_ratio*np.cos(np.pi*y))/(np.pi*ratio)
rect.add_patch(Rectangle((-1/ratio,-1),2/ratio,2,fill=False,color='#333333',lw=1.5))
rect.fill_betweenx(y,-x,x,color='#d9e8ef')
rect.plot(x,y,color='#245f9c',lw=2);rect.plot(-x,y,color='#245f9c',lw=2)
rect.text(0,0,'Occupied',ha='center',va='center')
rect.set(xlabel=r'$k_xa_y/\pi$',ylabel=r'$k_ya_y/\pi$',title=r'Rectangular: $a_x=0.65a_y$, $t_x=2t_y$',aspect='equal',xlim=(-1.8,1.8),ylim=(-1.2,1.2),xticks=[-1/ratio,0,1/ratio],yticks=[-1,0,1])
rect.set_xticklabels([r'$-a_y/a_x$','0',r'$a_y/a_x$'])
for ax in [square,rect]:
    ax.axhline(0,color='#888888',lw=.6,zorder=0)
    ax.axvline(0,color='#888888',lw=.6,zorder=0)
    ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
