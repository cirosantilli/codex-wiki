"""Original solution diagram; writes its PNG basename to the current directory."""
from pathlib import Path
import sys
for ancestor in Path(__file__).resolve().parents:
    if (ancestor/'tools'/'chemistry_diagram.py').exists():
        sys.path.insert(0,str(ancestor/'tools'));break
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, PathPatch
from matplotlib.path import Path as MplPath
from chemistry_diagram import bond, atom, curly, wedge, finish, save, BLUE, ORANGE

fig,axs=plt.subplots(2,3,figsize=(13,8.5),facecolor='white')
def acyl(ax,OR):
 C=(0,0);bond(ax,C,(0,1.1),2);atom(ax,(0,1.1),'O');bond(ax,C,(-1.1,-.35));atom(ax,(-1.1,-.35),'R');bond(ax,C,(1.2,-.35));atom(ax,(1.2,-.35),OR);return C
ax=axs[0,0];acyl(ax,'OMe');atom(ax,(-1.05,-1.2),r'$HO^-$');curly(ax,(-.75,-1.05),(-.1,-.13),-.25);curly(ax,(.06,.48),(.12,.98),-.4);finish(ax,(-1.9,1.9),(-1.9,1.8),'Base: carbonyl addition')
ax=axs[0,1];C=(0,0)
for pt,t in [((0,1.15),r'$O^-$'),((-1.2,0),'R'),((1.2,0),'OMe'),((0,-1.1),'OH')]:bond(ax,C,pt);atom(ax,pt,t)
curly(ax,(.15,1.0),(.12,.48),.4);curly(ax,(.53,.04),(1.03,.12),-.5);finish(ax,(-1.9,1.9),(-1.9,1.8),'Acyl–oxygen cleavage')
ax=axs[0,2];ax.text(0,.6,r'$RCOOH+MeO^-$',ha='center',fontsize=14);ax.text(0,-.05,r'$\longrightarrow RCOO^-+MeOH$',ha='center',fontsize=13);ax.text(0,-1,'acid work-up → RCOOH',ha='center',fontsize=13);finish(ax,(-2.2,2.2),(-1.9,1.8),'Carboxylate traps the hydrolysis product')
ax=axs[1,0];acyl(ax,r'$O\!tBu$');atom(ax,(1.5,.8),r'$H^+$');curly(ax,(1.24,-.1),(1.47,.62),.35);ax.text(0,-1.3,'Reactive alkoxy-protonated form',ha='center',fontsize=10);finish(ax,(-1.9,2.1),(-1.9,1.8),'Acid: protonation enables ionization')
ax=axs[1,1];C=(-.7,0);O=(-.7,1.1);bond(ax,C,O,2);atom(ax,O,'O');bond(ax,C,(-1.8,-.3));atom(ax,(-1.8,-.3),'R');bond(ax,C,(.4,-.3));atom(ax,(.4,-.3),r'$O(H)^+$');bond(ax,(.4,-.3),(1.6,-.3));atom(ax,(1.6,-.3),r'$CMe_3$');curly(ax,(1.05,-.25),(.58,-.15),-.5);ax.text(0,-1.25,r'$RCOOH+{}^+CMe_3$',ha='center',fontsize=12);finish(ax,(-2.25,2.25),(-1.9,1.8),'Alkyl–oxygen cleavage')
ax=axs[1,2];C=(0,0);atom(ax,C,r'$C^+$');bond(ax,C,(-1,-.5));atom(ax,(-1,-.5),'Me');bond(ax,C,(1,-.5));atom(ax,(1,-.5),'Me');bond(ax,C,(0,1));atom(ax,(0,1),r'$CH_2$');bond(ax,(0,1),(.8,1.5));atom(ax,(.8,1.5),'H');atom(ax,(1.8,1.2),r'$B^-$');curly(ax,(1.55,1.25),(.95,1.47),.25);curly(ax,(.4,1.25),(.08,.55),.35);ax.text(0,-1.25,r'$\longrightarrow (CH_3)_2C=CH_2+HB$',ha='center',fontsize=11);finish(ax,(-1.9,2.25),(-1.9,1.9),'Loss of a proton forms the alkene')
fig.text(.5,.015,'R denotes the retained cyclohexane substituent, including its other ester; Pr = n-propyl.',ha='center',fontsize=10)

fig.tight_layout();save(fig,'paper-1-ester-deprotection.png')
