"""Original forward/reverse solution plot, not a reproduction of the source diagram.
Python 3.14, root NumPy/Matplotlib dependencies. Write opaque PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

B = np.linspace(-.32, .32, 1600)
theta = 9*B
Bopt = np.pi/36
fig, (ax, state) = plt.subplots(1,2,figsize=(9,4),dpi=130,facecolor='white',
                                gridspec_kw={'width_ratios':[1.5,1]})
ax.plot(B,.5*np.cos(theta-np.pi/4)**2,color='#31688e',lw=2,label='Forward')
ax.plot(B,.5*np.cos(theta+np.pi/4)**2,color='#d55e00',lw=2,ls='--',label='Reverse or polarizers swapped')
ax.axvline(Bopt,color='0.4',ls=':',lw=1)
ax.annotate('87.3 mT', (Bopt,.5), (.13,.38), fontsize=10,
            arrowprops=dict(arrowstyle='->',color='0.4'))
ax.set(xlabel='Signed axial magnetic field / T',ylabel=r'$I/I_0$',xlim=(-.32,.32),ylim=(-.02,.58),
       title='Unpolarized input; Verdet constant 9 rad/(T m)')
ax.legend(fontsize=8.5,loc='upper left')
ax.grid(alpha=.2)
for angle, color, label in [(0,'#31688e','Entrance axis'),(np.pi/4,'#009e73','After forward pass'),
                             (np.pi/2,'#d55e00','Return at entrance')]:
    end=np.array([np.cos(angle),np.sin(angle)])
    state.plot([-end[0],end[0]],[-end[1],end[1]],color=color,lw=3,label=label)
phi=np.linspace(0,np.pi/2,100)
state.plot(.65*np.cos(phi),.65*np.sin(phi),color='0.5',lw=1)
state.annotate('',(.65*np.cos(phi[-1]),.65*np.sin(phi[-1])),
               (.65*np.cos(phi[-10]),.65*np.sin(phi[-10])),
               arrowprops=dict(arrowstyle='->',color='0.5'))
state.set_aspect('equal')
state.set(xlim=(-1.2,1.2),ylim=(-1.25,1.3),title='At the optimum field: 45° each pass')
state.axis('off')
state.legend(fontsize=8.5,loc='lower center',bbox_to_anchor=(.5,-.16),frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
