"""Original analytic illustration. Tested with Python 3.14, NumPy and Matplotlib.
Run from the intended output directory; the PNG is written to the current directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "savefig.facecolor": "white"})

n=np.linspace(0,1,801);D=np.sqrt((1-n)**2+4)
# Energies relative to each system's square value, in units |beta|.
d2=4-(n+1+D);d4=4-2*D
fig,ax=plt.subplots(figsize=(8,4),layout="constrained")
ax.plot(n,d2,color="#b7492a",lw=2,label="2 electrons")
ax.plot(n,d4,color="#173e62",lw=2,label="4 electrons")
ax.axhline(0,color=".5",lw=.8)
ax.scatter([1,1],[0,0],color="black",s=20)
ax.text(.97,.09,"square limit",ha="right")
ax.set(xlabel=r"Weakened-edge factor n (0 < n ≤ 1)",ylabel=r"$(E_{\rm trap}-E_{\rm square})/|\beta|$",title="Same one-edge weakening: opposite electronic preferences")
ax.legend(frameon=False)
fig.savefig("paper-2b-distortion-energies.png",dpi=165)
plt.close(fig)
