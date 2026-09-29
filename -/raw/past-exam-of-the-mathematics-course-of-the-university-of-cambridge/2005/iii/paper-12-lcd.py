"""Original LCD pairing illustration. Tested Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.
Emit opaque paper-12-lcd.png in the caller's CWD; preserve supplied MPLCONFIGDIR.
"""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/codex-wiki-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
pairs=[(1,3),(4,5),(7,8),(2,9),(6,11),(10,12)]
rights=[b for a,b in pairs]
colors=['#dfeefa','#e9f0dc','#f8e5d4','#e5dcf2','#d8eee8','#f2dfe5']
fig,ax=plt.subplots(figsize=(9.6,3.7),dpi=120,facecolor='white')
last=0
for i,(right,col) in enumerate(zip(rights,colors),1):
 ax.axvspan(last+.5,right+.5,facecolor=col,alpha=1,zorder=0)
 ax.text((last+right+1)/2,-.7,f'$v_{i}$',ha='center',fontsize=12)
 ax.text((last+right+1)/2,-1.05,f'degree {right-last}',ha='center',fontsize=9)
 last=right
for j,(left,right) in enumerate(pairs,1):
 t=np.linspace(0,np.pi,200);mid=(left+right)/2;radius=(right-left)/2
 ax.plot(mid+radius*np.cos(t),radius*np.sin(t),color='#234f75',lw=1.8)
 ax.scatter([left],[0],s=30,facecolor='white',edgecolor='#234f75',zorder=4)
 ax.scatter([right],[0],s=30,color='#234f75',zorder=4)
 ax.text(left,-.15,f'$L_{j}$',ha='center',va='top',fontsize=9)
 ax.text(right,-.15,f'$R_{j}$',ha='center',va='top',fontsize=9)
ax.axhline(0,color='#555',lw=.8);ax.set(xlim=(.5,12.5),ylim=(-1.4,4.2))
ax.axis('off');ax.set_title('Merge endpoints through each successive right endpoint into one vertex',fontsize=12,pad=10)
fig.text(.5,.035,'Open circles: left endpoints     Filled circles: right endpoints     Each chord is one edge',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.07,1,1));fig.savefig('paper-12-lcd.png',facecolor='white',transparent=False);plt.close(fig)
