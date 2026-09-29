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

fig,axs=plt.subplots(1,3,figsize=(11,4.3),layout="constrained")
titles=["Absorption","Stimulated emission","Spontaneous emission"]
for ax,title in zip(axs,titles,strict=True):
 ax.set(xlim=(0,10),ylim=(0,10),title=title);ax.axis("off")
 ax.hlines([2,7],2,8,color="#253858",lw=2)
 ax.text(8.3,7,"2",fontsize=11,va="center");ax.text(8.3,2,"1",fontsize=11,va="center")
 ax.text(1.4,4.5,r"$\hbar\omega$",rotation=90,ha="center",va="center",fontsize=11)
for i,ax in enumerate(axs):
 if i==0:
  arrow(ax,(5,2.2),(5,6.8));ax.text(5,8.8,r"$n\to n-1$",ha="center",fontsize=13);factor=r"$\Gamma\propto n$";label="An incident photon is removed"
 else:
  arrow(ax,(5,6.8),(5,2.2))
  ax.text(5,8.8,r"$n\to n+1$" if i==1 else r"$0\to1$",ha="center",fontsize=13)
  factor=r"$\Gamma_{\rm stim}\propto n$" if i==1 else r"$\Gamma_{\rm sp}\propto1$"
  label="Occupied mode is amplified" if i==1 else "Vacuum mode can be populated"
 ax.text(5,.55,factor,ha="center",fontsize=13);ax.text(5,-.55,label,ha="center",fontsize=9)
fig.supxlabel(r"Total emission into one mode has occupation factor $n+1$; diagrams do not assert isotropic emission",fontsize=10)
finish(fig,"paper-1-emission.png")
