"""Ideal-chair fragments joined conceptually at the same spiro carbon."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
from tools.chemistry_diagram import *
fig,axs=plt.subplots(2,2,figsize=(12,7.7),layout='constrained',facecolor='white')
for row,name,extupper,extlower in [(0,'A',True,False),(1,'B',False,True)]:
 for col in [0,1]:
  ax=axs[row,col];upper=col==0;pts,aa,ee=chair(ax,(0,0),phase=-1 if upper else 1,scale=1.5)
  atom(ax,pts[0],'S',color=BLUE);atom(ax,pts[1],'O')
  hindex=4 if upper else 2;H=r'$H_a$' if name=='A' and upper else r'$H_b$' if name=='A' else r'$H_c$' if upper else r'$H_d$'
  bond(ax,pts[hindex],aa[hindex],color=BLUE);atom(ax,aa[hindex],H,color=BLUE)
  bond(ax,pts[hindex],ee[hindex]);atom(ax,ee[hindex],'OAr' if upper else 'R',size=11)
  isax=extupper if upper else extlower;end=aa[0] if isax else ee[0];bond(ax,pts[0],end,color=ORANGE);atom(ax,end,r'$O_{\mathrm{lower}}$' if upper else r'$O_{\mathrm{upper}}$',size=11,color=ORANGE)
  ax.text(-2.25,-1.9,'External O: '+('AXIAL' if isax else 'EQUATORIAL'),fontsize=11,color=ORANGE)
  ax.text(-2.25,-2.35,('n(O) → σ*(S–O) favourable' if isax else 'No corresponding axial interaction'),fontsize=10)
  finish(ax,(-2.65,2.85),(-2.65,2.1),name+(': upper-ring chair' if upper else ': lower-ring chair'))
fig.suptitle('S labels the SAME spiro carbon in both chair fragments. Fixed side chains are abbreviated.',fontsize=12)
save(fig,'paper-1-spiroacetal-chairs.png')
