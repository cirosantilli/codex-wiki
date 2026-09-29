"""Original analytical diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10. Writes basename into cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

b=np.linspace(0,2.2,600)
fig,axes=plt.subplots(1,2,figsize=(10,4.1),layout='constrained',sharey=True)
for ax,g2 in zip(axes,[-.4,-2]):
 g1=2;u=b*(g1+g2);w=b*(g1-g2)
 ax.plot(b,.25-u/2,label=r'$\uparrow\uparrow$',color='#235789',lw=2)
 ax.plot(b,.25+u/2,label=r'$\downarrow\downarrow$' if g2!= -2 else 'parallel pair (2)',color='#235789' if g2==-2 else '#448866',ls='--',lw=2)
 ax.plot(b,-.25+.5*np.sqrt(1+w*w),label=r'$E_+$',color='#ce5a24',lw=2)
 ax.plot(b,-.25-.5*np.sqrt(1+w*w),label=r'$E_-$',color='#8a4e9f',lw=2)
 ax.set(xlabel=r'$b=\mu_0 B/\Delta$',title=fr'$g_1=2,\ g_2={g2:g}$');ax.grid(alpha=.2)
 ax.legend(fontsize=9,loc='lower left')
axes[0].set_ylabel(r'$E/\Delta$')
fig.suptitle(r'Illustrative signed moments; $\Delta>0$ (not measured parameters)',fontsize=12)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
