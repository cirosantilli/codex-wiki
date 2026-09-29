"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10,'axes.spines.top':False,'axes.spines.right':False})

delta=.5;k=np.sqrt(delta/6);c=-5*k;x=np.linspace(-20,20,600);fig,ax=plt.subplots(figsize=(7.5,3.7),layout='constrained')
for t in (0,3,6):ax.plot(x,(1+np.exp(-k*(x-c*t)))**-2,label=f't={t}')
ax.annotate('Propagation',(-10,.75),(-2,.75),arrowprops={'arrowstyle':'->'},ha='center');ax.set(xlabel='Position',ylabel='u',title='Increasing Fisher profile; negative wave speed',ylim=(-.03,1.04));ax.legend()
fig.savefig(Path.cwd()/'2010-fisher-front.png',dpi=150,facecolor='white');plt.close(fig)
