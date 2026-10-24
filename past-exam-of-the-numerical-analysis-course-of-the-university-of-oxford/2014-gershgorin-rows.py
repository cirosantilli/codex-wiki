"""Original Gershgorin diagram. Python 3.14.4; matplotlib 3.10.7; numpy 2.3.5.
Run in the matching _media directory; PNG output is relative to the CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
MODE = 'rows'
centres=np.arange(1,9); radii=np.full(8,0.48)
radii[0]=0.24; radii[-1]=3.49
isolated=range(4)
if MODE=='columns':
 radii=radii[::-1]; isolated=range(4,8)
fig,ax=plt.subplots(figsize=(9.5,5.7),layout='constrained',facecolor='white')
for i,(centre,radius) in enumerate(zip(centres,radii)):
 large=radius>1
 color='#755299' if large else '#176aa5' if i in isolated else '#888888'
 ax.add_patch(Circle((centre,0),radius,facecolor=color if i in isolated else 'none',edgecolor=color,alpha=0.2 if i in isolated else 0.9,lw=1.8))
 if i in isolated:ax.add_patch(Circle((centre,0),radius,fill=False,edgecolor=color,lw=1.8))
 ax.plot(centre,0,'o',color=color,ms=3)
 ax.text(centre,-0.10,str(centre),ha='center',va='top',fontsize=9)
ax.axhline(0,color='#aaaaaa',lw=0.7,zorder=0);ax.axvline(4.5,color='#555555',lw=0.8,ls='--')
ax.set_xlim((-2.7,9) if MODE=='columns' else (0,11.7));ax.set_ylim(-3.8,3.8)
ax.set_aspect('equal');ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part')
ax.set_title(f'{MODE.capitalize()} of A: '+('centres 1–4 isolated' if MODE=='rows' else 'centres 5–8 isolated'))
fig.suptitle(r'$n=8,\ c=13/4$: adjacent entries $0.24<1/4$')
ax.text(0.02,0.97,'Small radii: 0.24 or 0.48; enlarged radius: 3.49',transform=ax.transAxes,va='top',fontsize=9)
ax.spines[['top','right']].set_visible(False)
fig.savefig(f'2014-gershgorin-{MODE}.png',dpi=120,facecolor='white')
