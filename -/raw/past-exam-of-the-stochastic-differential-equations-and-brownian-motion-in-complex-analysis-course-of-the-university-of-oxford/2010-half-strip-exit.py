"""Python 3.14; NumPy and Matplotlib from the root pyproject.toml.
Write the original PNG into the current working directory.
"""
import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(9,3.6),facecolor='white',layout='constrained')
blue,orange,purple='#1976b8','#d35a16','#7c4198'
a=axs[0]
a.plot([0,2.3],[0,0],color=blue,lw=3)
a.plot([0,2.3],[1,1],color=orange,lw=3)
a.plot([0,0],[0,1],color=purple,lw=3)
a.scatter([.6],[.4],color='black',zorder=3)
a.text(.66,.42,'p/a + iq/a')
a.text(1.65,.88,'top edge',color=orange)
a.text(1.5,.08,'bottom edge',color=blue)
a.set(xlim=(-.15,2.4),ylim=(-.12,1.12),xlabel='x/a',ylabel='y/a',title='Half-strip')
a.set_aspect('equal')
a=axs[1]
a.plot([-5,-1],[0,0],color=orange,lw=3)
a.plot([-1,1],[0,0],color=purple,lw=3)
a.plot([1,5],[0,0],color=blue,lw=3)
w=np.cosh(np.pi*(.6+.4j))
a.scatter([w.real],[w.imag],color='black',zorder=3)
a.text(w.real+.15,w.imag,'A + iB')
a.annotate('top exit',xy=(-3,0),xytext=(-3,1.1),ha='center',color=orange,arrowprops={'arrowstyle':'->','color':orange})
a.set(xlim=(-5,5),ylim=(-.3,4.3),xlabel='Re w',ylabel='Im w',title='w = cosh(πz/a): upper half-plane',xticks=[-5,-1,1,5])
a.set_aspect('equal')
for a in axs:
 a.spines[['top','right']].set_visible(False)
 a.set_facecolor('white')
fig.savefig('2010-half-strip-exit.png',dpi=155,facecolor='white')
