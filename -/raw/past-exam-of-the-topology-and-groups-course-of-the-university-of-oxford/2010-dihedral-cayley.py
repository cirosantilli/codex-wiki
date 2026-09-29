#!/usr/bin/env python3
"""Right Cayley graph of D6; Python 3.14, NumPy/Matplotlib.
Writes a white-background PNG to the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
fig,ax=plt.subplots(figsize=(6,5.6),layout='constrained',facecolor='white')
angles=np.deg2rad([90,210,330]);outer=np.column_stack([2.1*np.cos(angles),2.1*np.sin(angles)]);inner=np.column_stack([.95*np.cos(angles),.95*np.sin(angles)])
for coords,edges in [(outer,[(0,1),(1,2),(2,0)]),(inner,[(0,2),(2,1),(1,0)])]:
 for i,j in edges:
  u,v=coords[i],coords[j];ax.add_patch(FancyArrowPatch(u,v,arrowstyle='-|>',mutation_scale=15,color='#2c6aab',lw=1.8,shrinkA=14,shrinkB=14));mid=(u+v)/2;direction=v-u;perp=np.array([-direction[1],direction[0]])/np.linalg.norm(direction);ax.text(*(mid+.13*perp),r'$\sigma$',color='#2c6aab',ha='center',va='center',fontsize=13,bbox={'facecolor':'white','edgecolor':'none','pad':.2})
for i in range(3):
 ax.plot([inner[i,0],outer[i,0]],[inner[i,1],outer[i,1]],color='#bd7229',lw=2,zorder=0);mid=(inner[i]+outer[i])/2;ax.text(*(mid+np.array([.12,.02])),r'$\tau$',color='#995016',fontsize=13,bbox={'facecolor':'white','edgecolor':'none','pad':.2})
for coords,labels in [(outer,[r'$1$',r'$\sigma$',r'$\sigma^2$']),(inner,[r'$\tau$',r'$\tau\sigma^2$',r'$\tau\sigma$'])]:
 for pos,label in zip(coords,labels):ax.text(*pos,label,ha='center',va='center',fontsize=13,bbox={'boxstyle':'round,pad=.22','facecolor':'white','edgecolor':'#444444'})
ax.set(aspect='equal',xlim=(-2.4,2.4),ylim=(-1.65,2.65),title=r'Right Cayley graph of $D_6$')
ax.text(0,-1.58,r'Blue directed edges: $\sigma$; orange involution edges: $\tau$.',ha='center',fontsize=10)
ax.axis('off');fig.savefig(Path.cwd()/'2010-dihedral-cayley.png',dpi=165,facecolor='white')
