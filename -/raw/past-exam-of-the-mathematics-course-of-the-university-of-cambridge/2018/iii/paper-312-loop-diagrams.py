#!/usr/bin/env python3
"""Wick-contraction topologies; Python 3.14 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,axes=plt.subplots(1,2,figsize=(8,3.4),dpi=100)
for ax in axes:
    ax.set_xlim(-1.4,1.4);ax.set_ylim(-1.3,1.8);ax.set_aspect('equal');ax.axis('off')
def edge(ax,p,q): ax.plot([p[0],q[0]],[p[1],q[1]],color='#356fa8',lw=2)
def node(ax,p,s):
    ax.scatter(*p,s=210,c='white',edgecolors='black',zorder=4)
    ax.text(p[0],p[1],s,ha='center',va='center',fontsize=10,zorder=5)
def out(ax,p,q,s):
    ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','lw':1.5})
    ax.text(q[0],q[1]+.08,s,ha='center',fontsize=11)
a=axes[0];p1=(0,.6);p2=(-.7,-.6);p3=(.7,-.6)
for p,q in [(p1,p2),(p2,p3),(p3,p1)]:edge(a,p,q)
for p in [p1,p2,p3]:node(a,p,'2')
out(a,p1,(0,1.15),r'$k_1$');out(a,p2,(-1.2,-.85),r'$k_2$');out(a,p3,(1.2,-.85),r'$k_3$')
a.text(-.51,.14,r'$q$',color='#356fa8');a.text(.4,.14,r'$k_1-q$',color='#356fa8');a.text(-.24,-.76,r'$k_2+q$',color='#356fa8')
a.set_title(r'$B_{222}$: triangle',fontsize=12);a.text(0,-1.18,'8 contractions',ha='center')
a=axes[1];center=(0,.1);left=(-.85,-.6);right=(.85,-.6)
edge(a,center,left);edge(a,center,right)
a.add_patch(Circle((0,.64),.54,fill=False,color='#356fa8',lw=2))
a.text(.63,.65,r'$q,-q$',color='#356fa8')
node(a,center,'4');node(a,left,'1');node(a,right,'1')
a.annotate('',xy=(0,-.55),xytext=center,arrowprops={'arrowstyle':'->','lw':1.5});a.text(.08,-.4,r'$k_3$',fontsize=11);out(a,left,(-1.2,-.95),r'$k_1$');out(a,right,(1.2,-.95),r'$k_2$')
a.set_title(r'$B_{411}$: loop at a fourth-order vertex',fontsize=11)
a.text(0,-1.18,'12 contractions; 3 external assignments',ha='center',fontsize=9)
fig.tight_layout();fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),facecolor='white')
