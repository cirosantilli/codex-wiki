"""Original orbital/order sketches; Python 3.14, NumPy, Matplotlib. Output: CWD/basename.png."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,4,figsize=(15.2,4.6),dpi=100,facecolor='white',gridspec_kw={'width_ratios':[1,1,1,1.2]})
labels=[r'$d_{xy}$',r'$d_{xz}$',r'$d_{yz}$',r'$d_{z^2}$',r'$d_{x^2-y^2}$']
xs=[.15,.5,.85,.25,.75]
energies=[[-.35,-.35,-.35,1.15,1.15],[.02,-.55,-.55,.9,1.4],[-.65,-.08,-.08,1.4,.9]]
occupied=[[0,1],[1,2],[0,1]]
for ax,title,ys,occ in zip(axes[:3],['I: regular','II: elongated along z','III: compressed along z'],energies,occupied):
    for j,(x,y,label) in enumerate(zip(xs,ys,labels)):
        ax.plot([x-.115,x+.115],[y,y],color='#263e51',lw=2)
        ax.text(x,y-.11,label,ha='center',va='top',fontsize=10)
        if j in occ:ax.plot(x,y+.055,'o',ms=7,color='#c65b2d')
    ax.set(xlim=(-.02,1.02),ylim=(-1.1,1.78),title=title)
    ax.set_xticks([]);ax.set_yticks([])
    ax.spines[['top','right','bottom']].set_visible(False)
axes[0].set_ylabel('One-electron energy (schematic)')
ax=axes[3];T=np.linspace(0,1.3,600);order=np.sqrt(np.maximum(1-T,0))
ax.plot(T,order,lw=2,color='#247eac');ax.axvline(1,ls='--',color='#6e7c83',lw=1)
ax.set(xlabel='$T/T_{JT}$',ylabel=r'$|\Psi|/\Psi(0)$',title='Continuous ordering: illustration',xlim=(0,1.3),ylim=(-.03,1.08))
ax.spines[['top','right']].set_visible(False)
fig.text(.39,.025,'Dots: two parallel-spin electrons; one representative degenerate-state choice',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.08,1,1),pad=1.5)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
