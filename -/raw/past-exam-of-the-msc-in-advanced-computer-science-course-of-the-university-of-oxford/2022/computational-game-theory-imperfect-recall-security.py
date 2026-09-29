#!/usr/bin/env python3
"""Original payoff analysis; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Run from any directory. Writes the same-basename opaque PNG to the CWD.
Dependencies are pinned in the repository's top-level pyproject.toml.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white',
                     'axes.facecolor': 'white', 'savefig.facecolor': 'white',
                     'font.family': 'DejaVu Sans'})
t = np.linspace(0, 1, 401)
p, r = np.meshgrid(t, t)
g = np.minimum(p*r, (1-p)*(1-r))
fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.0, 3.6), layout='constrained')
im = ax.imshow(g, origin='lower', extent=(0,1,0,1), vmin=0, vmax=.25,
               cmap='viridis', aspect='equal', interpolation='nearest')
ax.plot(.5,.5,'o',color='white',markeredgecolor='black',markersize=7)
ax.annotate('Maximum 1/4',(.5,.5),xytext=(.08,.84),color='white',
            arrowprops={'arrowstyle':'->','color':'white'})
ax.set(xlabel='First choice: probability p of L',
       ylabel='Later choice: probability r of L',
       title='Guaranteed behavioural payoff')
fig.colorbar(im, ax=ax, shrink=.78, ticks=[0,.125,.25], pad=.02)
bx.plot(t,np.minimum(t*t,(1-t)**2),color='#2166ac',lw=2.4,
        label='Fresh independent choices: p = r = t')
bx.axhline(.5,color='#b2182b',lw=2,ls='--',label='One shared draw: half LL, half RR')
bx.scatter([.5],[.25],color='#2166ac',s=30,zorder=3)
bx.annotate('1/4',(.5,.25),xytext=(.54,.29))
bx.annotate('1/2',(.72,.5),xytext=(.74,.45))
bx.set(xlim=(0,1),ylim=(0,.56),xlabel='Common L probability t',
       ylabel='Guaranteed payoff',
       title='Correlating the two choices helps')
bx.grid(alpha=.18)
bx.legend(loc='lower center',bbox_to_anchor=(.5,-.35),fontsize=8.0,frameon=False)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,
            metadata={'Software':'Matplotlib original analytical figure'})
plt.close(fig)
