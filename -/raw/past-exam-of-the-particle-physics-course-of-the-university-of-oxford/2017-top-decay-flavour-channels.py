"""Original dominant charged-current and representative neutral-current top diagrams."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig=plt.figure(figsize=(12,8.1),layout='constrained')
gs=fig.add_gridspec(2,2)
blue,red='#284f70','#b44b38'

def line(ax,a,b,reverse=False):
    a,b=np.array(a,float),np.array(b,float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=blue,lw=1.8)
    if reverse:a,b=b,a
    ax.annotate('',a+.65*(b-a),a+.38*(b-a),arrowprops={'arrowstyle':'->','color':blue,'lw':1.7})
def wave(ax,a,b):
    a,b=np.array(a,float),np.array(b,float);t=np.linspace(0,1,301);normal=np.array([-(b-a)[1],(b-a)[0]])/np.linalg.norm(b-a)
    p=a+t[:,None]*(b-a)+.04*np.sin(t*2*np.pi*8)[:,None]*normal
    ax.plot(p[:,0],p[:,1],color=red,lw=1.6)
def warc(ax,halfwidth):
    t=np.linspace(np.pi,0,501);x=halfwidth*np.cos(t);y=-.62*np.sin(t)
    dx=np.gradient(x);dy=np.gradient(y);normal=np.column_stack([-dy,dx]);normal/=np.linalg.norm(normal,axis=1)[:,None]
    p=np.column_stack([x,y])+.035*np.sin(np.linspace(0,20*np.pi,len(t)))[:,None]*normal
    ax.plot(p[:,0],p[:,1],color=red,lw=1.6)
def triangle(ax,radiative=False):
    a=(-.85,0);b=(0,.9);c=(.85,0)
    line(ax,(-2.,0),a);line(ax,a,b);line(ax,b,c);warc(ax,.85);wave(ax,b,(.55,1.55))
    ax.text(-2.1,.12,'t',fontsize=15);ax.text(-.48,.63,r'$d_i$',fontsize=14);ax.text(0,-.85,r'$W^+$',ha='center',color=red,fontsize=14);ax.text(.68,1.48,'Z',color=red,fontsize=14)
    if radiative:
        d=(1.60,0);line(ax,c,d);line(ax,d,(2.6,0));wave(ax,d,(2.15,.9));ax.plot(*d,'ko',ms=4)
        ax.text(2.7,.1,'c',fontsize=15);ax.text(2.28,.94,r'$\gamma$',color=red,fontsize=15)
    else:
        line(ax,c,(1.9,0));ax.text(2.,.12,'c',fontsize=15)
    for p in [a,b,c]:ax.plot(*p,'ko',ms=4)
ax=fig.add_subplot(gs[0,0]);ax.axis('off');ax.set(xlim=(-2.3,2.3),ylim=(-1.4,1.8),aspect='equal')
a=(-.7,.3);b=(.6,-.35)
line(ax,(-2,.3),a);line(ax,a,(1.85,1.1));wave(ax,a,b);line(ax,b,(1.9,-.1),True);line(ax,b,(1.9,-1.05))
for p in [a,b]:ax.plot(*p,'ko',ms=4)
for xy,text in [((-2.12,.5),'t'),((2.,1.18),'b'),((2.02,0),r'$\ell^+$'),((2.02,-1.03),r'$\nu_\ell$'),((-.25,-.35),r'$W^+$')]:ax.text(*xy,text,ha='center',fontsize=14)
ax.set_title(r'$t\to bW^+\to b\ell^+\nu_\ell$',weight='bold')
ax=fig.add_subplot(gs[0,1]);ax.axis('off');ax.set(xlim=(-2.3,2.4),ylim=(-1.4,1.8),aspect='equal');triangle(ax)
ax.set_title(r'Three vertices: $t\to cZ$',weight='bold')
ax=fig.add_subplot(gs[1,:]);ax.axis('off');ax.set(xlim=(-2.7,2.9),ylim=(-1.0,1.9),aspect='equal')
a=(-1.,-.25);b=(0,.65);c=(1.,-.25)
line(ax,(-2.3,-.25),a);line(ax,a,c);line(ax,c,(2.3,-.25))
wave(ax,a,b);wave(ax,b,c);wave(ax,b,(-.8,1.55));wave(ax,b,(.85,1.55))
for pos in [a,b,c]:ax.plot(*pos,'ko',ms=5)
for xy,label in [((-2.45,-.1),'t'),((2.45,-.1),'c'),((0,-.5),r'$d_i$'),((-.75,.40),r'$W^+$'),((.75,.40),r'$W^+$'),((-1.,1.63),'Z'),((1.05,1.63),r'$\gamma$')]:ax.text(*xy,label,ha='center',fontsize=14)
ax.set_title(r'Three vertices, including a quartic vertex: $t\to cZ\gamma$',weight='bold')
ax.text(0,-.86,r'Quartic $W^+W^-Z\gamma$: both neutral bosons at one vertex; loop flavour $d_i=d,s,b$',ha='center',fontsize=11)
fig.suptitle('Top-quark flavour flow; neutral-current panels show representative attachments\nThe physical loop amplitudes require the full gauge-consistent diagram sets',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
