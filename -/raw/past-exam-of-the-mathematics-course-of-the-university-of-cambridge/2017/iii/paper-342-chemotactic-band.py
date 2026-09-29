"""Original Keller--Segel band sketches. Run beside the destination PNG.
Tested Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (Debian build).
Output: paper-342-chemotactic-band.png in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
xi=np.linspace(-8,6,1201)
fig,axs=plt.subplots(1,2,figsize=(8,4.5),dpi=100,facecolor='white')
colors=['#0072B2','#D55E00','#009E73']
for mu,color in zip([1.5,2.,3.],colors):
 c=np.exp(-np.logaddexp(0,-xi)/(mu-1))
 b=np.exp(-xi-mu/(mu-1)*np.logaddexp(0,-xi))/(mu-1)
 axs[0].plot(xi,c,color=color,label=rf'$\mu={mu:g}$',lw=2)
 axs[1].plot(xi,b,color=color,label=rf'$\mu={mu:g}$',lw=2)
 peak=-np.log(mu-1);height=mu**(-mu/(mu-1))
 axs[1].plot(peak,height,'o',color=color,ms=5)
for ax in axs:
 ax.set_xlim(-8,6);ax.set_xlabel(r'$\xi=vz/D$');ax.grid(alpha=.2)
 ax.set_facecolor('white');ax.legend(frameon=False,fontsize=9)
axs[0].set_ylim(0,1.04);axs[0].set_ylabel(r'$C/C_\infty$');axs[0].set_title('Nutrient front')
axs[1].set_ylim(0,.34);axs[1].set_ylabel(r'$kDB/(v^2C_\infty)$');axs[1].set_title('Bacterial band; dots mark maxima')
fig.tight_layout(pad=1.4)
fig.savefig('paper-342-chemotactic-band.png',facecolor='white',transparent=False,dpi=100)
plt.close(fig)
