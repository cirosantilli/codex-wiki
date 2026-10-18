"""Original diagrams; Python 3.14, NumPy and Matplotlib. Save only in the caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"font.size":11,"axes.titlesize":11,"figure.facecolor":"white","savefig.facecolor":"white"})
BLUE="#126782";RED="#ba4c30"
def line(ax,a,b,arrow=False,color=BLUE):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>" if arrow else "-",mutation_scale=10,color=color,lw=1.6,shrinkA=0,shrinkB=0))
def wave(ax,a,b,height=0,color=RED,turns=9):
    a=np.array(a);b=np.array(b);t=np.linspace(0,1,400)
    x=a[0]+(b[0]-a[0])*t;y=a[1]+(b[1]-a[1])*t+height*np.sin(np.pi*t)
    dx=np.gradient(x);dy=np.gradient(y);norm=np.sqrt(dx*dx+dy*dy);wiggle=.012*np.sin(2*np.pi*turns*t)
    ax.plot(x-wiggle*dy/norm,y+wiggle*dx/norm,color=color,lw=1.3)
def dot(ax,p,seagull=False):ax.scatter(*p,s=30,marker="s" if seagull else "o",color="#222222",zorder=5)
def clean(ax):ax.set(xlim=(-.03,1.03),ylim=(-.07,1.03));ax.set_aspect("equal");ax.axis("off")

fig,axes=plt.subplots(1,4,figsize=(12.4,3.6),layout="constrained")
for ax in axes:clean(ax)
ext={'k1':(.04,.87),'k2':(.04,.13),'p1':(.96,.87),'p2':(.96,.13)}
for ax,swap,title in [(axes[0],False,'Ordered quark exchange t'),(axes[1],True,'Ordered quark exchange u')]:
    upper=(.57,.75);lower=(.57,.25)
    wave(ax,ext['k1'],lower if swap else upper,turns=8);wave(ax,ext['k2'],upper if swap else lower,turns=8)
    line(ax,lower,upper,True);line(ax,upper,ext['p1'],True);line(ax,ext['p2'],lower,True);dot(ax,upper);dot(ax,lower)
    for name,p in ext.items():ax.text(p[0],p[1]+(.055 if name[1]=='1' else -.08),'$'+name[0]+'_'+name[1]+'$',ha='center',fontsize=10)
    ax.set_title(title)
ax=axes[2];v=(.31,.5);w=(.68,.5);wave(ax,ext['k1'],v);wave(ax,ext['k2'],v);wave(ax,v,w,turns=7)
line(ax,w,ext['p1'],True);line(ax,ext['p2'],w,True);dot(ax,v);dot(ax,w)
for name,p in ext.items():ax.text(p[0],p[1]+(.055 if name[1]=='1' else -.08),'$'+name[0]+'_'+name[1]+'$',ha='center',fontsize=10)
ax.set_title('Three-gluon exchange s')
ax=axes[3];left=(.25,.5);right=(.75,.5);line(ax,(.02,.5),left);line(ax,right,(.98,.5))
t=np.linspace(0,np.pi,130);xx=.5-.25*np.cos(t);yy=.5+.25*np.sin(t);ax.plot(xx,yy,color=BLUE,lw=1.6)
xx2=.5+.25*np.cos(t);yy2=.5-.25*np.sin(t);ax.plot(xx2,yy2,color=BLUE,lw=1.6)
for xs,ys in [(xx,yy),(xx2,yy2)]:
    j=57;ax.add_patch(FancyArrowPatch((xs[j],ys[j]),(xs[j+10],ys[j+10]),arrowstyle='-|>',mutation_scale=10,color=BLUE,lw=1.6))
dot(ax,left);dot(ax,right);ax.text(.25,.39,'x',ha='center');ax.text(.75,.39,'y',ha='center');ax.text(.04,.38,r'$x_a$',ha='center');ax.text(.96,.38,r'$y_a$',ha='center')
ax.set_title('Yukawa scalar two-point loop');ax.text(.5,.04,'Closed-fermion-loop sign: −1',ha='center',fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,transparent=False)
plt.close(fig)
