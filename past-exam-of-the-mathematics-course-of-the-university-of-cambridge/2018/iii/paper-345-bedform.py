"""Conditional dimensionless dispersion curves; opaque PNG in CWD."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(0,2,500)
fig,axs=plt.subplots(1,2,figsize=(9,4.60001),dpi=100,facecolor='white')
for r,col in [(-.5,'#b65040'),(.5,'#337ba2'),(1.5,'#34805c')]:
 axs[0].plot(x,x*x*(r-x)/(1+x*x),color=col,label=f'$b/a={r:g}$')
 axs[1].plot(x,x*(1+r*x)/(1+x*x),color=col,label=f'$b/a={r:g}$')
for ax in axs:
 ax.axhline(0,color='#666666',lw=.8);ax.set_xlabel('$kL_{\\rm sat}$');ax.spines[['top','right']].set_visible(False);ax.legend(frameon=False,fontsize=10)
axs[0].set(ylabel='$\\sigma L_{\\rm sat}^2/(Ca)$',title='Growth: positive only in an unstable band')
axs[1].set(ylabel='$cL_{\\rm sat}/(Ca)$',title='Migration velocity')
fig.tight_layout();fig.savefig('paper-345-bedform.png',facecolor='white',transparent=False)
