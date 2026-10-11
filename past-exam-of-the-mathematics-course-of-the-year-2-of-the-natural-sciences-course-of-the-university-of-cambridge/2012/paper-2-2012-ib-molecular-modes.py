"""Original longitudinal molecular mode patterns. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the mirrored _media directory; PNG is saved to cwd on opaque white.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
import numpy as np


def spring(ax,left,right):
    xx=np.linspace(left,right,100);yy=np.zeros_like(xx)
    yy[8:-8]=.055*np.sin(np.linspace(0,14*np.pi,len(xx)-16))
    ax.plot(xx,yy,color='#8291a1',lw=1.5)


fig,axes=plt.subplots(1,3,figsize=(10,4.3),facecolor='white')
ratio=.75
shapes=[(1,1,1),(1,0,-1),(1,-2/ratio,1)]
titles=['Rigid translation','Symmetric stretch','Antisymmetric stretch']
freqs=[r'$\omega_0=0$',r'$\omega_s^2=k/m$',r'$\omega_a^2=k/m+2k/M$']
positions=[0,1.7,3.4];radii=[.19,.165,.19]
for ax,shape,title,freq in zip(axes,shapes,titles,freqs):
    spring(ax,positions[0]+radii[0],positions[1]-radii[1]);spring(ax,positions[1]+radii[1],positions[2]-radii[2])
    for p,rad,amplitude,label in zip(positions,radii,shape,['O','C','O']):
        ax.add_patch(Circle((p,0),rad,facecolor='#e2eaf2' if label=='O' else '#d0d5dd',edgecolor='#294d70',lw=1.5,zorder=3))
        ax.text(p,0,label,ha='center',va='center',fontsize=11)
        ax.text(p,.95,f'{amplitude:+.3f}' if amplitude else '0',ha='center',fontsize=10,color='#294d70')
        if amplitude:
            length=.3*amplitude
            ax.add_patch(FancyArrowPatch((p-length/2,.62),(p+length/2,.62),arrowstyle='-|>',shrinkA=0,shrinkB=0,mutation_scale=9,color='#b4502d',lw=1.8))
        else:ax.text(p,.62,'fixed',ha='center',va='center',fontsize=9,color='#718091')
    ax.text(1.7,-.63,freq,ha='center',fontsize=11)
    ax.set(xlim=(-.55,3.95),ylim=(-1,1.35),aspect='equal',title=title)
    ax.axis('off')
fig.suptitle('Longitudinal patterns of a free O–C–O spring model',fontsize=15,y=.98)
fig.text(.5,.13,'Numbers are relative displacements; the illustrated mass ratio is M/m = 3/4.',ha='center',fontsize=10)
fig.text(.5,.065,'Stretch patterns have sinusoidal amplitudes; rigid translation has amplitude A + Bt.',ha='center',fontsize=10)
fig.text(.5,.015,'“Symmetric” and “antisymmetric” refer to the two bond-length changes, not the directions of all three arrows.',ha='center',fontsize=9)
fig.subplots_adjust(left=.02,right=.98,top=.81,bottom=.25,wspace=.16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
plt.close(fig)
