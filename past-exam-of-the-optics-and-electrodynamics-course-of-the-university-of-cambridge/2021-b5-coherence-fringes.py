"""Original lifetime-broadened interference solution plot; Python 3.14, root deps.
Write opaque PNG basename in cwd. The coherence scale is illustrative only.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

u=np.linspace(-14,14,6000)  # y divided by fringe period lambda/sqrt(2)
env=np.exp(-np.abs(u)/5)
signal=1+env*np.cos(2*np.pi*u)
fig,(profile,geometry)=plt.subplots(1,2,figsize=(10,4.2),dpi=130,facecolor='white',
                                  gridspec_kw={'width_ratios':[1.6,1]})
profile.plot(u,signal,color='#31688e',lw=1.3)
profile.plot(u,1+env,'--',color='#d55e00',lw=1)
profile.plot(u,1-env,'--',color='#d55e00',lw=1)
profile.axhline(1,color='.6',lw=.7)
profile.set(xlim=(-14,14),ylim=(-.06,2.12),xlabel=r'$y/(\lambda/\sqrt{2})$',
            ylabel=r'$I(y)/I_0$',title='Exponential visibility envelope; central maximum 2')
profile.spines[['top','right']].set_visible(False)
for yy in [-.8,0,.8]:
    geometry.annotate('',(1.5,yy),(-.5,yy),arrowprops=dict(arrowstyle='->',color='#31688e',lw=1.8))
geometry.plot([1.6,1.6],[-1.1,1.1],color='#d55e00',lw=4)
geometry.annotate(r'$\langle\mathbf{S}\rangle\parallel+\hat{x}$',(.2,.1),fontsize=12)
geometry.text(1.7,0,'sensor\nplane',va='center',fontsize=10,color='#d55e00')
geometry.annotate('',(-.8,1.05),(-.8,-1.05),arrowprops=dict(arrowstyle='->',color='.3'))
geometry.text(-.91,1.12,'y',fontsize=11)
geometry.text(-.55,-1.28,'Flux crosses a y-profile sensor.\nAn x-profile lies along the energy flow.',fontsize=9)
geometry.set(xlim=(-1.1,2.5),ylim=(-1.5,1.5),title='A transverse sensor samples y')
geometry.axis('off')
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
