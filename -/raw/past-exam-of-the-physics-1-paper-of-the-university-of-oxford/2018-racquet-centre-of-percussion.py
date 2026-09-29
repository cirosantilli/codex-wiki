"""Plot the computed racquet geometry in a vertical layout. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({'font.size': 13, 'figure.facecolor': 'white'})
fig, ax = plt.subplots(figsize=(8,6.5), layout='constrained')
ax.set_aspect('equal')
ax.set_xlim(-1.45,2.65)
ax.set_ylim(-3.55,1.4)
ax.axis('off')
ax.add_patch(Circle((0,0),1,fill=False,edgecolor='#333333',lw=3))
ax.plot([0,0],[-1,-3],color='#333333',lw=7,solid_capstyle='butt')
ax.plot([0,0],[-3.2,1.12],color='#aaaaaa',lw=.8,linestyle=':')
points=[(0.,'#666666',r'Head centre: $X=0$',(1.15,.42)),(-7/24,'#a23c27',r'Impact: $X=7a/24$',(1.15,-.38)),(-1.,'#205c96',r'CM: $X=a$',(1.15,-1.05)),(-3.,'#222222',r'Hand P: $X=3a$',(1.15,-3.))]
for y,color,label,text_pos in points:
    ax.scatter([0],[y],s=75 if y !=0 else 30,color=color,edgecolor='white',linewidth=.8,zorder=5)
    ax.annotate(label,xy=(0,y),xytext=text_pos,fontsize=13,color=color,va='center',arrowprops={'arrowstyle':'-','color':color,'lw':1})
ax.annotate('',xy=(-.65,-3),xytext=(-.65,-7/24),arrowprops={'arrowstyle':'<->','color':'#a23c27','lw':1.5})
ax.text(-.80,-1.8,r'$b=65a/24$',rotation=90,ha='center',va='center',color='#a23c27')
ax.annotate('',xy=(-1.18,-3),xytext=(-1.18,-1),arrowprops={'arrowstyle':'<->','color':'#205c96','lw':1.5})
ax.text(-1.32,-2,r'$d=2a$',rotation=90,ha='center',va='center',color='#205c96')
ax.text(0,1.18,r'Head radius $a$, head mass $M$',ha='center',fontsize=12)
ax.text(1.2,-2.,r'Handle length $2a$'+'\n'+r'Handle mass $M$',ha='left',va='center',fontsize=12)
ax.text(.5,-3.4,r'Impact impulse is perpendicular to the racquet face',ha='center',fontsize=11)
ax.set_title('Centre of percussion: zero impulsive hand reaction',fontsize=16,pad=12)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
