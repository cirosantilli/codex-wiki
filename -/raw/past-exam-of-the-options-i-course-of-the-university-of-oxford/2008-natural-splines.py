"""Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7; output in CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,2,500);t=x-1;s=np.where(x<=1,x**3-x,2*t+3*t**2-t**3)
fig,ax=plt.subplots(figsize=(6,4.2),facecolor='white');ax.set_facecolor('white')
ax.plot(x,s,color='#256493',label='$S(x)$');ax.plot(x,s+x,color='#b34c32',label='$S(x)+x$')
ax.scatter([0,1,2],[0,0,4],color='#256493',zorder=4);ax.scatter([0,1,2],[0,1,6],color='#b34c32',marker='s',zorder=5)
ax.axhline(0,color='#bbbbbb',lw=.6);ax.set(xlabel='$x$',ylabel='Interpolated value',title='Natural cubic splines and a linear trend',xlim=(-.05,2.05))
ax.legend();ax.grid(alpha=.15);fig.tight_layout();fig.savefig('2008-natural-splines.png',dpi=160,facecolor='white');plt.close(fig)
