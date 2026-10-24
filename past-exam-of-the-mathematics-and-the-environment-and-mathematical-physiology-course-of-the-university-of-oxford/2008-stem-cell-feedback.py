# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Output in current working directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
b=3.;mu=1.;n=3;u=np.linspace(0,2.2,500);star=(mu*b-1)**(1/n);g=b*u/(1+u**n)
fig,ax=plt.subplots(figsize=(6.5,4.4));ax.plot(u,mu*g,label=r'$\mu g(u)$');ax.plot(u,u,label='$u$');ax.plot([0,star],[0,star],'ko');ax.annotate('unique positive equilibrium',(star,star),(1.2,.48),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlabel='$u$',ylabel='steady balance',title=r'Stem-cell feedback: $\mu b=3>1$, $n=3$',xlim=(0,2.2),ylim=(0,2.25));ax.legend(loc='upper left');ax.grid(alpha=.2);fig.tight_layout();fig.savefig(Path('2008-stem-cell-feedback.png'),dpi=150,facecolor='white');plt.close(fig)
