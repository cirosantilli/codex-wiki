"""Original analytic illustration. Tested with Python 3.14, NumPy and Matplotlib.
Run from the intended output directory; the PNG is written to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig=plt.figure(figsize=(10,6.8),layout="constrained")
gs=fig.add_gridspec(2,3,height_ratios=(1.4,1))
ax=fig.add_subplot(gs[0,:])
u=np.linspace(-1.1,3.7,1501); D=1.; alpha=1.
ax.plot(u,u*u,color="#567a9c",label=r"Harmonic: $V/D_e=u^2$")
ax.plot(u,(1-np.exp(-u))**2,color="#b7492a",label=r"Morse: $V/D_e=(1-e^{-u})^2$")
ax.axhline(1,color=".4",ls="--",lw=1)
ax.text(3.4,1.025,r"$D_e$",ha="right")
# Dimensionless illustrative hbar*omega/D = 0.24; x_e = 0.06.
w=.24; xe=.06
for v in range(3):
 eh=w*(v+.5); em=w*((v+.5)-xe*(v+.5)**2)
 width=np.sqrt(eh)
 ax.plot([-width,width],[eh,eh],color="#567a9c",alpha=.65)
 left=-np.log(1+np.sqrt(em)); right=-np.log(1-np.sqrt(em))
 ax.plot([left,right],[em,em],color="#b7492a",ls=":",lw=2)
ax.set(xlim=(-1.1,3.7),ylim=(0,1.4),xlabel=r"Displacement $u=\alpha(r-r_e)$",ylabel=r"Potential / $D_e$",title="Equal local curvature; minimum at u = 0")
ax.legend(frameon=False,loc="upper right")
q=np.linspace(-3.5,3.5,1201); g=np.pi**(-.25)*np.exp(-q*q/2)
phis=[g,np.sqrt(2)*q*g,(2*q*q-1)*g/np.sqrt(2)]
for v,phi in enumerate(phis):
 a=fig.add_subplot(gs[1,v]);a.axhline(0,color=".6",lw=.7);a.plot(q,phi,color="#173e62",lw=2)
 a.set(xlabel="Reduced coordinate q",title=f"v = {v}; {v} node"+("s" if v!=1 else ""),ylim=(-.85,.85),xlim=(-3.5,3.5))
 if v==0:a.set_ylabel("Normalized wavefunction")
fig.savefig("paper-2b-vibrational-models.png",dpi=165)
plt.close(fig)
