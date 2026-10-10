"""Original mass-distance scaling family and predicted radial velocities."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
AU=149597870700.;YEAR=365.25*86400;GM_SUN=1.3271244e20
P=18*YEAR;e=.7;i,w=np.deg2rad([55,35]);alpha_arcsec=.110
phase=np.linspace(0,1,1601);M=2*np.pi*phase;E=M.copy()
for _ in range(20):E-=(E-e*np.sin(E)-M)/(1-e*np.cos(E))
Dgrid=np.linspace(5,10,400);a=alpha_arcsec*Dgrid*1000*AU
mass=4*np.pi**2*a**3/P**2/GM_SUN/1e6
fig,axs=plt.subplots(1,2,figsize=(12,4.8),dpi=140,facecolor='white')
axs[0].plot(Dgrid,mass,color='#888',lw=2)
colors=['#3678ad','#d0853a','#498966']
for D,color in zip([6,7.5,9],colors):
    a=alpha_arcsec*D*1000*AU;mu=4*np.pi**2*a**3/P**2
    RV=(2*np.pi*a/P)*np.sin(i)*(-np.sin(w)*np.sin(E)+np.sqrt(1-e*e)*np.cos(w)*np.cos(E))/(1-e*np.cos(E))/1000
    axs[0].scatter([D],[mu/GM_SUN/1e6],s=52,c=color,zorder=4)
    axs[0].annotate(f'{D:g} kpc',(D,mu/GM_SUN/1e6),xytext=(8,6),textcoords='offset points',fontsize=10,color=color)
    axs[1].plot(phase,RV,color=color,lw=2,label=f'D = {D:g} kpc')
axs[0].set(xlabel='Distance D (kpc)',ylabel='Mass / nominal solar mass (millions)',title='Same angular astrometry: mass ∝ distance³')
axs[0].text(.04,.94,'Angular scale α = 0.110 arcsec\nPeriod, shape and orientation fixed',transform=axs[0].transAxes,va='top',fontsize=10)
axs[1].set(xlabel='Time / period',ylabel='Line-of-sight velocity (km/s)',title='Spectral velocities supply a physical ruler')
axs[1].legend(frameon=False,fontsize=10);axs[1].axhline(0,color='#777',lw=.7)
for ax in axs:ax.grid(alpha=.17)
fig.suptitle('Mass and distance are degenerate until a physical velocity scale is added',fontsize=15,y=.98)
fig.text(.5,.025,'Chosen Newtonian model: P = 18 years, e = 0.70, i = 55°, ω = 35°, systemic velocity = 0. Curves are predictions, not data.',ha='center',fontsize=10)
fig.subplots_adjust(left=.075,right=.97,top=.82,bottom=.20,wspace=.27)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
