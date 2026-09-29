"""Python 3.12; requires numpy and matplotlib; writes PNG into CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
nodes=np.arange(5.);x=np.linspace(0,4,700)
def t(x):return .27*(x-1)*(x-2)*(x-3)
y=t(nodes)
fig,ax=plt.subplots(figsize=(7.2,3.8),facecolor='white')
ax.axhline(0,color='.6',lw=.8)
ax.plot(x,t(x),label='$t=q-r$',color='#2366a8',lw=2)
ax.plot(nodes,y,'o-',label='linear interpolant $s$',color='#c6502b',lw=2)
for xi in nodes[1:-1]:ax.axvline(xi,color='.8',ls=':',lw=.8)
ax.set(xticks=nodes,xticklabels=['$x_0$','$x_1$','$x_2$','$x_3$','$x_4$'],xlabel='interpolation nodes',ylabel='function value',title='Endpoint ramps and zero interior spline pieces')
ax.legend();ax.grid(axis='y',alpha=.15);fig.tight_layout()
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=150,facecolor='white')
