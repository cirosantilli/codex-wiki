"""Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Output only to the cwd."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
u=np.linspace(0,4,600)
mu_absolute=u*u/8
fig,ax=plt.subplots(figsize=(7.2,3.6),dpi=100)
ax.fill_between(u,-.4,0,color='#dbe8ec')
ax.fill_between(u,0,mu_absolute,color='#fff0c9')
ax.fill_between(u,mu_absolute,2.8,color='#f4d1d5')
ax.plot(u,mu_absolute,color='#a02b3d',linewidth=2)
ax.axhline(0,color='#34495e',linewidth=1.5)
ax.text(2.1,-.24,'Stable',ha='center',fontsize=11)
ax.text(2.9,.48,'Convective instability',ha='center',fontsize=10)
ax.text(1.4,1.8,'Absolute instability',ha='center',fontsize=11)
ax.text(3.16,1.49,r'$\mu=U^2/8$',fontsize=10,color='#7e1f2c')
ax.set(xlim=(0,4),ylim=(-.4,2.8),xlabel=r'Advection speed $U$',ylabel=r'Local growth rate $\mu$',title=r'Ginzburg–Landau stability regions ($c_d=1$)')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
fig.savefig('paper-331-stability-regions.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
