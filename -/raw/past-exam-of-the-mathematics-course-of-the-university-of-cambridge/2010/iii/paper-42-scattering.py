"""Original pseudoscalar-exchange diagrams; Python 3.14.4, Matplotlib 3.10.7.
Run from the desired output directory. Preserve the caller's MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def fermion(ax, start, end, reverse=False):
    ax.plot([start[0], end[0]], [start[1], end[1]], color='#18324b', lw=2)
    if reverse:
        start, end = end, start
    a = tuple(.62*x+.38*y for x,y in zip(start,end))
    b = tuple(.38*x+.62*y for x,y in zip(start,end))
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color='#18324b',lw=1.5))


def labels(ax, anti=False):
    entries=[(.02,.9,r'$\psi,\ p_1$'),(.98,.9,r'$\psi,\ p_3$'),(.02,.1,r'$\bar\psi,\ p_2$' if anti else r'$\psi,\ p_2$'),(.98,.1,r'$\bar\psi,\ p_4$' if anti else r'$\psi,\ p_4$')]
    for x,y,s in entries: ax.text(x,y,s,ha='left' if x<.5 else 'right',va='center',fontsize=11)


def exchange(ax,cross=False,anti=False):
    top,bot=(.5,.75),(.5,.25)
    fermion(ax,(.04,.78),top)
    fermion(ax,(.04,.22),bot,reverse=anti)
    fermion(ax,top,(.96,.22) if cross else (.96,.78))
    fermion(ax,bot,(.96,.78) if cross else (.96,.22),reverse=anti)
    ax.plot([.5,.5],[.25,.75],ls=(0,(4,3)),lw=2,color='#ad5129')
    ax.text(.37,.5,r'$\phi$',ha='center',fontsize=12,color='#ad5129')
    ax.scatter([.5,.5],[.25,.75],s=25,color='black',zorder=5)
    labels(ax,anti)


fig,axes=plt.subplots(2,2,figsize=(10,6.4),facecolor='white')
for ax in axes.flat:
    ax.set(xlim=(0,1),ylim=(0,1));ax.set_facecolor('white');ax.axis('off')
exchange(axes[0,0]);axes[0,0].set_title(r'$\psi\psi\to\psi\psi$: $t$ exchange',fontsize=13,pad=8)
exchange(axes[0,1],cross=True);axes[0,1].set_title(r'$\psi\psi\to\psi\psi$: $u$ exchange',fontsize=13,pad=8)
exchange(axes[1,0],anti=True);axes[1,0].set_title(r'$\psi\bar\psi\to\psi\bar\psi$: $t$ exchange',fontsize=13,pad=8)
a=axes[1,1];vl,vr=(.32,.5),(.68,.5)
fermion(a,(.04,.78),vl);fermion(a,(.04,.22),vl,reverse=True)
fermion(a,vr,(.96,.78));fermion(a,vr,(.96,.22),reverse=True)
a.plot([.32,.68],[.5,.5],ls=(0,(4,3)),lw=2,color='#ad5129');a.text(.5,.59,r'$\phi$',ha='center',fontsize=12,color='#ad5129')
a.scatter([.32,.68],[.5,.5],s=25,color='black',zorder=5);labels(a,True)
a.set_title(r'$\psi\bar\psi\to\psi\bar\psi$: $s$ annihilation',fontsize=13,pad=8)
fig.text(.5,.02,'Time runs left to right. Arrows show fermion-number flow. Only black dots are vertices.',ha='center',fontsize=10)
fig.subplots_adjust(left=.035,right=.965,top=.94,bottom=.075,hspace=.32,wspace=.18)
fig.savefig(Path.cwd()/'paper-42-scattering.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
