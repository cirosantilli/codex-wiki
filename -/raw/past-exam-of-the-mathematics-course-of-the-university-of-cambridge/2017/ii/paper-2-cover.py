#!/usr/bin/env python3
"""Original schematic; Python 3.14, Matplotlib 3.10.7, NumPy 2.3.5.
Run from any output directory; writes the same-basename opaque white PNG there.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 5), dpi=100, facecolor='white')
ax.set_facecolor('white')
xs = (1.6, 4.7, 7.8)
ytop, ybottom = 3.25, 1.55
for i,x in enumerate(xs):
    ax.add_patch(Ellipse((x,2.4),1.25,1.7,facecolor='#e7eef8',edgecolor='#42638d',linewidth=1.8,zorder=1))
    ax.add_patch(Ellipse((x,2.4),.42,1.7,fill=False,edgecolor='#7793b6',linewidth=1,linestyle='--',zorder=2))
    ax.text(x+.82,2.4,rf'$S^2_{i+1}$',fontsize=14,color='#42638d',ha='center',va='center')
labels_top = (r'$e$',r'$b$',r'$b^2$')
labels_bottom = (r'$a$',r'$ab^2$',r'$ab$')
for x,t,b in zip(xs,labels_top,labels_bottom):
    ax.plot([x,x],[ytop,ybottom],'o',color='#172b46',ms=6,zorder=5)
    ax.text(x,ytop+.13,t,ha='center',va='bottom',fontsize=16,bbox=dict(facecolor='white',edgecolor='none',pad=.4),zorder=6)
    ax.text(x,ybottom-.13,b,ha='center',va='top',fontsize=16,bbox=dict(facecolor='white',edgecolor='none',pad=.4),zorder=6)

def edge(x1,x2,y,rad,color):
    ax.add_patch(FancyArrowPatch((x1,y),(x2,y),connectionstyle=f'arc3,rad={rad}',arrowstyle='-|>',mutation_scale=15,linewidth=2,color=color,shrinkA=5,shrinkB=5,zorder=3))
# The two directed b-cycles are separate lifted circles.
edge(xs[0],xs[1],ytop,0,'#9c4b20');edge(xs[1],xs[2],ytop,0,'#9c4b20');edge(xs[2],xs[0],ytop,.24,'#9c4b20')
edge(xs[0],xs[2],ybottom,.24,'#187369');edge(xs[2],xs[1],ybottom,0,'#187369');edge(xs[1],xs[0],ybottom,0,'#187369')
ax.text(4.7,4.35,'Three spheres; two circles attached at six marked points',ha='center',fontsize=15)
ax.text(4.7,.18,r'Each sphere pairs $b^i$ with $b^ia=ab^{-i}$; arrows lift the generator $b$.',ha='center',fontsize=12)
ax.set_xlim(0,9.7);ax.set_ylim(-.05,4.7);ax.axis('off')
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
