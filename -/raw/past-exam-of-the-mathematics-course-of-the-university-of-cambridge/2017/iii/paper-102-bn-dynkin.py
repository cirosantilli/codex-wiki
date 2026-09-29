"""Original ordinary and affine B_n diagrams; Python 3.14 / Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(10.8, 5.4), dpi=100, facecolor='white')

def node(ax, x, y, label, short=False):
    ax.scatter([x], [y], s=160, facecolor='#365f8e' if short else 'white', edgecolor='#253746', linewidth=1.5, zorder=4)
    ax.text(x, y+.22 if label=='0' and y>1 else y-.27, label, ha='center', va='bottom' if label=='0' and y>1 else 'top', fontsize=11)

def bond(ax, a, b, double=False, arrow=False):
    x0,y0=a; x1,y1=b
    if double:
        for d in [-.045,.045]:ax.plot([x0+.13,x1-.13],[y0+d,y1+d],color='#253746',lw=1.4)
        if arrow:ax.annotate('',xy=(x1-.18,y1),xytext=((x0+x1)/2-.04,(y0+y1)/2),arrowprops=dict(arrowstyle='->',color='#253746',lw=1.5))
    else:ax.plot([x0,x1],[y0,y1],color='#253746',lw=1.5,zorder=1)

for ax in axes.flat:ax.set(xlim=(-.45,3.55),ylim=(-.65,1.75));ax.axis('off')
axes[0,0].set_title(r'$B_n$: ordinary chain ($n=4$ shown)',fontsize=11)
for i in range(4):node(axes[0,0],i,.7,str(i+1),short=i==3)
for i in range(3):bond(axes[0,0],(i,.7),(i+1,.7),double=i==2,arrow=i==2)
axes[1,0].set_title(r'Affine $B_n$: node 0 joins node 2 ($n\geq3$)',fontsize=11)
for i in range(4):node(axes[1,0],i,.35,str(i+1),short=i==3)
node(axes[1,0],1,1.35,'0')
bond(axes[1,0],(1,1.35),(1,.35))
for i in range(3):bond(axes[1,0],(i,.35),(i+1,.35),double=i==2,arrow=i==2)
axes[0,1].set_title(r'$B_2$: ordinary diagram',fontsize=11)
node(axes[0,1],.6,.7,'1');node(axes[0,1],2.4,.7,'2',True)
bond(axes[0,1],(.6,.7),(2.4,.7),True,True)
axes[1,1].set_title(r'Affine $B_2$: both arrows point to 2',fontsize=11)
node(axes[1,1],0,.7,'0');node(axes[1,1],1.5,.7,'2',True);node(axes[1,1],3,.7,'1')
bond(axes[1,1],(0,.7),(1.5,.7),True,True)
bond(axes[1,1],(1.5,.7),(3,.7),True,False)
axes[1,1].annotate('',xy=(1.68,.7),xytext=(2.3,.7),arrowprops=dict(arrowstyle='->',color='#253746',lw=1.5))
axes[0,2].set_title(r'$B_1=A_1$: one root length',fontsize=11)
node(axes[0,2],1.5,.7,'1')
axes[1,2].set_title(r'Affine $A_1$: equal-length double bond',fontsize=11)
node(axes[1,2],.6,.7,'0');node(axes[1,2],2.4,.7,'1')
bond(axes[1,2],(.6,.7),(2.4,.7),True,False)
fig.text(.5,.035,'Filled nodes are short roots; arrows on unequal-length double bonds point toward the short root.',ha='center',fontsize=10)
fig.subplots_adjust(left=.035,right=.99,top=.92,bottom=.12,wspace=.16,hspace=.45)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
