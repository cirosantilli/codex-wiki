"""Idealized convective tracks. Python 3.14; root NumPy/Matplotlib dependencies.
Output is a basename PNG in cwd; caller owns MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def main():
    mu1=1/(2*.7+3*.28/4+.02/2)
    mu2=1/(2*.8+3*.18/4+.02/2)
    radius=np.geomspace(3,.45,180)
    fig,ax=plt.subplots(figsize=(10,6.4),dpi=100,facecolor="white")
    for mu,label,color in [(mu1,r"$X=0.7,\ \mu=0.617$","#ad4b00"),(mu2,r"$X=0.8,\ \mu=0.573$","#12679f")]:
        temp=(mu/mu1)**.5*radius**.125
        lum=(mu/mu1)**2*radius**2.5
        xx=np.log10(temp);yy=np.log10(lum)
        ax.plot(xx,yy,color=color,lw=3,label=label)
        a,b=65,103
        ax.annotate("",xy=(xx[b],yy[b]),xytext=(xx[a],yy[a]),arrowprops=dict(arrowstyle="-|>",color=color,lw=2.5,mutation_scale=21))
    ax.set_xlim(.28,-.28);ax.set_ylim(-1.2,1.5)
    ax.set_xlabel(r"$\log_{10}(T_{\rm eff}/T_*)$   (hotter to the left)",fontsize=14)
    ax.set_ylabel(r"$\log_{10}(L/L_*)$",fontsize=14)
    ax.set_title("Composition shift of idealized pre-main-sequence tracks",fontsize=17,pad=14)
    ax.legend(loc="upper right",fontsize=13,framealpha=1)
    ax.text(.04,.065,"Arrows: contraction and increasing time\nHigher mean molecular weight: hotter at fixed luminosity",fontsize=12,va="bottom",transform=ax.transAxes)
    ax.grid(alpha=.2);ax.tick_params(labelsize=12)
    fig.text(.5,.025,r"Fixed mass, $Z=0.02$, common opacity coefficient; $\kappa\propto\rho T^4$ and $L\propto T_{\rm eff}^{20}\mu^{-8}$",ha="center",fontsize=11)
    fig.tight_layout(rect=(0,.06,1,1))
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
    plt.close(fig)
if __name__=="__main__":main()
