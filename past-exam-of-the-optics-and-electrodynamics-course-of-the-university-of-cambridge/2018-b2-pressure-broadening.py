"""Original solution figure; tested with Python 3.14.

Uses the NumPy and Matplotlib dependencies in the root pyproject.toml.
Writes the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    lifetime=1e-9;delta_nu=5e9;carrier=50e9
    fig=plt.figure(figsize=(10.4,7),layout="constrained");grid=fig.add_gridspec(2,2)
    interferogram=fig.add_subplot(grid[0,:]);visibility=fig.add_subplot(grid[1,0]);spectrum=fig.add_subplot(grid[1,1])
    delay=np.linspace(-300e-12,300e-12,6000)
    envelope=np.exp(-np.abs(delay)/lifetime)*np.abs(np.cos(np.pi*delta_nu*delay))
    signal=1+np.exp(-np.abs(delay)/lifetime)*np.cos(np.pi*delta_nu*delay)*np.cos(2*np.pi*carrier*delay)
    interferogram.plot(delay*1e12,signal,color="#0068a0",lw=1)
    interferogram.plot(delay*1e12,1+envelope,color="#b55713",ls="--",lw=1)
    interferogram.plot(delay*1e12,1-envelope,color="#b55713",ls="--",lw=1)
    interferogram.axhline(1,color="#777777",lw=.6)
    interferogram.set(xlabel="Delay τ (ps)",ylabel="Intensity / constant background",title="Broadened interferogram: exponential loss of contrast, unchanged beat zeros",xlim=(-300,300),ylim=(-.04,2.04))
    interferogram.text(.015,.94,"Carrier chosen as 50 GHz for legibility",transform=interferogram.transAxes,fontsize=9,va="top")
    delay_long=np.linspace(-2.5e-9,2.5e-9,15000)
    decay=np.exp(-np.abs(delay_long)/lifetime)
    visible=decay*np.abs(np.cos(np.pi*delta_nu*delay_long))
    visibility.plot(delay_long*1e9,visible,color="#0068a0",lw=1.1)
    visibility.plot(delay_long*1e9,decay,color="#b55713",ls="--",lw=1.5,label=r"$e^{-|\tau|/(1\,\mathrm{ns})}$")
    visibility.set(xlabel="Delay τ (ns)",ylabel="Normalized visibility",title="Long-delay revivals decay",ylim=(0,1.08),xlim=(-2.5,2.5))
    visibility.legend(fontsize=9)
    freq=np.linspace(-1.5,6.5,4000);halfwidth=1/(2*np.pi*lifetime)/1e9
    lines=sum(halfwidth**2/((freq-center)**2+halfwidth**2) for center in (0,5))
    spectrum.plot(freq,lines,color="#0068a0",lw=1.6)
    spectrum.set(xlabel="Frequency relative to first line (GHz)",ylabel="Peak-normalized spectral power",title="Two intrinsic Lorentzian lines",xlim=(-1.5,6.5),ylim=(0,1.15))
    spectrum.text(.5,.87,"Line spacing 5.0 GHz\nEach FWHM = 0.318 GHz",transform=spectrum.transAxes,fontsize=9,ha="center")
    for ax in (interferogram,visibility,spectrum):ax.grid(alpha=.15)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
