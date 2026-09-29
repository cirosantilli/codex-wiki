#!/usr/bin/env python3
"""Original quartic-scalar diagrams. Emits paper-52-diagrams.png to caller CWD.
Test environment: Python 3.14, NumPy 2.3.5, matplotlib 3.10.7.
MPLCONFIGDIR is supplied by the caller/Makefile and is never overridden.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

fig, axes = plt.subplots(3, 4, figsize=(12, 9.3), dpi=110)
fig.patch.set_facecolor('white')
for ax in axes.flat:
    ax.set(xlim=(-1.4, 1.4), ylim=(-1.25, 1.35), aspect='equal')
    ax.set_facecolor('white')
    ax.axis('off')

def line(ax,a,b):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.6)

def vertex(ax,v):
    ax.plot(*v,'o',color='black',ms=4.2)

def label(ax,p,text):
    ax.text(*p,text,fontsize=10.5,ha='center',va='center')

def caption(ax,title,sub):
    ax.set_title(title,fontsize=11.3,fontweight='bold',pad=8)
    ax.text(0,-1.1,sub,ha='center',va='center',fontsize=10)

ax=axes[0,0]
line(ax,(-1,0),(1,0));label(ax,(-1.18,0),'1');label(ax,(1.18,0),'2')
caption(ax,'Free two-point line',r'$O(1)$; no loop integral')
ax=axes[0,1]
line(ax,(-1,0),(0,0));line(ax,(0,0),(1,0));ax.add_patch(Circle((0,.45),.45,fill=False,lw=1.6,color='black'));vertex(ax,(0,0))
label(ax,(-1.18,0),'1');label(ax,(1.18,0),'2')
caption(ax,'Two-point tadpole',r'$O(\lambda_0)$; $D=2$; $S=2$')
ax=axes[0,2]
vertex(ax,(0,0))
for p,n in [((-0.9,.7),1),((-.9,-.7),2),((.9,.7),3),((.9,-.7),4)]:
    line(ax,(0,0),p);label(ax,(p[0]*1.15,p[1]*1.15),str(n))
caption(ax,'Four-point contact',r'$O(\lambda_0)$; no loop integral')

def bubble(ax,title,lab):
    vl=(-.45,0);vr=(.45,0)
    for rad in [-.85,.85]:
        ax.add_patch(FancyArrowPatch(vl,vr,arrowstyle='-',connectionstyle=f'arc3,rad={rad}',lw=1.6,color='black'))
    for v,p,n in [(vl,(-1.05,.7),lab[0]),(vl,(-1.05,-.7),lab[1]),(vr,(1.05,.7),lab[2]),(vr,(1.05,-.7),lab[3])]:
        line(ax,v,p);label(ax,(p[0]*1.17,p[1]*1.14),str(n))
    vertex(ax,vl);vertex(ax,vr)
    caption(ax,title,r'$O(\lambda_0^2)$; $D=0$; $S=2$')

bubble(axes[0,3],r'Four-point bubble: $s$',(1,2,3,4))
bubble(axes[1,0],r'Four-point bubble: $t$',(1,3,2,4))
bubble(axes[1,1],r'Four-point bubble: $u$',(1,4,2,3))
ax=axes[1,2]
vs=[np.array([-.45,.4]),np.array([.45,.4]),np.array([0.,-.22])]
for i in range(3):line(ax,vs[i],vs[(i+1)%3])
n=1
for v in vs:
    base=np.arctan2(v[1],v[0])
    for shift in [-.38,.38]:
        d=np.array([np.cos(base+shift),np.sin(base+shift)])
        p=v+.62*d;line(ax,v,p);label(ax,p+.16*d,str(n));n+=1
    vertex(ax,v)
caption(ax,'Six-point triangle',r'$O(\lambda_0^3)$; $D=-2$; $S=1$')
ax=axes[1,3]
ax.text(0,.85,'Solid lines: scalar propagators\nDots: quartic interaction vertices',ha='center',va='center',fontsize=10.2,linespacing=1.5)
ax.text(0,.12,r'$s=(p_1+p_2)^2$'+'\n'+r'$t=(p_1+p_3)^2$'+'\n'+r'$u=(p_1+p_4)^2$',ha='center',va='center',fontsize=11,linespacing=1.7)
ax.text(0,-.95,'All external momenta incoming.\nExternal propagators are omitted\nfrom interaction sketches.',ha='center',va='center',fontsize=9.4,linespacing=1.3)
def pairing(ax,title,pairs):
    pts={1:(-.9,.55),2:(-.9,-.55),3:(.9,.55),4:(.9,-.55)}
    for i,j in pairs:line(ax,pts[i],pts[j])
    for n,p in pts.items():label(ax,(p[0]*1.16,p[1]*1.15),str(n))
    caption(ax,title,r'$O(1)$; disconnected, no loops')

pairing(axes[2,0],'Free four-point pairing 12 | 34',[(1,2),(3,4)])
pairing(axes[2,1],'Free four-point pairing 13 | 24',[(1,3),(2,4)])
pairing(axes[2,2],'Free four-point pairing 14 | 23',[(1,4),(2,3)])
axes[2,3].text(0,.4,'Bottom row: three Wick pairings\nof the full free four-point correlator.',ha='center',va='center',fontsize=10,linespacing=1.5)
axes[2,3].text(0,-.25,'A crossing without a dot\nis not an interaction vertex.\nThe connected free four-point\ncorrelator vanishes.',ha='center',va='center',fontsize=10,linespacing=1.5)
fig.suptitle('Lowest-order scalar graphs and the one-loop quartic channels',fontsize=14,y=.98)
fig.subplots_adjust(left=.025,right=.975,top=.93,bottom=.035,wspace=.2,hspace=.28)
fig.savefig(Path('paper-52-diagrams.png'),facecolor='white',edgecolor='white',transparent=False)
plt.close(fig)
