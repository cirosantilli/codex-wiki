"""Cubic-area dam-break profiles; respect caller MPLCONFIGDIR; cwd output."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
s=np.linspace(-1,6,500)
h=((6-s)/7)**2;u=6*(1+s)/7
fig,axes=plt.subplots(1,2,figsize=(9.5,4.2),dpi=140,facecolor='white')
for ax,y,label in [(axes[0],h,r'Depth $h/H$'),(axes[1],u,r'Wet-region velocity $u/c_0$')]:
    ax.plot([-2,-1],[y[0],y[0]],color='#245b8c',lw=2)
    ax.plot(s,y,color='#245b8c',lw=2)
    ax.axvline(-1,color='#89939b',ls=':',lw=1)
    ax.axvline(6,color='#89939b',ls=':',lw=1)
    ax.set_xlim(-2,7);ax.set_xlabel(r'$x/(c_0t)$');ax.set_ylabel(label)
    ax.spines[['top','right']].set_visible(False)
axes[0].plot([6,7],[0,0],color='#245b8c',lw=2)
axes[1].axvspan(6,7,color='#eeeeee');axes[1].text(6.5,3,'dry',ha='center')
axes[0].set_title('Depth reaches zero at the front')
axes[1].set_title('Wet-side tip speed is $6c_0$')
fig.suptitle(r'Dry-bed release: $A\propto h^3$, $c_0=\sqrt{gH/3}$',fontsize=14)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-76-dam-break.png',facecolor='white',transparent=False)
plt.close(fig)
