"""Original source/image arrangements, not copied exam artwork; PNG into cwd."""
from pathlib import Path
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(13,4.5),facecolor='white');ax=fig.add_subplot(131,projection='3d')
source=np.array([.4,.5,.6])
for signs in itertools.product([-1,1],repeat=3):
 point=source*np.array(signs);strength=np.prod(signs);original=signs==(1,1,1)
 ax.scatter(*point,color='#278c4a' if original else '#ba3434' if strength>0 else '#247ba0',s=45)
 ax.text(*point,'  +1' if strength>0 else '  -1',fontsize=8)
for axis in range(3):
 a,b=np.meshgrid([-.75,.75],[-.75,.75]);parts=[a,b];parts.insert(axis,np.zeros_like(a));ax.plot_surface(*parts,color='gray',alpha=.06)
ax.set(xlabel='x',ylabel='y',zlabel='z',title='Octant: seven image points',xlim=(-.8,.8),ylim=(-.8,.8),zlim=(-.8,.8));ax.view_init(20,-50)
ax=fig.add_subplot(132);theta=np.linspace(0,2*np.pi,400);ax.plot(np.cos(theta),np.sin(theta),color='gray',lw=2)
r0=.45;star=1/r0
ax.scatter([r0],[0],color='#278c4a',s=60);ax.scatter([star],[0],color='#247ba0',s=90)
ax.annotate('Source: +1',(r0,0),(.0,.55),arrowprops={'arrowstyle':'-','color':'gray'},fontsize=9)
ax.annotate(r'Image: $-a/r_0$',(star,0),(1.25,.55),arrowprops={'arrowstyle':'-','color':'gray'},fontsize=9)
ax.text(.0,-1.18,r'$a=1,\ r_0=0.45,\ r_* = a^2/r_0$',fontsize=9)
ax.axhline(0,color='gray',lw=.5);ax.set(xlim=(-1.25,2.8),ylim=(-1.4,1.3),aspect='equal',title='Sphere: weighted exterior image');ax.axis('off')
ax=fig.add_subplot(133);ax.axvspan(-1,1,color='#e8f2ec');ax.axvline(-1,color='gray',lw=2);ax.axvline(1,color='gray',lw=2)
for n in range(-3,4):
 xx=2*n;color='#278c4a' if n==0 else '#ba3434' if n%2==0 else '#247ba0'
 ax.scatter([xx],[0],color=color,s=45);ax.text(xx,.2,'+1' if n%2==0 else '-1',ha='center',fontsize=9)
ax.text(-6.6,0,'...',ha='right');ax.text(6.6,0,'...',ha='left');ax.text(0,-.5,'Source region',ha='center',fontsize=9)
ax.set(xlim=(-7,7),ylim=(-.7,1),title='Plates: alternating infinite array',xlabel='Image position x = 2n');ax.set_yticks([])
fig.suptitle('Green-function images: green marks the original positive source',fontsize=13)
fig.tight_layout(rect=(0,0,1,.93));fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white');plt.close(fig)
