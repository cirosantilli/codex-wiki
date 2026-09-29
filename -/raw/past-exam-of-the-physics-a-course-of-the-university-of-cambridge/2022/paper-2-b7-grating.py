"""Original grating solution figure; Python 3.14, root NumPy/Matplotlib dependencies.
Write opaque PNG basename in cwd. N=20 is illustrative, not additional paper data.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

N = 20
u = np.linspace(-2.25,2.25,20001)
def pattern(u):
    d = u-np.rint(u)
    return (np.sinc(N*d)/np.sinc(d))**2
fig, (ax, zoom) = plt.subplots(1,2,figsize=(9,3.7),dpi=130,facecolor='white',
                               gridspec_kw={'width_ratios':[1.3,1]})
ax.plot(u,pattern(u),color='#31688e',lw=1)
ax.set(xlabel=r'$u=D\sin\theta/\lambda$',ylabel=r'$I/(N^2I_1)$',
       title='Narrow-slit grating; illustration N = 20',ylim=(-.03,1.12))
ax.set_xticks(range(-2,3))
s = np.linspace(-2.4,2.4,3000)
zoom.plot(s,np.sinc(s)**2,color='#31688e')
zoom.axvline(1,color='#d55e00',ls='--',lw=1)
zoom.annotate('First minimum', (1,0),(.65,.45),fontsize=9,
              arrowprops=dict(arrowstyle='->',color='#d55e00'))
zoom.annotate('',(1,.1),(0,.1),arrowprops=dict(arrowstyle='<->',color='#d55e00'))
zoom.text(.5,.15,r'$\delta u=1/N$',ha='center',fontsize=10)
zoom.set(xlabel=r'$N(u-m)$',title='One principal maximum (large N)',ylim=(-.03,1.12))
for a in (ax,zoom):
    a.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
