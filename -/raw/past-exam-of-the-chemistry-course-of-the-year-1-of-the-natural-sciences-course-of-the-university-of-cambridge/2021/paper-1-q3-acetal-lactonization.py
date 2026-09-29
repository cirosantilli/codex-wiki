"""Original solution diagram. Python 3.14 / matplotlib 3.10 / numpy 2.3.
Run from the mirrored media directory; output is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,ring,curly,flow,finish,save,BLUE,ORANGE

fig,axs=plt.subplots(2,1,figsize=(10,7));fig.subplots_adjust(hspace=.42,top=.92,bottom=.05)
ax=axs[0];finish(ax,(-1,10),(-1.8,1.7),'1 · Acid-catalysed acetal cleavage reveals a hydroxy ester')
atom(ax,(4.4,.8),'HO–CH(CH₂CH=CH₂)–C(CH₂OH)=CH–C(=O)–OMe',15)
ax.text(4.5,-.05,'Protonate acetal O → C–O cleavage → water addition → hemiacetal cleavage',ha='center',fontsize=11)
ax.text(4.5,-.8,'Benzaldehyde is released; both substrate OH groups become available.',ha='center',fontsize=11,color=BLUE)
ax=axs[1];finish(ax,(-1,10),(-2.1,2.2),'2 · Lactonization through a tetrahedral intermediate')
pts=[(1.5,.7),(2.5,1.2),(3.3,.3),(2.7,-.7),(1.5,-.4)];ring(ax,pts,{3:2});atom(ax,pts[1],'O');atom(ax,pts[2],'C',11);atom(ax,(4,.8),'OH');bond(ax,pts[2],(3.85,.74));atom(ax,(4,-.15),'OMeH⁺');bond(ax,pts[2],(3.78,-.09));atom(ax,(.4,1.1),'allyl');bond(ax,pts[0],(.8,.96));atom(ax,(.4,-.9),'CH₂OH');bond(ax,pts[4],(.85,-.7))
curly(ax,(3.9,.9),(3.4,.5),rad=.4);curly(ax,(3.7,.05),(4.15,-.1),rad=-.45)
flow(ax,(4.7,.2),(6,.2),'−MeOH; −H⁺')
p=[(6.6,.7),(7.6,1.2),(8.4,.3),(7.8,-.7),(6.6,-.4)];ring(ax,p,{3:2});atom(ax,p[1],'O');bond(ax,p[2],(9,.9),2);atom(ax,(9,.9),'O');atom(ax,(5.4,1.1),'allyl');bond(ax,p[0],(5.85,.97));atom(ax,(5.4,-.9),'CH₂OH');bond(ax,p[4],(5.85,-.71))
ax.text(4.5,-1.65,'The allyl-bearing OH becomes ring O; the CH₂OH substituent remains free.',ha='center',fontsize=11,color=BLUE)
save(fig,Path(__file__).with_suffix('.png').name)
