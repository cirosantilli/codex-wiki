"""Original atom-labelled skeletal explanation of spiro-to-fused rearrangement."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond,atom,ring,curly,finish,save
fig,axes=plt.subplots(1,2,figsize=(9.3,5.2),facecolor='white')
p=[(0,1.8),(.866,1.3),(.866,.3),(0,-.2),(-.866,.3),(-.866,1.3)]
for ax in axes:finish(ax,(-1.65,2.50),(-2.2,2.9))
ax=axes[0];ring(ax,p,{1:2,4:2});bond(ax,p[0],(0,2.55),2);atom(ax,(0,2.68),'O')
phi=np.pi/2+np.arange(5)*2*np.pi/5;pent=np.column_stack([.9*np.cos(phi),-1.1+.9*np.sin(phi)])
ring(ax,pent);bond(ax,pent[4],p[3],color='#b45309',lw=2.5)
atom(ax,p[3],'4',size=11,color='#245c9f');atom(ax,p[2],'3',size=11,color='#245c9f');atom(ax,pent[4],'Ct',size=10,color='#b45309')
curly(ax,(.42,-.51),(.91,.27),rad=-.4)
ax.set_title('Base stage: para-spirodienone',fontsize=12)
ax=axes[1];ring(ax,p,{0:2,2:2,4:2});bond(ax,p[0],(0,2.55));atom(ax,(0,2.68),'OH')
chain=[p[3],(0,-1.2),(.866,-1.7),(1.732,-1.2),(1.732,-.2),p[2]]
for i in range(5):bond(ax,chain[i],chain[i+1],color='#b45309' if i==4 else '0.20')
atom(ax,p[3],'4',size=11,color='#245c9f');atom(ax,p[2],'3',size=11,color='#245c9f');atom(ax,chain[4],'Ct',size=10,color='#b45309')
ax.set_title('Acid stage: migrated aromatic product',fontsize=12)
fig.text(.5,.035,'The orange tether bond migrates from carbon 4 to carbon 3; rearomatization restores the phenol.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.09,1,1));save(fig,'paper-3-spiro-dienone.png')
