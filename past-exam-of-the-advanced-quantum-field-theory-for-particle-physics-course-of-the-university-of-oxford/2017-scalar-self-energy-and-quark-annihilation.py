"""Original scalar self-energy and distinct-flavour annihilation diagrams."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig=plt.figure(figsize=(12,7.4),layout='constrained')
gs=fig.add_gridspec(2,3,height_ratios=[1,1.05])
blue,red='#244a6c','#b34a36'

def straight(ax,a,b,reverse=False):
    a,b=np.array(a,float),np.array(b,float)
    ax.plot([a[0],b[0]],[a[1],b[1]],color=blue,lw=1.8)
    if reverse:a,b=b,a
    ax.annotate('',a+.63*(b-a),a+.37*(b-a),arrowprops={'arrowstyle':'->','color':blue,'lw':1.7})

def wave(ax,x,y,kind='photon'):
    # Offset a smooth centre-line in its normal direction.
    t=np.linspace(0,1,len(x));dx=np.gradient(x);dy=np.gradient(y)
    norm=np.hypot(dx,dy);phase=np.sin(t*2*np.pi*(10 if kind=='photon' else 15))
    xx=x-.045*dy/norm*phase;yy=y+.045*dx/norm*phase
    ax.plot(xx,yy,color=red,lw=1.6)

for j in range(3):
    ax=fig.add_subplot(gs[0,j]);ax.set(xlim=(-1.5,1.5),ylim=(-.8,1.4),aspect='equal');ax.axis('off')
    if j==0:
        straight(ax,(-1.4,0),(-.65,0));straight(ax,(.65,0),(1.4,0))
        t=np.linspace(np.pi,0,301)
        wave(ax,.65*np.cos(t),.65*np.sin(t))
        ax.plot(.65*np.cos(t),-.42*np.sin(t),color=blue,lw=1.8)
        straight(ax,(-.12,-.41),(.12,-.41))
        ax.text(0,.85,r'$\gamma$',color=red,ha='center');ax.text(0,-.66,r'$\phi$',color=blue,ha='center')
        ax.set_title('Scalar–photon exchange',weight='bold')
        ax.text(0,1.12,r'Two cubic vertices; order $e^2$',ha='center',fontsize=11)
        ax.plot([-.65,.65],[0,0],'ko',ms=4)
    else:
        straight(ax,(-1.4,0),(0,0));straight(ax,(0,0),(1.4,0));ax.plot(0,0,'ko',ms=5)
        t=np.linspace(-np.pi/2,3*np.pi/2,500);x=.43*np.cos(t);y=.43+.43*np.sin(t)
        if j==1:
            wave(ax,x,y);ax.text(0,1.07,r'Photon loop: symmetry factor $1/2$',ha='center',fontsize=11)
            ax.set_title('Seagull tadpole',weight='bold')
        else:
            ax.plot(x,y,color=blue,lw=1.8)
            ax.annotate('',(.30,.73),(.38,.60),arrowprops={'arrowstyle':'->','color':blue,'lw':1.8})
            ax.text(0,1.07,r'Complex scalar loop; order $\lambda$',ha='center',fontsize=11)
            ax.set_title('Quartic scalar tadpole',weight='bold')
        ax.text(0,-.5,'External scalar legs',ha='center',color=blue,fontsize=11)
ax=fig.add_subplot(gs[1,:]);ax.axis('off');ax.set(xlim=(-3.3,3.3),ylim=(-1.4,1.6),aspect='equal')
ax.set_title(r'Distinct flavours: $q\bar q\longrightarrow g^*\longrightarrow t\bar t$',weight='bold',fontsize=14)
a=(-1.,0);b=(1.,0)
for start,end,reverse in [((-2.4,1),a,False),((-2.4,-1),a,True),(b,(2.4,1),False),(b,(2.4,-1),True)]:
    straight(ax,start,end,reverse)
t=np.linspace(-1,1,500);wave(ax,t,np.zeros_like(t),'gluon')
ax.text(0,.25,r'$g^*$',ha='center',color=red,fontsize=15)
for xy,label in [((-2.6,1.05),r'$q(k_1)$'),((-2.6,-1.05),r'$\bar q(k_2)$'),((2.65,1.05),r'$t(p_1)$'),((2.65,-1.05),r'$\bar t(p_2)$')]:ax.text(*xy,label,ha='center',fontsize=14)
ax.plot([-1,1],[0,0],'ko',ms=5)
ax.text(0,-1.30,r'Initial colour average: $2/9$     Initial spin average: $1/4$',ha='center',fontsize=12)
fig.suptitle('Original perturbative diagrams — arrows follow scalar charge or fermion number\nAt vanishing scalar quartic coupling, only the first two self-energy graphs remain',fontsize=13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
