"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. Output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.linspace(-.7,4.7,1200)
v=sum(c*np.maximum(x-j,0)**3 for j,c in enumerate([1,-4,6,-4,1]))/6
v[(x<0)|(x>4)]=0
fig,ax=plt.subplots(figsize=(7,3.7),facecolor="white")
ax.plot(x,v,lw=2.4)
ax.scatter([0,1,2,3,4],[0,1/6,2/3,1/6,0],color="C1",zorder=4)
for j,value in [(1,"1/6"),(2,"2/3"),(3,"1/6")]:ax.text(j+.08,[0,1/6,2/3,1/6][j]+.015,value)
for j in range(5):ax.axvline(j,color=".85",lw=.7,zorder=0)
ax.set(xlabel="x",ylabel=r"$\phi(x)$",title="Cubic cardinal spline: knot values sum to one",xlim=(-.7,4.7),ylim=(-.03,.77),xticks=range(5))
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2009-cardinal-cubic.png",dpi=150,facecolor="white")
