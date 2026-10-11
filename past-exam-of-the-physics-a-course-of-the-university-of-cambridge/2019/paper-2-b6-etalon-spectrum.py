"""Original solution figure; tested with Python 3.14.

Uses NumPy and Matplotlib as declared in the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    R=.99;d=476*589e-9/2;c=299792458.
    coeff=4*R/(1-R)**2;fsr=c/(2*d)
    wavelength_nm=np.linspace(588.8,590.4,50000);lam=wavelength_nm*1e-9
    bare=1/(1+coeff*np.sin(2*np.pi*d/lam)**2)
    scan=sum(1/(1+coeff*np.sin(np.pi*(c/lam-c/line)/fsr)**2) for line in (589e-9,589.6e-9))
    fig,(ax,scanned)=plt.subplots(1,2,figsize=(11,4.2),layout="constrained")
    ax.plot(wavelength_nm,bare,color="#0068a0",lw=1.5)
    scanned.plot(wavelength_nm,scan,color="#b55713",lw=1.5)
    for a in (ax,scanned):
        a.set(xlabel="Wavelength (nm)",xlim=(588.8,590.4),ylim=(0,1.1));a.grid(alpha=.16)
    ax.set(ylabel="Fixed-etalon intensity transmission",title="Transmission comb of one fixed gap")
    ax.text(.04,.91,"R = 0.99; d = 0.14018 mm\nFinesse ≈ 313; FSR ≈ 1.24 nm",transform=ax.transAxes,fontsize=9,va="top")
    scanned.set(ylabel="Normalized detected scan signal",title="Two input lines in a calibrated etalon scan")
    for center in (589.,589.6):
        scanned.annotate(f"{center:.1f} nm",xy=(center,1),xytext=(center+.1,.76),fontsize=9,
                         arrowprops={"arrowstyle":"->","color":"#555555"})
    scanned.text(.04,.15,"Equal narrow input lines\nInstrumental FWHM ≈ 0.0040 nm",transform=scanned.transAxes,fontsize=9)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
