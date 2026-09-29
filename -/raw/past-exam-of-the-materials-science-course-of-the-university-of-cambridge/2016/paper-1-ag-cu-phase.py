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

fig,ax=plt.subplots(figsize=(9,6),layout="constrained")
x1=np.linspace(0,28,200);x2=np.linspace(28,100,300)
ax.plot(x1,779+181*(1-x1/28)**1.5,color="#253858",lw=2)
ax.plot(x2,779+304*((x2-28)/72)**1.5,color="#253858",lw=2)
ax.plot([0,9],[960,779],color="#007f91",lw=1.8);ax.plot([92,100],[779,1083],color="#007f91",lw=1.8)
T=np.linspace(20,779,300);xl=9*((T-20)/759)**2.2;xr=100-8*((T-20)/759)**2.2
ax.plot(xl,T,color="#8b3a82",lw=1.8);ax.plot(xr,T,color="#8b3a82",lw=1.8)
ax.hlines(779,9,92,color="#a35012",lw=1.5);ax.vlines(20,20,1120,color="#888888",ls=":",lw=1)
for x,t,txt,dx,dy in [(0,960,"Ag: 960 C",4,24),(100,1083,"Cu: 1083 C",-24,27),(9,779,"9",0,-45),(28,779,"E: 28 wt% Cu",4,-48),(92,779,"92",0,-45)]:
 ax.scatter([x],[t],s=22,color="#111111",zorder=4);ax.text(x+dx,t+dy,txt,ha="center" if txt in ["9","92"] else "left",fontsize=9)
ax.text(50,1020,"Liquid",fontsize=13);ax.text(9,865,r"$L+\alpha$",fontsize=12);ax.text(70,865,r"$L+\beta$",fontsize=12)
ax.text(49,470,r"$\alpha+\beta$",fontsize=17);ax.text(.7,565,r"$\alpha$",fontsize=13);ax.text(97.7,565,r"$\beta$",fontsize=13)
ax.text(43,790,"779 C",fontsize=10);ax.text(8,58,"Room-temperature endpoints: pure Ag and pure Cu",fontsize=9)
ax.set(xlim=(-2,102),ylim=(0,1140),xlabel="Copper mass percentage",ylabel="Temperature (degrees C)",title="Schematic Ag-Cu equilibrium diagram: supplied constraints")
ax.set_xticks([0,9,20,28,50,75,92,100]);ax.grid(alpha=.12)
finish(fig,"paper-1-ag-cu-phase.png")
