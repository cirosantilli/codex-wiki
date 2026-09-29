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

from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(12.5,3.2))
xs=[0,4.4,8.8,13.2]
for i,x in enumerate(xs):
 atom(ax,(x,0),'Pt' if i%2==0 else 'Mn',size=16)
 if i%2:
  for yy in [-1.15,1.15]:bond(ax,(x,0),(x,yy));atom(ax,(x,yy),r'$H_2O$',size=12)
 for d in [-1,1]:
  for y in [-.33,.33]:bond(ax,(x,0),(x+d*.8,y))
for i in range(3):
 l,r=xs[i],xs[i+1];m=(l+r)/2
 ax.add_patch(FancyBboxPatch((l+.65,-.65),3.1,1.3,boxstyle='round,pad=.05',ec='.55',fc='#f5f8fc'))
 for yy,t in [(.33,'N'),(-.33,'O')]:atom(ax,(l+.85,yy),t if i%2==0 else 'O',size=11)
 for yy,t in [(.33,'O'),(-.33,'O')]:atom(ax,(r-.85,yy),t if i%2==0 else ('N' if yy>.0 else 'O'),size=11)
 ax.text(m,.12,r'$L^{2-}$',ha='center',fontsize=14);ax.text(m,-.28,'one pyridyl-dicarboxylate',ha='center',fontsize=8)
 for a,b in [(l+1.03,m-.5),(m+.5,r-1.03)]:bond(ax,(a,0),(b,0))
ax.text(-1.25,0,'···',fontsize=20,ha='center');ax.text(14.45,0,'···',fontsize=20,ha='center')
ax.text(6.6,-1.8,'Pt: two N,O chelates (CN 4).   Mn: two O,O chelates + two waters (CN 6).',ha='center',fontsize=11)
finish(ax,(-1.7,14.9),(-2,1.65),'Proposed donor connectivity: an alternating Pt(II)–Mn(II) chain')
fig.tight_layout();save(fig,'paper-2-chain.png')
