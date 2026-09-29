"""Original illustration for the 2016 Oxford Physics 2 resit solutions.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,ax=plt.subplots(figsize=(6,4),layout='constrained');x=np.linspace(0,1,200);y=np.linspace(1,4,500)
ax.plot(x,x,color='#246ea6',lw=2.3,label='inside: proportional to $r$');ax.plot(y,1/y,color='#b45a28',lw=2.3,label='outside: proportional to $1/r$')
ax.scatter([1],[1],color='black',s=26,zorder=4);ax.axvline(1,color='.6',ls=':',lw=1);ax.set(xlabel='$r/a$',ylabel='$B(r)/B(a)$',title='Uniform DC current in a nonmagnetic wire',xlim=(0,4),ylim=(0,1.12));ax.legend(fontsize=9);ax.grid(alpha=.2)
fig.savefig(Path.cwd()/'2016-resit-wire-magnetic-field.png',dpi=140,transparent=False);plt.close(fig)
