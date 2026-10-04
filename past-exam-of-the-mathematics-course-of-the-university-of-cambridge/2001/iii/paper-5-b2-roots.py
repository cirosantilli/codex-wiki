"""Original exam diagram. Tested Python3.14.4/NumPy2.3.5/Matplotlib3.10.7.
Writes its PNG basename only to caller CWD; honors caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


fig,ax=plt.subplots(figsize=(5.7,5.4),layout='constrained')
fig.patch.set_facecolor('white');ax.set_facecolor('white')
positive=[(1,-1),(0,1),(1,0),(1,1)]
for x,y in positive:
    for sign in [1,-1]:
        xx,yy=sign*x,sign*y;colour='#2166ac' if sign==1 else '#999999'
        ax.annotate('',(xx,yy),(0,0),arrowprops={'arrowstyle':'-|>','lw':2,'color':colour})
        ax.scatter([xx],[yy],s=25,color=colour,zorder=5)
labels={(1,-1):r'$\alpha_1=\varepsilon_1-\varepsilon_2$',(0,1):r'$\alpha_2=\varepsilon_2$',(1,0):r'$\varepsilon_1$',(1,1):r'$\varepsilon_1+\varepsilon_2$',(-1,1):r'$-\alpha_1$',(0,-1):r'$-\varepsilon_2$',(-1,0):r'$-\varepsilon_1$',(-1,-1):r'$-\varepsilon_1-\varepsilon_2$'}
for (x,y),label in labels.items():
    ax.text(x+(0.08 if x>0 else -.08 if x<0 else 0),y+(0.11 if y>0 else -.14 if y<0 else .1),label,ha='left' if x>0 else 'right' if x<0 else 'center',va='center',fontsize=10)
ax.axhline(0,color='#bbbbbb',lw=.8,zorder=0);ax.axvline(0,color='#bbbbbb',lw=.8,zorder=0)
ax.set(xlim=(-1.8,2.0),ylim=(-1.45,1.5),xlabel=r'$\varepsilon_1$ coordinate',ylabel=r'$\varepsilon_2$ coordinate',title='B2 roots: blue positive, grey negative')
ax.set_aspect('equal');ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
fig.savefig(Path('paper-5-b2-roots.png'),dpi=145,facecolor='white',transparent=False);plt.close(fig)
