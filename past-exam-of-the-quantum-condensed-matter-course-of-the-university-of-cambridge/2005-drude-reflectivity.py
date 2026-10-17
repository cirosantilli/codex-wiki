"""Original Drude curves, not a tracing or digitization of exam data."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

EPS_B=16.0
LIGHT_SPEED=299792458.0
LAMBDA_MIN=22e-6
TAU=0.3e-12  # illustrative damping, not fitted
OMEGA_P2=(EPS_B-1)*(2*np.pi*LIGHT_SPEED/LAMBDA_MIN)**2

def epsilon(wavelength_m,tau=np.inf):
    omega=2*np.pi*LIGHT_SPEED/wavelength_m
    return EPS_B-OMEGA_P2/(omega*(omega+1j/tau))
def reflectivity(wavelength_m,tau=np.inf):
    index=np.sqrt(epsilon(wavelength_m,tau)+0j)
    return abs((index-1)/(index+1))**2

if __name__=="__main__":
    lam=np.linspace(2,40,3000)
    edge=LAMBDA_MIN*np.sqrt(EPS_B/(EPS_B-1))*1e6
    fig,axes=plt.subplots(1,2,figsize=(9.5,4.0),layout="constrained")
    axes[0].plot(lam,reflectivity(lam*1e-6),color="#888888",ls="--",lw=1.5,label="Lossless model")
    axes[0].plot(lam,reflectivity(lam*1e-6,TAU),color="#286e9b",lw=2,label="Illustrative 0.3 ps scattering time")
    axes[0].axhline(0.36,color="#a95429",ls=":",lw=1.2,label="Background reflectance 0.36")
    axes[0].set(xlabel="Wavelength (µm)",ylabel="Reflectivity",xlim=(2,40),ylim=(-.02,1.04),title="A minimum separates dielectric and metallic response")
    axes[0].legend(loc="upper left",fontsize=8)
    zoom=np.linspace(20.5,24,700)
    axes[1].plot(zoom,epsilon(zoom*1e-6).real,color="#286e9b",lw=2)
    axes[1].axhline(1,color="#b15c2d",ls="--",lw=1)
    axes[1].axhline(0,color="#777777",lw=1)
    axes[1].scatter([22,edge],[1,0],color=["#b15c2d","#555555"],zorder=4)
    axes[1].annotate("Reflectivity minimum\nε = 1",(22,1),(20.6,2.1),arrowprops={"arrowstyle":"->"},fontsize=10)
    axes[1].annotate("Plasma edge\nε = 0",(edge,0),(22.8,1.3),arrowprops={"arrowstyle":"->"},fontsize=10)
    axes[1].set(xlabel="Wavelength (µm)",ylabel="Lossless relative dielectric function",xlim=(20.5,24),ylim=(-2.5,3),title="Index matching and the plasma zero differ")
    for ax in axes:ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
    plt.close(fig)
