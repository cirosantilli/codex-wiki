from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
G=6.67430e-11;c=299792458.;mp=1.67262192369e-27;sigma=6.65e-29
solar_mass=1.98847e30;solar_lum=3.828e26;year=365.25*86400
mass=6.3e13*solar_lum/(4*np.pi*G*mp*c*solar_mass/sigma)
time=.1/.9*sigma*c/(4*np.pi*G*mp)/year/1e9
seeds=np.geomspace(10,1e6,700);needed=time*np.log(mass/seeds)
fig,ax=plt.subplots(figsize=(7.8,4.5),dpi=130,facecolor='white')
ax.semilogx(seeds,needed,color='#2268a3',lw=2.5)
ax.axhline(.77,color='#b13939',ls='--',lw=1.8,label='Quoted cosmic age 0.77 Gyr')
minimum=mass*np.exp(-.77/time);ax.axvline(minimum,color='0.55',ls=':',lw=1.3)
ax.text(minimum*1.18,.33,fr'Absolute seed floor $\simeq {minimum:.0f}\,M_\odot$',fontsize=10)
for val,txt in [(100,r'$100\,M_\odot$'),(1e5,r'$10^5\,M_\odot$')]:
 tv=time*np.log(mass/val);ax.plot(val,tv,'o',color='#26764e');ax.annotate(txt,(val,tv),xytext=(8,9),textcoords='offset points',fontsize=11)
ax.set(xlim=(10,1e6),ylim=(.28,1.03),xlabel=r'Seed mass $M_{\rm seed}/M_\odot$',ylabel='Required growth time (Gyr)',title=r'Eddington growth to $1.92\times10^9M_\odot$, $\epsilon=0.1$')
ax.legend(loc='upper right',fontsize=10,frameon=False)
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
