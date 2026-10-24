#!/usr/bin/env python3
"""Monodromy cycles of the six-sheeted cover; Python 3.14, NumPy/Matplotlib.
Vertex positions are rearranged consistently in both panels for legibility.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
names=['B','V','L','T','C','U'];angles=np.deg2rad([270,210,150,90,30,330]);pos={s:np.array([np.cos(t),np.sin(t)])for s,t in zip(names,angles)}
fig,axs=plt.subplots(1,2,figsize=(8.1,4.1),layout='constrained',facecolor='white')
for ax,cycle,color,label in [(axs[0],names,'#2d6cab','x'),(axs[1],['B','C','V','T','U','L'],'#b76820','y')]:
 for s,t in zip(cycle,cycle[1:]+cycle[:1]):ax.add_patch(FancyArrowPatch(pos[s],pos[t],arrowstyle='-|>',mutation_scale=15,lw=1.8,color=color,shrinkA=15,shrinkB=15,connectionstyle='arc3,rad='+('0'if label=='x'else'.1')))
 for s,p in pos.items():ax.text(*p,s,ha='center',va='center',fontsize=13,bbox={'boxstyle':'circle,pad=.25','facecolor':'white','edgecolor':'#444444'})
 ax.set(aspect='equal',xlim=(-1.25,1.25),ylim=(-1.3,1.3),title=f'{label}-labelled directed edges');ax.axis('off')
fig.suptitle('Two directed cycles on the same six vertices',fontsize=14)
fig.savefig(Path.cwd()/'2010-octahedral-cover.png',dpi=165,facecolor='white')
