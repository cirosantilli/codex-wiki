"""Original charged causal blocks, truncated with repetition arrows.
Python 3.14; Matplotlib and NumPy. PNG basename output to caller CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,ax=plt.subplots(figsize=(7.8,7.1),facecolor='white')
ax.axis('off');ax.set_aspect('equal');ax.set_facecolor('white')
outer='#175b91';inner='#ad650c';red='#ab2538';dark='#333333'
def line(a,b,color,lw=1.8):ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=lw)
def fill(p,col):ax.add_patch(Polygon(p,facecolor=col,edgecolor='none'))
fill([(0,0),(-1,1),(0,2),(1,1)],'#e5eef9')
fill([(0,2),(-1,3),(0,4),(1,3)],'#f2eadc')
for sign in [-1,1]:
 fill([(0,2),(sign,1),(sign,3)],'#fae9ec')
 line((0,2),(sign,1),inner);line((0,2),(sign,3),inner)
 y=np.linspace(1,3,121);x=sign+.025*np.sin(np.arange(121)*np.pi/2)
 ax.plot(x,y,color=red,lw=2.5)
 ax.text(.60*sign,2,'Static\n'+r'$r<r_-$',ha='center',va='center',fontsize=10)
 ax.text(1.15*sign,2,r'$r=0$',ha='center',va='center',color=red,rotation=90,fontsize=11)
 for level in [0,4]:
  fill([(0,level),(sign,level-1),(2*sign,level),(sign,level+1)],'#edf4ea')
  line((0,level),(sign,level-1),outer);line((0,level),(sign,level+1),outer)
  line((sign,level-1),(2*sign,level),dark);line((2*sign,level),(sign,level+1),dark)
  ax.text(1.16*sign,level,'Exterior\n'+r'$r>r_+$',ha='center',va='center',fontsize=10)
  ax.text(1.79*sign,level+.63,r'$\mathcal{I}^+$',ha='center',fontsize=12)
  ax.text(1.79*sign,level-.71,r'$\mathcal{I}^-$',ha='center',fontsize=12)
  ax.text(2.17*sign,level,r'$i^0$',ha='center',va='center',fontsize=11)
 ax.text(.44*sign,.32,r'$r_+$',ha='center',color=outer,fontsize=10)
 ax.text(.43*sign,1.67,r'$r_-$',ha='center',color=inner,fontsize=10)
ax.text(0,1,'Trapped band\n'+r'$r_-<r<r_+$'+'\nr decreases to future',ha='center',va='center',fontsize=9)
ax.text(0,3,'White-hole band\n'+r'$r_-<r<r_+$'+'\nr increases to future',ha='center',va='center',fontsize=9)
for y,direction in [(0,-1),(4,1)]:
 ax.annotate('Repeat',xy=(0,y+direction*1.36),xytext=(0,y+direction*.74),ha='center',va='center',fontsize=10,color='#555555',arrowprops={'arrowstyle':'->','color':'#555555'})
ax.annotate('Future',xy=(2.5,3.3),xytext=(2.5,2.6),ha='center',fontsize=10,arrowprops={'arrowstyle':'->'})
ax.set_xlim(-2.7,2.85);ax.set_ylim(-1.55,5.55)
fig.suptitle('Nonextremal charged extension: 0 < |Q| < M',fontsize=13,y=.965)
fig.text(.5,.045,'Blue: outer horizons   Ochre: inner Cauchy horizons   Red: timelike singularities',ha='center',fontsize=9)
fig.text(.5,.018,'The displayed blocks continue indefinitely in both time directions.',ha='center',fontsize=9)
fig.subplots_adjust(left=.04,right=.95,bottom=.09,top=.92)
fig.savefig(Path.cwd()/'paper-57-causal-charged.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
