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

fig,axs=plt.subplots(2,3,figsize=(14,8))
models=[('E1: C–O cleavage','e1a'),('E1: proton loss from cation','e1b'),('E1cb: enolate formation','cba'),('E1cb: hydroxide loss','cbb'),('E2: concerted elimination','e2')]
for ax,(title,mode) in zip(axs.flat,models):
 A=np.array([1.8,0]);B=np.array([3.05,0]);C=np.array([.55,0]);O=np.array([.55,1.1]);H=np.array([1.8,-.9]);W=np.array([1.8,-1.9]);OH=np.array([3.05,1.15]);Me=np.array([4.25,0])
 bond(ax,(-.4,-.35),C);atom(ax,(-.45,-.4),r'$CH_3$',size=11)
 bond(ax,C,O,1 if mode=='cba' else 2)
 if mode=='cba':bond(ax,C+np.array([.13,0]),O+np.array([.13,0]),style='dotted',color='#b45309')
 atom(ax,O,r'$O^{\delta-}$' if mode=='cba' else 'O',size=12)
 bond(ax,C,A);bond(ax,A,B);bond(ax,B,Me);atom(ax,Me,r'$CH_3$',size=11)
 atom(ax,A,r'$CH_2$' if mode=='e1a' else r'$CH^{\delta-}$' if mode in ['cba','cbb'] else 'CH',size=12)
 atom(ax,B,r'$CH^{\delta+}$' if mode in ['e1a','e1b'] else 'CH',size=12)
 if mode!='e1b':
  breaking=mode in ['e1a','cbb','e2'];bond(ax,B,OH,style='dotted' if breaking else 'solid');atom(ax,OH,r'$OH^{\delta-}$' if breaking else 'OH',size=12)
 if mode in ['e1b','cba','e2']:
  bond(ax,A,H,style='dotted');atom(ax,H,'H',size=12);bond(ax,H,W,style='dotted');atom(ax,W,r'$OH_2^{\delta+}$',size=12)
  ax.text(3.4,-1.7,'proton-accepting\nwater',fontsize=9,ha='center')
 if mode in ['e1b','cbb','e2']:bond(ax,A+np.array([0,.14]),B+np.array([0,.14]),style='dotted',color='#b45309')
 if mode=='cba':
  bond(ax,C+np.array([0,.13]),A+np.array([0,.13]),style='dotted',color='#b45309')
  ax.text(-.35,1.7,'enolate charge is delocalized',fontsize=8.5)
 for x,direction in [(-.8,1),(4.8,-1)]:
  ax.plot([x,x],[2,-2.4],color='.25',lw=1);ax.plot([x,x+.13*direction],[2,2],color='.25');ax.plot([x,x+.13*direction],[-2.4,-2.4],color='.25')
 ax.text(4.85,2,r'$\ddagger$',fontsize=15)
 if mode=='e1b':ax.text(.0,1.55,r'$OH^-$ spectator',fontsize=10)
 if mode=='cbb':ax.text(.0,1.55,r'$H_3O^+$ spectator',fontsize=10)
 finish(ax,(-1,5.3),(-2.7,2.7),title)
a=axs[1,2];a.axis('off');a.text(.03,.9,'Transition-state notation',weight='bold',fontsize=13,transform=a.transAxes)
a.text(.03,.75,'Dotted: breaking or forming bond\nOrange dotted: changing π bond\nSolid: retained skeletal bond\nδ+ / δ−: developing partial charge\nEvery bracketed structure is a TS.\n\nReacting chain: CH₃–CO–Cα–Cβ–CH₃\nAn explicit transferred H is on Cα;\nthe OH leaving group is on Cβ.',fontsize=11,va='top',linespacing=1.6,transform=a.transAxes)
fig.tight_layout(pad=1.5);save(fig,'paper-2-elimination.png')
