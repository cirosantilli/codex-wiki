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

fig,ax=plt.subplots(figsize=(7.5,3.8),layout="constrained");ax.set(xlim=(0,10),ylim=(0,5));ax.axis("off")
for x,y in [([1,1],[.8,1.75]),([1,1],[2.85,3.6]),([1,4],[3.6,3.6]),([5.5,8],[3.6,3.6]),([8,8],[2.9,3.6]),([8,8],[.8,1.7]),([1,8],[.8,.8])]:
    ax.plot(x,y,color="#253858",lw=1.7)
ax.add_patch(Circle((1,2.3),.55,fc="white",ec="#253858",lw=1.5));ax.text(1,2.53,"+",ha="center");ax.text(1,2.03,"−",ha="center")
ax.text(2,2.3,r"$V_{oc}=S_{eff}\Delta T$",va="center",fontsize=12)
box(ax,4,3.25,1.5,.7,"R",fc="white",size=12)
ax.add_patch(Rectangle((7.65,1.7),.7,1.2,fc="white",ec="#253858",lw=1.4));ax.text(8.7,2.3,r"$R_L$",va="center",fontsize=12)
arrow(ax,(6,4.3),(7.5,4.3));ax.text(6.7,4.5,"I",ha="center")
ax.text(4.75,2.7,"Internal resistance",ha="center",fontsize=10);ax.text(8.7,1.7,"Load",fontsize=10)
ax.text(4.8,.1,"Fixed hot/cold temperatures sustain the source",ha="center",fontsize=11)
finish(fig,"paper-1-teg-circuit.png")
