#!/usr/bin/env python3
"""Original planetary-dynamics figure; outputs its same-basename PNG to CWD.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Dependencies match the repository pyproject; no external visual assets.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
blue='#22577a'; orange='#c66a24'; green='#387c58'; gray='#666666'
def finish(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
    plt.close(fig)

fig,ax=plt.subplots(figsize=(7.5,5),dpi=100)
a=1;e=.3;b=np.sqrt(1-e*e);E=1.05;M=E-e*np.sin(E)
f=np.arctan2(b*np.sin(E),np.cos(E)-e)
theta=np.linspace(0,2*np.pi,700)
ax.plot(np.cos(theta),b*np.sin(theta),color=blue,label='Ellipse')
ax.plot(np.cos(theta),np.sin(theta),'--',color=gray,label='Auxiliary circle')
P=np.array([np.cos(E),b*np.sin(E)]);U=np.array([np.cos(E),np.sin(E)]);V=np.array([np.cos(M),np.sin(M)])
ax.plot([P[0],U[0]],[0,U[1]],':',color=gray)
ax.plot([0,U[0]],[0,U[1]],color=orange);ax.plot([e,P[0]],[0,P[1]],color=blue)
ax.plot([0,V[0]],[0,V[1]],color=green,ls=':')
ax.plot(*P,'o',color=blue);ax.plot(*U,'o',color=orange);ax.plot(*V,'s',color=green)
ax.plot(e,0,'*',ms=13,color='#bb921d');ax.plot(0,0,'+',color=gray)
for center,r,ang,color,label in [((0,0),.26,E,orange,'E'),((0,0),.42,M,green,'M'),((e,0),.36,f,blue,'f')]:
    ax.add_patch(Arc(center,2*r,2*r,theta1=0,theta2=np.degrees(ang),color=color,lw=1.5))
    ax.text(center[0]+r*np.cos(ang/2),center[1]+r*np.sin(ang/2),label,color=color,fontsize=12)
ax.annotate('Particle P',P,(.77,.50),arrowprops={'arrowstyle':'->','color':blue},color=blue);ax.text(.25,1.10,'Auxiliary point',color=orange)
ax.annotate('Mean-phase marker',V,(.72,1.02),arrowprops={'arrowstyle':'->','color':green},color=green)
ax.text(e+.02,-.12,'Star / focus');ax.text(-.18,-.11,'Center');ax.text(.9,-.11,'Pericentre')
ax.plot([-1.15,1.2],[0,0],color=gray,lw=.6)
ax.set_aspect('equal');ax.set(xlim=(-1.2,1.3),ylim=(-1.13,1.23));ax.axis('off')
ax.set_title('Kepler anomaly geometry (eccentricity exaggerated for clarity)');ax.legend(loc='lower left')
fig.tight_layout();finish(fig)
