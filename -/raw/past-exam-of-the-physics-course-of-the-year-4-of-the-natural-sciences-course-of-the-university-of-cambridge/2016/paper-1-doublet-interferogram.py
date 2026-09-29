"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; the output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

l1,l2=589.59e-9,590.00e-9;k1,k2=2*np.pi/l1,2*np.pi/l2;dk=abs(k1-k2);rev=np.pi/dk;d=np.linspace(0,2*rev,3000)
fig,axs=plt.subplots(3,1,figsize=(8,8),gridspec_kw={'height_ratios':[1,1,1]})
# Illustrative finite width, not a recovered numeric width from the exam figure.
sigma=.10*dk
for ax,w,title in zip(axs[:2],[.5,.75],['Equal line powers','Unequal line powers: 3:1']):
 V=np.sqrt(w*w+(1-w)**2+2*w*(1-w)*np.cos(2*dk*d));D=np.exp(-2*sigma*sigma*d*d)
 ax.fill_between(d*1e3,.5*(1-V),.5*(1+V),color='steelblue',alpha=.18,label='Narrow-line intensity bounds');ax.plot(d*1e3,.5*(1-D*V),color='darkorange',lw=2,label='Illustrative finite-width bounds');ax.plot(d*1e3,.5*(1+D*V),color='darkorange',lw=2);ax.axvline(rev*1e3,color='.4',ls=':');ax.axhline(.5,color='.5',lw=.7);ax.set(xlim=(0,2*rev*1e3),ylim=(-.03,1.03),ylabel='I / total input',title=title);ax.grid(alpha=.15)
axs[0].legend(fontsize=8,loc='upper right');axs[1].set_xlabel('One-way arm difference δ (mm); first visibility revival = 0.4242 mm')
z=np.linspace(0,2e-6,4000);I=.5+.25*(np.cos(2*k1*z)+np.cos(2*k2*z));axs[2].plot(z*1e6,I,color='navy',lw=1.3);axs[2].set(xlabel='One-way arm difference δ (µm)',ylabel='I / total input',title='Resolved carrier fringes near balance (equal narrow lines)',ylim=(-.03,1.03));axs[2].grid(alpha=.2)
fig.suptitle('Sodium doublet using the printed 589.59 nm and 590.00 nm centres');fig.tight_layout(rect=(0,.04,1,.96));fig.text(.5,.005,'Orange illustration: Gaussian σk = 0.10 |k₁−k₂|; the exam supplies no numerical linewidth.',ha='center',fontsize=9)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
