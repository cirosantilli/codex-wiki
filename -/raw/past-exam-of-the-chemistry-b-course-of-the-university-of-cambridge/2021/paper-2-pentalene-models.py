"""Original explanatory diagram; Python 3.14, matplotlib and numpy.
Run from the desired output directory; the PNG is written to that directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,3,figsize=(12,4.5),layout='constrained')
A=np.array([0,.55]);B=np.array([0,-.55]);left=[A,[-.95,.95],[-1.55,0],[-.95,-.95],B];right=[A,[.95,.95],[1.55,0],[.95,-.95],B]
for ax,metal in zip(axs,['Fe','Co','Ni']):
    for pts in [left,right]:
        for a,b in zip(pts,pts[1:]):bond(ax,a,b)
    if metal!='Ni':bond(ax,A,B)
    if metal=='Ni':
        bond(ax,A,B,2)
        for seq in [left[1:4],right[1:4]]:
            for a,b in zip(seq,seq[1:]):bond(ax,a,b,color=BLUE,lw=4)
        ms=[(-1.35,1.6),(1.35,-1.6)];rs=[(-1.1,0),(1.1,0)];cnt='10 + 5 + 3 = 18';mode='η³:η³, outer allyl regions'
    else:
        ms=[(-.75,1.8),(.75,1.8 if metal=='Fe' else -1.8)];rs=[(-.65,0),(.65,0)]
        for r in rs:ax.add_patch(Circle(r,.45,fill=False,ec=BLUE,lw=1.4))
        cnt='8 + 5 + 4 + 1 = 18' if metal=='Fe' else '9 + 5 + 4 = 18';mode='syn η⁵:η⁵ + Fe–Fe' if metal=='Fe' else 'anti η⁵:η⁵ shown; syn also possible'
    for m,r in zip(ms,rs):
        bond(ax,m,r,style='dashed',color=BLUE);atom(ax,m,metal);dy=.48 if m[1]>0 else -.48;bond(ax,m,(m[0],m[1]+dy));atom(ax,(m[0],m[1]+dy),'Cp')
    if metal=='Fe':bond(ax,ms[0],ms[1],color=ORANGE,lw=2.5)
    ax.text(0,-3.0,cnt,ha='center');ax.text(0,-3.5,'per metal, neutral counting',ha='center',fontsize=10)
    finish(ax,(-2.2,2.2),(-3.9,3),metal+': '+mode)
fig.suptitle('Formal 18-electron proposals; coordination lines are schematic',fontsize=12)
save(fig,'paper-2-pentalene-models.png')
