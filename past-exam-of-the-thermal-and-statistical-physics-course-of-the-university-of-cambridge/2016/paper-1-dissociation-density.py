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

d=np.geomspace(1e-3,1e3,700);alpha=2/(1+np.sqrt(1+16*d));fig,ax=plt.subplots(figsize=(6.8,3.8));ax.semilogx(d,alpha,color='#12669b',lw=2);ax.set(xlabel='Conserved formula-unit density / kappa(T)',ylabel='Dissociated fraction alpha',ylim=(0,1.04),xlim=(1e-3,1e3),title='Ideal A <-> 2B: increasing density suppresses dissociation');ax.grid(alpha=.2);ax.text(.0018,.25,'kappa(T) = NB^2 / (NA V)\nFixed temperature',fontsize=10);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
