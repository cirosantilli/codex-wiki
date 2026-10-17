"""Original explanatory diagram; Python 3.14, numpy, matplotlib.
Outputs its basename PNG to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
x=np.linspace(-95,105,1000);y=np.linspace(-65,110,900);X,Y=np.meshgrid(x,y);age=np.full(X.shape,np.nan)
A=(X>=0)&(Y>=0);B=(X>=0)&(Y<=0)&(Y>=-5*X/12);C=(X<=0)&(Y>=-5*X/12)
age[A]=np.minimum(X[A]/24,Y[A]/10);age[B]=-Y[B]/10;age[C]=-X[C]/24
polarity=np.ma.masked_invalid(np.floor(age)%2);cmap=ListedColormap(["#d4e7f3","#e9c8a9"]);cmap.set_bad("#eeeeee")
fig,ax=plt.subplots(figsize=(8.3,6),layout="constrained");ax.pcolormesh(X,Y,polarity,cmap=cmap,vmin=0,vmax=1,shading="nearest",rasterized=True)
ax.plot([0,105],[0,0],color="#ad3232",lw=2);ax.plot([0,0],[0,110],color="#ad3232",lw=2);ax.plot([0,105],[0,-5*105/12],"k",lw=2)
ax.text(65,65,"A",fontsize=15);ax.text(80,-13,"B",fontsize=15);ax.text(-70,80,"C",fontsize=15)
ax.text(40,4,"AB ridge: 10 km/Myr each side",fontsize=8,color="#8d2020")
ax.text(-4,25,"AC ridge: 24 km/Myr each side",rotation=90,ha="right",fontsize=9,color="#8d2020")
ax.text(30,-24,"BC transform: no crust creation",rotation=-22.62,fontsize=8)
ax.text(-85,-45,"Inherited C crust:\nprior history not supplied",fontsize=10)
ax.annotate("matched age bands\njoin as corners in A",xy=(48,20),xytext=(50,95),arrowprops=dict(arrowstyle="->"),fontsize=10)
ax.plot(0,0,"ko",ms=5);ax.annotate("moving junction",xy=(0,0),xytext=(-5,-58),arrowprops=dict(arrowstyle="->"),fontsize=10)
ax.legend(handles=[Patch(color="#d4e7f3",label="one polarity"),Patch(color="#e9c8a9",label="opposite polarity"),Patch(color="#eeeeee",label="unassigned history")],fontsize=9,loc="lower right")
ax.set(xlabel="Junction-frame x / km",ylabel="Junction-frame y / km",title="Original conditional crustal polarity pattern; arbitrary 1-Myr equal intervals");ax.set_aspect("equal")
fig.savefig("paper-1-magnetic-stripes.png",dpi=150,facecolor="white")
