"""Original circuit diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

fig, axs=plt.subplots(3,2,figsize=(13,10),layout='constrained',facecolor='white')
def setup(ax, title, ins, outs):
    n=len(ins);ax.set_title(title,fontsize=12,pad=10)
    for i,(x,y) in enumerate(zip(ins,outs)):
        ax.plot([.7,5.3],[-i,-i],color='#334155',lw=1.5)
        ax.text(.52,-i,x,ha='right',va='center',fontsize=11)
        ax.text(5.48,-i,y,ha='left',va='center',fontsize=11)
    ax.set(xlim=(-.2,6.9),ylim=(-n+.45,.7));ax.axis('off')
def box(ax,x,y,label):
    ax.add_patch(Rectangle((x-.23,y-.21),.46,.42,facecolor='white',edgecolor='#2563eb',lw=1.7,zorder=3));ax.text(x,y,label,ha='center',va='center',fontsize=11,zorder=4)
def controlled(ax,x,cs,t):
    ax.plot([x,x],[-max(cs+[t]),-min(cs+[t])],color='#2563eb',lw=1.8)
    for c in cs:ax.plot(x,-c,'o',color='#2563eb',ms=7,zorder=4)
    ax.add_patch(Circle((x,-t),.14,facecolor='white',edgecolor='#2563eb',lw=1.8,zorder=3));ax.plot([x-.14,x+.14],[-t,-t],color='#2563eb',zorder=4);ax.plot([x,x],[-t-.14,-t+.14],color='#2563eb',zorder=4)
a=axs[0,0];setup(a,'AND: retained controls, clean target',['a','b','0'],['a','b','ab']);controlled(a,3,[0,1],2)
a=axs[0,1];setup(a,'OR: complement controls and restore',['a','b','1'],['a','b',r'$a\vee b$']);box(a,1.5,0,'X');box(a,1.5,-1,'X');controlled(a,3,[0,1],2);box(a,4.4,0,'X');box(a,4.4,-1,'X')
a=axs[1,0];setup(a,'CLONE: classical basis bits only',['a','0'],['a','a']);controlled(a,3,[0],1)
a=axs[1,1];setup(a,'SWAP: three controlled NOT operations',['a','b'],['b','a']);controlled(a,1.7,[0],1);controlled(a,3,[1],0);controlled(a,4.3,[0],1)
a=axs[2,0];setup(a,'Full truth table: two classical calls',['0','0','1','0'],['0',r'$f(0)$','1',r'$f(1)$'])
for cy in [-.5,-2.5]:
    a.add_patch(Rectangle((2.65,cy-.7),.7,1.4,facecolor='#eff6ff',edgecolor='#2563eb',zorder=3));a.text(3,cy,r'$U_f$',ha='center',va='center',fontsize=13)
a=axs[2,1];setup(a,'Constant / balanced: one coherent query',[r'$|0\rangle$',r'$|1\rangle$'],[r'$f(0)\oplus f(1)$',r'$|-\rangle$'])
box(a,1.4,0,'H');box(a,1.4,-1,'H');a.add_patch(Rectangle((2.6,-1.3),.8,1.6,facecolor='#eff6ff',edgecolor='#2563eb',zorder=3));a.text(3,-.5,r'$U_f$',ha='center',va='center',fontsize=13);box(a,4.1,0,'H');box(a,5,0,'M')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
