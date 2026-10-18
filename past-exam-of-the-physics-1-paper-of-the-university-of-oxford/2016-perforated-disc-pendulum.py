from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
plt.rcParams.update({'font.size':13,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white'})
R=1.;a=.23;b=.48;M=1.;m=a*a;c=R-a
fig,axs=plt.subplots(1,2,figsize=(11,5.8),layout='constrained')
for j,ax in enumerate(axs):
 ax.add_patch(Circle((0,0),R,facecolor='#e4e6e8',edgecolor='.25',lw=2))
 ax.add_patch(Circle((b,0),a,facecolor='white',edgecolor='#D55E00',lw=2))
 if j:ax.add_patch(Circle((-c,0),a,facecolor='#acd7e5',edgecolor='#0072B2',lw=2))
 ax.plot([0,b],[0,0],'--',color='#D55E00');ax.text(b/2,.055,r'$b$',ha='center');ax.scatter(0,0,s=50,c='black',zorder=5);ax.text(.03,-.13,r'$O$',fontsize=13)
 cm=-m*b/(M-m) if not j else -m*(b+c)/M
 ax.scatter(cm,0,c='#c42b30',marker='x',s=85,lw=2,zorder=6);ax.annotate('centre of mass',xy=(cm,0),xytext=(-.65,-.6),arrowprops={'arrowstyle':'->','color':'#c42b30'},color='#c42b30',fontsize=11)
 ax.annotate('removed disk',xy=(b,0),xytext=(.15,.65),arrowprops={'arrowstyle':'->','color':'#D55E00'},color='#D55E00',fontsize=11)
 ax.set(xlim=(-1.25,1.25),ylim=(-1.15,1.17),aspect='equal');ax.axis('off')
axs[0].set_title('Hole only: restoring moment mgb')
axs[1].set_title('Hole plus reattached disk: mg(b+c)')
axs[1].annotate('same small disk\nattached over this region',xy=(-c,0),xytext=(-1.1,.7),arrowprops={'arrowstyle':'->','color':'#0072B2'},color='#0072B2',fontsize=11)
axs[1].text(-.72,-.32,r'$c=R-a$',fontsize=12)
fig.suptitle('The pivot stays at O; removing and relocating mass changes both inertia and restoring torque',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white');plt.close(fig)
