"""Original four-channel momentum and spin construction for resonant Z exchange."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'figure.facecolor':'white','axes.facecolor':'white'})
fig, axes = plt.subplots(2,2,figsize=(11.6,8.0),layout='constrained')
blue, red = '#1764a2','#bd3c37'
z=np.array([0.,1.])
n=np.array([.78,.625])

def arrow(ax,pos,vec,color):
    ax.annotate('',np.array(pos)+vec,np.array(pos),arrowprops={'arrowstyle':'->','color':color,'lw':2.2})

for ax,channel in zip(axes.flat,['LL','LR','RL','RR']):
    hi,hf=channel
    ax.set(xlim=(-1.9,1.9),ylim=(-1.65,1.65),aspect='equal')
    ax.axis('off')
    equal=hi==hf
    angular='+' if equal else '-'
    ax.set_title(rf'{channel}: $|g_{hi}^e g_{hf}^f|^2(1{angular}\cos\theta^\star)^2$',weight='bold',fontsize=13)
    ax.text(-1.03,1.25,'Incoming',ha='center',weight='bold')
    ax.text(.95,1.25,'Outgoing',ha='center',weight='bold')
    for side, direction, spin_sign, labels in [(-1.05,z, -1 if hi=='L' else 1,[r'$e^-$',r'$e^+$']),(.95,n,-1 if hf=='L' else 1,[r'$f$',r'$\bar f$'])]:
        for j, sign in enumerate([1,-1]):
            # Separate momentum and spin arrows at each particle; all are spatial vectors.
            pos=np.array([side,-.15 if j==0 else -1.0])
            ax.text(pos[0]-.52,pos[1]+.1,labels[j],ha='center',fontsize=14)
            arrow(ax,pos,sign*.50*direction,blue)
            arrow(ax,pos+np.array([.24,0]),spin_sign*.30*direction,red)
    ax.plot([-.03,-.03],[-1.37,1.02],color='0.82',lw=1)
    # Angle convention displayed independently of the particle arrows.
    arrow(ax,(.62,.45),.47*z,'0.55')
    arrow(ax,(.62,.45),.47*n,blue)
    ax.text(1.13,.7,r'$\theta^\star$',fontsize=11)
fig.suptitle('Four massless helicity channels at a Z resonance\nBlue: momentum direction     Red: spin direction (arrow lengths are schematic)',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
