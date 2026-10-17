"""Original normalized radial deuteron square-well model; output cwd."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
mp,mn,md,hc,b=938.272,939.565,1875.613,197.3,2.1
B=mp+mn-md;mu=mp*mn/(mp+mn);kap=np.sqrt(2*mu*B)/hc
lo,hi=np.pi/2+1e-12,np.pi-1e-12
for _ in range(80):
 x=(lo+hi)/2
 if x/np.tan(x)>-kap*b:lo=x
 else:hi=x
k=x/b;V0=B+hc**2*k*k/(2*mu)
norm=(b/2-np.sin(2*x)/(4*k)+np.sin(x)**2/(2*kap))**-.5
r=np.linspace(0,18,1500);u=np.where(r<=b,norm*np.sin(k*r),norm*np.sin(x)*np.exp(-kap*(r-b)))
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout="constrained")
axs[0].plot([0,b,b,10],[-V0,-V0,0,0],color="#174972",lw=2)
axs[0].axhline(-B,color="#a13d23",ls="--",label=rf"$E=-{B:.3f}$ MeV")
axs[0].set(xlabel="Relative separation r (fm)",ylabel="Potential / energy (MeV)",title=rf"$V_0={V0:.2f}$ MeV, $b={b:.1f}$ fm")
axs[0].legend()
axs[1].plot(r,u,color="#174972",lw=2,label=r"Normalized $u(r)$")
axs[1].axvline(b,color=".4",ls=":",label="Well boundary")
axs[1].fill_between(r,u,where=r>b,alpha=.15,color="#a13d23")
axs[1].set(xlabel="Relative separation r (fm)",ylabel=r"$u(r)$ (fm$^{-1/2}$)",title="Exponential tail outside the attraction")
axs[1].legend()
for ax in axs:ax.grid(alpha=.18)
fig.savefig("paper-1-deuteron-well.png",dpi=150,facecolor="white")
