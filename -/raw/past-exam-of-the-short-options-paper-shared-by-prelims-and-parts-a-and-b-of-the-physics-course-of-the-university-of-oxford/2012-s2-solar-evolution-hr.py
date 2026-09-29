"""Schematic solar-mass H-R track; positions are illustrative, not model data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size":12,"figure.facecolor":"white","axes.facecolor":"white"})
    fig,ax=plt.subplots(figsize=(9,5),layout="constrained")
    ax.loglog([3000,4000,5772,10000,30000],[.02,.15,1,30,1e4],color=".6",lw=8,alpha=.5,label="main sequence (schematic)")
    temp=np.array([5772,5500,4500,3500,5000,3300,90000,100000,35000,15000]);lum=np.array([1,2,20,1800,50,5000,5000,10,.04,.003])
    ax.loglog(temp,lum,color="#D55E00",lw=1.8,label="solar-mass evolutionary path")
    for j in range(len(temp)-1):
        mid=np.sqrt(temp[j:j+2].prod());lmid=np.sqrt(lum[j:j+2].prod());a=np.array([temp[j],lum[j]]);b=np.array([temp[j+1],lum[j+1]])
        ax.annotate("",b**.55*a**.45,b**.45*a**.55,arrowprops={"arrowstyle":"->","color":"#D55E00","lw":1.5})
    ax.scatter([5772],[1],color="black",s=30,zorder=5)
    notes=[("Sun: core H fusion",(5772,1),(13000,.7)),("Red giant: H shell",(3500,1800),(16000,1800)),("Red clump: core He + H shell",(5000,50),(30000,100)),("AGB: H and He shells",(3300,5000),(15000,9500)),("Hot exposed core",(90000,5000),(105000,1300)),("White dwarf: cooling",(35000,.04),(100000,.002))]
    for text,xy,where in notes:ax.annotate(text,xy,where,arrowprops={"arrowstyle":"-","color":".3"},fontsize=10)
    ax.set(xlim=(120000,2500),ylim=(1e-4,2e4),xlabel=r"effective temperature $T_{\rm eff}$ [K], hotter to the left",ylabel=r"luminosity $L/L_\odot$",title="Solar-mass evolution and its changing energy source (schematic)");ax.legend(loc="lower right",fontsize=9);ax.grid(alpha=.18)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
