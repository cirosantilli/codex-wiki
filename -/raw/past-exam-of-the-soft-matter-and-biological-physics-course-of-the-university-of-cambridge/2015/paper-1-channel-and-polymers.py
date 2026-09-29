"""Original generic-physics solution diagram; Python3.14.4,numpy2.3.5,matplotlib3.10.7.
Run from mirrored _media directory; save basename in cwd. No biological model.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
y=np.linspace(0,1,1600);fig,axs=plt.subplots(1,2,figsize=(10.8,4.7))
for theta in [2.,10.,50.]:
 u=1-(1-1/np.cosh(theta))*y-np.cosh(theta*(1-y))/np.cosh(theta);ym=1-np.arcsinh((np.cosh(theta)-1)/theta)/theta;um=1-(1-1/np.cosh(theta))*ym-np.cosh(theta*(1-ym))/np.cosh(theta);line=axs[0].plot(y,u,lw=2,label='κd = %g'%theta)[0];axs[0].scatter([ym],[um],color=line.get_color(),s=35)
axs[0].set(xlabel='Position x / channel width d',ylabel='Velocity / isolated-wall bulk speed U',title='One charged wall; dots mark maxima');axs[0].legend(fontsize=9);axs[0].grid(alpha=.15)
for ratio in [.05,.2]:
 n=(1-np.exp(-y/ratio))*(1-np.exp(-(1-y)/ratio));axs[1].plot(y,n,lw=2,label='Illustrative depletion scale / d = %.2f'%ratio)
axs[1].set(xlabel='Position x / channel width d',ylabel='Relative polymer concentration',title='Nonadsorbing, weak-flow depletion sketch',ylim=(0,1.1));axs[1].legend(fontsize=8);axs[1].grid(alpha=.15);fig.text(.5,.015,'Charged wall x = 0; neutral wall x = d. Polymer curves are qualitative shapes, not a solved transport model.',ha='center',fontsize=9);fig.tight_layout(rect=(0,.05,1,1))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
