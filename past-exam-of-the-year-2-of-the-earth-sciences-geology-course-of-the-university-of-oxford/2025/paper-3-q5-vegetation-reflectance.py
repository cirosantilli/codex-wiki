"""Original qualitative healthy-leaf spectral cartoon, not laboratory data.
Python 3.14.4 / NumPy 2.3.5 / Matplotlib 3.10.7; CWD basename opaque PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def spectrum(w):
    r=.045+.075*np.exp(-((w-.55)/.045)**2)+.44/(1+np.exp(-(w-.715)/.012))
    r*=1-.25*np.exp(-((w-.97)/.035)**2)-.3*np.exp(-((w-1.2)/.06)**2)-.86*np.exp(-((w-1.45)/.09)**2)-.88*np.exp(-((w-1.94)/.14)**2)
    r*=1-.35*np.clip((w-1.3)/1.2,0,1)
    return r

def main():
    plt.rcParams.update({"font.size":10})
    w=np.linspace(.4,2.5,1600);fig,ax=plt.subplots(figsize=(9,4.2),layout="constrained")
    ax.plot(w,spectrum(w),color="#227044",lw=2.5)
    for low,high,color,label in [(.63,.68,"#cf625a","red"),(.78,.89,"#cda951","NIR")]:
        ax.axvspan(low,high,color=color,alpha=.25);ax.text((low+high)/2,.59,label,ha="center",fontsize=9)
    ax.annotate("green maximum",(.55,.12),(.42,.31),arrowprops={"arrowstyle":"->"})
    ax.annotate("red edge",(.71,.26),(.85,.26),arrowprops={"arrowstyle":"->"})
    ax.text(.88,.5,"internal leaf scattering",fontsize=9)
    for w0 in [1.45,1.94]:ax.annotate("water absorption",(w0,.07),(w0-.17,.23),fontsize=9,arrowprops={"arrowstyle":"->"})
    ax.set(xlim=(.4,2.5),ylim=(0,.64),xlabel="Wavelength / μm",ylabel="Reflectance (illustrative)",title="Healthy green vegetation: ideal qualitative spectrum, not measured data")
    ax.grid(alpha=.2);fig.savefig(Path(__file__).with_suffix(".png").name,dpi=130,facecolor="white")

if __name__=="__main__":main()
