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

fig,axs=plt.subplots(2,2,figsize=(11,8),facecolor='white')
def lobe(ax,pos,w=.6,h=.35,phase='+'):
 ax.add_patch(Ellipse(pos,w,h,fc=BLUE if phase=='+' else ORANGE,ec='none',alpha=.35));ax.text(*pos,phase,ha='center',va='center',fontsize=12)
def pi_star(ax,x=0,y=0):
 C=(x,y);O=(x,y+1.35);bond(ax,C,O,2);atom(ax,C,'C');atom(ax,O,'O')
 for dx,ph in [(-.48,'+'),(.48,'-')]:lobe(ax,(x+dx,y),.75,.46,ph)
 for dx,ph in [(-.37,'-'),(.37,'+')]:lobe(ax,(x+dx,y+1.35),.45,.32,ph)
 ax.plot([x-.8,x+.8],[y+.7,y+.7],color='.55',ls=':',lw=1)
ax=axs[0,0];bond(ax,(-1.4,.2),(-.4,.2));atom(ax,(-1.4,.2),'Et');atom(ax,(-.4,.2),r'$O^-$');lobe(ax,(.12,.2),.8,.45);ax.text(-.4,-.5,'occupied oxygen lone pair\nHOMO (donor)',ha='center',fontsize=11)
ax.add_patch(Circle((2.5,.2),.54,fc='#e5d5ee',ec='.4'));atom(ax,(2.5,.2),r'$Li^+$');ax.text(2.5,-.65,'empty Li-centred\nacceptor (LUMO)',ha='center',fontsize=11)
finish(ax,(-2.1,3.7),(-1.3,1.7),'Lithium ethoxide: ionic frontier picture')
ax=axs[0,1];atom(ax,(-1.5,.3),'O');lobe(ax,(-1,.3),.75,.4);ax.text(-1.3,-.5,'ester oxygen lone pair\nHOMO donor character',ha='center',fontsize=10);pi_star(ax,1.8,-.2);ax.text(1.8,-.85,r'$\pi^*(C=O)$ LUMO',ha='center',fontsize=11)
finish(ax,(-2.7,3.2),(-1.3,1.7),'Methyl acetate: nonbonding donor and π* acceptor')
ax=axs[1,0];pi_star(ax,.8,-.1);atom(ax,(-1.7,-.5),r'$EtO^-$');lobe(ax,(-1.15,-.35),.8,.4);ax.annotate('',(.25,-.1),(-.7,-.3),arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.6});ax.text(-.4,-1.05,r'$n_O\rightarrow\pi^*_{CO}$: acyl attack',ha='center',fontsize=11)
finish(ax,(-2.7,2.6),(-1.5,1.6),'Product-forming interaction')
ax=axs[1,1];atom(ax,(-1.5,.2),'ester O');lobe(ax,(-.8,.2),.8,.45);ax.add_patch(Circle((1.8,.2),.6,fc='#e5d5ee',ec='.4'));atom(ax,(1.8,.2),r'$Li^+$');ax.annotate('',(1.1,.2),(-.25,.2),arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.6});ax.text(.2,-.7,r'$n_O\rightarrow Li$: coordination',ha='center',fontsize=11)
finish(ax,(-2.7,3.0),(-1.5,1.6),'Complementary ester-to-lithium interaction')
fig.text(.5,.015,'Orbital signs denote phase, not electric charge. Shapes and energies are qualitative.',ha='center',fontsize=10)

fig.tight_layout();save(fig,'paper-1-acyl-frontiers.png')
