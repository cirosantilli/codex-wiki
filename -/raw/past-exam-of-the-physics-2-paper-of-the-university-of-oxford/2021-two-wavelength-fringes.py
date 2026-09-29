"""Original equal-strength spectral-doublet plot; Python 3.14, numpy/matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

theta=np.linspace(-1,1,12001);delta=.001*np.sin(np.deg2rad(theta))
a=np.pi*delta/520e-9;b=np.pi*delta/540e-9
intensity=.5*(np.cos(a)**2+np.cos(b)**2)
visibility=np.abs(np.cos(a-b))
fig,ax=plt.subplots(figsize=(9,4.3),facecolor='white')
ax.plot(theta,intensity,color='#245e97',lw=1.2,label=r'$I/I(0)$, equal spectral strengths')
ax.plot(theta,(1+visibility)/2,'--',color='#b34c35',lw=1,label='Local fringe bounds')
ax.plot(theta,(1-visibility)/2,'--',color='#b34c35',lw=1)
for deg in [-.402219675819,.402219675819]:ax.axvline(deg,color='#555',ls=':',lw=1)
for deg in [-.80445917522,.80445917522]:ax.annotate('revival',xy=(deg,1),xytext=(deg,.83),ha='center',arrowprops={'arrowstyle':'->','color':'#555'},fontsize=10)
ax.text(0,.1,'First contrast minima: ±0.402°',ha='center',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.set(xlim=(-1,1),ylim=(0,1.09),xlabel='Diffraction angle θ (degrees)',ylabel='Normalized intensity',title='Two-slit interference: 520 nm + 540 nm, separation 1 mm')
ax.grid(alpha=.18);ax.legend(loc='upper center',fontsize=9,ncol=2)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
