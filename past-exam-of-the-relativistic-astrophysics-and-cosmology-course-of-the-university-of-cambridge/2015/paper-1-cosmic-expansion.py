"""Original constant-fluid-pressure cosmology; basename output in cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
H0=72000/3.086e22;yr=365.25*86400;om=.3;ol=.7
t=np.linspace(.002,21,600)*1e9*yr;z=np.linspace(0,2.5,500)
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.2),layout="constrained")
for eps,color in [(0,"#285e85"),(.2,"#b65b29")]:
    n=3+eps
    scale=(om/ol)**(1/n)*np.sinh(n*H0*np.sqrt(ol)*t/2)**(2/n)
    age=2*np.arctanh(np.sqrt(ol))/(n*H0*np.sqrt(ol))
    q=((1+eps)*om*(1+z)**n/2-ol)/(om*(1+z)**n+ol)
    ztr=(2*ol/((1+eps)*om))**(1/n)-1
    label=rf"$\epsilon={eps:g}$"
    ax.plot(t/(1e9*yr),scale,color=color,lw=2,label=label+rf": $t_0={age/(1e9*yr):.2f}$ Gyr")
    ax.plot(age/(1e9*yr),1,"o",color=color)
    bx.plot(z,q,color=color,lw=2,label=label+rf": $z_{{\rm tr}}={ztr:.3f}$")
    bx.plot(ztr,0,"o",color=color)
ax.axhline(1,ls="--",color=".6");bx.axhline(0,ls="--",color=".6")
ax.set(xlabel="Time since Big Bang (Gyr)",ylabel=r"$R(t)/R_0$",title="Expansion history")
bx.set(xlabel="Redshift",ylabel=r"$q=-R\ddot R/\dot R^2$",title="Acceleration changes sign at q = 0")
for aa in (ax,bx):
    aa.grid(alpha=.2);aa.legend(fontsize=9)
fig.suptitle(r"$\Omega_{m0}=0.3,\ H_0=72\ {\rm km\,s^{-1}\,Mpc^{-1}},\ P=\epsilon\rho c^2/3$")
fig.savefig("paper-1-cosmic-expansion.png",dpi=155,facecolor="white")
