"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

v=np.linspace(0,1,1600); beta=20.;j=1-np.expm1(beta*v)/np.expm1(beta);power=v*j;i=np.argmax(power)
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.8,3.6),layout="constrained")
ax.plot(v,j,color="#2563eb",lw=2);ax.add_patch(Rectangle((0,0),v[i],j[i],facecolor="#dbeafe",edgecolor="#2563eb",alpha=.6));ax.plot(v[i],j[i],"o",color="#dc2626")
ax.annotate("Maximum-power point",xy=(v[i],j[i]),xytext=(.12,.5),arrowprops={"arrowstyle":"->"})
ax.set(xlabel=r"$V/V_{\rm oc}$",ylabel=r"$J/J_{\rm sc}$",xlim=(0,1.03),ylim=(0,1.08),title="Illuminated current-voltage curve")
bx.plot(v,power,color="#059669",lw=2);bx.plot(v[i],power[i],"o",color="#dc2626");bx.set(xlabel=r"$V/V_{\rm oc}$",ylabel=r"$P/(V_{\rm oc} I_{\rm sc})$",title="Delivered electrical power",xlim=(0,1),ylim=(0,.9))
for a in (ax,bx):a.grid(alpha=.2)
fig.suptitle(r"Ideal illustrative diode, $eV_{\rm oc}/(k_BT)=20$")

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
