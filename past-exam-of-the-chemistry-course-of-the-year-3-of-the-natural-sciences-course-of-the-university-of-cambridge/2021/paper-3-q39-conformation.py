"""Original solution diagram; Python 3.14, matplotlib 3.10, numpy 2.3.
Run from the mirrored media directory: PNG basename is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save,wedge,BLUE,ORANGE

fig,axs=plt.subplots(1,2,figsize=(10,5));fig.subplots_adjust(top=.85,bottom=.08,wspace=.23)
ax=axs[0];finish(ax,(-2.5,2.2),(-2.1,2.1),'Relative trans-OH model · schematic pucker')
p=[(-.5,1.1),(.7,.85),(1.35,-.1),(.65,-.9),(-.55,-1.3),(-1.5,-.45),(-1.3,.8)];ring(ax,p);atom(ax,p[0],'C=O',11);atom(ax,p[6],'NH',12)
atom(ax,(.95,.65),'B ↓',11,color=BLUE);atom(ax,(-.6,-1.02),'A ↑',11,color=BLUE)
wedge(ax,p[1],(.8,1.8),True);atom(ax,(.8,1.8),'OH ↑',11);wedge(ax,p[4],(-.7,-2),False);atom(ax,(-.7,-2),'OH ↓',11)
for i,t in [(2,'E↓ / G↑'),(3,'F↑ / H↓'),(5,'C↑ / D↓')]:atom(ax,p[i],t,10,color=BLUE)
ax=axs[1];ax.axis('off');ax.set_title('Observed contacts and face convention',fontsize=12)
for y,a,b in [(.77,'A','C'),(.60,'A','F'),(.43,'B','D'),(.26,'B','E')]:
 ax.text(.1,y,a,fontsize=15,color=BLUE);ax.annotate('',(.76,y+.01),(.24,y+.01),arrowprops={'arrowstyle':'<->','color':ORANGE});ax.text(.85,y,b,fontsize=15,color=BLUE)
ax.text(.5,.07,'Mirror-related model gives the same achiral spectra.\nNOEs are proximity evidence, not calibrated distances.',ha='center',fontsize=10)
fig.suptitle('One twist-chair-like model consistent with the selected NOEs',fontsize=14)
save(fig,Path(__file__).with_suffix('.png').name)
