"""Original qualitative LOS phase cartoons; NOT elastic-dislocation forward models.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. CWD basename opaque PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def fields(x,y):
    # Arbitrary smooth lobe plus a finite-length discontinuity; all values in phase cycles.
    envelope=np.exp(-(y/1.7)**4)
    reaching=np.exp(-((x-.45)/1.6)**2-(y/2.1)**2)*2.4+1.35*(x>0)*envelope
    blind=3.7*np.exp(-((x-.5)/1.9)**2-(y/2.4)**2)
    return reaching,blind

def main():
    plt.rcParams.update({"font.size":10})
    x=np.linspace(-4,4,701);y=np.linspace(-3.5,3.5,601);X,Y=np.meshgrid(x,y)
    surface,blind=fields(X,Y)
    fig,axes=plt.subplots(2,2,figsize=(9.2,7.1),height_ratios=(2,1),layout="constrained")
    for ax,z,title in zip(axes[0],[surface,blind],["Rupture reaches surface","Blind reverse rupture"]):
        im=ax.imshow(np.mod(z,1),extent=(-4,4,-3.5,3.5),origin="lower",vmin=0,vmax=1,cmap="twilight",aspect="equal")
        ax.set(title=title,xlabel="Across strike / arbitrary unit",ylabel="Along strike / arbitrary unit")
    axes[0,0].plot([0,0],[-1.7,1.7],"k--",lw=1.8)
    axes[0,0].annotate("fringes offset or terminate\nat the rupture trace",(0,.4),xytext=(-3.7,2.4),fontsize=8,bbox={"facecolor":"white","alpha":.9},arrowprops={"arrowstyle":"->"})
    axes[0,1].text(-3.6,-3.05,"Continuous phase across buried tip",fontsize=9,bbox={"facecolor":"white","alpha":.9})
    for ax,z,label in zip(axes[1],[surface,blind],["Discontinuous LOS profile","Smooth LOS profile"]):
        ax.plot(x,z[len(y)//2],color="#225f89",lw=2)
        ax.set(xlabel="Across strike / arbitrary unit",ylabel="Unwrapped cycles",title=label,ylim=(-.15,4.5));ax.grid(alpha=.2)
    fig.colorbar(im,ax=axes[0],label="Wrapped phase / 2π (one cycle = λ/2 LOS motion)",shrink=.8)
    fig.suptitle("Original phase cartoons; motion toward radar positive; no prescribed viewing geometry or fault inversion",fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=130,facecolor="white")

if __name__=="__main__":main()
