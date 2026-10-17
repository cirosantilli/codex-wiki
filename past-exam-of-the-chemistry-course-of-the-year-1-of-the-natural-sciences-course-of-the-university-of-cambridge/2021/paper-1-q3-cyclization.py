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

fig,axs=plt.subplots(1,3,figsize=(11,4.2));fig.subplots_adjust(left=.02,right=.99,top=.82,bottom=.12,wspace=.18)
# Condensed connectivity makes the five-carbon tether explicit without copying the source drawing.
ax=axs[0];finish(ax,(-1.8,2.5),(-1.6,2),'1 · Bromonium opening')
a=(-.7,.2);b=(.8,.2);br=(.05,1.3);bond(ax,a,b);bond(ax,a,br);bond(ax,b,br);atom(ax,br,'Br⁺');atom(ax,a,'CH');atom(ax,b,'CMe₂');atom(ax,(-.9,-.75),'(CH₂)₃OH');bond(ax,a,(-.9,-.5));curly(ax,(-.5,-.7),(.65,.08),rad=-.4);curly(ax,(.4,.8),(.05,1.3),rad=-.45);ax.text(.1,-1.4,'Br⁻ is the counterion',ha='center',fontsize=10)
ax=axs[1];finish(ax,(-1.7,2.3),(-1.6,2),'2 · Intramolecular opening')
pts=[(-.7,-.7),(-1,.25),(-.3,1),(.8,.8),(1.3,-.1),(.6,-.9)];ring(ax,pts);atom(ax,pts[3],'O⁺');atom(ax,(1.3,1.2),'H',11);bond(ax,(1.,.92),(1.23,1.12));atom(ax,pts[2],'CMe₂',11);atom(ax,pts[1],'CHBr',11)
ax.text(1.6,1.5,'Br⁻',fontsize=11);curly(ax,(1.5,1.35),(1.3,1.2),rad=.2);curly(ax,(1.12,1.04),(.82,.85),rad=-.4);ax.text(.15,-1.5,'6-membered cyclic oxonium',ha='center',fontsize=10)
ax=axs[2];finish(ax,(-1.7,2.3),(-1.6,2),'3 · Deprotonation')
ring(ax,pts);atom(ax,pts[3],'O');atom(ax,pts[2],'CMe₂',11);atom(ax,pts[1],'CHBr',11);ax.text(.15,-1.5,'Neutral bromoether + HBr',ha='center',fontsize=10)
fig.text(.5,.03,'O attacks the more substituted bromonium carbon; anti opening gives a racemic product.',ha='center',fontsize=11)
save(fig,Path(__file__).with_suffix('.png').name)
