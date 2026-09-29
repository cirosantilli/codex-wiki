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

fig,ax=plt.subplots(figsize=(8,5.3),layout="constrained")
times=[0,2,5,7.5,13];temps=[1100,915,779,779,25]
ax.plot(times,temps,color="#253858",lw=2.4)
ax.scatter([2,5,7.5],[915,779,779],color="#a35012",s=25,zorder=4)
ax.hlines(779,0,13,color="#888888",ls=":",lw=1);ax.hlines(915,0,2,color="#888888",ls=":",lw=1)
ax.text(1,1050,"Liquid",fontsize=11);ax.text(2.9,875,"Primary Ag-rich solid + liquid",fontsize=10)
ax.text(6.25,808,"Eutectic arrest",ha="center",fontsize=11);ax.text(8.8,500,"Two solids;\ncontinued solute rejection",fontsize=10)
ax.text(2.15,940,"Liquidus onset (not numerically specified)",fontsize=9)
ax.set(xlim=(0,13.5),ylim=(0,1150),xlabel="Cooling time (schematic)",ylabel="Temperature (degrees C)",yticks=[25,779,915],yticklabels=["Room","779","Unspecified liquidus"],xticks=[],title="Original equilibrium-cooling construction: Ag-20 wt% Cu")
finish(fig,"paper-1-ag-cu-cooling.png")
