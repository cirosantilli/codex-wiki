"""Original four-point scalar diagrams; Python 3.14, matplotlib 3.10.7.

Run from the desired output directory. The caller controls MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path as Curve
from matplotlib.patches import PathPatch

fig,axes=plt.subplots(1,2,figsize=(9,3.6),facecolor='white')
for ax in axes:
    ax.set_facecolor('white')
    for sx in (-1,1):
        for sy in (-1,1):
            ax.plot([0.65*sx,1.5*sx],[0,0.78*sy],color='black',lw=2)
    ax.scatter([-0.65,0.65],[0,0],s=38,color='black',zorder=5)
    ax.set_xlim(-1.7,1.7)
    ax.set_ylim(-1.15,1.28)
    ax.set_aspect('equal')
    ax.axis('off')
for sign in (-1,1):
    curve=Curve([(-0.65,0),(-0.5,0.82*sign),(0.5,0.82*sign),(0.65,0)],
                [Curve.MOVETO,Curve.CURVE4,Curve.CURVE4,Curve.CURVE4])
    axes[0].add_patch(PathPatch(curve,fill=False,edgecolor='black',lw=2))
axes[0].set_title('1PI: two quartic vertices',fontsize=13,pad=12)
axes[0].text(0,-1.01,'Either internal line can be cut\nwithout disconnecting the graph.',ha='center',va='top',fontsize=10)
axes[1].plot([-0.65,0.65],[0,0],color='black',lw=2)
axes[1].set_title('1PR: two cubic vertices',fontsize=13,pad=12)
axes[1].text(0,-1.01,'Cutting the single bridge\ndisconnects the graph.',ha='center',va='top',fontsize=10)
fig.tight_layout(pad=1.1,w_pad=2,rect=(0,0.02,1,0.94))
fig.savefig(Path.cwd()/'paper-65-four-point-diagrams.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
