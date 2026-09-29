"""Original explanatory diagram; Python 3.14, numpy, matplotlib.
Outputs its basename PNG to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
x=np.linspace(-1,1,501);X,Y=np.meshgrid(x,x);r2=X*X+Y*Y;valid=r2<=1
# Equal-area map of the lower hemisphere: center is downward takeoff.
factor=np.sqrt(np.maximum(0,2-r2));N=np.stack([X*factor,Y*factor,-(1-r2)],axis=-1)
matrices=[np.array([[0,1,0],[1,0,0],[0,0,0]]),np.diag([1,0,-1]),np.diag([-1,0,1])]
fig,axs=plt.subplots(1,3,figsize=(10,3.6),layout="constrained")
for ax,M,label in zip(axs,matrices,["Strike slip","Normal fault","Reverse fault"]):
 amp=np.einsum("...i,ij,...j->...",N,M,N);amp=np.ma.masked_where(~valid,amp)
 ax.contourf(X,Y,amp,levels=[-3,0,3],colors=["white","#333333"]);ax.contour(X,Y,amp,levels=[0],colors="#777777",linewidths=.7)
 ax.add_patch(plt.Circle((0,0),1,fill=False,color="#333333",lw=1));ax.set(xlim=(-1.05,1.05),ylim=(-1.05,1.05),title=label);ax.set_aspect("equal");ax.axis("off")
fig.suptitle("Original ideal P-radiation patterns: dark = positive outward amplitude, white = negative")
fig.savefig("paper-1-focal-mechanisms.png",dpi=155,facecolor="white")
