"""Original theoretical curves, not reconstructed data.
Python 3.14, numpy 2.3, matplotlib 3.10. Writes basename PNG in CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(11,4.2),facecolor='white')
c=np.linspace(-1,1,300);w=.231;gl=-.5+w;gr=w;A=(gl**2-gr**2)/(gl**2+gr**2)
axs[0].plot(c,3/8*(1+c*c),label='QED',lw=2,color='#236b8e');axs[0].plot(c,3/8*(1+c*c+2*A*A*c),label=r'$Z$ pole, $\sin^2\theta_W=0.231$',ls='--',color='#b14c29',lw=2)
axs[0].set(xlabel=r'$\cos\theta^*$',ylabel=r'$\sigma^{-1}d\sigma/d\cos\theta^*$',title='Forward–backward asymmetry');axs[0].legend(fontsize=9)
mt,mh,et=1.777,1.5,45.6;r=mh**2/mt**2;energy=np.linspace(et*r,et,300);cost=(2*energy/et-1-r)/(1-r)
for spin,alpha,color in [('Spin 0',1,'#236b8e'),('Spin 1',(1-2*r)/(1+2*r),'#b14c29')]:
    for pol,style in [(1,'-'),(-1,'--')]:
        axs[1].plot(energy,(1+alpha*pol*cost)/((1-r)*et),ls=style,color=color,lw=2,label=f'{spin}, P = {pol:+d}')
axs[1].set(xlabel='Total hadronic energy (GeV)',ylabel='Normalized density (1/GeV)',title=r'$\tau^-\to h^-\nu_\tau$, $m_h=1.5$ GeV');axs[1].legend(fontsize=8.5,loc='upper center')
for ax in axs:ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(Path('2015-angular-and-tau-energy.png'),dpi=140,facecolor='white')
