#!/usr/bin/env python3
"""Symmetric-input channel information; Python 3.14, NumPy/Matplotlib.
Run in the directory where the white-background PNG should be written.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
t=np.linspace(0,1,700)
z=(1-t)/2
safe=np.clip(z,1e-15,1-1e-15)
h=-safe*np.log2(safe)-(1-safe)*np.log2(1-safe)
h[z==0]=0
fig,ax=plt.subplots(figsize=(7.6,4.5),layout='constrained',facecolor='white')
ax.set_facecolor('white')
ax.plot(t,h-z,color='#2466a4',lw=2.4,label='Channels (i) and (ii)')
ax.plot(t,(1-t)/2,color='#bb7025',lw=2.4,label='Channel (iii)')
ax.scatter([1/3],[np.log2(1.5)],color='#2466a4',s=36,zorder=4)
ax.scatter([0],[.5],color='#bb7025',s=36,zorder=4)
ax.annotate(r'$C=\log_2(3/2)$ at $t=1/3$',(1/3,np.log2(1.5)),xytext=(.43,.65),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
ax.annotate(r'$C=1/2$ at $t=0$',(0,.5),xytext=(.05,.31),arrowprops={'arrowstyle':'->','color':'0.3'},fontsize=10)
ax.set(xlim=(-.02,1.02),ylim=(0,.72),xlabel=r'Middle-input probability $t$; outer inputs each have probability $(1-t)/2$',ylabel='Mutual information (bits per use)',title='Capacity along the symmetric family of input laws')
ax.legend(loc='upper right',bbox_to_anchor=(1,.79),facecolor='white')
ax.grid(alpha=.18)
fig.savefig(Path.cwd()/'2010-channel-capacities.png',dpi=160,facecolor='white')
