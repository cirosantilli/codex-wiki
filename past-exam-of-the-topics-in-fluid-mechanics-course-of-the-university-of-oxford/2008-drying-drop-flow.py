# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Output in current working directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,axs=plt.subplots(1,2,figsize=(9,3.6),sharex=True,sharey=True)
x=np.linspace(-1,1,400)
for ax,pinned,title in zip(axs,[False,True],['Receding edge, fixed outer angle','Pinned edge, decreasing angle']):
    ax.plot(x,.5*(1-x*x),color='#2171b5',lw=2)
    for scale in [.75,.5]:
        xx=x if pinned else scale*x
        hh=.5*scale*(1-xx*xx) if pinned else .5/scale*(scale*scale-xx*xx)
        ax.plot(xx,hh,'--',color='#7cadd0',lw=1)
    for xx in [-.65,-.35,.35,.65]:
        direction=1 if (xx>0)==pinned else -1
        ax.annotate('',(xx+direction*.15,.12),(xx-direction*.05,.12),arrowprops={'arrowstyle':'->','color':'#c34f2d','lw':1.8})
    if pinned:ax.plot([-1,1],[0,0],'ko',ms=5)
    else:
        ax.annotate('',(.65,0),(.98,0),arrowprops={'arrowstyle':'->','color':'.2'});ax.annotate('',(-.65,0),(-.98,0),arrowprops={'arrowstyle':'->','color':'.2'})
    ax.axhline(0,color='.4',lw=.8);ax.set(xlabel='$x$',title=title,xlim=(-1.1,1.1),ylim=(-.04,.59));ax.grid(alpha=.15)
axs[0].set_ylabel('$h$');axs[0].text(0,.54,'inward liquid flow',ha='center',fontsize=9);axs[1].text(0,.54,'outward liquid flow',ha='center',fontsize=9)
fig.tight_layout();fig.savefig(Path('2008-drying-drop-flow.png'),dpi=150,facecolor='white');plt.close(fig)
