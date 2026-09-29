#!/usr/bin/env python3
"""Python 3.14; matplotlib from repository pyproject.toml. White PNG in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,ax=plt.subplots(figsize=(8.2,2.2),facecolor='white')
ax.plot([.12,.88],[0,0],color='black',lw=1.5)
ax.plot([2.12,2.88],[0,0],color='black',lw=1.5)
ax.plot([1.12,1.88],[.045,.045],color='black',lw=1.2)
ax.plot([1.12,1.88],[-.045,-.045],color='black',lw=1.2)
ax.plot([1.47,1.60,1.47],[.15,0,-.15],color='black',lw=1.5)
for i in range(4):
 ax.add_patch(Circle((i,0),.12,facecolor='white',edgecolor='black',lw=1.5,zorder=3))
 ax.text(i,.25,str(i+1),ha='center',va='center',fontsize=12)
 ax.text(i,-.31,'long: squared length 2' if i<2 else 'short: squared length 1',ha='center',va='center',fontsize=9)
ax.text(1.5,.63,'F4: the double bond points toward the shorter root',ha='center',fontsize=13)
ax.set_xlim(-.55,3.55);ax.set_ylim(-.55,.85);ax.set_aspect('equal');ax.axis('off');fig.tight_layout()
fig.savefig(Path.cwd()/'2007-f4-dynkin.png',dpi=160,facecolor='white');plt.close(fig)
