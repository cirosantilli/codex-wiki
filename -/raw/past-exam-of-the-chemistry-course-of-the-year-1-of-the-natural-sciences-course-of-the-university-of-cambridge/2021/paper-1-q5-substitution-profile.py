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

fig,axs=plt.subplots(1,2,figsize=(10,4));fig.subplots_adjust(left=.08,right=.98,bottom=.17,top=.85,wspace=.3)
ax=axs[0];x=np.linspace(-3,3,400);y=2.5*np.exp(-x*x)-.15*x;ax.plot(x,y,color=BLUE,lw=2);ax.set(xlabel='Reaction coordinate',ylabel='Potential energy',xticks=[],yticks=[]);ax.spines[['top','right']].set_visible(False);ax.annotate('one saddle point',(0,2.5),(.4,3),arrowprops={'arrowstyle':'->'},fontsize=10);ax.text(-2.8,.65,'reactants',fontsize=10);ax.text(1.5,-.1,'products',fontsize=10)
ax=axs[1];finish(ax,(-2.2,2.2),(-1.6,1.8),'SN2 transition structure · total charge −1')
atom(ax,(-1.7,0),'HO');atom(ax,(0,0),'C');atom(ax,(1.7,0),'X');bond(ax,(-1.4,0),(-.2,0),style='dashed');bond(ax,(.2,0),(1.5,0),style='dashed')
for p in [(0,1),(-.5,-.8),(.5,-.8)]:bond(ax,(0,0),p);atom(ax,p,'H')
ax.text(0,-1.4,'O···C···X approximately collinear',ha='center',fontsize=10)
fig.suptitle('Concerted substitution: bond formation and cleavage share one barrier',fontsize=13)
fig.text(.3,.035,'Product energy is illustrative, not inferred from rate data.',ha='center',fontsize=9)
save(fig,Path(__file__).with_suffix('.png').name)
