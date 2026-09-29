"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

E=np.linspace(-2.3,-.45,500)
g=lambda x,c,w:np.exp(-((x-c)/w)**2)
negative=-.9*g(E,-1.78,.13)-1.3*g(E,-1.38,.14)
positive=.18*g(E,-1.60,.14)+1.05*g(E,-1.15,.16)+.32*g(E,-.72,.11)
fig,axes=plt.subplots(1,2,figsize=(9.5,3.6),layout='constrained',sharey=True)
for ax,scale,title in zip(axes,[1,.1],['10 mM: reference shape','1 mM: faradaic current ÷ 10']):
    ax.plot(E,scale*negative,color='#2166ac',lw=2)
    ax.plot(E,scale*positive,color='#2166ac',lw=2)
    ax.axhline(0,color='.65',lw=.7)
    ax.annotate('',xy=(-1.9,-.01),xytext=(-1.7,-.01),arrowprops={'arrowstyle':'->'})
    ax.annotate('',xy=(-.85,.01),xytext=(-1.05,.01),arrowprops={'arrowstyle':'->'})
    ax.set(xlabel='Potential (V versus Fc⁺/Fc)',title=title,ylim=(-1.5,1.3))
axes[0].set_ylabel('Schematic faradaic current / reference scale')
axes[1].text(-.75,.12,'III',fontsize=9)
fig.suptitle('Qualitative model: excess CO₂, fixed scan rate, background subtracted')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
