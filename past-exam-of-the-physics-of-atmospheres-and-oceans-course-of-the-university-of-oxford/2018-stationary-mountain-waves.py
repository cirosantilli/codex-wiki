"""Original stationary phase geometry and upper-layer cutoff; directions are frame-labelled."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,4.7),layout='constrained',facecolor='white')
x=np.linspace(-15,15,500);z=np.linspace(0,12,400);X,Z=np.meshgrid(x,z);k=-.1;m=-np.sqrt(1-.1**2);phase=k*X+m*Z;a=axes[0];a.contour(X,Z,phase,levels=np.arange(-16,3)*np.pi,colors='#355a9b',linewidths=1.2);ridge=.4*np.exp(-(x/5)**2);a.fill_between(x,0,ridge,color='#b19a77',zorder=3);a.plot(x,ridge,color='#6b5535',lw=1)
a.annotate('',xy=(-7.7,7),xytext=(-8,4),arrowprops={'arrowstyle':'->','color':'#269572','lw':2});a.text(-14,9.1,'ground-frame energy',fontsize=9,color='#147455');a.annotate('',xy=(5.7,3),xytext=(6,6),arrowprops={'arrowstyle':'->','color':'#bd7820','lw':2});a.text(3,8.8,'intrinsic phase',fontsize=9,color='#98621b');a.annotate('',xy=(-7,1.5),xytext=(-14,1.5),arrowprops={'arrowstyle':'->','color':'#555'});a.text(-14,1.9,'U = 10 m/s',fontsize=9);a.annotate('',xy=(13,7.315),xytext=(13,1),arrowprops={'arrowstyle':'<->','color':'#555'});a.text(13.4,4,'λz ≈ 6.3 km',rotation=90,va='center',fontsize=9);a.text(-14,11,'phase lines fixed in the ground frame',fontsize=9);a.set(xlabel='downwind distance (km)',ylabel='height (km)',xlim=(-15,15),ylim=(0,12),title='A  Dominant inverse-width component');a.set_aspect('equal')
lam=np.geomspace(10,200,600);critical=2*np.pi*10/.001/1000;m2=1-(critical/lam)**2;a=axes[1];a.axhspan(0,1.2,color='#e5edda');a.axhspan(-5,0,color='#f0e8dd');a.plot(lam,m2,color='#355a9b',lw=2);a.axhline(0,color='#555',ls=':');a.axvline(critical,color='#555',ls=':');a.text(80,.35,'vertical propagation',fontsize=10);a.text(13,-3,'evanescent above the cap',fontsize=10);a.annotate('cutoff ≈ 62.8 km',(critical,0),(72,-1.5),arrowprops={'arrowstyle':'->'},fontsize=10);a.set(xscale='log',xlabel='horizontal wavelength (km)',ylabel=r'$m^2/(N_{\rm upper}/U)^2$',ylim=(-5,1.2),xlim=(10,200),title='B  Weak upper layer: N = 10⁻³ s⁻¹')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
