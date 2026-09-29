"""Original unequal-mass mode illustration. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the mirrored _media directory; the opaque white PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,FancyArrowPatch
import numpy as np


def spring(ax,left,right):
    xx=np.linspace(left,right,121);yy=np.zeros_like(xx)
    yy[8:-8]=.07*np.sin(np.linspace(0,16*np.pi,len(xx)-16))
    ax.plot(xx,yy,color='#72859a',lw=1.4)


fig,axes=plt.subplots(1,2,figsize=(9,3.9),facecolor='white')
ratios=[(1+np.sqrt(3))/2,(1-np.sqrt(3))/2]
labels=[r'$\omega_-^2=\dfrac{k}{m_1}\dfrac{3-\sqrt{3}}{2}$',r'$\omega_+^2=\dfrac{k}{m_1}\dfrac{3+\sqrt{3}}{2}$']
for ax,ratio,title,freq in zip(axes,ratios,['Lower mode: in phase','Higher mode: opposite directions'],labels):
    for wall in [-.08,4]:ax.add_patch(Rectangle((wall,-.4),.08,.8,color='#bbc6d0'))
    points=[1.15,2.85];radii=[.19,.19*np.sqrt(2)]
    spring(ax,0,points[0]-radii[0]);spring(ax,points[0]+radii[0],points[1]-radii[1]);spring(ax,points[1]+radii[1],4)
    for j,(p,rad,amp) in enumerate(zip(points,radii,[1,ratio]),1):
        ax.add_patch(Circle((p,0),rad,facecolor='#e0ebf4',edgecolor='#2a557b',lw=1.5,zorder=3))
        ax.text(p,0,rf'$m_{j}$',ha='center',va='center',fontsize=11)
        length=.6*amp
        ax.add_patch(FancyArrowPatch((p-length/2,.57),(p+length/2,.57),arrowstyle='-|>',mutation_scale=11,shrinkA=0,shrinkB=0,lw=1.9,color='#b45131'))
        ax.text(p,.84,f'{amp:+.3f}',ha='center',fontsize=11,color='#2a557b')
    ax.text(2,-.7,freq,ha='center',fontsize=13)
    ax.set(xlim=(-.3,4.3),ylim=(-1.1,1.25),aspect='equal',title=title)
    ax.axis('off')
fig.suptitle('Two normal modes for an example with $m_2=2m_1$',fontsize=15,y=.98)
fig.text(.5,.12,'Arrows give relative horizontal displacements; all three spring constants equal k.',ha='center',fontsize=10)
fig.text(.5,.035,'Springs are drawn at equilibrium; each arrow pattern acquires one sinusoidal time amplitude.',ha='center',fontsize=9)
fig.subplots_adjust(left=.03,right=.97,top=.8,bottom=.21,wspace=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
plt.close(fig)
