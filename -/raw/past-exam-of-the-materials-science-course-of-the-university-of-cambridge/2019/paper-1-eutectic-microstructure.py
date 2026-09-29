"""Original mathematical illustration; write the matching PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
plt.rcParams.update({"font.size":11,"axes.titlesize":13,"figure.facecolor":"white","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=150,facecolor="white")
    plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout='constrained')
polys=[np.array([[.04,.06],[.38,.03],[.48,.25],[.32,.43],[.03,.33]]),np.array([[.60,.39],[.93,.24],[.98,.60],[.73,.80],[.54,.65]]),np.array([[.08,.66],[.30,.48],[.47,.69],[.34,.96],[.02,.94]])]
for i,ax in enumerate(axs):
    ax.set_facecolor('#ecd394' if i==0 else '#c6d5df')
    if i:
        for v in np.arange(-1,2,.08):ax.plot([v,v+.7],[0,1],c='#a9a8b5',lw=4,zorder=1)
    for p in polys:ax.add_patch(Polygon(p,facecolor='#6992b2',edgecolor='#305672',lw=1.5,zorder=3))
    ax.text(.10,.17,'Primary\nBi-rich solid',fontsize=10,color='white',zorder=4)
    ax.text(.52,.05,'Remaining liquid' if i==0 else 'Two-phase eutectic',fontsize=10,backgroundcolor='white',zorder=4)
    ax.set(xlim=(0,1),ylim=(0,1),title='150 °C: solid + liquid' if i==0 else '125 °C: primary solid + eutectic');ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([])
fig.suptitle('Original cartoons; drawn area is not a calibrated phase mass fraction')
save(fig)
