"""Original solution diagram; Python 3.14, numpy and matplotlib.
Write the PNG basename to the current working directory (Make supplies _media).
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, ring, wedge, flow, finish, save

from matplotlib.patches import FancyArrowPatch
fig,axs=plt.subplots(1,3,figsize=(11,3.6))
P={'+x':np.array([1.45,-.42]),'-x':np.array([-1.45,.42]),'+y':np.array([.8,.83]),'-y':np.array([-.8,-.83]),'+z':np.array([0,1.6]),'-z':np.array([0,-1.6])}
models=[(['+z','-z'],[('+x','+y'),('-x','-y')],'trans (achiral)'),(['+z','+x'],[('-z','+y'),('-x','-y')],'cis: one handed form'),(['+z','+x'],[('-z','-y'),('-x','+y')],'cis: its mirror partner')]
for ax,(py,pairs,title) in zip(axs,models):
 for k,p in P.items():bond(ax,(0,0),p,style='dashed' if k in ['-y'] else 'solid');atom(ax,p,'N' if k in py else 'O',size=12)
 atom(ax,(0,0),'Co')
 for i,(a,b) in enumerate(pairs):
  x,y=P[a],P[b];ax.add_patch(FancyArrowPatch(x,y,connectionstyle='arc3,rad='+str(.5 if i==0 else -.5),arrowstyle='-',lw=3,color=['#245c9f','#b45309'][i],zorder=1))
 ax.text(0,-2.2,'N = pyridine; linked O pairs = one ligand',ha='center',fontsize=8.5)
 finish(ax,(-2,2),(-2.45,2),title)
fig.tight_layout();save(fig,'paper-2-isomers.png')
