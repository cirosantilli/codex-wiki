"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
delta=.6;c=(1-delta**2)/(1+delta**2);s=2*delta/(1+delta**2)
A=np.array([[1,0],[delta,1.]])
B=np.array([[1,0],[-delta,1.]])
C=np.array([[1,-s],[delta,c]])
fig,axs=plt.subplots(1,2,figsize=(9,4),facecolor="white",layout="constrained")
for ax,axis,other,title in[(axs[0],0,B,r"$N=e_1$: $U_1$ and $U_2$"),(axs[1],1,C,r"$N=e_3$: $U_1$ and $\overline{R} U_2$")]:
 def transform(q):
  return np.where((q[:,axis]>=0)[:,None],q@A.T,q@other.T)
 halves=([np.array([[0,-1],[1,-1],[1,1],[0,1]]),np.array([[-1,-1],[0,-1],[0,1],[-1,1]])]if axis==0 else[np.array([[-1,0],[1,0],[1,1],[-1,1]]),np.array([[-1,-1],[1,-1],[1,0],[-1,0]])])
 for poly,mat,col in zip(halves,[A,other],["#d4eaf6","#fbe1ca"]):ax.add_patch(Polygon(poly@mat.T,facecolor=col,edgecolor="none"))
 ts=np.linspace(-1,1,201)
 for v in np.linspace(-1,1,9):
  for q in[np.column_stack([ts,np.full_like(ts,v)]),np.column_stack([np.full_like(ts,v),ts])]:
   z=transform(q);ax.plot(z[:,0],z[:,1],color="0.55",lw=.7)
 q=np.column_stack([np.zeros_like(ts),ts])if axis==0 else np.column_stack([ts,np.zeros_like(ts)])
 z=q@A.T;ax.plot(z[:,0],z[:,1],color="#b23c41",lw=3,label="Continuous interface")
 ax.set(aspect="equal",xlim=(-1.9,1.9),ylim=(-1.9,1.9),xlabel="$y_1$",ylabel="$y_3$",title=title)
 ax.legend(frameon=False,loc="lower right",fontsize=9)
fig.suptitle(r"Compatible deformed lattices ($\delta=0.6$); reference normals shown in titles",fontsize=11)
fig.savefig("2007-compatible-twins.png",dpi=160,facecolor="white")
