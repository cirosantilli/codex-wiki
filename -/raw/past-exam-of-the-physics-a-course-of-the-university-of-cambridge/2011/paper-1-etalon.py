"""Original pedagogical figure; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from the destination directory: output is the script's basename PNG in cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})
fig,ax=plt.subplots(figsize=(8.3,3.5),layout='constrained');lam=np.linspace(1200,1600,12000);delta=4*np.pi*3.5*1000/lam
for R,color,label in [(25/81,'#176493','Bare silicon: R=25/81'),(.9,'#b64b24','Illustrative coatings: R=0.90')]:
 T=(1-R)**2/((1-R)**2+4*R*np.sin(delta/2)**2);ax.plot(lam,T,color=color,lw=1.4,label=label)
ax.axvline(1400,c='0.7',lw=.7,ls=':');ax.set(xlabel='Wavelength (nm)',ylabel='Intensity transmittance',ylim=(0,1.06),xlim=(1200,1600));ax.legend(fontsize=9)
fig.savefig("paper-1-etalon.png", dpi=165, facecolor="white", bbox_inches="tight")
plt.close(fig)
