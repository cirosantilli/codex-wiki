#!/usr/bin/env python3
"""Original scalar-box drawings. Tested Python 3.14.4, mpl 3.10.7, numpy 2.3.5.
Run with CWD set to the target media directory; output is paper-304-boxes.png.
Dependencies are those of the repository root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,3,figsize=(9,3),dpi=100,facecolor='white')
vertices=np.array([[-.6,.55],[.6,.55],[.6,-.55],[-.6,-.55]])
orders=[(1,2,3,4),(1,2,4,3),(1,3,2,4)]
for ax,order in zip(axes,orders):
    closed=np.vstack([vertices,vertices[0]])
    ax.plot(closed[:,0],closed[:,1],color='#1a1a1a',lw=1.8)
    for v,label in zip(vertices,order):
        endpoint=v*1.65
        ax.plot([v[0],endpoint[0]],[v[1],endpoint[1]],color='#1a1a1a',lw=1.8)
        ax.text(*(v*1.88),f'$p_{label}$',ha='center',va='center',fontsize=13)
    ax.scatter(vertices[:,0],vertices[:,1],s=24,color='#1a1a1a',zorder=3)
    ax.text(0,-1.35,'Cyclic order '+''.join(map(str,order)),ha='center',fontsize=11)
    ax.set_xlim(-1.4,1.4);ax.set_ylim(-1.55,1.35);ax.set_aspect('equal');ax.axis('off')
fig.subplots_adjust(left=.01,right=.99,bottom=.03,top=.98,wspace=.06)
fig.savefig(Path.cwd()/'paper-304-boxes.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
