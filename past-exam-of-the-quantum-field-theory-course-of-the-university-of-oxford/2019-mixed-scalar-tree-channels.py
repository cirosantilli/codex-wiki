"""Original mixed-scalar tree graphs; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

LIGHT='#126782'
HEAVY='#b54708'


def line(ax, start, end, species):
    ax.plot(*zip(start,end), color=LIGHT if species=='light' else HEAVY,
            lw=2, linestyle='-' if species=='light' else (0,(4,3)))


def diagram(ax, channel, internal, coupling):
    ax.set(xlim=(-.08,1.08),ylim=(-.08,1.12))
    ax.axis('off')
    symbol=r'\Phi' if internal=='heavy' else r'\phi'
    ax.set_title(rf'${coupling}^2$: {channel} channel, internal ${symbol}$',
                 fontsize=14, weight='bold',pad=13)
    p1,p2,p3,p4=(.01,.92),(.01,.08),(.99,.92),(.99,.08)
    if channel=='s':
        a,b=(.30,.5),(.70,.5)
        line(ax,p1,a,'light');line(ax,p2,a,'heavy')
        line(ax,b,p3,'light');line(ax,b,p4,'heavy')
        line(ax,a,b,internal)
        ax.text(.5,.68,r'$q_s=p_1+p_2$',ha='center',fontsize=12)
        ax.annotate('',xy=(.65,.43),xytext=(.35,.43),
                    arrowprops={'arrowstyle':'->','color':'#5c6470','lw':1})
    else:
        a,b=(.43,.75),(.43,.25)
        line(ax,p1,a,'light');line(ax,p2,b,'heavy')
        line(ax,a,p4,'heavy');line(ax,b,p3,'light')
        line(ax,a,b,internal)
        ax.text(.17,.48,r'$q_u=p_1-p_4$',ha='center',fontsize=12,
                bbox={'facecolor':'white','edgecolor':'none','pad':1})
        ax.annotate('',xy=(.39,.31),xytext=(.39,.69),
                    arrowprops={'arrowstyle':'->','color':'#5c6470','lw':1})
    for node in (a,b):
        ax.plot(*node,'o',color='#273343',ms=4)
    for pos,label,dy in [(p1,r'$\phi(p_1)$',.07),(p2,r'$\Phi(p_2)$',-.07),
                         (p3,r'$\phi(p_3)$',.07),(p4,r'$\Phi(p_4)$',-.07)]:
        ax.text(pos[0],pos[1]+dy,label,ha='center',va='center',fontsize=13)


fig,axes=plt.subplots(2,2,figsize=(10.4,6.9),facecolor='white')
fig.subplots_adjust(left=.07,right=.95,bottom=.10,top=.85,hspace=.55,wspace=.38)
fig.suptitle(r'Mixed-scalar scattering: $\phi\Phi\to\phi\Phi$',fontsize=19,weight='bold',y=.98)
for row,(species,coupling) in enumerate([('heavy',r'\lambda'),('light','g')]):
    for col,channel in enumerate(['s','u']):
        diagram(axes[row,col],channel,species,coupling)
fig.text(.5,.033,r'Solid blue: $\phi$     Dashed orange: $\Phi$     Grey arrows: exchanged momentum',
         ha='center',fontsize=11,color='#273343')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,
            facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
