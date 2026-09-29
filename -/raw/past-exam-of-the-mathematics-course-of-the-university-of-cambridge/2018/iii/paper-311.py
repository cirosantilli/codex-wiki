#!/usr/bin/env python3
"""Original schematic Penrose diagram; Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.
Run in the desired output directory: the PNG is written to the current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,4.6001), dpi=100, facecolor='white')
ax.set_facecolor('white')
# Compactified null coordinates: each ordinary null ray has slope +1 or -1.
ax.fill([-1,0,1], [1,0,1], color='#edf1f9')
ax.fill([-1,0,1], [-1,0,-1], color='#f3edf7')
for x,y in [([-2,-1],[0,1]),([-1,-2],[-1,0]),([1,2],[1,0]),([2,1],[0,-1])]:
    ax.plot(x,y,color='#303d4c',lw=1.8)
for x,y in [([0,-1],[0,1]),([0,1],[0,1]),([0,-1],[0,-1]),([0,1],[0,-1])]:
    ax.plot(x,y,color='#3562a4',lw=1.7,ls='--')
x=np.linspace(-1,1,161)
for sign in [1,-1]:
    ax.plot(x, sign*(1+0.018*np.sin(40*np.pi*(x+1))),color='#222222',lw=2.1)
ax.text(0,.65,'Future black hole (II)',ha='center',va='center',fontsize=11)
ax.text(0,-.65,'Past white hole (IV)',ha='center',va='center',fontsize=11)
ax.text(1.05,0,'Exterior I',ha='center',va='center',fontsize=11)
ax.text(-1.05,0,'Exterior III',ha='center',va='center',fontsize=11)
ax.text(0,1.15,r'$r=r_-$: future spacelike singularity',ha='center',fontsize=11)
ax.text(0,-1.23,r'$r=r_-$: past spacelike singularity',ha='center',fontsize=11)
for s in [-1,1]:
    ax.text(s*1.68,.63,r'$\mathcal{I}^+$',ha='center',fontsize=14)
    ax.text(s*1.68,-.73,r'$\mathcal{I}^-$',ha='center',fontsize=14)
    ax.text(s*2.13,-.02,r'$i^0$',ha='center',fontsize=12)
    ax.text(s*1.03,1.06,r'$i^+$',ha='center',fontsize=11)
    ax.text(s*1.03,-1.15,r'$i^-$',ha='center',fontsize=11)
ax.annotate('Future',xy=(2.4,.7),xytext=(2.4,-.1),ha='center',fontsize=10,
            arrowprops={'arrowstyle':'->','color':'#303d4c','lw':1.2})
ax.text(0,-1.48,r'Dashed: Killing horizons $r=r_+$;  $0\leq r_-<r_+$',ha='center',fontsize=10)
ax.set(xlim=(-2.55,2.72),ylim=(-1.58,1.4),aspect='equal')
ax.axis('off')
fig.subplots_adjust(left=.03,right=.97,bottom=.03,top=.98)
fig.savefig(Path.cwd()/'paper-311.png', dpi=100, facecolor='white')
plt.close(fig)
