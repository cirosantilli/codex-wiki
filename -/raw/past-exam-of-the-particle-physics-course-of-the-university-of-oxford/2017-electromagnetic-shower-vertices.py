"""Original representative nuclear-field pair and bremsstrahlung graphs."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':13,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(11.8,5.8),layout='constrained')
blue,red='#284f70','#b44b38'

def line(ax,a,b,reverse=False):
    a,b=np.array(a,float),np.array(b,float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=blue,lw=1.9)
    if reverse:a,b=b,a
    ax.annotate('',a+.64*(b-a),a+.38*(b-a),arrowprops={'arrowstyle':'->','color':blue,'lw':1.8})
def photon(ax,a,b):
    a,b=np.array(a,float),np.array(b,float);t=np.linspace(0,1,301)
    normal=np.array([-(b-a)[1],(b-a)[0]])/np.linalg.norm(b-a)
    pts=a[None,:]+t[:,None]*(b-a)[None,:]+.035*np.sin(2*np.pi*7*t)[:,None]*normal[None,:]
    ax.plot(pts[:,0],pts[:,1],color=red,lw=1.7)
def nucleus(ax,y):
    ax.plot([-1.45,1.45],[y,y],color='0.4',lw=2.6)
    ax.text(-1.50,y-.22,'Nucleus',ha='left',fontsize=11,color='0.3')
    ax.text(1.48,y-.22,'Recoil',ha='right',fontsize=11,color='0.3')
for ax in axes:
    ax.set(xlim=(-1.8,1.8),ylim=(-1.6,1.5),aspect='equal');ax.axis('off')
ax=axes[0];A=(0,.65);B=(0,-.25);C=(0,-1.05)
photon(ax,(-1.4,1.05),A);line(ax,B,A);line(ax,A,(1.35,1.05));line(ax,B,(1.35,-.25),True)
photon(ax,C,B);nucleus(ax,C[1])
for pos in [A,B,C]:ax.plot(*pos,'ko',ms=4)
for xy,text in [((-1.43,1.22),r'$\gamma$'),((1.43,1.22),r'$e^-$'),((1.47,-.1),r'$e^+$'),((.18,-.70),r'$\gamma^*$')]:ax.text(*xy,text,ha='center',fontsize=15)
ax.set_title(r'(a) $\gamma Z\to e^-e^+Z$',weight='bold')
ax=axes[1];A=(-.45,.45);B=(.45,.45);C=(.45,-1.05)
line(ax,(-1.45,.45),A);line(ax,A,B);line(ax,B,(1.45,.45));photon(ax,A,(.1,1.30));photon(ax,C,B);nucleus(ax,C[1])
for pos in [A,B,C]:ax.plot(*pos,'ko',ms=4)
for xy,text in [((-1.46,.7),r'$e^-$'),((1.43,.7),r'$e^-$'),((.28,1.35),r'$\gamma$'),((.68,-.45),r'$\gamma^*$')]:ax.text(*xy,text,ha='center',fontsize=15)
ax.set_title(r'(b) $e^-Z\to e^-\gamma Z$',weight='bold')
fig.suptitle('Nuclear-field electromagnetic processes\nOne attachment ordering is shown in each panel; add its companion for the full amplitude',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
