"""Radiative Roche-model cross-section. Python 3.14; root NumPy/Matplotlib deps.
Basename PNG in cwd; respects caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
def surface(theta,q=.27):
    low=np.ones_like(theta);high=np.full_like(theta,1.5)
    for _ in range(60):
        mid=(low+high)/2
        positive=1/mid+.5*q*mid**2*np.sin(theta)**2>1
        low=np.where(positive,mid,low);high=np.where(positive,high,mid)
    radius=(low+high)/2
    x=radius*np.sin(theta);z=radius*np.cos(theta)
    g=np.hypot(x/radius**3-q*x,z/radius**3)
    return x,z,g
def main():
    theta=np.linspace(0,2*np.pi,1201)
    x,z,g=surface(theta)
    pts=np.column_stack([x,z]);segments=np.stack([pts[:-1],pts[1:]],axis=1)
    values=((g[:-1]+g[1:])/2)**.25
    fig,ax=plt.subplots(figsize=(10,6.4),dpi=100,facecolor="white")
    ax.fill(x,z,color="#f1f1f1",zorder=1)
    lc=LineCollection(segments,array=values,cmap="viridis",linewidth=8,clim=(values.min(),1))
    ax.add_collection(lc)
    ax.plot([0,0],[-1.36,1.36],"--",color="#555555",lw=1.4,zorder=0)
    ax.annotate("Hottest pole",xy=(0,1),xytext=(-1.58,1.25),fontsize=14,arrowprops=dict(arrowstyle="->",lw=1.4))
    ax.annotate("Hottest pole",xy=(0,-1),xytext=(-1.58,-1.29),fontsize=14,arrowprops=dict(arrowstyle="->",lw=1.4))
    ax.annotate("Cooler equator",xy=(x[300],0),xytext=(.75,.7),fontsize=14,arrowprops=dict(arrowstyle="->",lw=1.4))
    ax.text(.05,1.42,"rotation axis",fontsize=11)
    ax.text(0,0,"Oblate star",ha="center",fontsize=15)
    ax.set_aspect("equal");ax.set_xlim(-1.85,1.9);ax.set_ylim(-1.55,1.62);ax.axis("off")
    ax.set_title("Rapid rotation and radiative gravity darkening",fontsize=17,pad=14)
    cb=fig.colorbar(lc,ax=ax,shrink=.75,pad=.025)
    cb.set_label(r"Surface $T_{\rm eff}/T_{\rm pole}=(g/g_{\rm pole})^{1/4}$",fontsize=13)
    cb.ax.tick_params(labelsize=11)
    fig.text(.5,.03,r"Illustrative Roche surface: $\Omega^2R_{\rm pole}^3/(GM)=0.27$. Colour shows effective surface temperature only.",ha="center",fontsize=11)
    fig.tight_layout(rect=(0,.07,1,1))
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
    plt.close(fig)
if __name__=="__main__":main()
