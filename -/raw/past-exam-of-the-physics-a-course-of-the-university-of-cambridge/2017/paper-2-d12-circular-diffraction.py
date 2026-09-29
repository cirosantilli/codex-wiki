"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
# Integrate the angular representation of J0 and the radial diffraction integral.
# This avoids adding SciPy to the documented project dependencies.
g,w=np.polynomial.legendre.leggauss(180);r=(g+1)/2;rw=w/2
ag,aw=np.polynomial.legendre.leggauss(110);phi=np.pi*(ag+1)/2;aw=aw/2

def j0(x):
 return np.cos(x[...,None]*np.cos(phi))@aw

def circular(rho,N):
 out=np.empty(rho.size,dtype=complex)
 for start in range(0,rho.size,60):
  s=rho[start:start+60]
  J=j0(2*np.pi*N*s[:,None]*r[None,:])
  out[start:start+60]=2*np.pi*N/1j*np.exp(1j*np.pi*N*s*s)*(J@(rw*r*np.exp(1j*np.pi*N*r*r)))
 return out

fig,ax=plt.subplots(1,3,figsize=(10.6,3.8),layout="constrained")
u=np.linspace(0,16,1200);airy=2*j0(u[:,None]*r[None,:])@(rw*r)
ax[0].semilogy(u,airy**2,color="#1565a8",lw=1.7)
ax[0].axvline(3.8317,color=".5",ls=":",lw=1)
ax[0].text(4.1,.25,"first zero\n3.8317",fontsize=9)
ax[0].set(xlim=(0,16),ylim=(1e-5,1.2),xlabel=r"$ka\sin\theta$",ylabel=r"$I/I(0)$",title="Fraunhofer circular aperture")
rho=np.linspace(0,3,700)
for N,col in [(.5,"#ca6720"),(3.,"#1565a8")]:
 U=circular(rho,N)
 ax[1].plot(rho,abs(U)**2,color=col,lw=1.5,label=f"N_F = {N:g}")
 ax[2].plot(rho,abs(1-U)**2,color=col,lw=1.5,label=f"N_F = {N:g}")
for a,title in zip(ax[1:],["Fresnel circular aperture","Fresnel complementary opaque disk"]):
 a.axvline(1,color=".6",ls=":",lw=1)
 a.set(xlim=(0,3),xlabel=r"Screen radius $\rho/a$",ylabel=r"$I/I_0$",title=title)
 a.legend(frameon=False,fontsize=8)
ax[1].set_ylim(0,4.3);ax[2].set_ylim(0,1.9)
ax[2].scatter([0],[1],color="black",s=15,zorder=5)
ax[2].annotate("axial spot: I = I₀",xy=(0,1),xytext=(.6,1.65),arrowprops={"arrowstyle":"->"},fontsize=9)
for a in ax:a.grid(alpha=.13)
fig.suptitle("Scalar paraxial plane-wave model; vertical dotted lines in Fresnel panels mark ρ = a")
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
