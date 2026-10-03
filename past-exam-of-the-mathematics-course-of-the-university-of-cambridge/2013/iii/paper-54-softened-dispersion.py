"""Plot original softened density-wave dispersion curves in caller cwd."""
import os
os.environ.setdefault('MPLBACKEND','Agg')
import numpy as np
import matplotlib.pyplot as plt
Q=.65
s=np.linspace(0,2.2,600)
# A tiny subpixel margin avoids integer truncation of decimal inch sizes.
fig,ax=plt.subplots(figsize=((820+1e-6)/100,(460+1e-6)/100),dpi=100)
fig.patch.set_facecolor('white')
for delta,color in [(0,'#215e81'),(.5,'#ad5b20'),(1,'#34813d')]:
    w2=1+(s*s-2*s*np.exp(-delta*s))/(Q*Q)
    ax.plot(s,w2,lw=2,color=color,label=rf'$\delta={delta:g}$')
ax.axhline(0,color='#333333',lw=1)
ax.axhspan(-1.7,0,color='#bc3838',alpha=.09)
ax.text(1.90,-1.48,'Unstable',color='#882d2d',ha='center')
ax.set(xlim=(0,2.2),ylim=(-1.7,5),xlabel=r'Dimensionless wavenumber $s=Q c_s k/\kappa$',ylabel=r'Squared frequency $\omega^2/\kappa^2$')
ax.set_title(r'Softened disc gravity at fixed $Q=0.65$')
ax.legend(title='Softening',loc='upper left')
ax.grid(alpha=.18)
fig.subplots_adjust(left=.12,right=.97,bottom=.16,top=.89)
fig.savefig('paper-54-softened-dispersion.png',dpi=100,facecolor='white')
plt.close(fig)
