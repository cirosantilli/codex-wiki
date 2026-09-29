"""Original reciprocal-coordinate circle loci with the origin explicitly removed."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

angle = np.linspace(0, 2*np.pi, 600)
fig, ax = plt.subplots(figsize=(6.8, 6.6), facecolor='white', layout='constrained')
ax.axhline(0, color='.7', lw=.8)
ax.axvline(0, color='.7', lw=.8)
ax.plot(np.cos(angle),np.sin(angle),'--',color='.5',label='Unit circle')
ax.plot(.5+.5*np.cos(angle),.5*np.sin(angle),lw=2.3,color='#176b87',label='Re(1/z) = 1')
ax.plot(.5*np.cos(angle),-.5+.5*np.sin(angle),lw=2.3,color='#c05229',label='Im(1/z) = 1')
ax.scatter([0],[0],facecolors='white',edgecolors='black',s=90,zorder=5)
ax.scatter([.5],[ -.5],color='black',s=35,zorder=5)
ax.scatter([1,0],[0,-1],color='#625345',s=35,zorder=5)
ax.annotate('Origin excluded\nfrom both loci',xy=(0,0),xytext=(-.95,.35),fontsize=11,arrowprops={'arrowstyle':'->'})
ax.annotate('Intersection\n(1 − i)/2; 90°',xy=(.5,-.5),xytext=(.58,-.78),fontsize=11,arrowprops={'arrowstyle':'->'})
ax.text(1.04,.04,'1',fontsize=12)
ax.text(-.13,-1.1,'−i',fontsize=12)
ax.legend(loc='upper left',fontsize=10,frameon=False)
ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),aspect='equal',xlabel='Real part',ylabel='Imaginary part',title='Reciprocal-coordinate circles: intersection and tangencies')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software':'matplotlib'})
