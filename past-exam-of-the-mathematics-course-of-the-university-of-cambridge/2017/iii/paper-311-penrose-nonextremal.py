"""Original causal quotient blocks; Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5.
Run from the intended media directory; writes the same-basename PNG to CWD.
The null lines and blocks are derived from the signed tortoise coordinate,
not traced from an external image. The infinite extension is truncated.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pathlib import Path
import numpy as np
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(9.20000001,9),dpi=100,facecolor='white')
ax.set_facecolor('white');ax.set_aspect('equal');ax.axis('off')
outer='#2166ac';inner='#b36a00';singular='#ad1d25'
def fill(pts,color):ax.add_patch(Polygon(pts,facecolor=color,edgecolor='none',zorder=0))
def line(a,b,c,lw=2.1):ax.plot([a[0],b[0]],[a[1],b[1]],color=c,lw=lw)
# Future trapped block, inner static blocks, next white-hole block.
fill([(0,0),(-1,1),(0,2),(1,1)],'#d9e9f7')
fill([(0,2),(-1,3),(0,4),(1,3)],'#f0e2ce')
for s in [-1,1]:
 fill([(0,2),(s,1),(s,3)],'#ffeded')
 for level in [0,4]:
  fill([(0,level),(s,level-1),(2*s,level),(s,level+1)],'#eef5ec')
  line((0,level),(s,level-1),outer);line((0,level),(s,level+1),outer)
  line((s,level-1),(2*s,level),'#333333');line((2*s,level),(s,level+1),'#333333')
  ax.text(1.12*s,level,'Exterior\n'+r'$r>r_+$',ha='center',va='center',fontsize=12)
  # Null infinities on the two sloped outer edges; i^0 at their junction.
  ax.text(1.77*s,level+.60,r'$\mathcal{I}^+$',ha='center',fontsize=14)
  ax.text(1.77*s,level-.70,r'$\mathcal{I}^-$',ha='center',fontsize=14)
  ax.text(2.11*s,level,r'$i^0$',ha='center',va='center',fontsize=13)
 line((0,2),(s,1),inner);line((0,2),(s,3),inner)
 # Timelike curvature boundary, rendered as a vertical zigzag.
 y=np.linspace(1,3,61);x=s+.028*np.sin(np.arange(61)*np.pi/2)
 ax.plot(x,y,color=singular,lw=2.6)
 ax.text(.59*s,2,'Static\n'+r'$0<r<r_-$',ha='center',va='center',fontsize=11)
 ax.text(1.13*s,2,r'$r=0$',ha='center',va='center',rotation=90 if s==1 else -90,color=singular,fontsize=12)
 ax.text(.46*s,.35,r'$r_+$',ha='center',color=outer,fontsize=12)
 ax.text(.45*s,1.60,r'$r_-$',ha='center',color=inner,fontsize=12)
ax.text(0,1,'Future black hole\n'+r'$r_-<r<r_+$'+'\n'+r'$r$ decreases to the future',ha='center',va='center',fontsize=10)
ax.text(0,3,'White hole\n'+r'$r_-<r<r_+$'+'\n'+r'$r$ increases to the future',ha='center',va='center',fontsize=10)
# Adjacent blocks continue beyond this finite strip, rather than ending at i^±.
for sign,level in [(-1,0),(1,4)]:
 fill([(0,level),(-1,level+sign),(0,level+2*sign),(1,level+sign)],'#f4f4f4')
 ax.text(0,level+.65*sign,'Extension repeats',ha='center',va='center',fontsize=11,color='#555555')
 ax.text(0,level+1.15*sign,'⋮',ha='center',va='center',fontsize=24)
ax.annotate('Future',xy=(2.50,3.9),xytext=(2.50,2.8),ha='center',arrowprops={'arrowstyle':'->','lw':1.8})
ax.set_xlim(-2.65,2.8);ax.set_ylim(-1.5,5.5)
fig.suptitle('Nonextremal equal-spin black hole: causal quotient',fontsize=15,y=.973)
fig.text(.5,.045,'Blue: outer horizons     Ochre: inner Cauchy horizons     Red: timelike singularities',ha='center',fontsize=10.5)
fig.text(.5,.022,'The circle fiber is suppressed. Each exterior has its own null infinities.',ha='center',fontsize=10.5)
fig.subplots_adjust(left=.055,right=.945,bottom=.09,top=.925)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
