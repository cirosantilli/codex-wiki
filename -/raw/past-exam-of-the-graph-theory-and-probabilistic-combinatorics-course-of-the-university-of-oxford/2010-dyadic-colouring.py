#!/usr/bin/env python3
"""Alternating dyadic colouring; Python 3.14, NumPy and Matplotlib.
Outputs a white-background PNG in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(8,3.8),layout='constrained',facecolor='white')
ax.set_facecolor('white')
colors=['#376eaa','#d98532']
for j in range(7):
 ax.add_patch(Rectangle((j,.1),1,.32,color=colors[j%2],alpha=.85))
 ax.text(j+.5,.26,r'$C_'+str(j%2)+'$',ha='center',va='center',color='white',fontsize=12)
for row,x in enumerate([3,5,9,17]):
 lx=np.log2(x); y=-.16-.24*row
 ax.annotate('',xy=(lx+1,y),xytext=(lx,y),arrowprops={'arrowstyle':'->','lw':1.6,'color':'#333333'})
 ax.scatter([lx,lx+1],[y,y],c=[colors[int(lx)%2],colors[int(lx+1)%2]],s=27,zorder=4)
 ax.text(lx-.08,y,str(x),ha='right',va='center',fontsize=10)
 ax.text(lx+1.08,y,str(2*x),ha='left',va='center',fontsize=10)
ax.set_xticks(range(8),[str(2**j)for j in range(8)])
ax.xaxis.tick_top()
ax.set(xlim=(-.1,7.1),ylim=(-1.05,.65),yticks=[],title='Alternating dyadic blocks: doubling always changes colour')
ax.text(3.5,-1.02,r'Addition-closed $S$ contains $x$ and $2x$, so it cannot be monochromatic.',ha='center',va='bottom',fontsize=11)
for spine in ax.spines.values():spine.set_visible(False)
fig.savefig(Path.cwd()/'2010-dyadic-colouring.png',dpi=160,facecolor='white')
