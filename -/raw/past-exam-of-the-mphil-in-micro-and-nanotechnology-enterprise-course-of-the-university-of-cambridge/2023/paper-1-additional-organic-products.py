"""Original derived B, D and F skeletal structures; Python 3.14.

Uses the shared chemical drawing primitives; PNG output remains a cwd basename.
"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond,atom,ring,finish,save

fig,axes=plt.subplots(1,3,figsize=(13,4.2),layout='constrained',gridspec_kw={'width_ratios':[1.15,1.45,1]})
fig.patch.set_facecolor('white')

def triple(ax,a,b):
    a=np.asarray(a,float);b=np.asarray(b,float)
    v=b-a;off=np.array([-v[1],v[0]])/np.linalg.norm(v)*.065
    for f in [-1,0,1]:bond(ax,a+f*off,b+f*off,lw=1.4)

def mark(ax,p,text):
    ax.text(*p,text,color='#285f96',fontsize=11,ha='center',va='center')

ax=axes[0]
c=np.array([0.,0.]);sp=np.array([-1.05,.38]);end=np.array([-2.1,.76])
bond(ax,c,sp);triple(ax,sp,end)
for pt in [(.05,1.12),(-.43,-1.02)]:bond(ax,c,pt)
bond(ax,c,(1.0,0));atom(ax,(1,0),'O')
bond(ax,(1,0),(1.85,.5));bond(ax,(1.85,.5),(2.75,0))
for pt,label in [((2.94,.1),'a'),((1.9,.78),'b'),((.05,1.4),'c'),((-.5,-1.3),'c'),((-2.3,.93),'d')]:mark(ax,pt,label)
ax.text(.25,-1.85,'a 1.21   b 3.59\nc 1.46   d 2.66 ppm',ha='center',fontsize=10,color='#285f96')
finish(ax,(-2.7,3.4),(-2.2,1.9),'B: tertiary propargylic ether')
ax=axes[1]
th=np.deg2rad(np.arange(30,390,60))
pts=np.column_stack([np.cos(th),np.sin(th)])
ring(ax,pts,{0:2,2:2,4:2})
# Benzylic substitution at vertex 0, ring chlorine at vertex 2: meta.
a=pts[0];chain=[a,(1.73,1.0),(2.60,.5),(3.47,1.0),(4.34,.5)]
for x,y in zip(chain[:-1],chain[1:]):bond(ax,x,y)
atom(ax,chain[2],'O')
bond(ax,pts[2],(-1.73,1.0));atom(ax,(-1.9,1.1),'Cl')
for pt,label in [((4.55,.55),'e'),((3.5,1.3),'f'),((1.72,1.3),'g'),((0,1.35),'h'),((-1.1,-.85),'h'),((0,-1.35),'h'),((1.1,-.85),'h')]:mark(ax,pt,label)
ax.text(1.35,-1.85,'e 1.18   f 3.58   g 4.80\nh 7.20–7.58 ppm',ha='center',fontsize=10,color='#285f96')
finish(ax,(-2.5,4.9),(-2.2,1.9),'D: meta-chlorobenzyl ethyl ether')
ax=axes[2]
triple(ax,(-2,0),(-1,0));bond(ax,(-1,0),(0,0))
bond(ax,(0,0),(1,.7),order=2)
bond(ax,(0,0),(0,-1))
ax.text(-.45,-1.85,r'$\mathrm{C_5H_6}$: conjugated enyne',ha='center',fontsize=10.5)
finish(ax,(-2.6,1.8),(-2.2,1.9),'F: elimination product')
save(fig,'paper-1-additional-organic-products.png',dpi=160)
