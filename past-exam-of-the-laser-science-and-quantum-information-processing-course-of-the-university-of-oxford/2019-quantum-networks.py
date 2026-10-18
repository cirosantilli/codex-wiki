"""Original gate networks for measurement and Boolean-oracle identities; Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
fig,axs=plt.subplots(2,2,figsize=(11.6,7.2),facecolor='white')
fig.subplots_adjust(left=.06,right=.95,bottom=.08,top=.89,wspace=.30,hspace=.42)
def setup(ax,title,labels):
    ax.set(xlim=(-.1,1.1),ylim=(-.15,1.1));ax.axis('off');ax.set_title(title,fontsize=13)
    ys=[.8-.30*i for i in range(len(labels))]
    for y,label in zip(ys,labels):ax.plot([0,1],[y,y],color='#25394c',lw=1.2);ax.text(-.035,y,label,ha='right',va='center',fontsize=12)
    return ys
def box(ax,x,y,label,w=.12,h=.17):
    ax.add_patch(Rectangle((x-w/2,y-h/2),w,h,facecolor='white',edgecolor='#25394c',zorder=4));ax.text(x,y,label,ha='center',va='center',fontsize=12,zorder=5)
def cx(ax,x,control,target,extra=None):
    ends=[control,target]+([] if extra is None else [extra]);ax.plot([x,x],[min(ends),max(ends)],color='#25394c')
    for y in [control]+([] if extra is None else [extra]):ax.plot(x,y,'o',color='#25394c',ms=5)
    ax.add_patch(Circle((x,target),.035,facecolor='white',edgecolor='#25394c',zorder=4));ax.plot([x-.035,x+.035],[target,target],color='#25394c',zorder=5);ax.plot([x,x],[target-.035,target+.035],color='#25394c',zorder=5)
a=axs[0,0];(y,)=setup(a,'X measurement using a Z instrument',[r'$|\psi\rangle$'])
for x,label in [(.20,'H'),(.48,r'$M_Z$'),(.76,'H')]:box(a,x,y,label)
a.text(.48,.47,'Record: 0 = +, 1 = −',ha='center',fontsize=11)
a.text(.5,.17,'Last H restores the X eigenstate\nfor a surviving measured qubit.',ha='center',fontsize=11)
a=axs[0,1];ya,yb,yc=setup(a,'Controlled swap from three gates',[r'$a$',r'$b$',r'$c$'])
cx(a,.23,yb,yc);cx(a,.50,ya,yb,extra=yc);cx(a,.77,yb,yc)
a.text(.5,-.03,'If a = 1, interchange b and c.',ha='center',fontsize=11)
a=axs[1,0];yx,yy=setup(a,'Two-query function-class test',[r'$|0\rangle_x$',r'$|0\rangle_y$'])
for x in [.23,.72]:
    a.add_patch(Rectangle((x-.08,yy-.10),.16,yx-yy+.20,facecolor='white',edgecolor='#25394c',zorder=4));a.text(x,(yx+yy)/2,r'$U_f$',ha='center',va='center',fontsize=14,zorder=5)
box(a,.48,yx,'X');box(a,.93,yy,r'$M_Z$',w=.13)
a.text(.5,.12,r'Answer: $f(0)\oplus f(1)$',ha='center',fontsize=13)
a=axs[1,1];yx,yy=setup(a,'Deutsch circuit after conjugating by H',[r'$|0\rangle_x$',r'$|1\rangle_y$'])
cx(a,.38,yy,yx);a.text(.38,.99,r'Apply iff $b=1$',ha='center',fontsize=10)
box(a,.72,yy,r'$Z^a$');a.text(1.02,yx,r'$|b\rangle$',va='center',fontsize=12);a.text(1.02,yy,r'$|1\rangle$',va='center',fontsize=12)
a.text(.5,.12,r'$a=f(0),\quad b=f(0)\oplus f(1)$',ha='center',fontsize=12)
a.text(.5,-.02,r'Overall phase: $(-1)^a$',ha='center',fontsize=11)
fig.suptitle('Measurement and reversible-logic networks',fontsize=18,y=.97)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
