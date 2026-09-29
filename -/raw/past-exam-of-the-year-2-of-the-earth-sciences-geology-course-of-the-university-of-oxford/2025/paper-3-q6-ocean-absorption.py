"""Original ocean-optics sketches. Synthetic qualitative shapes, not measured spectra.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7. CWD basename opaque PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def spectra(w):
    ph=.08+.95*np.exp(-((w-440)/27)**2)+.48*np.exp(-((w-675)/15)**2)+.12*np.exp(-((w-490)/36)**2)
    cdom=np.exp(-.018*(w-400));nap=.7*np.exp(-.011*(w-400))
    # Illustrative effective attenuation: water removes red; particles/pigments remove blue.
    water=.016+.0000008*(w-450)**2+.18/(1+np.exp(-(w-605)/24))
    low=water+.007*ph+.002*cdom
    high=water+.13*ph+.09*cdom+.04*nap
    return ph,cdom,nap,low,high

def main():
    plt.rcParams.update({"font.size":10})
    w=np.linspace(400,700,1201);ph,cdom,nap,low,high=spectra(w)
    fig,axes=plt.subplots(1,2,figsize=(11.2,4.5),layout="constrained")
    ax=axes[0]
    for a,label,c in [(ph,"Phytoplankton pigments","#227044"),(cdom,"CDOM","#874d9e"),(nap,"Non-algal particles","#b86b29")]:ax.plot(w,a,label=label,color=c,lw=2)
    ax.set(xlabel="Wavelength / nm",ylabel="Absorption / arbitrary unit",xlim=(400,700),ylim=(0,1.3),title="Non-water absorbers: qualitative shapes")
    ax.legend(fontsize=9);ax.grid(alpha=.2)
    ax=axes[1]
    # Different illustrative depths; normalize spectra to compare spectral shape only.
    for k,z,label,c in [(low,100,"Low chlorophyll: blue-rich","#225f89"),(high,30,"High chlorophyll: greener","#227044")]:
        e=np.exp(-k*z);ax.plot(w,e/e.max(),label=label,color=c,lw=2)
    ax.set(xlabel="Wavelength / nm",ylabel="Normalized deep irradiance",xlim=(400,700),ylim=(0,1.15),title="Spectral filtering near the photic-zone base")
    ax.legend(fontsize=9);ax.grid(alpha=.2)
    fig.suptitle("Synthetic illustrative curves; amplitudes and depths are not observations or a calibrated water model",fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=130,facecolor="white")

if __name__=="__main__":main()
