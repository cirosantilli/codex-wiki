"""Original AQFT 2019 diagrams; Python 3.14, NumPy and Matplotlib.

The sole output is Path.cwd()/Path(__file__).with_suffix('.png').name.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(12,7.6),dpi=100,facecolor='white')
grid=fig.add_gridspec(2,12,wspace=.6,hspace=.35)
ink,blue,orange='#203549','#196da5','#a84c20'


def panel(row,start,width,title):
    ax=fig.add_subplot(grid[row,start:start+width])
    ax.set(xlim=(-.10,1.10),ylim=(-.04,1.04),aspect='equal')
    ax.axis('off');ax.set_title(title,fontsize=12,pad=14)
    return ax


def path(ax,x,y,kind='fermion',arrow=False):
    x=np.asarray(x);y=np.asarray(y)
    if kind in ('gluon','photon'):
        dx=np.gradient(x);dy=np.gradient(y);norm=np.hypot(dx,dy)
        t=np.linspace(0,1,len(x));phase=2*np.pi*max(4,int(np.hypot(np.diff(x),np.diff(y)).sum()*13))*t
        amp=.023 if kind=='gluon' else .017
        x=x+amp*np.sin(phase)*(-dy/norm);y=y+amp*np.sin(phase)*(dx/norm)
        if kind=='gluon':
            x=x+.016*np.sin(np.pi*t)*np.cos(phase)*dx/norm
            y=y+.016*np.sin(np.pi*t)*np.cos(phase)*dy/norm
    color=orange if kind=='gluon' else blue if kind=='photon' else ink
    ax.plot(x,y,color=color,lw=1.8,ls='--' if kind=='ghost' else '-')
    if arrow:
        i,j=int(len(x)*.43),int(len(x)*.57)
        ax.annotate('',xy=(x[j],y[j]),xytext=(x[i],y[i]),arrowprops={'arrowstyle':'-|>','lw':1.4,'color':color})


def line(ax,a,b,kind='fermion',arrow=False):
    t=np.linspace(0,1,350);a=np.array(a);b=np.array(b)
    p=a[None,:]+t[:,None]*(b-a)
    path(ax,p[:,0],p[:,1],kind,arrow)


def dot(ax,x,y):ax.plot(x,y,'o',ms=4,color=ink)


for col,(kind,title) in enumerate([('fermion','1(a)(i): quark loop'),('gluon','1(a)(i): gluon loop'),('ghost','1(a)(i): ghost loop')]):
    ax=panel(0,3*col,3,title)
    line(ax,(0,.50),(.23,.50),'gluon');line(ax,(.77,.50),(1,.50),'gluon')
    t=np.linspace(0,np.pi,450)
    path(ax,.5-.27*np.cos(t),.5+.23*np.sin(t),kind,kind!='gluon')
    path(ax,.5+.27*np.cos(t),.5-.23*np.sin(t),kind,kind!='gluon')
    dot(ax,.23,.5);dot(ax,.77,.5)
    ax.text(.02,.38,'$a,\\mu$',ha='center');ax.text(.98,.38,'$b,\\nu$',ha='center')
    if kind=='fermion':ax.text(.5,.86,'sum over flavours',ha='center',fontsize=10)

ax=panel(0,9,3,'1(a)(i): four-gluon tadpole')
line(ax,(0,.25),(.5,.25),'gluon');line(ax,(.5,.25),(1,.25),'gluon')
t=np.linspace(0,2*np.pi,700)
path(ax,.5+.24*np.sin(t),.49-.24*np.cos(t),'gluon')
dot(ax,.5,.25)
ax.text(.03,.10,'$a,\\mu$',ha='center');ax.text(.97,.10,'$b,\\nu$',ha='center')

for col,(title,finals) in enumerate([('2(b)(ii): electron-muon, t exchange',('$e^-(p_3)$','$\\mu^-(p_4)$')),
                                   ('2(b)(iii): electron-electron, t exchange',('$e^-(p_3)$','$e^-(p_4)$')),
                                   ('2(b)(iii): electron-electron, u exchange',('$e^-(p_4)$','$e^-(p_3)$'))]):
    ax=panel(1,4*col,4,title)
    for y in [.25,.75]:
        line(ax,(0,y),(.5,y),arrow=True);line(ax,(.5,y),(1,y),arrow=True);dot(ax,.5,y)
    line(ax,(.5,.25),(.5,.75),'photon')
    for x,y,label in [(0,.91,'$e^-(p_1)$'),(0,.08,'$\\mu^-(p_2)$' if col==0 else '$e^-(p_2)$'),
                      (1,.91,finals[0]),(1,.08,finals[1])]:
        ax.text(x,y,label,ha='center',fontsize=11)
    ax.text(.61,.5,'$p_1-p_4$' if col==2 else '$p_1-p_3$',ha='left',va='center',fontsize=10)
fig.suptitle('Oxford AQFT 2019: contributing diagrams',fontsize=17,y=.98)
fig.text(.5,.035,'Solid arrows: fermion flow     Curly orange: gluon     Dashed arrows: ghost     Wavy blue: photon',ha='center',fontsize=11,color=ink)
fig.subplots_adjust(left=.04,right=.96,top=.88,bottom=.11)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
