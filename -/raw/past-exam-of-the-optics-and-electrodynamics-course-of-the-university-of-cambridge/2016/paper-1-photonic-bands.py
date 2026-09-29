#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from the corresponding mirrored _media directory; writes a PNG basename to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

f=np.linspace(0,.9,18001);n1=1.;n2=2.5;d1=.5;d2=.5;delta1=2*np.pi*f*n1*d1;delta2=2*np.pi*f*n2*d2
F=np.cos(delta1)*np.cos(delta2)-.5*(n1/n2+n2/n1)*np.sin(delta1)*np.sin(delta2);allowed=np.abs(F)<=1;q=np.arccos(np.clip(F,-1,1))/np.pi
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,3.8),gridspec_kw={'width_ratios':[1,1.5]})
for j in range(6):
 ax.add_patch(plt.Rectangle((j,0),.5,1,color='#c5e2ee'));ax.add_patch(plt.Rectangle((j+.5,0),.5,1,color='#31658a'))
ax.set(xlim=(0,6),ylim=(-.3,1.4),title='Equal-thickness bilayer',xlabel='Position / period');ax.set_yticks([]);ax.text(.2,1.12,'n = 1',color='#24516d');ax.text(2.5,1.12,'n = 2.5',color='#24516d')
starts=np.r_[0,np.flatnonzero(allowed[1:]!=allowed[:-1])+1];ends=np.r_[starts[1:],len(f)]
for l,r in zip(starts,ends):
 if allowed[l]:bx.plot(q[l:r],f[l:r],color='#12669b',lw=1.7)
 else:bx.axhspan(f[l],f[r-1],color='#e6bb77',alpha=.45)
bx.set(xlim=(0,1),ylim=(0,.9),xlabel='Bloch wave number ka / pi',ylabel='Frequency: omega a / (2 pi c)',title='Exact normal-incidence Bloch bands');bx.grid(alpha=.2);bx.text(.1,.31,'Stop band',fontsize=10);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
