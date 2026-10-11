"""Original hyperbola branch sketch. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

PNG is saved in cwd, normally the mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

a,b=2.,1.;c=np.hypot(a,b);t=np.linspace(-2,2,700)
fig,ax=plt.subplots(figsize=(7.0,4.7),layout='constrained',facecolor='white')
x=np.linspace(-3,7,300)
ax.plot(x,b*x/a,'--',color='#888888',lw=1,label='Asymptotes')
ax.plot(x,-b*x/a,'--',color='#888888',lw=1)
ax.plot(a*np.cosh(t),b*np.sinh(t),color='#0072b2',lw=2,label='Parametrized branch')
ax.plot([-c,c],[0,0],'o',color='#009e73',ms=5)
ax.annotate(r'$F_-$',(-c,0),xytext=(-2.7,-.5),fontsize=11)
ax.annotate(r'$F_+$',(c,0),xytext=(2.7,-.5),fontsize=11,
            arrowprops={'arrowstyle':'-', 'color':'#777777'})
ax.plot(a,0,'o',color='#d55e00',ms=5)
ax.annotate(r'$(a,0)$',(a,0),xytext=(.4,.65),fontsize=11,
            arrowprops={'arrowstyle':'-', 'color':'#777777'})
ax.annotate('',xy=(a*np.cosh(1.2),b*np.sinh(1.2)),xytext=(a*np.cosh(1),b*np.sinh(1)),
            arrowprops={'arrowstyle':'->','color':'#0072b2','lw':2})
ax.axhline(0,color='#444444',lw=.8);ax.axvline(0,color='#444444',lw=.8)
ax.set(xlim=(-3,6.5),ylim=(-3.1,3.1),xlabel='$x$',ylabel='$y$',
       title=r'Only the right branch is traced (example: $a=2$, $b=1$)')
ax.set_aspect('equal');ax.grid(alpha=.16);ax.legend(loc='upper left',fontsize=9)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
