"""Original exam diagram. Tested Python3.14.4/NumPy2.3.5/Matplotlib3.10.7.
Writes its PNG basename only to caller CWD; honors caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

COLOURS={1:'#2166ac',2:'#d95f02'}
def graph(ax, positions, labels, edges, title, ylim=None):
    for a,b,i in edges:
        x,y=positions[a];xx,yy=positions[b]
        ax.annotate('',(xx,yy),(x,y),arrowprops={'arrowstyle':'-|>','color':COLOURS[i],'lw':1.8,'shrinkA':16,'shrinkB':16})
        dx,dy=xx-x,yy-y
        off=.13 if dx>=0 else -.13
        ax.text((x+xx)/2+off,(y+yy)/2,str(i),ha='center',va='center',fontsize=10,color=COLOURS[i],bbox={'facecolor':'white','edgecolor':'none','pad':.1})
    for key,(x,y) in positions.items():
        ax.text(x,y,labels[key],ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.28','facecolor':'white','edgecolor':'#555555','lw':.8},zorder=5)
    xs=[v[0] for v in positions.values()];ys=[v[1] for v in positions.values()]
    ax.set_xlim(min(xs)-.65,max(xs)+.65)
    ax.set_ylim(*(ylim if ylim else (min(ys)-.6,max(ys)+.8)))
    ax.set_title(title,pad=10,fontsize=12)
    ax.axis('off')

fig,axs=plt.subplots(1,3,figsize=(10.5,7.0),gridspec_kw={"width_ratios":[1,1,2.25]},layout="constrained")
fig.patch.set_facecolor("white")
graph(axs[0],{'1': (0, 4), '2': (0, 3), '0': (0, 2), 'b2': (0, 1), 'b1': (0, 0)},{'1': '$\\varepsilon_1$', '2': '$\\varepsilon_2$', '0': '$0$', 'b2': '$-\\varepsilon_2$', 'b1': '$-\\varepsilon_1$'},[['1', '2', 1], ['2', '0', 2], ['0', 'b2', 2], ['b2', 'b1', 1]],'$B(\\Lambda_1)$: dimension5')
graph(axs[1],{'++': (0, 3), '+-': (0, 2), '-+': (0, 1), '--': (0, 0)},{'++': '$++$', '+-': '$+-$', '-+': '$-+$', '--': '$--$'},[['++', '+-', 2], ['+-', '-+', 1], ['-+', '--', 2]],'$B(\\Lambda_2)$: dimension4')
graph(axs[2],{'r1,1': (0, 3), 'r1,0': (0, 2), 'r1,-1': (-0.85, 1), 'r0,1': (0.85, 1), 'z1': (-0.85, 0), 'z2': (0.85, 0), 'r-1,1': (-0.85, -1), 'r0,-1': (0.85, -1), 'r-1,0': (0, -2), 'r-1,-1': (0, -3)},{'r1,1': '$\\varepsilon_1+\\varepsilon_2$', 'r1,0': '$\\varepsilon_1$', 'r1,-1': '$\\alpha_1$', 'r0,1': '$\\varepsilon_2$', 'z1': '$z_1$', 'z2': '$z_2$', 'r-1,1': '$-\\alpha_1$', 'r0,-1': '$-\\varepsilon_2$', 'r-1,0': '$-\\varepsilon_1$', 'r-1,-1': '$-\\varepsilon_1-\\varepsilon_2$'},[['r1,1', 'r1,0', 2], ['r1,0', 'r0,1', 1], ['r1,0', 'r1,-1', 2], ['r1,-1', 'z1', 1], ['r0,1', 'z2', 2], ['z1', 'r-1,1', 1], ['r-1,1', 'r-1,0', 2], ['z2', 'r0,-1', 2], ['r0,-1', 'r-1,0', 1], ['r-1,0', 'r-1,-1', 2]],'$B(2\\Lambda_2)$: adjoint, dimension10')
fig.suptitle("B2 crystals: each arrow lowers its simple-root color",fontsize=13)
fig.savefig(Path("paper-5-b2-crystals.png"),dpi=145,facecolor="white",transparent=False);plt.close(fig)
