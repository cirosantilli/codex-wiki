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

fig,axs=plt.subplots(2,1,figsize=(11,8.5),facecolor='white')
ax=axs[0];p=[(0,0),(1.2,.5),(2.4,0),(3.6,.5),(4.8,0)]
for i in range(4):bond(ax,p[i],p[i+1],2 if i==0 else 1)
atom(ax,p[-1],'Br');bond(ax,p[0],(-.2,-1));atom(ax,(-.2,-1),'Br');bond(ax,p[1],(1.2,1.5));atom(ax,(1.2,1.5),r'$CH_3$');atom(ax,(3.2,1.6),r'$MeO^-$');curly(ax,(3.45,1.4),(3.6,.62),.25);curly(ax,(4.16,.3),(4.63,.08),-.45)
ax.text(2.2,-1.65,r'Product: $BrCH=C(CH_3)CH_2CH_2OMe\ +\ Br^-$',ha='center',fontsize=12);finish(ax,(-1.4,6),(-2.25,2.25),'Primary C–Br substitution; the vinylic C–Br bond remains')
ax=axs[1];S=(0,1);O=(1.2,.5);p=[S,O,(1.2,-.7),(0,-1.3),(-1.2,-.7),(-1.2,.5)]
for a,b in zip(p,p[1:]+p[:1]):bond(ax,a,b)
atom(ax,S,'S');atom(ax,O,'O')
for endpoint in [(-.65,2),(.65,2)]:bond(ax,S,endpoint,2);atom(ax,endpoint,'O')
atom(ax,(2.7,-.75),r'$PrO^-$');curly(ax,(2.25,-.68),(1.35,-.68),.30);curly(ax,(1.25,-.08),(1.3,.36),-.55)
ax.text(3.5,1.3,r'$PrOH+NaH$'+'\n'+r'$\longrightarrow PrO^-Na^++H_2$',ha='center',fontsize=11)
ax.text(.9,-2.05,r'Product: $PrO(CH_2)_4SO_3^-\ Na^+$',ha='center',fontsize=12);finish(ax,(-2.2,5.5),(-2.55,2.5),'Alkoxide formation followed by carbon-centred sultone opening')

fig.tight_layout();save(fig,'paper-1-substitution-mechanisms.png')
