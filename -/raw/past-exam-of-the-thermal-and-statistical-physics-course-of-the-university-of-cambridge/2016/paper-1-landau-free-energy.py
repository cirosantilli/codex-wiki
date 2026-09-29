#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7. Run from mirrored _media directory; PNG basename goes to cwd.
All plotted parameter choices are illustrative and do not assert provided exam data.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

q=np.linspace(-1.75,1.75,700);fig,ax=plt.subplots(figsize=(6.8,3.8))
for r,label in [(1.,'Above Tc'),(0.,'At Tc'),(-1.,'Below Tc')]:ax.plot(q,r*q*q/2+q**4/4,lw=2,label=label)
ax.plot([-1,1],[-.25,-.25],'o',color='#2b8f3e');ax.axhline(0,color='.6',lw=.7);ax.set(xlabel='Order parameter (scaled)',ylabel='Free-energy density relative to f0 (scaled)',xlim=(-1.75,1.75),ylim=(-.4,2.6),title='Symmetric quartic Landau model');ax.legend(fontsize=9);ax.grid(alpha=.2);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
