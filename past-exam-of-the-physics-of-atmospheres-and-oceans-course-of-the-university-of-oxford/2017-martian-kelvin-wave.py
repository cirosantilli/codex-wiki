"""Original Mars Kelvin-wave trapping and phase structure for the corrected anelastic model; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
a=3.4e6;H=1e4;N=.01;c=20.;period=24.4*3600
beta=4*np.pi/(period*a);Ld=np.sqrt(c/beta);latd=np.degrees(Ld/a)
m=-np.sqrt((N/c)**2-(1/a)**2-1/(4*H*H))
fig,axes=plt.subplots(1,2,figsize=(10.8,4.5),gridspec_kw={'width_ratios':[1,1.35]},constrained_layout=True,facecolor='white')
lat=np.linspace(-35,35,501);envelope=np.exp(-.5*(lat/latd)**2)
axes[0].plot(lat,envelope,color='#1864ab',lw=2.3)
for sign in [-1,1]:axes[0].axvline(sign*latd,color='.5',lw=1,ls=':')
axes[0].axhline(np.exp(-.5),color='.65',ls=':',lw=1)
axes[0].text(0,.68,r'$L_D/a\simeq11.6^\circ$',ha='center')
axes[0].set(xlabel='Latitude (degrees)',ylabel='Meridional amplitude / equatorial amplitude',ylim=(0,1.06),title='Equatorial overlap of localized thermal forcing')
axes[0].grid(alpha=.16)
lon=np.linspace(0,360,601);height=np.linspace(0,32,401)
field=np.cos(np.radians(lon)[None,:]+m*height[:,None]*1000)
im=axes[1].pcolormesh(lon,height,field,cmap='RdBu_r',vmin=-1,vmax=1,rasterized=True,shading='auto')
axes[1].set(xlabel='Longitude (degrees)',ylabel='Height (km)',title='Density-weighted vertical velocity at the equator')
axes[1].text(180,30.3,r'$\lambda_z\simeq12.6\ \mathrm{km}$; ground pattern stationary',ha='center',fontsize=10,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
cb=fig.colorbar(im,ax=axes[1],shrink=.83,pad=.02);cb.set_label(r'$e^{-z/(2H)}w$ / amplitude')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
