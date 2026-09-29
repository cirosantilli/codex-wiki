"""Original NFW rotation sketch; writes its PNG basename to caller CWD.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Uses the caller's MPLCONFIGDIR unchanged and an opaque white background.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.logspace(-3,3,900)
y=np.sqrt((np.log1p(x)-x/(1+x))/x)
lo,hi=1.,3.
for _ in range(80):
    q=(lo+hi)/2
    if q*q/(1+q)**2>math.log1p(q)-q/(1+q):
        lo=q
    else:
        hi=q
peak=(lo+hi)/2
vpeak=math.sqrt((math.log1p(peak)-peak/(1+peak))/peak)
fig,ax=plt.subplots(figsize=(8,4.3),dpi=120,facecolor='white')
ax.set_facecolor('white')
ax.semilogx(x,y,color='#235b9c',lw=2.3,label='NFW circular speed')
small=np.logspace(-3,-1.1,150)
large=np.logspace(1.3,3,150)
ax.semilogx(small,np.sqrt(small/2),'--',color='#bd6e18',lw=1.5,label=r'Inner limit: $\sqrt{x/2}$')
ax.semilogx(large,np.sqrt((np.log(large)-1)/large),'--',color='#548343',lw=1.5,label=r'Outer limit: $\sqrt{(\log x-1)/x}$')
ax.scatter([peak],[vpeak],color='#882b37',zorder=4,s=32)
ax.annotate('Maximum\n$x=2.163$, $v/v_s=0.465$',xy=(peak,vpeak),xytext=(18,.47),arrowprops={'arrowstyle':'->','color':'#882b37'},fontsize=10,color='#882b37')
ax.set(xlabel=r'$x=r/r_1$',ylabel=r'$v_c/v_s$,  $v_s=\sqrt{4\pi G\rho_1r_1^2}$',xlim=(1e-3,1e3),ylim=(0,.55),title='NFW circular speed and its limiting scalings')
ax.grid(alpha=.2)
ax.legend(loc='upper left',frameon=False,fontsize=9)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-44-nfw-rotation.png',facecolor='white',transparent=False)
plt.close(fig)
