"""Hypothetical binary classification example, not experimental observations.
Python 3.14; NumPy and Matplotlib from the repository pyproject.toml.
Writes the same-basename opaque white PNG into the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, ax=plt.subplots(1,2,figsize=(10.2,3.9),layout="constrained",facecolor="white")
p=np.linspace(0,1,501);s=.8;f=.2;ppv=s*p/(s*p+f*(1-p))
ax[0].plot(p,ppv,color="#245b83",lw=2.5)
for prior in [.1,.5]:
 v=s*prior/(s*prior+f*(1-prior));ax[0].plot(prior,v,"o",color="#b84919");ax[0].annotate(f"({prior:.1f}, {v:.3f})",(prior,v),xytext=(9,-17),textcoords="offset points",fontsize=10)
ax[0].set(xlim=(0,1),ylim=(0,1),xlabel="Target-state base rate",ylabel="Probability of target state given +",title="Same conditional performance")
ax[0].grid(alpha=.18)
labels=["True target", "Not target"];positive=np.array([80,180]);negative=np.array([20,720])
ax[1].bar(labels,positive,color="#245b83",label="Positive classification")
ax[1].bar(labels,negative,bottom=positive,color="#d8e3e9",label="Negative classification")
for k,(pos,neg)in enumerate(zip(positive,negative)):
 ax[1].text(k,pos/2,str(pos),ha="center",va="center",color="white",weight="bold")
 ax[1].text(k,pos+neg/2,str(neg),ha="center",va="center")
ax[1].set(ylim=(0,1080),ylabel="Hypothetical cases out of 1,000",title="Target-state base rate = 0.1")
ax[1].legend(frameon=False,fontsize=9,loc="upper right")
fig.suptitle("Illustration only: true-positive probability 0.8; false-positive probability 0.2",fontsize=12)
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
