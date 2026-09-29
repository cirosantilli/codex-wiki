"""Original local fluid-disk stability plots. Python 3.14, NumPy/Matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
fig,(wave,radial)=plt.subplots(1,2,figsize=(9.2,3.8),layout="constrained")
colors=["#1767a2","#b66b26","#32794a"]
q=np.linspace(0,9,700)
for Q,col in zip([.65,1.,1.4],colors):
    wave.plot(q,1-q+Q*Q*q*q/4,color=col,label=fr"$Q={Q:g}$")
wave.axhspan(-1.6,0,color="#e7eff5")
wave.axhline(0,color=".3",lw=.8)
wave.text(4.2,-1.52,"exponential growth",fontsize=9)
wave.set(xlim=(0,9),ylim=(-1.6,3.5),xlabel=r"$q=|k|/k_T$",
         ylabel=r"$\omega^2/\kappa^2$",title="Axisymmetric dispersion")
wave.legend(frameon=False,fontsize=9)
wave.grid(alpha=.15)
x=np.linspace(.055,5,900)
for Q0,col in zip([.65,1.,1.4],colors):
    radial.plot(x,Q0*np.exp(x-1)/x,color=col,label=fr"$Q_0={Q0:g}$")
    radial.plot(1,Q0,"o",color=col,ms=4)
unstable=.65*np.exp(x-1)/x<1
radial.fill_between(x,.65*np.exp(x-1)/x,1,where=unstable,
                    color="#e7eff5")
radial.axhline(1,color=".3",ls="--",lw=.8)
radial.axvline(1,color=".5",ls=":",lw=.8)
radial.text(1.35,.22,"unstable annulus for "+r"$Q_0<1$",fontsize=9)
radial.set(xlim=(0,5),ylim=(0,3.5),xlabel=r"$x=r/r_0$",
           ylabel=r"$Q(x)$",title="Flat rotation + exponential density")
radial.legend(frameon=False,fontsize=9)
radial.grid(alpha=.15)
fig.savefig("paper-1-disk-stability.png",dpi=155,facecolor="white")
