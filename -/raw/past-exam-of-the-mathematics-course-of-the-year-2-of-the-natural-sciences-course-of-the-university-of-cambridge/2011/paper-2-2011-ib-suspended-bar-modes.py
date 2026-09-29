"""Original mode-shape illustration; Python 3.14, NumPy, Matplotlib.

Run with cwd equal to the mirrored _media paper directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

fig, axes = plt.subplots(1,3,figsize=(10.4,4.4),facecolor='white')
modes = [np.array([1,1+np.sqrt(2),1+np.sqrt(2)]),np.array([0,1,-1]),np.array([1,1-np.sqrt(2),1-np.sqrt(2)])]
labels = [r'$\omega^2=2-\sqrt{2}$', r'$\omega^2=1$',r'$\omega^2=2+\sqrt{2}$']
ratios = [r'$(1,\ 1+\sqrt{2},\ 1+\sqrt{2})$',r'$(0,\ 1,\ -1)$',r'$(1,\ 1-\sqrt{2},\ 1-\sqrt{2})$']
captions = ['All move in phase','Bar stationary; lower pair opposed','Lower pair moves against bar']
for ax,mode,label,ratio,caption in zip(axes,modes,labels,ratios,captions):
    ax.plot([-.3,.3],[0,0],color='#334155',lw=2)
    ax.plot([0,0],[0,.64],color='#94a3b8',lw=1.8)
    ax.add_patch(Rectangle((-.66,.64),1.32,.12,facecolor='#64748b'))
    for xpos in [-.6,.6]:
        ax.plot([xpos,xpos],[.76,1.66],color='#94a3b8',lw=1.8)
        ax.add_patch(Circle((xpos,1.76),.12,facecolor='#64748b'))
    for xpos,ypos,val in zip([.17,-.83,.83],[.7,1.76,1.76],mode):
        if val:
            dy=.65*val/np.max(np.abs(mode))
            ax.annotate('',xy=(xpos,ypos+dy),xytext=(xpos,ypos),arrowprops={'arrowstyle':'-|>','color':'#be123c','lw':2,'mutation_scale':13})
        else:
            ax.text(xpos+.08,ypos,'0',color='#be123c',va='center',fontsize=11)
    ax.text(0,2.68,ratio,ha='center',fontsize=11,color='#be123c')
    ax.text(0,3.03,caption,ha='center',fontsize=9)
    ax.set_title(label,fontsize=13,pad=15)
    ax.set(xlim=(-1.2,1.2),ylim=(3.25,-.2))
    ax.set_aspect('equal')
    ax.axis('off')
fig.suptitle('Physical displacement ratios (positive downward)',fontsize=12,y=.97)
fig.subplots_adjust(left=.025,right=.975,top=.82,bottom=.02,wspace=.08)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=155,facecolor='white')
plt.close(fig)
