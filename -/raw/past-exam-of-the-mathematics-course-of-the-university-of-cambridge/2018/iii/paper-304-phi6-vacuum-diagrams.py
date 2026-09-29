#!/usr/bin/env python3
"""Sextic vacuum graphs. Tested with Python 3.14.4, NumPy 2.3.5,
Matplotlib 3.10.7+dfsg1 (upstream dependency pin: 3.10.7).

Run from the desired output directory. Dependencies: matplotlib and numpy,
matching the repository's figure environment. Output: 1000 x 600 opaque PNG.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

fig, axes = plt.subplots(2, 3, figsize=(10, 6), dpi=100)
fig.patch.set_facecolor('white')
ink='#193b56'

def node(ax, x, y):
    ax.plot(x, y, 'o', color=ink, markersize=6, zorder=5)

def loop(ax, x, y, angle, radius=.115):
    t=np.linspace(0, 2*np.pi, 200)
    u=np.array([np.cos(angle), np.sin(angle)])
    v=np.array([-u[1],u[0]])
    pts=np.array([x,y])[:,None]+radius*((1-np.cos(t))[None,:]*u[:,None]+.7*np.sin(t)[None,:]*v[:,None])
    ax.plot(pts[0],pts[1],color=ink,lw=1.8)

def edge(ax, bend):
    vertices=[(.28,.53),(.40,.53+bend),(.60,.53+bend),(.72,.53)]
    ax.add_patch(PathPatch(MplPath(vertices,[MplPath.MOVETO,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4]),facecolor='none',edgecolor=ink,lw=1.8))

labels=['Empty graph: weight 1','One vertex: S = 48','Two vertices: r = 0, S = 4608','Two vertices: r = 2, S = 256','Two vertices: r = 4, S = 192','Two vertices: r = 6, S = 1440']
for ax,label in zip(axes.flat,labels):
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(label,fontsize=11,color=ink,pad=4)
axes.flat[0].text(.5,.53,r'$\varnothing$',ha='center',va='center',fontsize=42,color=ink)
ax=axes.flat[1]
for angle in [np.pi/2,7*np.pi/6,11*np.pi/6]:loop(ax,.5,.53,angle,.14)
node(ax,.5,.53)
for ax,r in zip(list(axes.flat)[2:],[0,2,4,6]):
    if r==0:
        left=[np.pi/2,np.pi,3*np.pi/2]; right=[np.pi/2,0,3*np.pi/2]
    elif r==2:
        left=[3*np.pi/4,5*np.pi/4];right=[np.pi/4,7*np.pi/4]
    elif r==4:
        left=[np.pi];right=[0]
    else:left=[];right=[]
    for a in left:loop(ax,.28,.53,a)
    for a in right:loop(ax,.72,.53,a)
    if r:
        for bend in np.linspace(-.32,.32,r):edge(ax,bend)
    node(ax,.28,.53);node(ax,.72,.53)
fig.subplots_adjust(left=.03,right=.97,bottom=.08,top=.93,wspace=.08,hspace=.30)
fig.text(.5,.025,'Each dot is a six-valent vertex. Lines may join vertices or form self-loops.',ha='center',fontsize=11,color=ink)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
plt.close(fig)
