"""Exact balanced PCA counterexample; constructed rates, not recordings.
Python 3.14; NumPy and Matplotlib from repository pyproject.toml.
Writes same-basename opaque white PNG to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
fig,axes=plt.subplots(1,2,figsize=(10,3.9),layout="constrained",facecolor="white")
for S,col,marker in [(-1,"#245b83","o"),(1,"#bf5422","+")]:
 rates=np.array([[20+10*W,5+S]for W in [-1,1]])
 axes[0].scatter(rates[:,0],rates[:,1],s=110,c=col,marker=marker,linewidths=2,label=f"Label S = {S:+d}")
 axes[1].scatter(rates[:,0]-20,np.zeros(2),s=180 if S==-1 else 100,facecolors="none" if S==-1 else col,edgecolors=col,marker=marker,linewidths=2,label=f"S = {S:+d}")
axes[0].set(xlim=(6,34),ylim=(3,7),xticks=[10,20,30],yticks=[4,5,6],xlabel="Neuron 1 mean rate",ylabel="Neuron 2 mean rate",title="Class information lies vertically")
axes[0].legend(frameon=False,loc="center",fontsize=10)
axes[1].set(xlim=(-14,14),ylim=(-.9,.9),xticks=[-10,0,10],yticks=[],xlabel="First principal-component score",title="PC1 retains 100/101 = 99.01% variance")
axes[1].axhline(0,color="#aaaaaa",lw=1,zorder=-1)
axes[1].text(0,.60,"Both labels overlap at each score",ha="center",fontsize=11)
axes[1].text(0,-.65,"Best expected accuracy from PC1: 1/2",ha="center",fontsize=11,weight="bold")
fig.suptitle("Constructed positive rates: (20 + 10W, 5 + S); independent balanced signs W and S",fontsize=12)
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
