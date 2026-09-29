"""Original solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; saves a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(11,4.5));ax=axs[0];ax.add_patch(Circle((0,0),1,fc='#fff0ce',ec='#a86500'));ax.add_patch(Circle((0,0),.38,fc='#80b9dc',ec='none',alpha=.8));ax.add_patch(Circle((0,0),.31,fc='#111111'));ax.annotate('Atmospheric annulus',xy=(.34,.1),xytext=(.55,.8),arrowprops={'arrowstyle':'->'},ha='center');ax.annotate('Opaque planet',xy=(0,-.1),xytext=(-.58,-.7),arrowprops={'arrowstyle':'->'},ha='center');ax.text(0,1.18,'Transmission: wavelength-dependent blocked area',ha='center');ax.text(0,-1.28,'Feature scale ≈ 2 Rp N_H H / R★²',ha='center');ax.set(aspect='equal',xlim=(-1.3,1.3),ylim=(-1.42,1.4));ax.axis('off')
lam=np.geomspace(.4,30,400);hc_k=1.438776877e4;Ts=5000.;radius=.1
for Tp in [1000.,1500.]:
 ratio=radius*radius*np.expm1(hc_k/(lam*Ts))/np.expm1(hc_k/(lam*Tp));axs[1].semilogx(lam,1e6*ratio,lw=2,label='Planet T = %d K'%Tp)
axs[1].set(xlabel='Wavelength / μm',ylabel='Thermal eclipse depth / ppm',title='Occultation isolates dayside emission');axs[1].legend(fontsize=9);axs[1].grid(alpha=.15);fig.text(.74,.025,'Illustrative blackbodies: star5000K, Rp/R★=0.1; not exam data.',ha='center',fontsize=8);fig.tight_layout(rect=(0,.04,1,1))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
