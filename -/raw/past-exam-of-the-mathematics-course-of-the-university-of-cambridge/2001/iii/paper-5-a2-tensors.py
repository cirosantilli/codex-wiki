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

fig,axs=plt.subplots(2,2,figsize=(10.0,9.2),gridspec_kw={"width_ratios":[2,1]},layout="constrained")
fig.patch.set_facecolor("white")
graph(axs[0,0],{'1|1': (0, 0), '2|1': (-0.65, -1), '2|2': (-1.3, -2), '3|1': (0.65, -2), '3|2': (0, -3), '3|3': (0.65, -4)},{'1|1': '$1\\otimes 1$', '2|1': '$2\\otimes 1$', '2|2': '$2\\otimes 2$', '3|1': '$3\\otimes 1$', '3|2': '$3\\otimes 2$', '3|3': '$3\\otimes 3$'},[['1|1', '2|1', 1], ['2|1', '2|2', 1], ['2|1', '3|1', 2], ['2|2', '3|2', 2], ['3|1', '3|2', 1], ['3|2', '3|3', 2]],'$B\\otimes B$: highest weight $2\\omega_1$',ylim=(-4.6,.8))
graph(axs[0,1],{'1|2': (0, 0), '1|3': (0, -1), '2|3': (0, -2)},{'1|2': '$1\\otimes 2$', '1|3': '$1\\otimes 3$', '2|3': '$2\\otimes 3$'},[['1|2', '1|3', 2], ['1|3', '2|3', 1]],'$B\\otimes B$: highest weight $\\omega_2$',ylim=(-4.6,.8))
graph(axs[1,0],{'1|b3': (0, 0), '2|b3': (-0.9, -1), '1|b2': (0.9, -1), '3|b3': (-0.9, -2), '2|b2': (0.9, -2), '3|b2': (-0.9, -3), '2|b1': (0.9, -3), '3|b1': (0, -4)},{'1|b3': '$1\\otimes \\bar{3}$', '2|b3': '$2\\otimes \\bar{3}$', '1|b2': '$1\\otimes \\bar{2}$', '3|b3': '$3\\otimes \\bar{3}$', '2|b2': '$2\\otimes \\bar{2}$', '3|b2': '$3\\otimes \\bar{2}$', '2|b1': '$2\\otimes \\bar{1}$', '3|b1': '$3\\otimes \\bar{1}$'},[['1|b3', '2|b3', 1], ['1|b3', '1|b2', 2], ['1|b2', '2|b2', 1], ['2|b3', '3|b3', 2], ['2|b2', '2|b1', 1], ['2|b1', '3|b1', 2], ['3|b3', '3|b2', 2], ['3|b2', '3|b1', 1]],'$B\\otimes B^\\vee$: highest weight $\\omega_1+\\omega_2$',ylim=(-4.6,.8))
graph(axs[1,1],{'1|b1': (0, -2)},{'1|b1': '$1\\otimes \\bar{1}$'},[],'$B\\otimes B^\\vee$: highest weight $0$',ylim=(-4.6,.8))
fig.suptitle("A2 tensor crystals: blue edges1, orange edges2",fontsize=13)
fig.savefig(Path("paper-5-a2-tensors.png"),dpi=140,facecolor="white",transparent=False);plt.close(fig)
