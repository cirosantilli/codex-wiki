"""Original diagram; tested with Python 3.14, NumPy and Matplotlib.
Write the matching PNG basename to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,4.7),dpi=140,facecolor='white')
for y,name,nodes,mults in [(2.5,'U',[-4,-2,0,2,4],[1,2,2,2,1]),(1.4,'L(4)',[-4,-2,0,2,4],[1]*5),(.3,'L(2)',[-2,0,2],[1]*3)]:
 ax.text(-5.5,y,name,fontsize=15,va='center')
 ax.plot([min(nodes),max(nodes)],[y,y],color='#aaaaaa',lw=1)
 for w,m in zip(nodes,mults):
  highest=name!='U' and w==max(nodes)
  ax.scatter(w,y,s=170,marker='*' if highest else 'o',color='#bb4039' if highest else '#24649f',zorder=4)
  ax.text(w,y+.2,str(m),ha='center',fontsize=13)
  ax.text(w,y-.28,str(w),ha='center',fontsize=12)
ax.set_title('sl2 tensor weights and irreducible summands',fontsize=16,pad=15)
ax.text(-.5,-.35,'Weights below; multiplicities above. Red stars: highest weights.',ha='center',fontsize=11)
ax.set_xlim(-6,5);ax.set_ylim(-.65,3.1);ax.axis('off')
fig.tight_layout();fig.savefig('paper-1-sl2-weights.png',facecolor='white',transparent=False);plt.close(fig)
