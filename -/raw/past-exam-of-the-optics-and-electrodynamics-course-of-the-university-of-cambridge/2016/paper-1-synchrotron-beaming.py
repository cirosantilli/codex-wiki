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

fig,ax=plt.subplots(figsize=(6.8,4));angle=np.linspace(0,2*np.pi,400);ax.plot(np.cos(angle),np.sin(angle),color='.5',lw=1.7)
ax.plot([1],[0],'o',color='#bd6915');ax.annotate('',(1,1.05),(1,0),arrowprops={'arrowstyle':'->','lw':2,'color':'#12669b'});ax.text(1.07,.6,'Velocity v',color='#12669b')
for a in [-.14,.14]:ax.plot([1,1+2.3*np.sin(a)],[0,2.3*np.cos(a)],'--',color='#bd6915')
ax.fill([1,1+2.3*np.sin(-.14),1+2.3*np.sin(.14)],[0,2.3*np.cos(.14),2.3*np.cos(.14)],color='#bd6915',alpha=.15)
ax.annotate('',(0,0),(1,0),arrowprops={'arrowstyle':'->','color':'#555555'});ax.text(.25,.08,'Inward acceleration');ax.text(1.36,1.72,'Cone angle\n~ 1 / gamma',color='#9b5910');ax.text(-.7,-1.35,'Schematic only; no particular gamma assumed')
ax.set(xlim=(-1.5,2.5),ylim=(-1.5,2.5),title='Synchrotron radiation follows the instantaneous tangent');ax.set_aspect('equal');ax.axis('off');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
