"""Original Planck wavelength spectra at illustrative temperatures.
Python3.14/NumPy2.3/Matplotlib3.10. Output PNG basename in cwd.
SI-defined exact h,c,kB are used; this is not a measured exam spectrum.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
h=6.62607015e-34;c=299792458.;kB=1.380649e-23
lam_um=np.linspace(1,48,1800);lam=lam_um*1e-6
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white"})
fig,ax=plt.subplots(figsize=(7.7,3.6),layout="constrained")
for T,color in [(300.,"#14608b"),(350.,"#b04726")]:
    M=2*np.pi*h*c*c/lam**5/np.expm1(h*c/(lam*kB*T))*1e-6
    ax.plot(lam_um,M,lw=2,color=color,label=rf"$T={T:g}\,\mathrm{{K}}$")
    imax=np.argmax(M);ax.plot(lam_um[imax],M[imax],"o",color=color,ms=4)
ax.set(xlabel=r"Wavelength $\lambda$ ($\mu$m)",ylabel=r"$M_\lambda$ (W m$^{-2}$ $\mu$m$^{-1}$)",title="Per unit wavelength: hotter curve shifts left and has greater area",xlim=(1,48),ylim=(0,None))
ax.legend(frameon=False)
fig.savefig("paper-1-ap2013-blackbody-spectra.png",dpi=140,facecolor="white",bbox_inches="tight")
