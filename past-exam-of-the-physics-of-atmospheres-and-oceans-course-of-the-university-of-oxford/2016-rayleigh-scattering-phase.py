"""Original explanatory figure. Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from any directory; the only output is a same-basename PNG in that directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

th=np.linspace(0,2*np.pi,900)
phase=.75*(1+np.cos(th)**2)
fig,ax=plt.subplots(figsize=(6.4,5.0),subplot_kw={'projection':'polar'},layout='constrained')
ax.plot(th,phase,lw=2.8,color='#126782')
ax.fill(th,phase,color='#126782',alpha=.10)
ax.set_rticks([.5,1,1.5]);ax.set_rlim(0,1.8);ax.set_rlabel_position(45)
ax.set_thetagrids([0,90,180,270],['Forward 0°','90°','Backward 180°','270°'])
ax.grid(alpha=.4)
ax.set_title('Unpolarized Rayleigh scattering\n'+r'$P(\Theta)=\frac{3}{4}(1+\cos^2\Theta),\quad g=0$',pad=24)

fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
plt.close(fig)
