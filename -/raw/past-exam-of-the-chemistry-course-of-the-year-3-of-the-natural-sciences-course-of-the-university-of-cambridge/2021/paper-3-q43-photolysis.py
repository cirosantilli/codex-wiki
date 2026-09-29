"""Original solution diagram; Python 3.14, matplotlib 3.10, numpy 2.3.
Run from the mirrored media directory: PNG basename is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save,wedge,BLUE,ORANGE

fig,ax=plt.subplots(figsize=(6.5,4));z=np.linspace(10,65,300)
ax.plot(1/(1+np.exp(-(z-48)/4)),z,label='HCl · later short-UV turn-on',color=BLUE,lw=2)
ax.plot(.10+.9/(1+np.exp(-(z-28)/9)),z,label='HNO₃ · longer UV penetrates lower',color=ORANGE,lw=2)
ax.set(xlabel='Relative J (independent arbitrary scales)',ylabel='Altitude / km',title='Qualitative reservoir photolysis',xticks=[],ylim=(10,65));ax.legend(fontsize=9,loc='lower right');ax.grid(alpha=.2);fig.tight_layout()
save(fig,Path(__file__).with_suffix('.png').name)
