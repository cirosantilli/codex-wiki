# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Run in desired output directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
fig,axs=plt.subplots(1,3,figsize=(10,3.7),sharex=True,sharey=True)
x=np.linspace(-1,1,800)
for ax,h in zip(axs,[.2,.6,.9]):
    s=1-np.sqrt(1-h);f=h-x*x;w=np.where(np.abs(x)<=s,f,2*s*(1-np.abs(x)))
    ax.plot(x,f,'--',color='.45',label='obstacle');ax.plot(x,w,color='#2171b5',lw=2,label='string')
    mask=np.abs(x)<=s;ax.plot(x[mask],w[mask],color='#c34f2d',lw=3,label='contact');ax.plot([-s,s],[h-s*s,h-s*s],'ko',ms=3)
    ax.axhline(0,color='.7',lw=.7);ax.set(xlabel='$x$',title=rf'$h={h},\ s={s:.3f}$',xlim=(-1,1),ylim=(-.85,1));ax.grid(alpha=.15)
axs[0].set_ylabel('$w, f$');axs[0].legend(fontsize=8,loc='lower center');fig.suptitle('Taut string above a parabolic obstacle')
fig.tight_layout();fig.savefig(Path('2008-string-contact.png'),dpi=150,facecolor='white');plt.close(fig)
