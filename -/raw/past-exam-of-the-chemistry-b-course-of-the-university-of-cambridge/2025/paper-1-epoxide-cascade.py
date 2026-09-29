"""Original three-stage epoxide-opening/SNAr cascade; output to cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
from tools.chemistry_diagram import *
fig,axs=plt.subplots(2,2,figsize=(14,10.5),layout='constrained',facecolor='white')
ax=axs.flat[0]
C1=(0,.3);C2=(1,.3);epoxyO=(.5,1.3)
ring(ax,[C1,C2,(1.5,-.65),(.5,-1.35),(-.5,-.65)])
wedge(ax,C1,epoxyO);wedge(ax,C2,epoxyO);atom(ax,epoxyO,'O')
atom(ax,(-1.7,1.2),'ArSO₂N⁻(iPr)',size=15)
curly(ax,(-1.05,1.05),(-.05,.35),.35)
curly(ax,(.18,.65),(.47,1.2),-.45)
ax.text(-2.6,-2.2,'Backside N attack; C–O bond electrons move to O.',fontsize=11)
ax.text(-2.6,-2.65,'Ar = 2,4-difluorophenyl. Base removes N–H first.',fontsize=11)
finish(ax,(-3,4.2),(-3,2.5),'1. Opening the meso epoxide')
for ax,stage,title in zip(list(axs.flat)[1:],[0,1,2],['2. Opened epoxide: tethered alkoxide','3. F: cyclic product; one enantiomer shown','4. G: pyrrolidine replaces para F']):
 r=[(0,1),(.866,.5),(.866,-.5),(0,-1),(-.866,-.5),(-.866,.5)];ring(ax,r,{0:2,2:2,4:2})
 S=(1.9,1);N=(2.8,.3);C1=(3.3,-.5);C2=(2.8,-1.5);O=(1.8,-1)
 bond(ax,r[1],S);atom(ax,S,'S');bond(ax,S,(1.6,1.95),2);atom(ax,(1.6,1.95),'O');bond(ax,S,(2.8,1.8),2);atom(ax,(2.8,1.8),'O');bond(ax,S,N);atom(ax,N,'N');bond(ax,N,(3.65,.9));atom(ax,(3.65,.9),'iPr')
 ring(ax,[C1,(4.3,-.35),(4.7,-1.25),(3.8,-1.9),C2]);wedge(ax,C1,N,False);wedge(ax,C2,O,True);atom(ax,O,'O⁻' if stage==0 else 'O')
 if stage:bond(ax,O,r[2])
 else:
  bond(ax,r[2],(.9,-1.4));atom(ax,(.9,-1.4),'F');curly(ax,(1.65,-1),(.92,-.57),-.4);curly(ax,(.91,-.95),(.9,-1.4),-.4);ax.text(-1.1,-2.7,'SNAr addition, then F⁻ loss',fontsize=10)
 bond(ax,r[4],(-1.7,-1))
 if stage<2:atom(ax,(-1.7,-1),'F')
 else:
  atom(ax,(-1.7,-1),'N');ring(ax,[(-1.7,-1),(-2.3,-.25),(-3.1,-.55),(-3.1,-1.45),(-2.3,-1.8)])
 if stage==1:ax.text(-1.3,-2.7,'N/O attachments on cyclopentane are trans.',fontsize=10)
 if stage==2:ax.text(-1.3,-2.7,'The mirror image is formed equally.',fontsize=10)
 finish(ax,(-3.6,5.25),(-3.05,2.5),title)
fig.suptitle('Epoxide opening gives trans N/O attachments, followed by two aromatic substitutions.',fontsize=13)
save(fig,'paper-1-epoxide-cascade.png')
