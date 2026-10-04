"""Original phase-portrait sketches on primary/compound homoclinic curves.
Numpy/matplotlib, Python 3.14; caller-CWD PNG basename output only.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Circle, Ellipse
blue='#0068a3';orange='#b45720'

def lobe(ax,s=1):
    vertices=np.array([(0,0),(.8,0),(1.6,0),(1.6,.8),(1.6,1.6),(1.6,1.6),(.8,1.6),(0,1.6),(0,.8),(0,0)])*s
    ax.add_patch(PathPatch(Path(vertices,[Path.MOVETO]+[Path.CURVE4]*9),fill=False,color=orange,lw=1.8))
    ax.annotate('',xy=(s*1.6,s*1.1),xytext=(s*1.6,s*.65),arrowprops={'arrowstyle':'->','color':orange,'lw':1.3})

def compound(ax,s=1):
    vertices=np.array([(0,0),(-.8,0),(-1.6,0),(-1.6,-.8),(-1.6,-1.6),(-1.0,-1.6),(-.5,-1.3),(.1,-.8),(.1,-.18),(.4,-.03),(1.1,0),(1.6,.15),(1.6,.8),(1.6,1.6),(1.2,1.6),(.8,1.6),(0,1.6),(0,.8),(0,0)])*s
    ax.add_patch(PathPatch(Path(vertices,[Path.MOVETO]+[Path.CURVE4]*18),fill=False,color=orange,lw=1.8))
    ax.annotate('',xy=(-s*1.6,-s*1.1),xytext=(-s*1.6,-s*.65),arrowprops={'arrowstyle':'->','color':orange,'lw':1.3})
    ax.annotate('',xy=(s*1.6,s*1.1),xytext=(s*1.6,s*.65),arrowprops={'arrowstyle':'->','color':orange,'lw':1.3})

def cycle(ax,s):
    ax.add_patch(Circle((s*.82,s*.82),.46,fill=False,color=blue,lw=1.6))

def outer(ax):
    ax.add_patch(Ellipse((0,0),5.15,2.4,angle=45,fill=False,color=blue,lw=1.6))

fig,axes=plt.subplots(2,4,figsize=(12,6.8),constrained_layout=True)
settings=[(r'$\mu=0,\ \nu<0$: R loop + L cycle','right',-1,False),(r'$\mu=0,\ \nu>0$: R loop + G cycle','right',None,True),(r'$\nu=0,\ \mu<0$: L loop + R cycle','left',1,False),(r'$\nu=0,\ \mu>0$: L loop + G cycle','left',None,True),(r'$C_R$: compound loop + R cycle','cr',1,False),(r'$C_L$: compound loop + L cycle','cl',-1,False),(r'$\mu=\nu=0$: two primary loops','double',None,False)]
for ax,(title,kind,other,g) in zip(axes.flat,settings):
    if kind in ['right','double']:lobe(ax,1)
    if kind in ['left','double']:lobe(ax,-1)
    if kind=='cr':compound(ax,1)
    if kind=='cl':compound(ax,-1)
    if other:cycle(ax,other)
    if g:outer(ax)
    ax.plot(0,0,'kx',ms=6,mew=1.3)
    ax.set(xlim=(-2.1,2.1),ylim=(-2.1,2.1),aspect='equal',title=title)
    ax.title.set_fontsize(8)
    ax.axis('off')
axes.flat[7].axis('off')
axes.flat[7].text(.05,.7,'Orange: homoclinic connections\nBlue: surviving stable cycles\n×: given saddle\n\nTopology schematics; unspecified\ninterior equilibria are omitted.',fontsize=10,va='center')
fig.suptitle('Every global curve, including both signs on each primary-loop axis',fontsize=11)
fig.savefig('paper-59-gluing-connections.png',dpi=120,facecolor='white')
plt.close(fig)
