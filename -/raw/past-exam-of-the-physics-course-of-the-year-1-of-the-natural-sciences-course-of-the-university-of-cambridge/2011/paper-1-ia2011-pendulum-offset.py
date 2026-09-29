"""Original normalized physical-pendulum period plot.
Python 3.14, NumPy, Matplotlib; writes the basename PNG to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.geomspace(.055,4.5,801);period=np.sqrt(x+2/(3*x));xm=np.sqrt(2/3);ym=np.sqrt(2*xm)
fig,ax=plt.subplots(figsize=(7.7,4.7),layout='constrained')
ax.plot(x,period,color='#2c6f9f',lw=2.5)
ax.scatter([xm],[ym],color='#a84d27',zorder=3)
ax.axvline(xm,ls=':',color='#a84d27')
ax.annotate('Minimum at a/R = √(2/3)',xy=(xm,ym),xytext=(1.35,2.65),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set(xlabel=r'Pivot offset $a/R$',ylabel='T / [2π √(R/g)]',title=r'Cylindrical density proportional to $r^2$',xlim=(0,4.5),ylim=(1.05,3.7))
ax.grid(alpha=.2)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=145,facecolor='white')
