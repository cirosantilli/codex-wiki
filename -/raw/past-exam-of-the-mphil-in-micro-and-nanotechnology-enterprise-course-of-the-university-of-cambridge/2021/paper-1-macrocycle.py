"""Original connectivity schematic of the product, not a source figure copy."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,finish,save
fig,ax=plt.subplots(figsize=(7,5.8),layout='constrained')
# Two meta-substituted phenylene bridges, above and below the cavity.
for cy,sign in [(2.15,1),(-2.15,-1)]:
 angles=np.deg2rad([90,150,210,270,330,30]);pts=np.array([[.65*np.cos(a),cy+.65*np.sin(a)] for a in angles]);ring(ax,pts,{0:2,2:2,4:2})
 # meta sites are 210 and 330 for top, 150 and 30 for bottom.
 sites=[2,4] if sign==1 else [1,5]
 for j,ix in enumerate(sites):
  ch=np.array([(-1 if j==0 else 1)*1.15,sign*1.12]);bond(ax,pts[ix],ch);atom(ax,ch,r'CH$_2$',11)
  n=np.array([(-1 if j==0 else 1)*1.85,sign*.59]);bond(ax,ch,n)
# Imidazolium rings have N at the upper/lower inner ends, sharing a central CH.
for sign in [-1,1]:
 pts=np.array([[sign*1.85,.59],[sign*1.40,0],[sign*1.85,-.59],[sign*2.52,-.36],[sign*2.52,.36]])
 ring(ax,pts,{0:2,3:2});atom(ax,pts[0],'N',12);atom(ax,pts[2],'N',12)
 ax.text(sign*2.35,.82,'+',fontsize=18,ha='center',color='#245c9f')
 h=np.array([sign*.92,0]);bond(ax,pts[1],h);atom(ax,h,'H',12)
 ax.plot([sign*.75,sign*.32],[0,0],ls=':',color='#b45309',lw=1.5)
atom(ax,[0,0],r'Cl$^-$',15,color='#b45309')
ax.text(0,-3.45,'Dicationic ring + two chloride counterions in total\n(one chloride shown as a bound guest; other ions omitted)',ha='center',fontsize=10)
finish(ax,(-3.15,3.15),(-3.9,3.05),'Two meta-xylylene bridges join two imidazolium units')
save(fig,Path(__file__).with_suffix('.png').name)
