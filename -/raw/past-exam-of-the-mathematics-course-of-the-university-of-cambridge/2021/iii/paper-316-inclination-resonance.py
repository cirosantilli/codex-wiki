#!/usr/bin/env python3
"""Generate paper-316-inclination-resonance.png."""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


fig,axs=plt.subplots(1,3,figsize=(12,4),constrained_layout=True)
# Face-on
ax=axs[0]
th=np.linspace(0,2*np.pi,400)
ax.plot(np.cos(th),np.sin(th),color='#777',lw=1.2)
ax.plot(1.65*np.cos(th),1.65*np.sin(th),color='#3a75a8',lw=1.2)
ax.axhline(0,color='#999',ls=':',lw=1)
ax.scatter([0],[0],s=90,color='#f4b942',edgecolor='#8c5f00',zorder=5)
u=.18
p1=np.array([np.cos(u),np.sin(u)])
p2=np.array([1.65*np.cos(u),1.65*np.sin(u)])
ax.scatter(*p1,s=70,color='#d62728',zorder=5)
ax.scatter(*p2,s=70,color='#006bb6',zorder=5)
ax.plot([0,1.8],[0,0],color='black',lw=1.6,label='ascending-node line')
ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color='#555',ls='--')
ax.annotate('$M_1$',p1,xytext=(-2,8),textcoords='offset points')
ax.annotate('$M_2$ (above plane)',p2,xytext=(-18,8),textcoords='offset points',fontsize=8)
ax.annotate('motion',xy=(1.55*np.cos(.55),1.55*np.sin(.55)),xytext=(1.65,.8),arrowprops=dict(arrowstyle='->'))
ax.set_title('Face-on: conjunction after node'); ax.set_aspect('equal'); ax.set_xlim(-1.9,1.9); ax.set_ylim(-1.9,1.9); ax.axis('off')
# side along node
ax=axs[1]
ax.axhline(0,color='#555',lw=1.4,label='plane of $M_1$')
ax.scatter([0],[0],s=90,color='#f4b942',edgecolor='#8c5f00',zorder=5)
ax.scatter([1.0],[0],s=70,color='#d62728',zorder=5)
ax.scatter([1.62],[.35],s=70,color='#006bb6',zorder=5)
ax.annotate('$M_1$',(1,0),xytext=(-8,-22),textcoords='offset points')
ax.annotate('$M_2$',(1.62,.35),xytext=(5,4),textcoords='offset points')
ax.add_patch(FancyArrowPatch((1.60,.33),(1.15,.06),arrowstyle='->',mutation_scale=13,color='#7b2cbf',lw=2))
ax.text(1.22,.25,'force from $M_1$',fontsize=8,rotation=-25)
ax.add_patch(FancyArrowPatch((1.62,.35),(1.60,.72),arrowstyle='->',mutation_scale=13,color='#006bb6',lw=1.6))
ax.text(1.63,.63,'vertical velocity',fontsize=8)
ax.annotate('star',(0,0),xytext=(-12,-22),textcoords='offset points')
ax.set_title('View along ascending node'); ax.set_xlim(-.2,2.05); ax.set_ylim(-.55,.95); ax.set_xlabel('distance from star'); ax.set_ylabel('height'); ax.grid(alpha=.18)
# rotating-frame projection p=1
ax=axs[2]
u=np.linspace(0,2*np.pi,700)
y=np.sin(np.pi-2*u)
z=.48*np.sin(u)
ax.plot(y,z,color='#006bb6',lw=2.3)
for uu in [np.pi/2,3*np.pi/2]:
 yy=np.sin(np.pi-2*uu); zz=.48*np.sin(uu)
 ax.scatter([yy],[zz],s=55,color='#d62728',zorder=5)
 ax.annotate('conjunction', (yy,zz),xytext=(8,0),textcoords='offset points',fontsize=8)
for uu in [0,np.pi]:
 yy=np.sin(np.pi-2*uu); zz=.48*np.sin(uu)
 ax.scatter([yy],[zz],s=35,color='black',zorder=5)
ax.axhline(0,color='#777',ls=':',lw=1)
ax.axvline(0,color='#777',ls=':',lw=1)
ax.set_aspect('equal'); ax.set_title('$q=2$, $p=1$: rotating-frame view')
ax.set_xlabel('transverse displacement'); ax.set_ylabel('height'); ax.grid(alpha=.18)
output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
