"""Original BCS zero-temperature electron occupations; no measured material data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def occ(x):return .5*(1-x/np.sqrt(x*x+1))
fig,axs=plt.subplots(1,2,figsize=(11,4.7),dpi=100,facecolor="white")
k=np.linspace(0,1.8,1201);ratio=.1;n=occ((k*k-1)/ratio)
axs[0].plot(k,n,lw=2.5,label="BCS electron occupation")
axs[0].plot(k,(k<1).astype(float),ls="--",color="0.4",label="Normal Fermi step")
axs[0].plot(k,np.zeros_like(k),ls=":",color="#a74935",lw=2,label="Quasiparticle occupation")
axs[0].fill_between(k,n,where=k>=1,color="#95bad2",alpha=.6)
axs[0].set(xlabel=r"$k/k_F$",ylabel="Occupation per spin state",xlim=(0,1.8),ylim=(-.04,1.08),title=r"Parabolic band, illustrative $\Delta/\mu=0.1$")
axs[0].legend(loc="lower left",fontsize=9)
x=np.linspace(-8,8,1601);n=occ(x)
axs[1].plot(x,n,lw=2.5);axs[1].fill_between(x,n,where=x>=0,color="#95bad2",alpha=.6)
axs[1].axvline(0,color="0.5",ls="--",lw=1)
axs[1].text(.97,.9,r"$\int_0^\infty n(\xi)\,d\xi=\Delta/2$",ha="right",transform=axs[1].transAxes,fontsize=12)
axs[1].set(xlabel=r"$\xi/\Delta$",ylabel=r"$n_{\mathbf{k}\sigma}$",xlim=(-8,8),ylim=(-.04,1.08),title="Pairing broadens the electron occupation")
for ax in axs:ax.grid(alpha=.2)
fig.suptitle("A quasiparticle vacuum need not be a sharp electron Fermi sea",fontsize=14,y=.98)
fig.text(.5,.025,"Original uniform isotropic BCS model at zero temperature; shaded electron population lies above the normal Fermi surface.",ha="center",fontsize=10)
fig.subplots_adjust(left=.065,right=.98,top=.81,bottom=.18,wspace=.22)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,facecolor="white")
