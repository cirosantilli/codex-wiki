"""Even periodic extension for a half-range cosine series; outputs to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.array([-2,-1,0,1,2]); y=np.array([0,1,0,1,0])
fig,ax=plt.subplots(figsize=(6.5,3.8),layout='constrained')
ax.plot(x,y,lw=2.6,color='#17609c')
ax.scatter([1.5],[.5],color='#a23b27',zorder=3)
ax.annotate(r'$(3L/2,L/2)$',xy=(1.5,.5),xytext=(.65,.8),arrowprops={'arrowstyle':'->'})
ax.set_xticks(x,['−2L','−L','0','L','2L']);ax.set_yticks([0,.5,1],['0','L/2','L'])
ax.set_ylim(-.08,1.16);ax.set_xlim(-2.1,2.1);ax.grid(alpha=.2)
ax.set_xlabel('$x$');ax.set_ylabel('Cosine-series sum')
ax.set_title('Continuous even extension, period 2L')
fig.savefig(Path('paper-1-cosine-extension.png'),dpi=135,facecolor='white')
