"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Write the same-basename PNG to the current working directory for Make.
No source image or source data file is read.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Arc
import numpy as np

def box(ax,x,y,w,h,text,fc="#e5edf5",size=9):
    ax.add_patch(Rectangle((x,y),w,h,fc=fc,ec="#253858",lw=1.2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=size)

def arrow(ax,a,b,text=None):
    ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=1.3,color="#253858"))
    if text:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2,text,fontsize=8,ha="center",va="bottom")

def finish(fig,name):
    fig.set_facecolor("white")
    fig.savefig(name,dpi=150,facecolor="white",bbox_inches="tight")
    plt.close(fig)

fig,axs=plt.subplots(2,2,figsize=(9,6),layout="constrained")
for col,w in enumerate([10.,100.]):
    x=np.linspace(-w, w, 901);depth=8.;true=-depth*np.maximum(1-np.abs(x)/(w/2),0)
    # Nonpenetration envelope for a parabolic tip of illustrative radius10nm.
    observed=np.max(true[None,:]-(x[:,None]-x[None,:])**2/(2*10.),axis=1)
    # A first-order lag is a transparent illustrative controller, not an instrument fit.
    recorded=np.empty_like(x);recorded[0]=observed[0];lag_length=0.4
    step=x[1]-x[0];alpha=1-np.exp(-step/lag_length)
    for j in range(1,len(x)):recorded[j]=recorded[j-1]+alpha*(observed[j]-recorded[j-1])
    error=(recorded-observed)/2
    axs[0,col].plot(x,true,"--",color="#999999",label="True depression")
    axs[0,col].plot(x,recorded,color="#007f91",label="Recorded height")
    axs[0,col].set(title=f"Opening width {w:g} nm",ylabel="Height (nm)",ylim=(-9,1));axs[0,col].legend(fontsize=8)
    axs[1,col].plot(x,error,color="#a35012");axs[1,col].axhline(0,color="#999999",lw=.8)
    axs[1,col].set(xlabel="Scan position (nm), left to right",ylabel="Amplitude minus setpoint\n(illustrative units)")
    for row in axs:row[col].grid(alpha=.2)
fig.suptitle("Illustrative depth 8 nm, tip radius 10 nm; geometry and feedback are separate")
finish(fig,"paper-1-tapping-response.png")
