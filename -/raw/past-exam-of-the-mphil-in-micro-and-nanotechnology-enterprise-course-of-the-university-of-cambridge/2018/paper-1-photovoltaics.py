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

fig,axs=plt.subplots(1,2,figsize=(9,4.8),layout="constrained")
ax=axs[0];V=np.linspace(-.15,1.14,700);a=.16;I0=1/np.expm1(1/a);dark=I0*np.expm1(V/a);light=dark-1
ax.plot(V,dark,label="Dark",color="#253858");ax.plot(V,light,label="Illuminated",color="#007f91")
vv=np.linspace(0,1,10001);ii=I0*np.expm1(vv/a)-1;j=np.argmax(-vv*ii);vm=vv[j];im=ii[j]
ax.add_patch(Rectangle((0,im),vm,-im,fc="#e9c37c",alpha=.45,ec="#a35012",label="Maximum-power rectangle"));ax.scatter([vm],[im],color="#a35012")
ax.axhline(0,color="black",lw=.8);ax.axvline(0,color="black",lw=.8)
ax.set(xlim=(-.15,1.14),ylim=(-1.2,1.5),xlabel=r"$V/V_{oc}$",ylabel=r"$I/I_{sc}$ (current into cell)",title="Illustrative ideal diode curves")
ax.legend(fontsize=8,loc="upper left");ax.grid(alpha=.15)
ax=axs[1];ax.set(xlim=(0,10),ylim=(0,10),title="Series multijunction stack");ax.axis("off")
arrow(ax,(5,9.6),(5,8.6));ax.text(5,9.8,"Incident light",ha="center",fontsize=10)
for y,t,fc in [(6.6,"TOP: InGaAlP, 1.88 eV\nBelow about 660 nm","#f4d58b"),(4.1,"MIDDLE: InGaAs, 1.40 eV\nAbout 660–886 nm","#e8aa7d"),(1.6,"BOTTOM: Ge, 0.67 eV\nAbout 886–1850 nm","#a2c5d6")]:box(ax,1,y,8,1.8,t,fc=fc,size=10)
for y in [6.6,4.1]:arrow(ax,(5,y),(5,y-.6))
ax.text(5,.5,"Ideal spectral allocation, not equal photocurrents",ha="center",fontsize=9)
finish(fig,"paper-1-photovoltaics.png")
